import os

import pytest

from datadog_api_client.api_client import ThreadedApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.v1.api import dashboards_api


def test_basic():
    if os.getenv("RECORD", "false").lower() != "none":
        pytest.skip("Integration test")
    configuration = Configuration(return_http_data_only=False)
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "fake")
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "fake")
    configuration.debug = os.getenv("DEBUG") in {"true", "1", "yes", "on"}
    if "DD_TEST_SITE" in os.environ:
        configuration.server_index = 2
        configuration.server_variables["site"] = os.environ["DD_TEST_SITE"]

    with ThreadedApiClient(configuration) as api_client:
        api_instance = dashboards_api.DashboardsApi(api_client)
        thread = api_instance.list_dashboards()
        _, code, headers = thread.get()
        assert code == 200
        assert headers["Content-Type"] == "application/json"
