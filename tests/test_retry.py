from unittest import mock
import urllib3
import http
from datadog_api_client.rest import DDRetry


@mock.patch("urllib3.connectionpool.HTTPConnectionPool._get_conn")
def test_retry_request_ddretry(getconn_mock):
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
    assert getconn_mock.return_value.request.mock_calls == [
        mock.call(
            "GET",
            mock_endpoint,
            body=None,
            headers=mock.ANY,
            chunked=False,
            preload_content=True,
            decode_content=True,
            enforce_content_length=True,
        ),
        mock.call(
            "GET",
            mock_endpoint,
            body=None,
            headers=mock.ANY,
            chunked=False,
            preload_content=True,
            decode_content=True,
            enforce_content_length=True,
        ),
        mock.call(
            "GET",
            mock_endpoint,
            body=None,
            headers=mock.ANY,
            chunked=False,
            preload_content=True,
            decode_content=True,
            enforce_content_length=True,
        ),
    ]
