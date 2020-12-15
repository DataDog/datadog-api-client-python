# coding=utf-8
"""Define basic fixtures."""

import os

# First patch httplib
tracer = None
try:
    from ddtrace import config, patch, tracer

    config.httplib["distributed_tracing"] = True
    patch(httplib=True)
except ImportError:
    pass

import importlib
import json
import logging
import pathlib
import re
import sys
import time
import warnings
from datetime import datetime

import pytest
from pytest_bdd import (
    given,
    parsers,
    scenarios,
    then,
    when,
)

logging.basicConfig()


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    if tracer is None:
        return

    context = tracer.get_call_context()
    span = tracer.start_span(
        step.type,
        resource=step.name,
        span_type=step.type,
        child_of=context,
    )
    setattr(step_func, "__dd_span__", span)


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    span = getattr(step_func, "__dd_span__", None)
    if span is not None:
        span.finish()


def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception
):
    span = getattr(step_func, "__dd_span__", None)
    if span is not None:
        span.set_exc_info(type(exception), exception, exception.__traceback__)
        span.finish()


def pytest_bdd_apply_tag(tag, function):
    """Register tags as custom markers and skip test for '@skip' ones."""
    if tag in {"skip", "skip-python"}:
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    elif tag.startswith("endpoint("):
        version = tag[len("endpoint(") : -1]
        marker = pytest.mark.dd_tag(version=version)
        marker(function)
        return True
    else:
        from pytest_bdd.utils import CONFIG_STACK

        config = CONFIG_STACK[-1]
        config.addinivalue_line("markers", f"{tag}: marker from feature")

        # Fall back to pytest-bdd's default behavior
        return None


def snake_case(value):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
    s1 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    s1 = re.sub(r"\W", "_", s1)
    s1 = re.sub(r"_+$", "", s1)
    return re.sub(r"__+", "_", s1)


def glom(value, path):
    from glom import glom as g

    # replace foo[index].bar by foo.index.bar
    return g(value, re.sub("\[([0-9]*)\]", ".\\1", path))


@pytest.fixture
def unique(request, freezer):
    test_class = request.cls
    if test_class:
        prefix = "{}.{}".format(test_class.__name__, request.node.name)
    else:
        prefix = request.node.name

    class Lazy:
        @staticmethod
        def __call__():
            with freezer:
                return (
                    f"datadog-api-client-python-{prefix}-{datetime.now().timestamp()}"
                )

        def __str__(self):
            return self()

    return Lazy()


@pytest.fixture
def unique_lower(request, freezer):
    test_class = request.cls
    if test_class:
        prefix = "{}.{}".format(test_class.__name__, request.node.name)
    else:
        prefix = request.node.name

    class Lazy:
        @staticmethod
        def __call__():
            with freezer:
                return f"datadog-api-client-python-{prefix}-{datetime.now().timestamp()}".lower()

        def __str__(self):
            return self()

    return Lazy()


@pytest.fixture
def context(package_name, request, unique, unique_lower):
    """
    Return a mapping with all defined fixtures, all objects created by `given` steps,
    and the undo operations to perform after a test scenario.
    """
    ctx = {
        "undo_operations": [],
        "unique": unique,
        "unique_lower": unique_lower,
    }

    yield ctx

    exceptions = importlib.import_module(package_name + ".exceptions")
    for undo in reversed(ctx["undo_operations"]):
        try:
            undo()
        except exceptions.ApiException as e:
            warnings.warn(str(e))


@pytest.fixture(scope="module", autouse=True)
def record_mode(request):
    """Manage compatibility with DD client libraries."""
    mode = os.getenv("RECORD", "false")
    if mode is not None:
        if mode == "none":
            request.config.option.disable_vcr = True
        else:
            setattr(
                request.config.option,
                "vcr_record",
                {
                    "true": "all",
                    "false": "none",
                }[mode],
            )
            request.config.option.disable_vcr = False
    return mode


@pytest.fixture(scope="module")
def vcr_config(record_mode):
    config = dict(
        filter_headers=("DD-API-KEY", "DD-APPLICATION-KEY"),
        filter_query_parameters=("api_key", "application_key"),
    )
    return config


@pytest.fixture
def freezer(vcr_cassette_name, record_mode, vcr):
    from freezegun import freeze_time
    from dateutil import parser

    if record_mode != "false":
        tzinfo = datetime.now().astimezone().tzinfo
        freeze_at = datetime.now().replace(tzinfo=tzinfo).isoformat()
        if record_mode == "true":
            pathlib.Path(vcr.cassette_library_dir).mkdir(parents=True, exist_ok=True)
            with open(
                os.path.join(vcr.cassette_library_dir, vcr_cassette_name + ".frozen"),
                "w+",
            ) as f:
                f.write(freeze_at)
    else:
        with open(
            os.path.join(vcr.cassette_library_dir, vcr_cassette_name + ".frozen"),
            "r",
        ) as f:
            freeze_at = f.readline().strip()

    return freeze_time(parser.isoparse(freeze_at))


@given('a valid "apiKeyAuth" key in the system')
def a_valid_api_key(configuration):
    """a valid API key."""
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "")


@given('a valid "appKeyAuth" key in the system')
def a_valid_application_key(configuration):
    """a valid Application key."""
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "")


@pytest.fixture
def _package(package_name):
    return importlib.import_module(package_name)


