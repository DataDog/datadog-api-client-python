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


def basic_type_to_python(type_, schema, typing=False):
    if type_ is None:
        if typing:
            return "Any"
        return "bool, date, datetime, dict, float, int, list, str, UUID, none_type"
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
        elif format_ == "uuid":
            return "UUID"
        return "str"
    elif type_ == "boolean":
        return "bool"
    elif type_ == "array":
        subtype = type_to_python(schema["items"], typing=typing)
        if typing:
            return "List[{}]".format(subtype)
        if schema["items"].get("nullable"):
            subtype += ", none_type"
        return "[{}]".format(subtype)
    elif type_ == "object":
        if "additionalProperties" in schema:
            nested_schema = schema["additionalProperties"]
            nested_name = type_to_python(nested_schema, typing=typing)
            if nested_schema.get("nullable"):
                if typing:
                    nested_name = f"Union[{nested_name}, none_type]"
                else:
                    nested_name += ", none_type"
            if typing:
                return f"Dict[str, {nested_name}]"
            return "{{str: ({},)}}".format(nested_name)
        return "dict"
    else:
        raise ValueError(f"Unknown type {type_}")


def type_to_python(schema, typing=False):
    """Return Python type name for the type."""

    # Special case for additionalProperties: True
    if schema is True:
        return basic_type_to_python(None, {}, typing=typing)

    name = formatter.get_name(schema)

    if "oneOf" in schema:
        types = list(get_oneof_types(schema, typing=typing))
        if name and typing:
            types.insert(0, name)
        type_ = ", ".join(types)
        if typing:
            return f"Union[{type_}]"
        elif name:
            return name
        return type_

    if "enum" in schema:
        return name

    type_ = schema.get("type")

    if name and (type_ == "object" or formatter.is_list_model_whitelisted(name)):
        return name

    return basic_type_to_python(type_, schema, typing=typing)


def get_type_for_attribute(schema, attribute, current_name=None):
    """Return Python type name for the attribute."""
    child_schema = schema.get("properties", {}).get(attribute)
    return type_to_python(child_schema)


def get_typing_for_attribute(schema, attribute, current_name=None, optional=False):
    child_schema = schema.get("properties", {}).get(attribute)
    attr_type = type_to_python(child_schema, typing=True)
    if child_schema.get("nullable"):
        attr_type = f"Union[{attr_type}, none_type]"
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
    return formatter.get_name(schema.get("items"))


def get_type_for_parameter(parameter, typing=False):
    """Return Python type name for the parameter."""
    if "content" in parameter:
        assert "in" not in parameter
        for content in parameter["content"].values():
            return type_to_python(content["schema"], typing=typing)
    return type_to_python(parameter.get("schema"), typing=typing)


def get_enum_type(schema):
    type_ = schema.get("type")

    if type_ == "integer":
        return "int"
    elif type_ == "string":
        return "str"

    raise ValueError(f"Unknown type {type_}")


def get_enum_default(model):
    return model["enum"][0] if len(model["enum"]) == 1 else model.get("default")


def child_models(schema, alternative_name=None, seen=None):
    seen = seen or set()
    current_name = formatter.get_name(schema)
    name = current_name or alternative_name

    if name in seen:
        return

    has_sub_models = False
    if "oneOf" in schema:
        has_sub_models = not formatter.is_list_model_whitelisted(name)
        for child in schema["oneOf"]:
            sub_models = list(child_models(child, seen=seen))
            if sub_models:
                has_sub_models = True
                yield from sub_models
        if not has_sub_models:
            return

    if "items" in schema:
        yield from child_models(schema["items"], seen=seen)

    if schema.get("type") == "object" or "properties" in schema or has_sub_models:
        if name is None:
            # this is a basic map object so we don't need a type
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
        if formatter.is_list_model_whitelisted(name):
            seen.add(name)
            yield name, schema

    if "enum" in schema:
        if name is None:
            raise ValueError(f"Schema {schema} has no name")

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
        if path.startswith("x-"):
            continue
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


def find_non_primitive_type(schema):
    if schema.get("enum"):
        return True
    return schema.get("type") not in PRIMITIVE_TYPES


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
            if name and formatter.is_list_model_whitelisted(name):
                result[name] = None
            else:
                items_name = formatter.get_name(definition.get("items"))
                if items_name:
                    if formatter.is_list_model_whitelisted(items_name):
                        result[items_name] = None
                    elif definition["items"].get("type") == "array":
                        nested_model = definition["items"]["items"]
                        nested_model_name = formatter.get_name(nested_model)
                        result[nested_model_name] = None
                        result.update(
                            {k: None for k in get_oneof_references_for_model(nested_model, nested_model_name)}
                        )
                    elif find_non_primitive_type(definition["items"]):
                        result[items_name] = None
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

            oneof_name = formatter.get_name(schema)
            if type_ == "object" or formatter.is_list_model_whitelisted(oneof_name):
                result[oneof_name] = None
            elif type_ == "array":
                sub_name = formatter.get_name(schema["items"])
                if sub_name:
                    result[sub_name] = None

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


def get_oneof_types(model, typing=False):
    for schema in model["oneOf"]:
        type_ = schema.get("type", "object")
        name = formatter.get_name(schema)
        if type_ == "object" or formatter.is_list_model_whitelisted(name):
            yield name
        else:
            yield basic_type_to_python(type_, schema, typing=typing)


def get_oneof_models(model):
    result = []
    for schema in model["oneOf"]:
        type_ = schema.get("type", "object")
        name = formatter.get_name(schema)
        if type_ == "object" or formatter.is_list_model_whitelisted(name):
            result.append(name)
        elif type_ == "array":
            name = formatter.get_name(schema["items"])
            if name:
                result.append(name)
    return result


def apis(spec):
    operations = {}

    for path in spec["paths"]:
        if path.startswith("x-"):
            continue
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
                                if schema.get("type", "object") == "object":
                                    name = formatter.get_name(schema)
                                    if name and name not in seen:
                                        seen.add(name)
                                        yield name
                    if "items" in content["schema"]:
                        name = formatter.get_name(content["schema"]["items"])
                        if name and name not in seen:
                            seen.add(name)
                            yield name

        if "x-pagination" in operation:
            name = get_type_at_path(operation, operation["x-pagination"].get("resultsPath"))
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
                yield (
                    name,
                    {
                        "in": "form",
                        "schema": schema,
                        "name": name,
                        "description": schema.get("description"),
                        "required": name in parent.get("required", []),
                    },
                )
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
                url = url.replace(f"{{{variable}}}", value)
            # replace server variables if they were not replace before
            for variable in server["variables"]:
                if variable in server_variables:
                    continue
                url = url.replace(f"{{{variable}}}", server["variables"][variable]["default"])
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
    content = content["schema"]
    if not attribute_path:
        return get_type_for_items(content)
    for attr in attribute_path.split("."):
        content = content["properties"][attr]
    return get_type_for_items(content)


def get_security_names(security):
    if security is None:
        return []

    auth_names = set()
    for auth in security:
        for key in auth.keys() if isinstance(auth, dict) else [auth]:
            auth_names.add(key)

    return list(auth_names)
