# coding=utf-8
"""Define basic fixtures."""

import os

RECORD = os.getenv("RECORD", "false").lower()
SLEEP_AFTER_REQUEST = int(os.getenv("SLEEP_AFTER_REQUEST", "0"))

# First patch urllib
tracer = None
try:
    from ddtrace import patch, tracer

    if RECORD != "none":
        from ddtrace.internal.writer import AgentWriter

        writer = AgentWriter(
            tracer.writer.agent_url,
            sync_mode=True,
            priority_sampler=tracer.priority_sampler,
        )
        tracer.configure(writer)

    patch(urllib3=True)

    from pytest import hookimpl

    @hookimpl(hookwrapper=True)
    def pytest_terminal_summary(terminalreporter, exitstatus, config):
        yield  # do normal output

        ci_pipeline_id = os.getenv("GITHUB_RUN_ID", None)
        dd_service = os.getenv("DD_SERVICE", None)
        if ci_pipeline_id and dd_service:
            terminalreporter.ensure_newline()
            terminalreporter.section("test reports", purple=True, bold=True)
            terminalreporter.line(
                "* View test APM traces and detailed time reports on Datadog (can take a few minutes to become available):"
            )
            terminalreporter.line(
                "* https://app.datadoghq.com/ci/test-runs?query="
                "%40test.service%3A{}%20%40ci.pipeline.id%3A{}&index=citest".format(dd_service, ci_pipeline_id)
            )

except ImportError:
    if os.getenv("CI", "false") == "true" and RECORD == "none":
        raise

import importlib
import functools
import json
import logging
import pathlib
import re
import time
import warnings
from datetime import datetime

import pytest
from dateutil.relativedelta import relativedelta
from jinja2 import Template, Environment, meta
from pytest_bdd import given, parsers, then, when

logging.basicConfig()

PATTERN_ALPHANUM = re.compile(r"[^A-Za-z0-9]+")
PATTERN_DOUBLE_UNDERSCORE = re.compile(r"__+")
PATTERN_LEADING_ALPHA = re.compile(r"(.)([A-Z][a-z]+)")
PATTERN_FOLLOWING_ALPHA = re.compile(r"([a-z0-9])([A-Z])")
PATTERN_WHITESPACE = re.compile(r"\W")
PATTERN_INDEX = re.compile(r"\[([0-9]*)\]")


def sleep_after_request(f):
    """Sleep after each request."""
    if RECORD == "false" or SLEEP_AFTER_REQUEST <= 0:
        return f

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        time.sleep(SLEEP_AFTER_REQUEST)
        return result

    return wrapper


def escape_reserved_keyword(word):
    """Escape reserved language keywords like openapi generator does it.

    :param word: Word to escape
    :return: The escaped word if it was a reserved keyword, the word unchanged otherwise
    """
    reserved_keywords = ["from"]
    if word in reserved_keywords:
        return f"_{word}"
    return word


def pytest_bdd_before_scenario(request, feature, scenario):
    if tracer is not None:
        span = tracer.current_span()
        if span is not None:
            span.set_tag("test.name", scenario.name)
            span.set_tag("test.suite", scenario.feature.filename.split("tests")[-1])

            codeowners = [f"@{tag[5:]}" for tag in scenario.tags | scenario.feature.tags if tag.startswith("team:")]
            if codeowners:
                span.set_tag("test.codeowners", json.dumps(codeowners))

    skip_tags = {"skip", "skip-python"}
    if RECORD != "none":
        # ignore integration-only scenarios if the recording is enabled
        skip_tags.add("integration-only")
    if RECORD != "false":
        skip_tags.add("replay-only")

    skipped_tags = [tag for tag in scenario.tags | scenario.feature.tags if tag in skip_tags]
    if skipped_tags:
        pytest.skip(f"skipped because of following tag(s): {', '.join(skipped_tags)}")


