import hashlib
import json
import pathlib
import random
import uuid
import yaml

from jsonref import JsonRef
from yaml import CSafeLoader

from . import formatter

PRIMITIVE_TYPES = ["string", "number", "boolean", "integer"]


def load(filename):
    path = pathlib.Path(filename)
    with path.open() as fp:
        return JsonRef.replace_refs(yaml.load(fp, Loader=CSafeLoader))


def type_to_python_helper(type_, schema, alternative_name=None, in_list=False):
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
        subtype = type_to_python(schema["items"], in_list=True)
        if schema["items"].get("nullable"):
             subtype += ", none_type"
        return "[{}]".format(subtype)
    elif type_ == "object":
        if "additionalProperties" in schema:
            nested_schema = schema["additionalProperties"]
            nested_name = type_to_python(nested_schema)
            if nested_schema.get("nullable"):
                nested_name += ", none_type"
            return "{{str: ({},)}}".format(nested_name)
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


def type_to_python(schema, alternative_name=None, in_list=False):
    """Return Python type name for the type."""
    name = formatter.get_name(schema)
    if name:
        if "enum" in schema:
            return name
        if schema.get("type", "object") in ("object", "array"):
            return name

    type_ = schema.get("type")
    if type_ is None:
        if "oneOf" in schema and in_list:
            type_ = ""
            for child in schema["oneOf"]:
                # We do not generate model for nested primitive oneOfs
                if in_list and "items" in child and child["items"].get("type") in PRIMITIVE_TYPES:
                    type_ += f"{type_to_python_helper(child.get('type'), child, in_list=in_list)},"
                else:
                    type_ += f"{type_to_python(child, in_list=in_list)},"
            return type_
        if "items" in schema:
            type_ = "array"

    return type_to_python_helper(type_, schema, alternative_name=alternative_name, in_list=in_list)


def get_type_for_attribute(schema, attribute, current_name=None):
    """Return Python type name for the attribute."""
    child_schema = schema.get("properties", {}).get(attribute)
    alternative_name = current_name + formatter.camel_case(attribute) if current_name else None
    return type_to_python(child_schema, alternative_name=alternative_name)


def typing_to_python_helper(type_, schema, alternative_name=None, in_list=False):
    if type_ is None:
        return "Any"

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
        return "List[{}]".format(typing_to_python(schema["items"], in_list=True))
    elif type_ == "object":
        if "additionalProperties" in schema:
            nested_schema = schema["additionalProperties"]
            nested_name = typing_to_python(nested_schema)
            if nested_schema.get("nullable"):
                nested_name = f"Union[{nested_name}, none_type]"
            return f"Dict[str, {nested_name}]"
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


def typing_to_python(schema, alternative_name=None, in_list=False):
    """Return Python type name for the type."""
    name = formatter.get_name(schema)
    if name:
        if "enum" in schema:
            return name
        if schema.get("type", "object") in ("object", "array"):
            if "oneOf" in schema:
                types = [name]
                types.extend(get_oneof_types(schema))
                return f"Union[{','.join(types)}]"
            return name

    type_ = schema.get("type")
    if type_ is None:
        if "oneOf" in schema and in_list:
            type_ = ""
            for child in schema["oneOf"]:
                # We do not generate model for nested primitive oneOfs
                if in_list and "items" in child and child["items"].get("type") in PRIMITIVE_TYPES:
                    type_ += f"{typing_to_python_helper(child.get('type'), child, in_list=in_list)},"
                else:
                    type_ += f"{typing_to_python(child, in_list=in_list)},"
            return type_
        if "items" in schema:
            type_ = "array"

    return typing_to_python_helper(type_, schema, alternative_name=alternative_name, in_list=in_list)


def get_typing_for_attribute(schema, attribute, current_name=None, optional=False):
    child_schema = schema.get("properties", {}).get(attribute)
    alternative_name = current_name + formatter.camel_case(attribute) if current_name else None
    attr_type = typing_to_python(child_schema, alternative_name=alternative_name)
    if child_schema.get("nullable"):
        if optional:
            return f"Union[{attr_type}, none_type, UnsetType]"
        return f"Union[{attr_type}, none_type]"
    if optional:
        if attr_type.startswith("Union"):
            return attr_type[:-1] + ", UnsetType]"
        return f"Union[{attr_type}, UnsetType]"
    return attr_type


def get_types_for_attribute(schema, attribute, current_name=None):
    child_schema = schema.get("properties", {}).get(attribute)
    base_type = get_type_for_attribute(schema, attribute, current_name)
    if child_schema.get("nullable") and not formatter.get_name(child_schema):
        return f"({base_type}, none_type)"
    return f"({base_type},)"


