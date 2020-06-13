# coding=utf-8
"""Define basic fixtures."""

import importlib
import logging
import os
import re
import time
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
# vcr_log = logging.getLogger("vcr")
# vcr_log.setLevel(logging.INFO)


def snake_case(value):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@pytest.fixture(scope='module')
def vcr_config():
    return dict(
        filter_headers=('DD-API-KEY', 'DD-APPLICATION-KEY'),
        filter_query_parameters=('api_key', 'application_key'),
    )


@pytest.fixture
def freezer(vcr_cassette_name, vcr_cassette, vcr):
    from freezegun import freeze_time
    from dateutil import parser

    if vcr_cassette.record_mode == "all":
        tzinfo = datetime.now().astimezone().tzinfo
        freeze_at = datetime.now().replace(tzinfo=tzinfo).isoformat()
        with open(
            os.path.join(
                vcr.cassette_library_dir, vcr_cassette_name + ".frozen"
            ),
            "w",
        ) as f:
            f.write(freeze_at)
    else:
        with open(
            os.path.join(
                vcr.cassette_library_dir, vcr_cassette_name + ".frozen"
            ),
            "r",
        ) as f:
            freeze_at = f.readline().strip()

    return freeze_time(parser.isoparse(freeze_at))


@given('a valid API key')
def a_valid_api_key(configuration):
    """a valid API key."""
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY")


@given('a valid Application key')
def a_valid_application_key(configuration):
    """a valid Application key."""
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY")


@pytest.fixture
def _package(package_name):
    return importlib.import_module(package_name)


@pytest.fixture
def configuration(_package):
    yield _package.Configuration()


@pytest.fixture
def client(_package, configuration):
    with _package.ApiClient(configuration) as api_client:
        yield api_client


@given(parsers.parse('an instance of "{name}" API'))
def api(package_name, client, name):
    """Return an API instance."""
    module_name = snake_case(name)
    package = importlib.import_module(f'{package_name}.api.{module_name}_api')
    return {
        'api': getattr(package, name + 'Api')(client),
        'calls': [],
    }


@when(parsers.parse('I call "{name}" endpoint'))
def endpoint_response(api, name):
    """Call an endpoint."""
    return api['calls'].append(getattr(api['api'], snake_case(name))())


@then(parsers.parse('I should get an instance of "{name}"'))
def i_should_get_an_instace_of(package_name, api, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f'{package_name}.model.{module_name}')
    assert isinstance(api['calls'][0], getattr(package, name))


@then(parsers.parse('I should get a list of "{name}" objects'))
def i_should_get_a_list_of_objects(package_name, api, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f'{package_name}.model.{module_name}')
    cls = getattr(package, name)
    assert all(isinstance(obj, cls) for obj in api['calls'][0])