@pytest.fixture(scope="module")
def undo_operations(package_name):
    version = package_name.split(".")[-1]
    with open(
        os.path.join(os.path.dirname(__file__), version, "features", "undo.json")
    ) as fp:
        data = json.load(fp)

    return {
        snake_case(operation_id): settings.get("undo")
        for operation_id, settings in data.items()
    }


@pytest.fixture
def configuration(_package):
    c = _package.Configuration()
    c.debug = debug = os.getenv("DEBUG") in {"true", "1", "yes", "on"}
    if debug:  # enable vcr logs for DEBUG=true
        vcr_log = logging.getLogger("vcr")
        vcr_log.setLevel(logging.INFO)
    return c


@pytest.fixture
def client(_package, configuration, record_mode, vcr_cassette):
    if record_mode == "true" and os.path.exists(vcr_cassette._path):
        os.remove(vcr_cassette._path)
        vcr_cassette.data.clear()

    with _package.ApiClient(configuration) as api_client:
        print(f"starting with {vcr_cassette}")
        yield api_client



@given(parsers.parse('an instance of "{name}" API'))
def api(context, package_name, client, name):
    """Return an API instance."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.api.{module_name}_api")
    context["api"] = {
        "api": getattr(package, name + "Api")(client),
        "calls": [],
    }


@given(parsers.parse('operation "{name}" enabled'))
def operation_enabled(client, name):
    """Enable the unstable operation specific in the clause."""
    client.configuration.unstable_operations[snake_case(name)] = True


@given(parsers.parse('new "{name}" request'))
def api_request(context, name):
    """Call an endpoint."""
    api = context["api"]
    context["api_request"] = {
        "api": api["api"],
        "request": getattr(api["api"], snake_case(name)),
        "args": [],
        "kwargs": {
            "_host_index": 0,
            "_check_input_type": False,
            "async_req": False,
            "_check_return_type": True,
            "_return_http_data_only": False,
            "_preload_content": True,
            "_request_timeout": None,
        },
        "response": (None, None, None),
    }


@given(parsers.parse("body {data}"))
def request_body(context, data):
    """Set request body."""
    import json
    from jinja2 import Template

    tpl = Template(data).render(**context)
    context["api_request"]["kwargs"]["body"] = json.loads(tpl)


@given(parsers.parse('request contains "{name}" parameter from "{path}"'))
def request_parameter(context, name, path):
    """Set request parameter."""
    context["api_request"]["kwargs"][snake_case(name)] = glom(context, path)


@given(parsers.parse('request contains "{name}" parameter with value {value}'))
def request_parameter_with_value(context, name, value):
    """Set request parameter."""
    import json
    from jinja2 import Template

    tpl = Template(value).render(**context)
    context["api_request"]["kwargs"][snake_case(name)] = json.loads(tpl)


@pytest.fixture
def undo(undo_operations, client):
    """Clean after operation."""

    def cleanup(api, operation_id, response, client=client):
        if operation_id not in undo_operations:
            raise NotImplementedError(operation_id)

        operation = undo_operations[operation_id]
        if operation["type"] is None:
            raise NotImplementedError(operation_id)

        if operation["type"] != "unsafe":
            return

        operation_name = snake_case(operation["operationId"])
        method = getattr(api, operation_name)
        args = [
            glom(response, parameter["source"])
            for parameter in operation.get("parameters", [])
        ]

        if operation_name in client.configuration.unstable_operations:
            client.configuration.unstable_operations[operation_name] = True

        return method(*args)

    return cleanup


@when("the request is sent")
def execute_request(undo, context, client):
    """Execute the prepared request."""
    api_request = context["api_request"]
    api_request["response"] = api_request["request"].call_with_http_info(
        *api_request["args"], **api_request["kwargs"]
    )

    api = api_request["api"]
    operation_id = api_request["request"].settings["operation_id"]
    response = api_request["response"][0]

    context["undo_operations"].append(lambda: undo(api, operation_id, response))


@then(parsers.parse('I should get an instance of "{name}"'))
def i_should_get_an_instace_of(context, package_name, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.model.{module_name}")
    assert isinstance(context["api_request"]["response"][0], getattr(package, name))


@then(parsers.parse('I should get a list of "{name}" objects'))
def i_should_get_a_list_of_objects(context, package_name, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.model.{module_name}")
    cls = getattr(package, name)
    assert all(isinstance(obj, cls) for obj in context["api_request"]["response"][0])


@then(parsers.parse("the response status is {status:d} {description}"))
def the_status_is(context, status, description):
    """Check the status."""
    assert status == context["api_request"]["response"][1]


@then(parsers.parse('the response "{response_path}" is equal to {value}'))
def expect_equal(context, response_path, value):
    from jinja2 import Template

    response_value = glom(context["api_request"]["response"][0], response_path)
    test_value = json.loads(Template(value).render(**context))
    assert test_value == response_value


@then(
    parsers.parse(
        'the response "{response_path}" has the same value as "{fixture_path}"'
    )
)
def expect_equal_value(context, response_path, fixture_path):
    fixture_value = glom(context, fixture_path)
    response_value = glom(context["api_request"]["response"][0], response_path)
    assert fixture_value == response_value


@then(parsers.parse('the response "{response_path}" has length {fixture_length:d}'))
def expect_equal_length(context, response_path, fixture_length):
    response_value = glom(context["api_request"]["response"][0], response_path)
    assert fixture_length == len(response_value)


@then(parsers.parse('the response "{response_path}" is false'))
def expect_false(context, response_path):
    response_value = glom(context["api_request"]["response"][0], response_path)
    assert not response_value
