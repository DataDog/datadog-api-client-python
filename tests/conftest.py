# coding=utf-8
"""Define basic fixtures."""

# First patch httplib
from ddtrace import config, patch

config.httplib["distributed_tracing"] = True
patch(httplib=True)

import importlib
import logging
import os
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store outcome for tracing."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "dd_outcome", rep)


def pytest_sessionfinish(session, exitstatus):
    """Flush open tracer."""
    from ddtrace import tracer

    tracer.shutdown()


@pytest.fixture(scope="function")
def ddspan(request):
    from ddtrace import tracer
    from ddtrace.constants import ANALYTICS_SAMPLE_RATE_KEY

    tags = [marker.kwargs for marker in request.node.iter_markers(name="dd_tags")]

    with tracer.trace("test", resource=request.node.name, span_type="test") as span:
        span.set_tag(ANALYTICS_SAMPLE_RATE_KEY, True)

        for tag in tags:
            for key, value in tag.items():
                span.set_tag(key, value)

        yield span

        outcome = request.node.dd_outcome
        if outcome.failed:
            span.set_exc_info(sys.last_type, sys.last_value, sys.last_traceback)


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    from ddtrace import tracer

    context = tracer.get_call_context()
    span = tracer.start_span(
        step.type,
        resource=f"{step.type.title()} {step.name}",
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
        pytest.set_trace()
        span.finish()


def pytest_bdd_apply_tag(tag, function):
    """Register tags as custom markers and skip test for 'todo' ones."""
    from pytest_bdd.utils import CONFIG_STACK

    config = CONFIG_STACK[-1]
    config.addinivalue_line("markers", f"{tag}: marker from feature")

    if tag in {"todo", "todo-python"}:
        marker = pytest.mark.skip(reason="Not implemented yet")
        marker(function)
        return True
    elif tag.startswith("endpoint("):
        version = tag[len("endpoint(") : -1]
        marker = pytest.mark.dd_tags(version=version)
        marker(function)
        return True
    else:
        # Fall back to pytest-bdd's default behavior
        return None


def snake_case(value):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", value)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


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
            return f"datadog-api-client-python-{prefix}-{datetime.now().timestamp()}"

        def __str__(self):
            return self()

    return Lazy()


@pytest.fixture
def fixtures(request, unique):
    """Return a mapping with all defined fixtures."""
    ctx = {}
    for f in request.fixturenames:
        if f == "fixtures":
            continue
        try:
            ctx[f] = request.getfixturevalue(f)
        except Exception:
            pass
    return ctx


@pytest.fixture(scope="module", autouse=True)
def record_mode(request):
    """Manage compatibility with DD client libraries."""
    mode = os.getenv("RECORD")
    if mode is not None:
        if mode == "none":
            request.config.option.disable_vcr = True
        else:
            setattr(
                request.config.option,
                "vcr_record",
                {"true": "all", "false": "none",}[mode],
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
def freezer(vcr_cassette_name, vcr_cassette, vcr):
    from freezegun import freeze_time
    from dateutil import parser

    if vcr_cassette.record_mode != "none":
        tzinfo = datetime.now().astimezone().tzinfo
        freeze_at = datetime.now().replace(tzinfo=tzinfo).isoformat()
        with open(
            os.path.join(vcr.cassette_library_dir, vcr_cassette_name + ".frozen"), "w",
        ) as f:
            f.write(freeze_at)
    else:
        with open(
            os.path.join(vcr.cassette_library_dir, vcr_cassette_name + ".frozen"), "r",
        ) as f:
            freeze_at = f.readline().strip()

    return freeze_time(parser.isoparse(freeze_at))


@given('a valid "apiKeyAuth" key')
def a_valid_api_key(configuration):
    """a valid API key."""
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY")


@given('a valid "appKeyAuth" key')
def a_valid_application_key(configuration):
    """a valid Application key."""
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY")


@pytest.fixture
def _package(package_name):
    return importlib.import_module(package_name)


@pytest.fixture
def configuration(_package):
    c = _package.Configuration()
    c.debug = debug = os.getenv("DEBUG") in {"true", "1", "yes", "on"}
    if debug:  # enable vcr logs for DEBUG=true
        vcr_log = logging.getLogger("vcr")
        vcr_log.setLevel(logging.INFO)
    return c


@pytest.fixture
def client(_package, configuration, ddspan):
    with _package.ApiClient(configuration) as api_client:
        yield api_client


@given(parsers.parse('an instance of "{name}" API'))
def api(package_name, client, name):
    """Return an API instance."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.api.{module_name}_api")
    return {
        "api": getattr(package, name + "Api")(client),
        "calls": [],
    }


@given(parsers.parse('new "{name}" request'))
def api_request(api, name):
    """Call an endpoint."""
    return {
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
def request_body(fixtures, api_request, data):
    """Set request body."""
    import json
    from jinja2 import Template

    tpl = Template(data).render(**fixtures)
    body = api_request["kwargs"]["body"] = json.loads(tpl)

    return body


@given(parsers.parse("parameter {name} from {path}"))
def request_parameter(fixtures, api_request, name, path):
    """Set request parameter."""
    from glom import glom

    api_request["kwargs"][name] = parameter = glom(fixtures, path)
    return parameter


def undo(api_request):
    """Clean after operation."""
    operation_id = api_request["request"].settings["operation_id"]
    if operation_id == "create_user":
        return api_request["api"].disable_user(api_request["response"][0].data.id)
    elif operation_id == "create_role":
        return api_request["api"].delete_role(api_request["response"][0].data.id)
    elif operation_id in {"update_user", "add_permission_to_role"}:
        return
    elif api_request["request"].settings["http_method"] == "PATCH":
        return
    raise NotImplementedError(operation_id)


@when("I execute the request")
def execute_request(api_request):
    api_request["response"] = api_request["request"].call_with_http_info(
        *api_request["args"], **api_request["kwargs"]
    )
    # TODO define clean-up methods
    if api_request["request"].settings["http_method"] not in {
        "GET",
        "HEAD",
        "OPTIONS",
        "DELETE",
    }:
        undo(api_request)


@then(parsers.parse('I should get an instance of "{name}"'))
def i_should_get_an_instace_of(package_name, api, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.model.{module_name}")
    assert isinstance(api_request["response"][0], getattr(package, name))


@then(parsers.parse('I should get a list of "{name}" objects'))
def i_should_get_a_list_of_objects(package_name, api, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.model.{module_name}")
    cls = getattr(package, name)
    assert all(isinstance(obj, cls) for obj in api_request["response"][0])


@then(parsers.parse("the status is {status:d} {description}"))
def the_status_is(api_request, status, description):
    """Check the status."""
    assert status == api_request["response"][1]
