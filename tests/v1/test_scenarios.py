# coding=utf-8
"""Get a list of IP prefixes belonging to Datadog. feature tests."""

import importlib
import os
import re

from pytest_bdd import (
    given,
    parsers,
    scenarios,
    then,
    when,
)

scenarios('features')


def snake_case(value):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@given(parsers.parse('an instance of "{name}" API'))
def api(client, name):
    """Return an API instance."""
    module_name = snake_case(name)
    package = importlib.import_module(f'datadog_api_client.v1.api.{module_name}_api')
    return {
        'api': getattr(package, name + 'Api')(client),
        'calls': [],
    }


@when(parsers.parse('I call "{name}" endpoint'))
def endpoint_response(api, name):
    """Call an endpoint."""
    api['calls'].append(getattr(api['api'], snake_case(name))())


@then(parsers.parse('I should get an instace of "{name}"'))
def i_should_get_an_instace_of(api, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f'datadog_api_client.v1.model.{module_name}')
    assert isinstance(api['calls'][0], getattr(package, name))


@then(parsers.parse('I should get a list of "{name}" objects'))
def i_should_get_a_list_of_objects(api, name):
    """I should get an instace."""
    module_name = snake_case(name)
    package = importlib.import_module(f'datadog_api_client.v1.model.{module_name}')
    cls = getattr(package, name)
    assert all(isinstance(obj, cls) for obj in api['calls'][0])
