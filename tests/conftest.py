# coding=utf-8
"""Define basic fixtures."""

import os

# First patch httplib
tracer = None
try:
    from ddtrace import config, patch, tracer

    if os.getenv("RECORD", "false") != "none":
        from ddtrace.internal.writer import AgentWriter

        class Writer(AgentWriter):
            def is_alive(self):
                return True

            def stop(self):
                self.flush_queue()

            def join(self, **kwargs):
                """No thread is started therefore no join is needed."""

            def write(self, *args, **kwargs):
                # make sure the thread won't get started
                self._started = True
                super(Writer, self).write(*args, **kwargs)

        tracer.writer.stop()
        tracer.writer = Writer(
            hostname=tracer.writer._hostname,
            port=tracer.writer._port,
            uds_path=tracer.writer._uds_path,
            https=tracer.writer._https,
        )

        import pytest

        @pytest.hookimpl(trylast=True)
        def pytest_configure(config):
            """Make sure the tracer on pin is the same as global one."""
            from ddtrace.pin import Pin

            pin = Pin.get_from(config)
            if pin:
                pin.tracer.writer = tracer.writer

    config.httplib["distributed_tracing"] = True
    patch(httplib=True)
except ImportError:
    pass

import importlib
import json
import logging
import pathlib
import re
import warnings
from datetime import datetime, timedelta

import pytest
from jinja2 import Template
from pytest_bdd import (
    given,
    parsers,
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


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    span = getattr(step_func, "__dd_span__", None)
    if span is not None:
        span.set_exc_info(type(exception), exception, exception.__traceback__)
        span.finish()


def pytest_bdd_apply_tag(tag, function):
    """Register tags as custom markers and skip test for '@skip' ones."""
    skip_tags = {"skip", "skip-python"}
    if not _disable_recording():
        # ignore integration-only scenarios if the recording is enabled
        skip_tags.add("integration-only")
    if tag in skip_tags:
        marker = pytest.mark.skip(reason=f"skipped because '{tag}' in {skip_tags}")
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
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    s1 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    s1 = re.sub(r"\W", "_", s1)
    s1 = re.sub(r"_+$", "", s1)
    return re.sub(r"__+", "_", s1)


def glom(value, path):
    from glom import glom as g

    # replace foo[index].bar by foo.index.bar
    return g(value, re.sub(r"\[([0-9]*)\]", r".\1", path))


def _get_prefix(request):
    test_class = request.cls
    if test_class:
        main = "{}.{}".format(test_class.__name__, request.node.name)
    else:
        base_name = request.node.__scenario_report__.scenario.name
        main = re.sub(r"[^A-Za-z0-9]+", "_", base_name)[:100]
    prefix = "Test-Python" if _disable_recording() else "Test"
    return f"{prefix}-{main}"


@pytest.fixture
def unique(request, freezer):
    prefix = _get_prefix(request)
    with freezer:
        return f"{prefix}-{int(datetime.now().timestamp())}"


@pytest.fixture
def unique_lower(request, freezer):
    prefix = _get_prefix(request).lower()
    with freezer:
        return f"{prefix}-{int(datetime.now().timestamp())}"


@pytest.fixture
def now_ts(freezer):
    with freezer:
        return int(datetime.now().timestamp())


@pytest.fixture
def now_iso(freezer):
    with freezer:
        return datetime.now().isoformat(timespec="seconds")


@pytest.fixture
def hour_later_ts(freezer):
    with freezer:
        return int((datetime.now() + timedelta(hours=1)).timestamp())


@pytest.fixture
def hour_later_iso(freezer):
    with freezer:
        return (datetime.now() + timedelta(hours=1)).isoformat(timespec="seconds")


@pytest.fixture
def hour_ago_ts(freezer):
    with freezer:
        return int((datetime.now() + timedelta(hours=-1)).timestamp())


@pytest.fixture
def hour_ago_iso(freezer):
    with freezer:
        return (datetime.now() + timedelta(hours=-1)).isoformat(timespec="seconds")

@pytest.fixture
def context(vcr, unique, unique_lower, now_ts, now_iso, hour_later_ts, hour_later_iso, hour_ago_ts, hour_ago_iso):
    """
    Return a mapping with all defined fixtures, all objects created by `given` steps,
    and the undo operations to perform after a test scenario.
    """
    ctx = {
        "undo_operations": [],
        "unique": unique,
        "unique_lower": unique_lower,
        "unique_alnum": re.sub(r"[^A-Za-z0-9]+", "", unique),
        "unique_lower_alnum": re.sub(r"[^A-Za-z0-9]+", "", unique).lower(),
        "now_ts": now_ts,
        "now_iso": now_iso,
        "hour_later_ts": hour_later_ts,
        "hour_later_iso": hour_later_iso,
        "hour_ago_ts": hour_ago_ts,
        "hour_ago_iso": hour_ago_iso,
    }

    yield ctx

    for undo in reversed(ctx["undo_operations"]):
        undo()


@pytest.fixture(scope="session")
def record_mode(request):
    """Manage compatibility with DD client libraries."""
    return {
        "false": "none",
        "true": "rewrite",
        "none": "new_episodes",
    }[os.getenv("RECORD", "false").lower()]


def _disable_recording():
    """Disable VCR.py integration."""
    return os.getenv("RECORD", "false").lower() == "none"


@pytest.fixture(scope="session")
def disable_recording(request):
    """Disable VCR.py integration."""
    return _disable_recording()


@pytest.fixture
def vcr_config():
    config = dict(
        filter_headers=("DD-API-KEY", "DD-APPLICATION-KEY"),
        filter_query_parameters=("api_key", "application_key"),
        match_on=['method', 'scheme', 'host', 'port', 'path', 'query', 'body']
    )
    if tracer:
        config["ignore_hosts"] = [tracer.writer._hostname]

    return config


@pytest.fixture
def freezer(default_cassette_name, record_mode, vcr):
    from freezegun import freeze_time
    from dateutil import parser

    if record_mode in {"new_episodes", "rewrite"}:
        tzinfo = datetime.now().astimezone().tzinfo
        freeze_at = datetime.now().replace(tzinfo=tzinfo).isoformat()
        if record_mode == "rewrite":
            pathlib.Path(vcr._path).parent.mkdir(parents=True, exist_ok=True)
            with pathlib.Path(vcr._path).with_suffix(".frozen").open("w+") as f:
                f.write(freeze_at)
    else:
        with pathlib.Path(vcr._path).with_suffix(".frozen").open("r") as f:
            freeze_at = f.readline().strip()

    return freeze_time(parser.isoparse(freeze_at))


@given('a valid "apiKeyAuth" key in the system')
def a_valid_api_key(configuration):
    """a valid API key."""
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "fake")


