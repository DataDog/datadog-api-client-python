import os
import time

import pytest

from datadog_api_client.api_client import AsyncApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.exceptions import ForbiddenException
from datadog_api_client.v1.api import dashboards_api, metrics_api


@pytest.mark.asyncio
async def test_error():
    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = "invalid"

    async with AsyncApiClient(configuration) as api_client:
        api_instance = metrics_api.MetricsApi(api_client)
        with pytest.raises(ForbiddenException) as e:
            await api_instance.get_metric_metadata("some_metric")
        error = str(e.value)
        assert "(403)" in error
        assert "Reason: Forbidden" in error
        assert e.value.headers["Content-Type"] == "application/json"
        assert e.value.body["errors"] == ["Forbidden"]


@pytest.mark.asyncio
async def test_basic():
    if os.getenv("RECORD", "false").lower() != "none":
        pytest.skip("Integration test")
    configuration = Configuration(return_http_data_only=False)
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "fake")
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "fake")
    configuration.debug = os.getenv("DEBUG") in {"true", "1", "yes", "on"}
    if "DD_TEST_SITE" in os.environ:
        configuration.server_index = 2
        configuration.server_variables["site"] = os.environ["DD_TEST_SITE"]

    async with AsyncApiClient(configuration) as api_client:
        api_instance = dashboards_api.DashboardsApi(api_client)
        _, code, headers = await api_instance.list_dashboards()
        assert code == 200
        assert headers["Content-Type"] == "application/json"


@pytest.mark.asyncio
async def test_body():
    if os.getenv("RECORD", "false").lower() != "none":
        pytest.skip("Integration test")
    configuration = Configuration(return_http_data_only=False)
    configuration.api_key["apiKeyAuth"] = os.getenv("DD_TEST_CLIENT_API_KEY", "fake")
    configuration.api_key["appKeyAuth"] = os.getenv("DD_TEST_CLIENT_APP_KEY", "fake")
    configuration.debug = os.getenv("DEBUG") in {"true", "1", "yes", "on"}
    if "DD_TEST_SITE" in os.environ:
        configuration.server_index = 2
        configuration.server_variables["site"] = os.environ["DD_TEST_SITE"]

    body = {
        "series": [
            {
                "metric": "system.load.1",
                "points": [[time.time(), 0.7]],
                "tags": ["test:async_test"],
            },
        ]
    }

    async with AsyncApiClient(configuration) as api_client:
        api_instance = metrics_api.MetricsApi(api_client)
        _, code, headers = await api_instance.submit_metrics(body=body)
        assert code == 202
