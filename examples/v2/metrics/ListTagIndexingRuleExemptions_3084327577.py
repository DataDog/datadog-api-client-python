"""
List tag indexing rule exemptions returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["list_tag_indexing_rule_exemptions"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    items = api_instance.list_tag_indexing_rule_exemptions_with_pagination()
    for item in items:
        print(item)
