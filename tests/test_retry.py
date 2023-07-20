from unittest import mock
from http.client import HTTPMessage
import urllib3
from datadog_api_client.rest import DDRetry

@mock.patch("urllib3.connectionpool.HTTPConnectionPool._get_conn")

def test_retry_request_ddretry(getconn_mock):
    ddretries = DDRetry(total=3)
    http= urllib3.PoolManager(retries=ddretries)
    mock_endpoint= "/api/test"
    getconn_mock.return_value.getresponse.side_effect = [
        mock.Mock(status=429, msg=HTTPMessage()),
        mock.Mock(status=429, msg=HTTPMessage()),
        mock.Mock(status=429, msg=HTTPMessage()),
        mock.Mock(status=200, msg=HTTPMessage()),
    ]

    http.request("GET", "http://ddog.url"+mock_endpoint)

    assert getconn_mock.return_value.request.mock_calls == [
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
    ]