"""
Delete a tag rule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_rules_api import TagRulesApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_tag_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagRulesApi(api_client)
    api_instance.delete_tag_rule(
        rule_id="rule_id",
    )
