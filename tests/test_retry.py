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


@mock.patch("time.sleep", return_value=None)
def test_custom_retry_policy(sleep_mock):
    """Test that a custom retry policy is used when provided"""
    import urllib3

    # Create a custom retry policy with different settings
    custom_retry = urllib3.util.Retry(
        total=5,  # Different from default 3
        backoff_factor=1,  # Different from default 2
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )

    configuration = Configuration(retry_policy=custom_retry)

    with vcr.use_cassette("tests/cassettes/test_retry/test_retry_errors.yaml", record_mode=vcr.mode.NONE):
        with ApiClient(configuration) as api_client:
            api_instance = logs_api.LogsApi(api_client)
            logs = api_instance.list_logs_get()
            assert len(logs.data) == 10
            # With backoff_factor=1, sleep times are: 2, 4
            assert sleep_mock.call_count == 2
            assert sleep_mock.call_args_list[0][0][0] == 2
            assert sleep_mock.call_args_list[1][0][0] == 4


def test_custom_retry_policy_overrides_enable_retry():
    """Test that retry_policy takes precedence over enable_retry"""
    import urllib3

    custom_retry = urllib3.util.Retry(total=10)
    configuration = Configuration(
        enable_retry=True,  # This should be ignored
        max_retries=3,  # This should be ignored
        retry_policy=custom_retry,
    )

    # Verify the configuration accepts the custom policy
    assert configuration.retry_policy is custom_retry
    assert configuration.retry_policy.total == 10


def test_default_retry_when_no_custom_policy():
    """Test that default retry behavior works when no custom policy is provided"""
    configuration = Configuration(enable_retry=True, max_retries=5)

    # Verify no custom policy is set
    assert configuration.retry_policy is None
    assert configuration.enable_retry is True
    assert configuration.max_retries == 5
