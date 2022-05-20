"""
List tag configurations with configured filter returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.unstable_operations["list_tag_configurations"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tag_configurations(
        filter_configured=True,
    )

    print(response)
