from unittest import mock
import urllib3
import http
import vcr

from datadog_api_client.rest import DDRetry
from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.api import logs_api


@mock.patch('time.sleep', return_value=None)
@mock.patch("urllib3.connectionpool.HTTPConnectionPool._get_conn")
def test_retry_request_ddretry(getconn_mock, sleep_mock):
    ddretries = DDRetry(total=3)
    pool_manager = urllib3.PoolManager(retries=ddretries)
    mock_endpoint = "/api/test"
    msg = http.client.HTTPMessage()
    response_429 = mock.Mock(status=429, msg=msg, headers={"X-Ratelimit-Reset": "1"})
    response_429.get_redirect_location.return_value = ""
    response_200 = mock.Mock(status=200, msg=msg, headers={})
    response_200.get_redirect_location.return_value = ""

    getconn_mock.return_value.getresponse.side_effect = [
        response_429,
        response_429,
        response_200,
    ]

    pool_manager.request("GET", "http://ddog.url" + mock_endpoint)

    assert getconn_mock.call_count == 3


@mock.patch('time.sleep', return_value=None)
def test_retry_client(sleep_mock):
    configuration = Configuration(enable_retry=True)

    with vcr.use_cassette('tests/cassettes/test_retry/test_retry_get_list_logs.yaml', record_mode=vcr.mode.NONE):
        with ApiClient(configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            logs = api_instance.list_logs_get()
            assert len(logs.data) == 10
            assert sleep_mock.call_count == 3
            assert sleep_mock.call_args_list[0][0][0] == 3
            assert sleep_mock.call_args_list[1][0][0] == 2
            assert sleep_mock.call_args_list[2][0][0] == 1
