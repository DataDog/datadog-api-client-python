from unittest import mock
import urllib3
from datadog_api_client.rest import DDRetry


@mock.patch("urllib3.connectionpool.HTTPConnectionPool._get_conn")
def test_retry_request_ddretry(getconn_mock):
    ddretries = DDRetry(total=3)
    pool_manager = urllib3.PoolManager(retries=ddretries)
    mock_endpoint = "/api/test"

    response_429 = urllib3.HTTPResponse(
        headers={"X-Ratelimit-Reset": "1"},
        status=429,
        reason="Too many requests",
        request_method="GET",
    )

    response_200 = urllib3.HTTPResponse(
        headers={"X-Ratelimit-Reset": "1"},
        status=200,
        reason="OK",
        request_method="GET",
    )

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
