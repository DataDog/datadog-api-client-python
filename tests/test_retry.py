from unittest import mock
import requests
from http.client import HTTPMessage

from datadog_api_client.rest import DDRetry


# @pytest.mark.vcr(ignore_localhost=True)
# @mock.patch("datadog_api_client.rest.DDRetry.get_retry_after")
# def test_retry_get_list_logs(retry_mock):
#     retry_mock.return_value = 0.1
#     configuration = Configuration()
#     configuration.enable_retry = True
#     with ApiClient(configuration) as api_client:
#         api_instance = LogsApi(api_client)
#         response = api_instance.list_logs_get()
#     assert retry_mock.call_count == 3


def request_with_retry(*args, **kwargs):
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        max_retries=DDRetry(
            total=kwargs.pop("max_retries", 3),
        )
    )
    session.mount("http://", adapter)
    return session.request(*args, **kwargs)


@mock.patch("urllib3.connectionpool.HTTPConnectionPool._get_conn")
def test_retry_request_ddretry(getconn_mock):
    mock_endpoint = "/api/test"
    getconn_mock.return_value.getresponse.side_effect = [
        mock.Mock(status=429, msg=HTTPMessage()),
        mock.Mock(status=429, msg=HTTPMessage()),
        mock.Mock(status=429, msg=HTTPMessage()),
        mock.Mock(status=200, msg=HTTPMessage()),
    ]
    r = request_with_retry("GET", "http://ddog.url" + mock_endpoint, max_retries=3)
    r.raise_for_status()

    assert getconn_mock.return_value.request.mock_calls == [
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
        mock.call("GET", mock_endpoint, body=None, headers=mock.ANY),
    ]
