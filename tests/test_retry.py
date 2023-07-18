import pytest
from unittest import mock

from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.api.logs_api import LogsApi
from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration


@pytest.mark.vcr(ignore_localhost=True)
@mock.patch("datadog_api_client.rest.DDRetry.get_retry_after")
def test_retry_get_list_logs(retry_mock):
    retry_mock.return_value = 0.1
    configuration = Configuration()
    configuration.enable_retry = True
    with ApiClient(configuration) as api_client:
        api_instance = LogsApi(api_client)
        response = api_instance.list_logs_get()
    assert retry_mock.call_count == 3 and response != None