@given('a valid "appKeyAuth" key in the system')
def a_valid_application_key(configuration):
    """a valid Application key."""
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "fake")


@pytest.fixture
def _package(package_name):
    return importlib.import_module(package_name)


@pytest.fixture(scope="module")
def undo_operations(package_name):
    version = package_name.split(".")[-1]
    with open(os.path.join(os.path.dirname(__file__), version, "features", "undo.json")) as fp:
        data = json.load(fp)

    return {snake_case(operation_id): settings.get("undo") for operation_id, settings in data.items()}


def build_configuration(package):
    c = package.Configuration()
    c.connection_pool_maxsize = 0
    c.debug = debug = os.getenv("DEBUG") in {"true", "1", "yes", "on"}
    if debug:  # enable vcr logs for DEBUG=true
        vcr_log = logging.getLogger("vcr")
        vcr_log.setLevel(logging.INFO)
    if "DD_TEST_SITE" in os.environ:
        c.server_index = 2
        c.server_variables["site"] = os.environ["DD_TEST_SITE"]
    return c


@pytest.fixture
def configuration(_package):
    return build_configuration(_package)


@pytest.fixture
def client(_package, context, configuration):
    with _package.ApiClient(configuration) as api_client:
        yield api_client


@given(parsers.parse('an instance of "{name}" API'))
def api(context, package_name, client, name):
    """Return an API instance."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.api.{module_name}_api")
    context["api"] = {
        "api": getattr(package, name + "Api")(client),
        "package": package_name,
        "calls": [],
    }


@given(parsers.parse('operation "{name}" enabled'))
def operation_enabled(client, name):
    """Enable the unstable operation specific in the clause."""
    client.configuration.unstable_operations[snake_case(name)] = True


@given(parsers.parse('new "{name}" request'))
def api_request(configuration, context, name):
    """Call an endpoint."""
    api = context["api"]
    context["api_request"] = {
        "api": api["api"],
        "request": getattr(api["api"], snake_case(name)),
        "args": [],
        "kwargs": {
            "_host_index": configuration.server_index,
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
    tpl = Template(data).render(**context)
    context["api_request"]["kwargs"]["body"] = json.loads(tpl)


@given(parsers.parse('request contains "{name}" parameter from "{path}"'))
def request_parameter(context, name, path):
    """Set request parameter."""
    context["api_request"]["kwargs"][snake_case(name)] = glom(context, path)


@given(parsers.parse('request contains "{name}" parameter with value {value}'))
def request_parameter_with_value(context, name, value):
    """Set request parameter."""
    tpl = Template(value).render(**context)
    context["api_request"]["kwargs"][snake_case(name)] = json.loads(tpl)


def build_given(version, operation):
    def wrapper(context, undo):
        name = operation["tag"].replace(" ", "")
        module_name = snake_case(operation["tag"])
        operation_name = snake_case(operation["operationId"])
        package_name = f"datadog_api_client.{version}"

        # make sure we have a fresh instance of API client and configuration
        configuration = build_configuration(importlib.import_module(package_name))
        configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "fake")
        configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "fake")

        # enable unstable operation
        configuration.unstable_operations[operation_name] = True

        package = importlib.import_module(f"{package_name}.api.{module_name}_api")
        with package.ApiClient(configuration) as client:
            api = getattr(package, name + "Api")(client)
            operation_method = getattr(api, operation_name)

            # perform operation
            def build_param(p):
                if "value" in p:
                    return json.loads(Template(p["value"]).render(**context))
                if "source" in p:
                    return glom(context, p["source"])

            kwargs = {snake_case(p["name"]): build_param(p) for p in operation.get("parameters", [])}
            kwargs["_check_input_type"] = False
            result = operation_method(**kwargs)
            client.last_response.urllib3_response.close()

            # register undo method
            context["undo_operations"].append(lambda: undo(api, operation_name, result, client=client))

            # optional re-shaping
            if "source" in operation:
                result = glom(result, operation["source"])

            # store response in fixtures
            context[operation["key"]] = result

            # Make sure that all connections are released
            client.rest_client.pool_manager.clear()

    return wrapper


for f in pathlib.Path(os.path.dirname(__file__)).rglob("given.json"):
    version = f.parent.parent.name
    with f.open() as fp:
        for settings in json.load(fp):
            given(settings["step"])(build_given(version, settings))


@pytest.fixture
def undo(package_name, undo_operations, client):
    """Clean after operation."""
    exceptions = importlib.import_module(package_name + ".exceptions")

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
        args = [glom(response, parameter["source"]) for parameter in operation.get("parameters", [])]

        if operation_name in client.configuration.unstable_operations:
            client.configuration.unstable_operations[operation_name] = True

        try:
            method(*args)
            client.last_response.urllib3_response.close()
        except exceptions.ApiException as e:
            warnings.warn(f"failed undo: {e}")

    yield cleanup


@when("the request is sent")
def execute_request(undo, context, client, _package):
    """Execute the prepared request."""
    api_request = context["api_request"]
    exceptions = importlib.import_module(context["api"]["package"] + ".exceptions")

    try:
        response = api_request["request"](
            *api_request["args"], **api_request["kwargs"]
        )
        client.last_response.urllib3_response.close()
        # Reserialise the response body to JSON to facilitate test assertions
        response_body_json = _package.api_client.ApiClient.sanitize_for_serialization(response[0])
        api_request["response"] = [response_body_json, response[1], response[2]]
    except exceptions.ApiException as e:
        # If we have an exception, make a stub response object to use for assertions
        # Instead of finding the response class of the method, we use the fact that all
        # responses returned have an ordered response of body|status|headers
        api_request["response"] = [e.body, e.status, e.headers]
        return

    api = api_request["api"]
    operation_id = api_request["request"].__name__
    response = api_request["response"][0]

    context["undo_operations"].append(lambda: undo(api, operation_id, response))


@then(parsers.parse('I should get an instance of "{name}"'))
def i_should_get_an_instance_of(context, package_name, name):
    """I should get an instance."""
    module_name = snake_case(name)
    package = importlib.import_module(f"{package_name}.model.{module_name}")
    assert isinstance(context["api_request"]["response"][0], getattr(package, name))


@then(parsers.parse('I should get a list of "{name}" objects'))
def i_should_get_a_list_of_objects(context, package_name, name):
    """I should get a list of objects."""
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
    response_value = glom(context["api_request"]["response"][0], response_path)
    test_value = json.loads(Template(value).render(**context))
    assert test_value == response_value


@then(parsers.parse('the response "{response_path}" has the same value as "{fixture_path}"'))
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
