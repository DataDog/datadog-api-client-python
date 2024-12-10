"""
Get a list of metrics returns "Success" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    items = api_instance.list_tag_configurations_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
