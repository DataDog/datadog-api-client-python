# coding=utf-8
"""Define basic fixtures."""

import json
import os
import pathlib
import re
import warnings
import zlib
from collections import defaultdict

import pytest
from dateutil.relativedelta import relativedelta
from jinja2 import Environment, FileSystemLoader, Template
from pytest_bdd import given, parsers, then, when
import hashlib

from generator import openapi

from generator.formatter import format_parameters, format_data_with_schema, safe_snake_case, snake_case, set_api_version


MODIFIED_FEATURES = {
    pathlib.Path(p).resolve()
    for p in os.getenv("BDD_MODIFIED_FEATURES", "").split(" ")
    if p
}

ROOT_PATH = pathlib.Path(__file__).parent.parent

PATTERN_ALPHANUM = re.compile(r"[^A-Za-z0-9]+")


if os.getenv("CI") is not None:

    def formatwarning(message, category, filename, lineno, line=None):
        p = pathlib.Path(filename)
        if p.is_absolute() and filename.startswith(str(ROOT_PATH)):
            p = p.relative_to(ROOT_PATH)
        return f"\n::warning file={p},line={lineno}::{message}\n"

    warnings.formatwarning = formatwarning


def pytest_bdd_before_scenario(request, feature, scenario):
    if MODIFIED_FEATURES:
        current = pathlib.Path(scenario.feature.filename).resolve()
        if current not in MODIFIED_FEATURES:
            pytest.skip(
                f"Feature file {scenario.feature.filename} has not been modified"
            )


def lookup(value, path):
    result = value
    for dot_path in path.split("."):
        for part in dot_path.split("["):
            if "]" in part:
                index = int(part[: part.index("]")])
                result = result[index]
            else:
                result = result[snake_case(part)]
    return result


class FloatEncoder(json.JSONEncoder):
    """Ensure that floats have decimal point and no trailing zeros."""

    def encode(self, obj):
        result = super().encode(obj)
        if isinstance(obj, float):
            if "." in result and result.endswith("0"):
                result = result.rstrip("0")
            result = result.rstrip(".")
            return result
        return result


JINJA_ENV = Environment(loader=FileSystemLoader(pathlib.Path(__file__).parent / "src" / "generator" / "templates"))
JINJA_ENV.filters["tojson"] = json.dumps
JINJA_ENV.filters["snake_case"] = snake_case
JINJA_ENV.filters["safe_snake_case"] = safe_snake_case
JINJA_ENV.globals["format_data_with_schema"] = format_data_with_schema
JINJA_ENV.globals["format_parameters"] = format_parameters

PYTHON_EXAMPLE_J2 = JINJA_ENV.get_template("example.j2")


