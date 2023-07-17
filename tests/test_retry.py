import os
import pytest

from datadog_api_client.api_client import ApiClient
from datadog_api_client.configuration import Configuration
from datadog_api_client.exceptions import ApiException
from datadog_api_client.v1.api import metrics_api


@pytest.mark.vcr(ignore_localhost=True)
@pytest.mark.skipif(os.getenv("RECORD", "false").lower() != "false", reason="random")
def test_retry():
    configuration = Configuration()
    configuration.enable_retry=True
    configuration.debug=True
    with ApiClient(configuration) as api_client:
        api_instance = metrics_api.MetricsApi(api_client)
        with pytest.raises(ApiException):
            api_instance.get_metric_metadata("some_metric")