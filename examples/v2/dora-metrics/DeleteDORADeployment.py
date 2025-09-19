"""
Delete a deployment event returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    api_instance.delete_dora_deployment(
        deployment_id="NO_VALUE",
    )
