import pytest

from datadog_api_client.v1 import Configuration, ApiClient
from datadog_api_client.v1.api import metrics_api
from datadog_api_client.v1.exceptions import ApiValueError


def test_invalid_header():
    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = None

    with ApiClient(configuration) as api_client:
        api_instance = metrics_api.MetricsApi(api_client)
        with pytest.raises(ApiValueError):
            api_instance.get_metric_metadata("some_metric")