def get_type_for_items(schema):
    name = formatter.get_name(schema.get("items"))
    return name


def get_type_for_parameter(parameter, typing=False):
    """Return Python type name for the parameter."""
    if "content" in parameter:
        assert "in" not in parameter
        for content in parameter["content"].values():
            data = type_to_python(content["schema"])
            if typing:
                if "oneOf" in content["schema"]:
                    types = [data]
                    types.extend(get_oneof_types(content["schema"]))
                    return f"Union[{','.join(types)}]"
                data = data.replace("[", "List[")
            return data
    data = type_to_python(parameter.get("schema"))
    if typing:
        data = data.replace("[", "List[")
    return data


def get_enum_type(schema):
    type_ = schema.get("type")

    if type_ == "integer":
        return "int"
    elif type_ == "string":
        return "str"


def get_enum_default(model):
    return model["enum"][0] if len(model["enum"]) == 1 else model.get("default")


def child_models(schema, alternative_name=None, seen=None, in_list=False):
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
            # Don't generate models for nested primitive types
            if in_list and child.get("type") in PRIMITIVE_TYPES:
                return
            yield from child_models(child, seen=seen)
    if "anyOf" in schema:
        has_sub_models = True
        for child in schema["anyOf"]:
            yield from child_models(child, seen=seen)

    if "items" in schema:
        yield from child_models(schema["items"], None, seen=seen, in_list=True)

    if schema.get("type") == "object" or "properties" in schema or has_sub_models:
        if not has_sub_models and name is None:
            # this is a basic map object so we don't need a type
            return

        if name is None:
            return

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
    result = {}
    top_name = formatter.get_name(model) or model_name
    for key, definition in model.get("properties", {}).items():
        if definition.get("type") == "object" or definition.get("enum") or definition.get("oneOf"):
            name = formatter.get_name(definition)
            if name:
                result[name] = None
            elif definition.get("properties") and top_name:
                result[top_name + formatter.camel_case(key)] = None
            elif definition.get("additionalProperties"):
                name = formatter.get_name(definition["additionalProperties"])
                if name:
                    result[name] = None
        elif definition.get("type") == "array":
            name = formatter.get_name(definition)
            if name:
                result[name] = None
            else:
                name = formatter.get_name(definition.get("items"))
                if name:
                    result[name] = None
        elif definition.get("properties") and top_name:
            result[top_name + formatter.camel_case(key)] = None
    if model.get("additionalProperties"):
        definition = model["additionalProperties"]
        name = formatter.get_name(definition)
        if name:
            result[name] = None
        elif definition.get("type") == "array":
            name = formatter.get_name(definition.get("items"))
            if name:
                result[name] = None
    result.pop(model_name, None)
    return list(result)


def get_oneof_references_for_model(model, model_name, seen=None):
    result = {}
    if seen is None:
        seen = set()
    name = formatter.get_name(model)
    if name:
        if name in seen:
            return []
        seen.add(name)

    if model.get("oneOf"):
        for schema in model["oneOf"]:
            type_ = schema.get("type", "object")
            if type_ in ("array", "object"):
                result[formatter.get_name(schema)] = None

    for key, definition in model.get("properties", {}).items():
        result.update({k: None for k in get_oneof_references_for_model(definition, model_name, seen)})
        if definition.get("items"):
            result.update({k: None for k in get_oneof_references_for_model(definition["items"], model_name, seen)})
        if definition.get("additionalProperties"):
            result.update(
                {k: None for k in get_oneof_references_for_model(definition["additionalProperties"], model_name, seen)}
            )
    result.pop(model_name, None)
    return list(result)


def get_oneof_parameters(model):
    seen = set()
    for schema in model["oneOf"]:
        for attr, definition in schema.get("properties", {}).items():
            if attr not in seen:
                seen.add(attr)
                yield attr, definition, schema


def get_oneof_types(model):
    for schema in model["oneOf"]:
        type_ = schema.get("type", "object")
        if type_ in ("array", "object"):
            yield formatter.get_name(schema)
        elif type_ == "integer":
            yield "int"
        elif type_ == "string":
            yield "str"
        elif type_ == "number":
            yield "float"
        elif type_ == "boolean":
            yield "bool"
        else:
            raise NotImplementedError(f"Type {type_} not implemented")


def get_oneof_models(model):
    result = []
    for schema in model["oneOf"]:
        if schema.get("type", "object") in ("array", "object"):
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
                        if "oneOf" in content["schema"]:
                            for schema in content["schema"]["oneOf"]:
                                type_ = schema.get("type", "object")
                                if type_ in ("array", "object"):
                                    name = formatter.get_name(schema)
                                    if name and name not in seen:
                                        seen.add(name)
                                        yield name
        if "x-pagination" in operation:
            name = get_type_at_path(operation, operation["x-pagination"]["resultsPath"])
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