def pytest_bdd_after_scenario(request, feature, scenario):
    try:
        operation_specs = request.getfixturevalue("operation_specs")
        version = request.getfixturevalue("api_version")
        context = request.getfixturevalue("context")
    except Exception:
        return
    operation_id = context["api_request"]["operation_id"]

    status_code = context["status_code"]
    if status_code >= 300:
        return

    operation_spec = operation_specs[version][operation_id]
    response_spec = operation_spec.spec["responses"][str(status_code)]
    group_name = "-".join(operation_spec.spec["tags"][0].split(" ")).lower()
    context["api_response"] = response_spec

    unique_suffix = ""
    scenario_name = f"{operation_spec.spec['summary']} returns \"{response_spec['description']}\" response"
    if scenario_name != scenario.name:
        unique_suffix = "_" + str(zlib.adler32(scenario.name.encode("utf-8")))

    code_examples = request.getfixturevalue("code_examples")
    code_examples.setdefault(version, {}).setdefault(operation_id, []).append(
        {
            "group": "_".join(operation_spec.spec["tags"][0].split(" ")).lower(),
            "suffix": unique_suffix,
            "description": scenario.name,
        }
    )

    data = PYTHON_EXAMPLE_J2.render(
        context=context,
        version=version,
        scenario=scenario,
        operation_spec=operation_spec.spec,
    )

    output = (
        ROOT_PATH
        / "examples"
        / version
        / group_name
        / f"{operation_id}{unique_suffix}.py"
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("w") as f:
        f.write(data)


def pytest_bdd_apply_tag(tag, function):
    """Register tags as custom markers and skip test for '@skip' ones."""
    skip_tags = {}
    if tag in skip_tags:
        marker = pytest.mark.skip(reason=f"skipped because '{tag}' in {skip_tags}")
        marker(function)
        return True
    return False


@pytest.fixture(scope="session")
def code_examples():
    return {}


@pytest.fixture
def api_version(request):
    path = pathlib.Path(request.node.__scenario_report__.scenario.feature.filename)
    set_api_version(path.parent.parent.name)
    return path.parent.parent.name


@pytest.fixture
def unique(request):
    main = PATTERN_ALPHANUM.sub("-", request.node.__scenario_report__.scenario.feature.name)
    if main.endswith("s"):
        # Let's strip the plural present in most names
        main = main[:-1]
    return f"Example-{main}"


TIME_FORMATTER = {
    "now": "datetime.now()",
    "timestamp": "{sret}.timestamp()",
    "isoformat": "{sret}",
    "units": {
        "s": "({sret} + relativedelta(seconds={num}))",
        "m": "({sret} + relativedelta(minutes={num}))",
        "h": "({sret} + relativedelta(hours={num}))",
        "d": "({sret} + relativedelta(days={num}))",
        "M": "({sret} + relativedelta(months={num}))",
        "y": "({sret} + relativedelta(years={num}))",
    },
}

def relative_time(imports, calls, freezed_time, iso):
    time_re = re.compile(r"now( *([+-]) *(\d+)([smhdMy]))?")

    def func(arg):
        imports["datetime"].add("datetime")
        sret = TIME_FORMATTER["now"]
        ret = freezed_time
        m = time_re.match(arg)
        if m:
            if m.group(1):
                sign = m.group(2)
                num = int(sign + m.group(3))
                unit = m.group(4)
                if unit == "s":
                    ret += relativedelta(seconds=num)
                elif unit == "m":
                    ret += relativedelta(minutes=num)
                elif unit == "h":
                    ret += relativedelta(hours=num)
                elif unit == "d":
                    ret += relativedelta(days=num)
                elif unit == "M":
                    ret += relativedelta(months=num)
                elif unit == "y":
                    ret += relativedelta(years=num)
                else:
                    raise ValueError(f"Unknown unit {unit}")
                sret = TIME_FORMATTER["units"][unit].format(sret=sret, num=num)
                imports["dateutil.relativedelta"].add("relativedelta")

            if iso:
                return (
                    ret.isoformat(timespec="seconds"),
                    TIME_FORMATTER["isoformat"].format(sret=sret),
                )
            return int(ret.timestamp()), TIME_FORMATTER["timestamp"].format(sret=sret)
        return "", ""

    def store_calls(arg):
        result, value = func(arg)
        calls[result] = value
        return result

    return store_calls

@pytest.fixture
def context(request, unique, freezed_time):
    """
    Return a mapping with all defined fixtures, all objects created by `given` steps,
    and the undo operations to perform after a test scenario.
    """

    class MarkUsed(dict):
        def __init__(self, *args, **kwargs):
            dict.__init__(self, *args, **kwargs)
            self.__used_keys__ = set()

        def __getitem__(self, key):
            value = super().__getitem__(key)
            self.__used_keys__.add(value)
            return value

        def is_used(self, key):
            return key in self.__used_keys__

    replace_values = MarkUsed()
    imports = defaultdict(set)
    given = defaultdict(dict)

    unique_hash = hashlib.sha256(unique.encode("utf-8")).hexdigest()[:16]
    ctx = {
        "undo_operations": [],
        "unique": unique,
        "unique_lower": unique.lower(),
        "unique_upper": unique.upper(),
        "unique_alnum": PATTERN_ALPHANUM.sub("", unique),
        "unique_lower_alnum": PATTERN_ALPHANUM.sub("", unique).lower(),
        "unique_upper_alnum": PATTERN_ALPHANUM.sub("", unique).upper(),
        "unique_hash": unique_hash,
        "timestamp": relative_time(imports, replace_values, freezed_time, False),
        "timeISO": relative_time(imports, replace_values, freezed_time, True),
        "uuid": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
        "_replace_values": replace_values,
        "_imports": imports,
        "_given": given,
        "_key_to_json_path": defaultdict(dict),
        "_enable_operations": set()
    }

    yield ctx


@pytest.fixture
def freezed_time():
    from dateutil import parser

    return parser.isoparse("2021-11-11T11:11:11.111111+00:00")


@given('a valid "apiKeyAuth" key in the system')
def a_valid_api_key(context):
    """a valid API key."""
    context["has_api_key"] = True


@given('a valid "appKeyAuth" key in the system')
def a_valid_application_key(context):
    """a valid Application key."""
    context["has_application_key"] = True


@pytest.fixture(scope="module")
def specs():
    result = {}
    for f in (ROOT_PATH / ".generator" / "schemas").rglob("openapi.yaml"):
        version = f.parent.name
        result[version] = openapi.load(f)

    return result


@pytest.fixture(scope="module")
def operation_specs(specs):
    by_operation = {}

    for version, spec in specs.items():
        by_operation[version] = {}
        for path in spec["paths"]:
            if path.startswith("x-"):
                continue
            for method, operation in spec["paths"][path].items():
                by_operation[version][operation["operationId"]] = openapi.Operation(
                    operation["operationId"], operation, method, path
                )

    return by_operation


@pytest.fixture(scope="module")
def undo_operations():
    result = {}

    for f in (ROOT_PATH / "tests").rglob("undo.json"):
        version = f.parent.parent.name
        with f.open() as fp:
            result[version] = json.load(fp)

    return result


@given(parsers.parse('an instance of "{name}" API'))
def api(context, api_version, specs, name):
    """Return an API instance."""
    assert name in {tag["name"].replace(" ", "") for tag in specs[api_version]["tags"]}
    sanitized_name = name.replace("-", "")
    context["api_instance"] = {"name": sanitized_name}


@given(parsers.parse('operation "{name}" enabled'))
def operation_enabled(context, name):
    """Enable the unstable operation specific in the clause."""
    context["_enable_operations"].add(name)


@given(parsers.parse('new "{name}" request'), target_fixture="operation_id")
def api_request(context, operation_specs, api_version, name):
    """Call an endpoint."""
    context["api_request"] = {"operation_id": name, "kwargs": {}}
    operation_spec = operation_specs[api_version][name]
    try:
        context["api_request"]["schema"] = operation_spec.request()
    except KeyError:
        pass
    return name


@given(parsers.parse("body with value {data}"))
def request_body(request, context, data):
    """Set request body."""
    tpl = Template(data).render(**context)
    context["body"] = {
        "tpl": data,
        "value": json.loads(tpl),
    }


@given(parsers.parse('body from file "{path}"'))
def request_body_from_file(request, context, path, api_version):
    """Set request body."""
    body_file = ROOT_PATH / "tests" / api_version / "features" / path
    with body_file.open() as f:
        data = f.read()
    tpl = Template(data).render(**context)
    context["body"] = {
        "tpl": data,
        "value": json.loads(tpl),
    }


@given(parsers.parse('request contains "{name}" parameter from "{path}"'))
def request_parameter(context, operation_id, api_version, operation_specs, name, path):
    """Set request parameter."""
    try:
        value = lookup(context, path)
        value = value.value(value)  # trigger replacement recording
    except KeyError:
        if path != "REPLACE.ME":
            raise

        parameters = operation_specs[api_version][operation_id].spec["parameters"]
        for parameter in parameters:
            if parameter["name"] == name:
                schema = parameter.get("schema", {})
                value = schema.get("example", schema.get("default"))
                if value is None:
                    type_ = schema.get("type")
                    format_ = schema.get("format")
                    value = {
                        "string": {
                            "date-time": "2021-11-11T11:11:11.111+00:00",
                            None: name,
                        },
                        "integer": {
                            "int32": 1,
                            "int64": 9223372036854775807,
                            None: 1,
                        },
                        "array": {
                            None: [],
                        },
                    }[type_][format_]
                break

    context["api_request"]["kwargs"][name] = {
        "path": path,
        "value": value,
    }


@given(parsers.parse('request contains "{name}" parameter with value {value}'))
def request_parameter_with_value(context, name, value):
    """Set request parameter."""
    tpl = Template(value).render(**context)
    context["api_request"]["kwargs"][name] = {
        "tpl": value,
        "value": json.loads(tpl),
    }


def build_given(version, operation):
    def wrapper(context, operation_specs):

        undo_prefix = [operation["key"]]

        def make_path(keys):
            result = operation["key"] + "_" + "_".join(str(k) for k in keys)
            return result.upper()

        # store response in fixtures
        def record_value(schema):
            if "default" in schema.spec and "enum" in schema.spec:
                return schema.spec["default"]

            value = openapi.generate_value(schema)
            key = make_path(schema.keys)
            context["_given"][operation["step"]][key] = schema.spec
            if context["_replace_values"].get(value, key) != key:
                value = openapi.generate_value(schema, use_random=True, prefix=key)

            context["_replace_values"][value] = key
            keys = (
                [operation["source"]] + list(schema.keys)
                if "source" in operation
                else schema.keys
            )
            json_path = "".join(
                f"[{k}]" if isinstance(k, int) else f".{k}" for k in keys
            ).strip(".")
            assert (
                context["_key_to_json_path"][operation["key"]].get(key, json_path)
                == json_path
            )
            context["_key_to_json_path"][operation["key"]][key] = json_path
            return value

        operation_spec = operation_specs[version][operation["operationId"]]
        response_spec = operation_spec.response()
        if "source" in operation:
            response_spec = lookup(response_spec, operation["source"])
            undo_prefix.extend(response_spec.keys)

        response_spec.keys = ()
        response_spec.value = record_value
        response_spec.__source__ = operation.get("source")

        context[operation["key"]] = response_spec

    return wrapper


for f in (ROOT_PATH / "tests").rglob("given.json"):
    version = f.parent.parent.name
    with f.open() as fp:
        for settings in json.load(fp):
            given(settings["step"])(build_given(version, settings))


@when("the request is sent")
def execute_request(context):
    """Execute the prepared request."""
    assert context["api_request"]["operation_id"] is not None


@when("the request with pagination is sent")
def execute_request_with_pagination(context):
    context["pagination"] = True


@then(parsers.parse("the response status is {status:d} {description}"))
def the_status_is(context, status, description):
    """Check the status."""
    context["status_code"] = status


@then(parsers.parse('the response "{response_path}" is equal to {value}'))
def expect_equal(context, response_path, value):
    """Compare a response attribute to a value."""


@then(
    parsers.parse(
        'the response "{response_path}" has the same value as "{fixture_path}"'
    )
)
def expect_equal_value(context, response_path, fixture_path):
    """Compare a response attribute to another attribute."""


@then(parsers.parse('the response "{response_path}" has length {fixture_length:d}'))
def expect_equal_length(context, response_path, fixture_length):
    """Check the length of a response attribute."""


@then(parsers.parse("the response has {fixture_length:d} items"))
def expect_equal_response_items(context, fixture_length):
    """Check the size of a response."""


@then(parsers.parse('the response "{response_path}" is false'))
def expect_false(context, response_path):
    """Check that a response attribute is false."""


@then(parsers.parse('the response "{response_path}" has field "{field}"'))
def expect_response_has_field(context, response_path, field):
    """Check that a response has field."""


@then(parsers.parse('the response "{response_path}" does not have field "{field}"'))
def expect_response_does_not_have_field(context, response_path, field):
    """Check that a response path does not have field."""


@then(parsers.parse('the response "{response_path}" has item with field "{key_path}" with value {value}'))
def expect_array_contains_object(context, response_path, key_path, value):
    """Check that a response attribute contains an object with the specified key and value."""


@then(parsers.parse('the response "{response_path}" array contains value {value}'))
def expect_array_contains_object(context, response_path, value):
    """Check that a response array contains the specified value."""
