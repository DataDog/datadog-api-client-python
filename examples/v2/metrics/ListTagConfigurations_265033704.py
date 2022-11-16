"""
Get a list of metrics with a tag filter returns "Success" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tag_configurations(
        filter_tags="ExampleGetalistofmetricswithatagfilterreturnsSuccessresponse",
    )

    print(response)
