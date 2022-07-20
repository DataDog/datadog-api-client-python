"""
Delete a tag configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    api_instance.delete_tag_configuration(
        metric_name="ExampleDeleteatagconfigurationreturnsNoContentresponse",
    )
