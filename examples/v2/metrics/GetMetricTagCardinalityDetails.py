"""
Get tag key cardinality details returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.get_metric_tag_cardinality_details(
        metric_name="metric_name",
    )

    print(response)
