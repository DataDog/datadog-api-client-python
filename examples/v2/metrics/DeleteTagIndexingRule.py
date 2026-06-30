"""
Delete a tag indexing rule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

# there is a valid "tag_indexing_rule" in the system
TAG_INDEXING_RULE_DATA_ID = environ["TAG_INDEXING_RULE_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_tag_indexing_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    api_instance.delete_tag_indexing_rule(
        id=TAG_INDEXING_RULE_DATA_ID,
    )
