"""
List Temporal Cloud OpenMetrics accounts returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.temporal_cloud_open_metrics_integration_api import TemporalCloudOpenMetricsIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_temporal_cloud_open_metrics_integration_accounts"] = True
with ApiClient(configuration) as api_client:
    api_instance = TemporalCloudOpenMetricsIntegrationApi(api_client)
    response = api_instance.list_temporal_cloud_open_metrics_integration_accounts()

    print(response)
