"""
Delete a tag indexing rule exemption returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.unstable_operations["delete_tag_indexing_rule_exemption"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    api_instance.delete_tag_indexing_rule_exemption(
        metric_name="metric_name",
    )