def pytest_bdd_after_scenario(request, feature, scenario):
    try:
        ctx = request.getfixturevalue("context")
    except Exception:
        return
    for undo in reversed(ctx["undo_operations"]):
        undo()


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    if tracer is None:
        return

    span = tracer.start_span(
        step.type,
        resource=step.name,
        span_type=step.type,
        child_of=tracer.current_span(),
        activate=True,
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
    """Do not register tags as custom markers."""
    return True


def snake_case(value):
    s1 = PATTERN_LEADING_ALPHA.sub(r"\1_\2", value)
    s1 = PATTERN_FOLLOWING_ALPHA.sub(r"\1_\2", s1).lower()
    s1 = PATTERN_WHITESPACE.sub("_", s1)
    s1 = s1.rstrip("_")
    return PATTERN_DOUBLE_UNDERSCORE.sub("_", s1)


def glom(value, path):
    from glom import glom as g

    # replace foo[index].bar by foo.index.bar
    path = PATTERN_INDEX.sub(r".\1", path)

    return g(value, path) if path else value


def _get_prefix(request):
    test_class = request.cls
    if test_class:
        main = "{}.{}".format(test_class.__name__, request.node.name)
    else:
        base_name = request.node.__scenario_report__.scenario.name
        main = PATTERN_ALPHANUM.sub("_", base_name)[:100]
    prefix = "Test-Python" if _disable_recording() else "Test"
    return f"{prefix}-{main}"


@pytest.fixture
def unique(request, freezer):
    prefix = _get_prefix(request)
    with freezer:
        return f"{prefix}-{int(datetime.utcnow().timestamp())}"


def relative_time(freezer, iso):
    time_re = re.compile(r"now( *([+-]) *(\d+)([smhdMy]))?")

    def func(arg):
        with freezer:
            ret = datetime.now()
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
                if iso:
                    return ret  # return datetime object and not string
                    # NOTE this is not a full ISO 8601 format, but it's enough for our needs
                    # return ret.strftime('%Y-%m-%dT%H:%M:%S') + ret.strftime('.%f')[:4] + 'Z'
                return int(ret.timestamp())
            return ""

    return func


@pytest.fixture
def context(vcr, unique, freezer):
    """
    Return a mapping with all defined fixtures, all objects created by `given` steps,
    and the undo operations to perform after a test scenario.
    """
    ctx = {
        "undo_operations": [],
        "unique": unique,
        "unique_lower": unique.lower(),
        "unique_upper": unique.upper(),
        "unique_alnum": PATTERN_ALPHANUM.sub("", unique),
        "unique_lower_alnum": PATTERN_ALPHANUM.sub("", unique).lower(),
        "unique_upper_alnum": PATTERN_ALPHANUM.sub("", unique).upper(),
        "timestamp": relative_time(freezer, False),
        "timeISO": relative_time(freezer, True),
    }

    yield ctx


@pytest.fixture(scope="session")
def record_mode(request):
    """Manage compatibility with DD client libraries."""
    return {"false": "none", "true": "rewrite", "none": "new_episodes"}[RECORD]


def _disable_recording():
    """Disable VCR.py integration."""
    return RECORD == "none"


@pytest.fixture(scope="session")
def disable_recording(request):
    """Disable VCR.py integration. This overrides a pytest-recording fixture."""
    return _disable_recording()


@pytest.fixture
def vcr_config():
    config = dict(
        filter_headers=("DD-API-KEY", "DD-APPLICATION-KEY"),
        filter_query_parameters=("api_key", "application_key"),
        match_on=["method", "scheme", "host", "port", "path", "query", "body"],
    )
    if tracer:
        from urllib.parse import urlparse

        config["ignore_hosts"] = [urlparse(tracer.writer.agent_url).hostname]

    return config


@pytest.fixture
def default_cassette_name(default_cassette_name):
    return PATTERN_DOUBLE_UNDERSCORE.sub("_", default_cassette_name)


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
        freeze_file = pathlib.Path(vcr._path).with_suffix(".frozen")
        if not freeze_file.exists():
            msg = (
                "Time file '{}' not found: create one setting `RECORD=true` or "
                "ignore it using `RECORD=none`".format(freeze_file)
            )
            raise RuntimeError(msg)
        with freeze_file.open("r") as f:
            freeze_at = f.readline().strip()

        if not pathlib.Path(vcr._path).exists():
            msg = (
                "Cassette '{}' not found: create one setting `RECORD=true` or "
                "ignore it using `RECORD=none`".format(vcr._path)
            )
            raise RuntimeError(msg)

    return freeze_time(parser.isoparse(freeze_at))


def pytest_recording_configure(config, vcr):
    from vcr import matchers
    from vcr.util import read_body

    is_text_json = matchers._header_checker("text/json")
    transformer = matchers._transform_json

    def body(r1, r2):
        if is_text_json(r1.headers) and is_text_json(r2.headers):
            assert transformer(read_body(r1)) == transformer(read_body(r2))
        else:
            matchers.body(r1, r2)

    vcr.matchers["body"] = body


@given('a valid "apiKeyAuth" key in the system')
def a_valid_api_key(configuration):
    """a valid API key."""
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "fake")