def generate_value(schema, use_random=False, prefix=None):
    spec = schema.spec
    if not use_random:
        if "example" in spec:
            return spec["example"]
        if "default" in spec:
            return spec["default"]

    if spec["type"] == "string":
        if use_random:
            return str(
                uuid.UUID(
                    bytes=hashlib.sha256(
                        str(prefix or schema.keys).encode("utf-8"),
                    ).digest()[:16]
                )
            )
        return "string"
    elif spec["type"] == "integer":
        return random.randint(0, 32000) if use_random else len(str(prefix or schema.keys))
    elif spec["type"] == "number":
        return random.random() if use_random else 1.0 / len(str(prefix or schema.keys))
    elif spec["type"] == "boolean":
        return True
    elif spec["type"] == "array":
        return [generate_value(schema[0], use_random=use_random)]
    elif spec["type"] == "object":
        return {key: generate_value(schema[key], use_random=use_random) for key in spec["properties"]}
    else:
        raise TypeError(f"Unknown type: {spec['type']}")


class Schema:
    def __init__(self, spec, value=None, keys=None):
        self.spec = spec
        self.value = value if value is not None else generate_value
        self.keys = keys or tuple()

    def __getattr__(self, key):
        return self[key]

    def __getitem__(self, key):
        type_ = self.spec.get("type", "object")
        if type_ == "object":
            try:
                return self.__class__(
                    self.spec["properties"][key],
                    value=self.value,
                    keys=self.keys + (key,),
                )
            except KeyError:
                if "oneOf" in self.spec:
                    for schema in self.spec["oneOf"]:
                        if schema.get("type", "object") == "object":
                            try:
                                return self.__class__(
                                    schema["properties"][key],
                                    value=self.value,
                                    keys=self.keys + (key,),
                                )
                            except KeyError:
                                pass
            raise KeyError(f"{key} not found in {self.spec.get('properties', {}).keys()}: {self.spec}")
        if type_ == "array":
            return self.__class__(self.spec["items"], value=self.value, keys=self.keys + (key,))

        raise KeyError(f"{key} not found in {self.spec}")

    def __repr__(self):
        value = self.value(self)
        if isinstance(value, (dict, list)):
            return json.dumps(value, indent=2)
        return str(value)


class Operation:
    def __init__(self, name, spec, method, path):
        self.name = name
        self.spec = spec
        self.method = method
        self.path = path

    def server_url_and_method(self, spec, server_index=0, server_variables=None):
        def format_server(server, path):
            url = server["url"] + path
            # replace potential path variables
            for variable, value in server_variables.items():
                url = url.replace("{" + variable + "}", value)
            # replace server variables if they were not replace before
            for variable in server["variables"]:
                if variable in server_variables:
                    continue
                url = url.replace("{" + variable + "}", server["variables"][variable]["default"])
            return url

        server_variables = server_variables or {}
        if "servers" in self.spec:
            server = self.spec["servers"][server_index]
        else:
            server = spec["servers"][server_index]
        return format_server(server, self.path), self.method

    def response_code_and_accept_type(self):
        for response in self.spec["responses"]:
            return int(response), next(iter(self.spec["responses"][response].get("content", {None: None})))
        return None, None

    def request_content_type(self):
        return next(iter(self.spec.get("requestBody", {}).get("content", {None: None})))

    def response(self):
        for response in self.spec["responses"]:
            return Schema(next(iter((self.spec["responses"][response]["content"].values())))["schema"])

    def request(self):
        return Schema(next(iter(self.spec["requestBody"]["content"].values()))["schema"])


def get_default(operation, attribute_path):
    attrs = attribute_path.split(".")
    for name, parameter in parameters(operation):
        if name == attrs[0]:
            break
    if name == attribute_path:
        # We found a top level attribute matching the full path, let's use the default
        return parameter["schema"]["default"]

    if name == "body":
        parameter = next(iter(parameter["content"].values()))["schema"]
    for attr in attrs[1:]:
        parameter = parameter["properties"][attr]
    return parameter["default"]


def get_type_at_path(operation, attribute_path):
    content = None
    for code, response in operation.get("responses", {}).items():
        if int(code) >= 300:
            continue
        for content in response.get("content", {}).values():
            if "schema" in content:
                break
    if content is None:
        raise RuntimeError("Default response not found")
    for attr in attribute_path.split("."):
        content = content["schema"]["properties"][attr]
    return get_type_for_items(content)
