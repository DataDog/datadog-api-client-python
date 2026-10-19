"""
Delete a Temporal Cloud OpenMetrics account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.temporal_cloud_open_metrics_integration_api import TemporalCloudOpenMetricsIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_temporal_cloud_open_metrics_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TemporalCloudOpenMetricsIntegrationApi(api_client)
    api_instance.delete_temporal_cloud_open_metrics_integration_account(
        account_id="account_id",
    )
