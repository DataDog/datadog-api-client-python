"""
Reorder tag indexing rules returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.tag_indexing_rule_order_attributes import TagIndexingRuleOrderAttributes
from datadog_api_client.v2.model.tag_indexing_rule_order_data import TagIndexingRuleOrderData
from datadog_api_client.v2.model.tag_indexing_rule_order_request import TagIndexingRuleOrderRequest
from datadog_api_client.v2.model.tag_indexing_rule_type import TagIndexingRuleType

# there is a valid "tag_indexing_rule" in the system
TAG_INDEXING_RULE_DATA_ID = environ["TAG_INDEXING_RULE_DATA_ID"]

body = TagIndexingRuleOrderRequest(
    data=TagIndexingRuleOrderData(
        attributes=TagIndexingRuleOrderAttributes(
            rule_ids=[
                TAG_INDEXING_RULE_DATA_ID,
            ],
        ),
        type=TagIndexingRuleType.TAG_INDEXING_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["reorder_tag_indexing_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    api_instance.reorder_tag_indexing_rules(body=body)
