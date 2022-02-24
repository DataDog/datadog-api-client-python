import pathlib
import yaml
from jsonref import JsonRef
from yaml import CSafeLoader

from . import formatter


def load(filename):
    path = pathlib.Path(filename)
    with path.open() as fp:
        return JsonRef.replace_refs(yaml.load(fp, Loader=CSafeLoader))


def type_to_python(schema, alternative_name=None):
    """Return Python type name for the type."""
    name = formatter.get_name(schema)
    if name:
        if "enum" in schema:
            return name
        if schema.get("type", "object") in ("object", "array"):
            return name

    type_ = schema.get("type")
    if type_ is None:
        if "items" in schema:
            type_ = "array"

    if type_ is None:
        return "bool, date, datetime, dict, float, int, list, str, none_type"

    if type_ == "integer":
        return "int"
    elif type_ == "number":
        return "float"
    elif type_ == "string":
        format_ = schema.get("format")
        if format_ in {"date", "date-time"}:
            return "datetime"
        elif format_ == "binary":
            return "file_type"
        return "str"
    elif type_ == "boolean":
        return "bool"
    elif type_ == "array":
        return "[{}]".format(type_to_python(schema["items"]))
    elif type_ == "object":
        if "additionalProperties" in schema:
            return "{{str: ({},)}}".format(type_to_python(schema["additionalProperties"]))
        return (
            alternative_name
            if alternative_name
            and ("properties" in schema or "oneOf" in schema or "anyOf" in schema or "allOf" in schema)
            else "dict"
        )
    elif type_ == "null":
        return "none_type"
    else:
        raise ValueError(f"Unknown type {type_}")


def get_type_for_attribute(schema, attribute, current_name=None):
    """Return Python type name for the attribute."""
    child_schema = schema.get("properties", {}).get(attribute)
    alternative_name = current_name + formatter.camel_case(attribute) if current_name else None
    return type_to_python(child_schema, alternative_name=alternative_name)


def get_types_for_attribute(schema, attribute, current_name=None):
    child_schema = schema.get("properties", {}).get(attribute)
    base_type = get_type_for_attribute(schema, attribute, current_name)
    if child_schema.get("nullable") and not formatter.get_name(child_schema):
        return f"({base_type}, none_type)"
    return f"({base_type},)"


def get_type_for_items(schema):
    name = formatter.get_name(schema.get("items"))
    return name


def get_type_for_parameter(parameter):
    """Return Python type name for the parameter."""
    if "content" in parameter:
        assert "in" not in parameter
        for content in parameter["content"].values():
            return type_to_python(content["schema"])
    return type_to_python(parameter.get("schema"))


def get_enum_type(schema):
    type_ = schema.get("type")

    if type_ == "integer":
        return "int"
    elif type_ == "string":
        return "str"


def get_enum_default(model):
    return model["enum"][0] if len(model["enum"]) == 1 else model.get("default")


def child_models(schema, alternative_name=None, seen=None):
    seen = seen or set()
    current_name = formatter.get_name(schema)
    name = current_name or alternative_name

    has_sub_models = False
    if "allOf" in schema:
        has_sub_models = True
        for child in schema["allOf"]:
            yield from child_models(child, seen=seen)
    if "oneOf" in schema:
        has_sub_models = True
        for child in schema["oneOf"]:
            yield from child_models(child, seen=seen)
    if "anyOf" in schema:
        has_sub_models = True
        for child in schema["anyOf"]:
            yield from child_models(child, seen=seen)

    if "items" in schema:
        yield from child_models(
            schema["items"],
            None,
            seen=seen,
        )

    if schema.get("type") == "object" or "properties" in schema or has_sub_models:
        if not has_sub_models and name is None:
            # this is a basic map object so we don't need a type
            return

        if name is None:
            raise ValueError(f"Schema {schema} has no name")

        if name in seen:
            return

        if "properties" in schema or has_sub_models:
            seen.add(name)
            yield name, schema

        if "additionalProperties" in schema and current_name:
            seen.add(name)
            yield name, schema

        for key, child in schema.get("properties", {}).items():
            yield from child_models(child, alternative_name=name + formatter.camel_case(key), seen=seen)

    if current_name and schema.get("type") == "array":
        if name in seen:
            return

        seen.add(name)
        yield name, schema

    if "enum" in schema:
        if name is None:
            raise ValueError(f"Schema {schema} has no name")

        if name in seen:
            return

        seen.add(name)
        yield name, schema

    if "additionalProperties" in schema:
        nested_name = formatter.get_name(schema["additionalProperties"])
        if nested_name:
            yield from child_models(
                schema["additionalProperties"],
                alternative_name=name,
                seen=seen,
            )


def models(spec):
    name_to_schema = {}

    for path in spec["paths"]:
        for method in spec["paths"][path]:
            operation = spec["paths"][path][method]

            for content in operation.get("parameters", []):
                if "schema" in content:
                    name_to_schema.update(dict(child_models(content["schema"])))

            for content in operation.get("requestBody", {}).get("content", {}).values():
                if "schema" in content:
                    name_to_schema.update(dict(child_models(content["schema"])))

            for response in operation.get("responses", {}).values():
                for content in response.get("content", {}).values():
                    if "schema" in content:
                        name_to_schema.update(dict(child_models(content["schema"])))

    return name_to_schema


