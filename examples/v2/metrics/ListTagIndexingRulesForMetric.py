"""
List tag indexing rules for a metric returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.unstable_operations["list_tag_indexing_rules_for_metric"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tag_indexing_rules_for_metric(
        metric_name="ExampleMetric",
    )

    print(response)