@given('a valid "appKeyAuth" key in the system')
def a_valid_application_key(configuration):
    """a valid Application key."""
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "fake")


@pytest.fixture(scope="module")
def package_name(api_version):
    return "datadog_api_client." + api_version


@pytest.fixture
def _package(package_name):
    return importlib.import_module(package_name)


@pytest.fixture(scope="module")
def undo_operations():
    result = {}
    for f in pathlib.Path(os.path.dirname(__file__)).rglob("undo.json"):
        version = f.parent.parent.name
        with f.open() as fp:
            data = json.load(fp)
            result[version] = {
                snake_case(operation_id): settings.get("undo") for operation_id, settings in data.items()
            }

    return result


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
            "_check_input_type": True,
            "async_req": False,
            "_check_return_type": True,
            "_return_http_data_only": False,
            "_preload_content": True,
            "_request_timeout": None,
            "_spec_property_naming": True,
        },
        "response": (None, None, None),
    }


@given(parsers.parse("body with value {data}"))
def request_body(context, data):
    """Set request body."""
    tpl = Template(data).render(**context)
    context["api_request"]["kwargs"]["body"] = json.loads(tpl)


@given(parsers.parse('body from file "{path}"'))
def request_body_from_file(context, path, package_name):
    """Set request body."""
    version = package_name.split(".")[-1]
    with open(os.path.join(os.path.dirname(__file__), version, "features", path)) as f:
        data = f.read()
    tpl = Template(data).render(**context)
    context["api_request"]["kwargs"]["body"] = json.loads(tpl)


@given(parsers.parse('request contains "{name}" parameter from "{path}"'))
def request_parameter(context, name, path):
    """Set request parameter."""
    context["api_request"]["kwargs"][escape_reserved_keyword(snake_case(name))] = glom(context, path)


@given(parsers.parse('request contains "{name}" parameter with value {value}'))
def request_parameter_with_value(context, name, value):
    """Set request parameter."""
    tpl = Template(value).render(**context)
    context["api_request"]["kwargs"][escape_reserved_keyword(snake_case(name))] = json.loads(tpl)


def build_given(version, operation):
    @sleep_after_request
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
        if operation_name in configuration.unstable_operations:
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

            kwargs = {
                escape_reserved_keyword(snake_case(p["name"])): build_param(p) for p in operation.get("parameters", [])
            }
            kwargs["_check_input_type"] = False
            result = operation_method(**kwargs)

            # register undo method
            context["undo_operations"].append(lambda: undo(api, version, operation_name, result, client=client))

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

    def cleanup(api, version, operation_id, response, client=client):
        operation = undo_operations.get(version, {}).get(operation_id)
        if operation_id is None:
            raise NotImplementedError((version, operation_id))

        if operation["type"] is None:
            raise NotImplementedError((version, operation_id))

        if operation["type"] != "unsafe":
            return

        operation_name = snake_case(operation["operationId"])
        method = getattr(api, operation_name)
        kwargs = {}
        for parameter in operation.get("parameters", []):
            if "source" in parameter:
                kwargs[parameter["name"]] = glom(response, parameter["source"])
            elif "template" in parameter:
                variables = meta.find_undeclared_variables(Environment().parse(parameter["template"]))
                ctx = {}
                for var in variables:
                    ctx[var] = glom(response, var)
                kwargs[parameter["name"]] = json.loads(Template(parameter["template"]).render(**ctx))

        if operation_name in client.configuration.unstable_operations:
            client.configuration.unstable_operations[operation_name] = True

        try:
            method(**kwargs)
        except exceptions.ApiException as e:
            warnings.warn(f"failed undo: {e}")

    yield cleanup


@when("the request is sent")
def execute_request(undo, context, client, api_version, _package):
    """Execute the prepared request."""
    api_request = context["api_request"]
    exceptions = importlib.import_module(context["api"]["package"] + ".exceptions")

    try:
        response = api_request["request"](*api_request["args"], **api_request["kwargs"])
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

    context["undo_operations"].append(lambda: undo(api, api_version, operation_id, response))


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
