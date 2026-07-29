"""
Enable historical metrics ingestion returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.historical_metrics_configuration_create_data import (
    HistoricalMetricsConfigurationCreateData,
)
from datadog_api_client.v2.model.historical_metrics_configuration_create_request import (
    HistoricalMetricsConfigurationCreateRequest,
)
from datadog_api_client.v2.model.historical_metrics_configuration_type import HistoricalMetricsConfigurationType

body = HistoricalMetricsConfigurationCreateRequest(
    data=HistoricalMetricsConfigurationCreateData(
        id="dd.test.metric",
        type=HistoricalMetricsConfigurationType.HISTORICAL_METRICS_CONFIGURATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_historical_metrics_configuration"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_historical_metrics_configuration(body=body)

    print(response)