def get_references_for_model(model, model_name):
    result = []
    top_name = formatter.get_name(model) or model_name
    for key, definition in model.get("properties", {}).items():
        if definition.get("type") == "object" or definition.get("enum") or definition.get("oneOf"):
            name = formatter.get_name(definition)
            if name:
                result.append(name)
            elif definition.get("properties") and top_name:
                result.append(top_name + formatter.camel_case(key))
            elif definition.get("additionalProperties"):
                name = formatter.get_name(definition["additionalProperties"])
                if name:
                    result.append(name)
        elif definition.get("type") == "array":
            name = formatter.get_name(definition)
            if name:
                result.append(name)
            else:
                name = formatter.get_name(definition.get("items"))
                if name:
                    result.append(name)
        elif definition.get("properties") and top_name:
            result.append(top_name + formatter.camel_case(key))
    if model.get("additionalProperties"):
        definition = model["additionalProperties"]
        name = formatter.get_name(definition)
        if name:
            result.append(name)
        elif definition.get("type") == "array":
            name = formatter.get_name(definition.get("items"))
            if name:
                result.append(name)
    return result


def get_oneof_parameters(model):
    seen = set()
    for schema in model["oneOf"]:
        for attr, definition in schema.get("properties", {}).items():
            if attr not in seen:
                seen.add(attr)
                yield attr, definition, schema


def get_oneof_types(model):
    for schema in model["oneOf"]:
        type_ = schema.get("type")
        if type_ in ("array", "object"):
            yield formatter.get_name(schema)
        elif type_ == "integer":
            yield "int"
        elif type_ == "string":
            yield "str"
        elif type_ == "number":
            yield "float"


def get_oneof_models(model):
    result = []
    for schema in model["oneOf"]:
        if schema.get("type") in ("array", "object"):
            result.append(formatter.get_name(schema))
    return result


def apis(spec):
    operations = {}

    for path in spec["paths"]:
        for method in spec["paths"][path]:
            operation = spec["paths"][path][method]
            tag = operation.get("tags", [None])[0]
            operations.setdefault(tag, []).append((path, method, operation))

    return operations


def operation(spec, operation_id):
    for path in spec["paths"]:
        for method in spec["paths"][path]:
            operation = spec["paths"][path][method]
            if operation["operationId"] == operation_id:
                return operation
    return None


def get_api_models(operations):
    seen = set()
    for _, _, operation in operations:
        for response in operation.get("responses", {}).values():
            for content in response.get("content", {}).values():
                if "schema" in content:
                    name = formatter.get_name(content["schema"])
                    if name and name not in seen:
                        seen.add(name)
                        yield name
                    elif "items" in content["schema"]:
                        name = formatter.get_name(content["schema"]["items"])
                        if name and name not in seen:
                            seen.add(name)
                            yield name
            break
        for content in operation.get("parameters", []):
            if "schema" in content and (
                content["schema"].get("type") in ("object", "array") or content["schema"].get("enum")
            ):
                name = formatter.get_name(content["schema"])
                if name and name not in seen:
                    seen.add(name)
                    yield name
                elif "items" in content["schema"]:
                    name = formatter.get_name(content["schema"]["items"])
                    if name and name not in seen:
                        seen.add(name)
                        yield name
        if "requestBody" in operation:
            for content in operation["requestBody"].get("content", {}).values():
                if "schema" in content:
                    name = formatter.get_name(content["schema"])
                    if name and name not in seen:
                        seen.add(name)
                        yield name


def parameters(operation):
    for content in operation.get("parameters", []):
        if "schema" in content:
            yield content["name"], content

    if "requestBody" in operation:
        if "multipart/form-data" in operation["requestBody"]["content"]:
            parent = operation["requestBody"]["content"]["multipart/form-data"]["schema"]
            for name, schema in parent["properties"].items():
                yield name, {
                    "in": "form",
                    "schema": schema,
                    "name": name,
                    "description": schema.get("description"),
                    "required": name in parent.get("required", []),
                }
        else:
            name = operation.get("x-codegen-request-body-name", "body")
            yield name, operation["requestBody"]


def parameter_schema(parameter):
    if "schema" in parameter:
        return parameter["schema"]
    if "content" in parameter:
        for content in parameter.get("content", {}).values():
            if "schema" in content:
                return content["schema"]
    raise ValueError(f"Unknown schema for parameter {parameter}")


def return_type(operation):
    for response in operation.get("responses", {}).values():
        for content in response.get("content", {}).values():
            if "schema" in content:
                return type_to_python(content["schema"])
        return


def accept_headers(operation):
    any_type = "*/*"
    seen = []
    for response in operation.get("responses", {}).values():
        if "content" in response:
            for media_type in response["content"].keys():
                if media_type not in seen:
                    seen.append(media_type)
        else:
            return [any_type]
    return seen


def collection_format(parameter):
    in_to_style = {
        "query": "form",
        "path": "simple",
        "header": "simple",
        "cookie": "form",
    }
    schema = parameter_schema(parameter)
    matrix = {
        ("form", False): "csv",
        ("form", True): "multi",
        # TODO add more cases from https://swagger.io/specification/#parameter-style
    }
    if schema.get("type") == "array" or "items" in schema:
        in_ = parameter.get("in", "query")
        style = parameter.get("style", in_to_style[in_])
        explode = parameter.get("explode", True if style == "form" else False)
        return matrix.get((style, explode), "multi")
