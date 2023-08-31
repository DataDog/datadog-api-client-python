from unittest import mock
import pytest
import vcr

from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.v2.api import logs_api


@mock.patch("time.sleep", return_value=None)
def test_retry_errors(sleep_mock):
    configuration = Configuration(enable_retry=True)

    with vcr.use_cassette("tests/cassettes/test_retry/test_retry_errors.yaml", record_mode=vcr.mode.NONE):
        with ApiClient(configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            logs = api_instance.list_logs_get()
            assert len(logs.data) == 10
            assert sleep_mock.call_count == 2
            assert sleep_mock.call_args_list[0][0][0] == 4
            assert sleep_mock.call_args_list[1][0][0] == 8


@mock.patch("time.sleep", return_value=None)
def test_retry_rate_limit(sleep_mock):
    configuration = Configuration(enable_retry=True)

    with vcr.use_cassette("tests/cassettes/test_retry/test_retry_rate_limit.yaml", record_mode=vcr.mode.NONE):
        with ApiClient(configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            logs = api_instance.list_logs_get()
            assert len(logs.data) == 10
            assert sleep_mock.call_count == 3
            assert sleep_mock.call_args_list[0][0][0] == 3
            assert sleep_mock.call_args_list[1][0][0] == 2
            assert sleep_mock.call_args_list[2][0][0] == 1


def test_retry_backoff_factor_validation():
    configuration = Configuration()
    with pytest.raises(ValueError):
        configuration.retry_backoff_factor = 1

    configuration.retry_backoff_factor = 3
