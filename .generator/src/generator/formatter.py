"""Data formatter."""
import keyword
import re
import warnings
from functools import singledispatch

KEYWORDS = set(keyword.kwlist)
KEYWORDS.add("property")

PATTERN_DOUBLE_UNDERSCORE = re.compile(r"__+")
PATTERN_LEADING_ALPHA = re.compile(r"(.)([A-Z][a-z]+)")
PATTERN_FOLLOWING_ALPHA = re.compile(r"([a-z0-9])([A-Z])")
PATTERN_WHITESPACE = re.compile(r"\W")


def snake_case(value):
    s1 = PATTERN_LEADING_ALPHA.sub(r"\1_\2", value)
    s1 = PATTERN_FOLLOWING_ALPHA.sub(r"\1_\2", s1).lower()
    s1 = PATTERN_WHITESPACE.sub("_", s1)
    s1 = s1.rstrip("_")
    return PATTERN_DOUBLE_UNDERSCORE.sub("_", s1)


def block_comment(comment, prefix="#"):
    return "\n".join(f"{prefix} {line}".rstrip() for line in comment.split("\n"))


def camel_case(value):
    return "".join(x.title() for x in snake_case(value).split("_"))


def untitle_case(value):
    return value[0].lower() + value[1:]


def schema_name(schema):
    if not schema:
        return None

    if hasattr(schema, "__reference__"):
        return schema.__reference__["$ref"].split("/")[-1]


def given_variables(context):
    """Return a list of variables using in given steps."""
    return {key for values in context.get("_given", {}).values() for key in values}


def escape_reserved_keyword(word):
    """
    Escape reserved language keywords like openapi generator does it
    :param word: Word to escape
    :return: The escaped word if it was a reserved keyword, the word unchanged otherwise
    """
    if word in KEYWORDS:
        return f"_{word}"
    return word


def attribute_name(attribute):
    return escape_reserved_keyword(snake_case(attribute))


def format_value(value, quotes="'"):
    if isinstance(value, str):
        return f"{quotes}{value}{quotes}"
    elif isinstance(value, bool):
        return "true" if value else "false"
    return value


def format_parameters(kwargs, spec, replace_values=None, has_body=False):
    parameters = ""
    optional_spec = {}
    opts = {}
    for p in spec.get("parameters", []):
        required = p.get("required", False)
        k = snake_case(p["name"])
        if required:
            v = kwargs.pop(k)  # otherwise there is a missing required parameters
            value = format_data_with_schema(
                v["value"],
                p["schema"],
                replace_values=replace_values,
            )
            parameters += f"{value}, "
        else:
            optional_spec[k] = p

    if optional_spec:
        for k, v in kwargs.items():
            k = snake_case(k)
            value = format_data_with_schema(
                v["value"],
                optional_spec[k]["schema"],
                replace_values=replace_values,
            )
            opts[escape_reserved_keyword(k)] = value

        if opts:
            parameters += "opts"

    return parameters, opts


def get_name(schema):

    name = None
    if hasattr(schema, "__reference__"):
        name = schema.__reference__["$ref"].split("/")[-1]

    return name


@singledispatch
def format_data_with_schema(
    data,
    schema,
    name_prefix="",
    replace_values=None,
    default_name=None,
):
    name = get_name(schema)

    if "enum" in schema and data not in schema["enum"]:
        raise ValueError(f"{data} is not valid enum value {schema['enum']}")

    if replace_values and data in replace_values:
        warnings.warn(f"implement '{replace_values[data]}' with value {data}")
        parameters = replace_values[data]
        if schema.get("type") == "integer":
            parameters = f"{parameters}.to_i"
        elif schema.get("type") == "number":
            parameters = f"{parameters}.to_f"
    elif "enum" in schema:
        parameters = schema["x-enum-varnames"][schema["enum"].index(data)]
    else:
        if schema.get("nullable") and data is None:
            return "nil"
        else:
            formatter = {
                "number": str,
                "integer": str,
                "boolean": lambda x: "true" if x else "false",
                "string": repr,
                None: repr,
            }[schema.get("type")]

            # TODO format date and datetime
            parameters = formatter(data)

    if "enum" in schema and name:
        return f"{name_prefix}{name}::{parameters.upper()}"

    if schema.get("type") == "string":
        return f"{parameters}"

    # NOTE we don't need named parameters for basic types except enums handled above
    # if name:
    #     return f"{name_prefix}{name}.new({{{parameters}}})"

    return parameters


@format_data_with_schema.register(list)
def format_data_with_schema_list(
    data,
    schema,
    name_prefix="",
    replace_values=None,
    default_name=None,
):
    name = get_name(schema)

    parameters = ""
    for d in data:
        value = format_data_with_schema(
            d,
            schema["items"],
            name_prefix=name_prefix,
            replace_values=replace_values,
            default_name=name,
        )
        parameters += f"{value},\n"
    return f"[\n{parameters}]"


@format_data_with_schema.register(dict)
def format_data_with_schema_dict(
    data,
    schema,
    name_prefix="",
    replace_values=None,
    default_name=None,
):
    name = get_name(schema)

    parameters = ""
    if "properties" in schema:
        for k, v in data.items():
            value = format_data_with_schema(
                v,
                schema["properties"][k],
                name_prefix=name_prefix,
                replace_values=replace_values,
                default_name=name + camel_case(k) if name else None,
            )
            parameters += f"{escape_reserved_keyword(snake_case(k))}: {value},\n"

    if "additionalProperties" in schema:
        for k, v in data.items():
            value = format_data_with_schema(
                v,
                schema["additionalProperties"],
                name_prefix=name_prefix,
                replace_values=replace_values,
            )
            parameters += f"{k}: {value}, "

    if not name and "oneOf" not in schema:
        if default_name:
            name = default_name
        else:
            name = "dict"
            warnings.warn(f"Unnamed schema {schema} for {data}")

    if "oneOf" in schema:
        matched = 0
        for sub_schema in schema["oneOf"]:
            try:
                formatted = format_data_with_schema(
                    data,
                    sub_schema,
                    name_prefix=name_prefix,
                    replace_values=replace_values,
                )
                if matched == 0:
                    # NOTE we do not support mixed schemas with oneOf
                    # parameters += formatted
                    parameters = formatted
                    name = None
                matched += 1
            except (KeyError, ValueError) as e:
                print(f"{e}")

        if matched == 0:
            raise ValueError(f"[{matched}] {data} is not valid for schema {name}")
        elif matched > 1:
            warnings.warn(f"[{matched}] {data} is not valid for schema {name}")

    if name:
        return f"{name_prefix}{name}.new({{\n{parameters}}})"

    return parameters
