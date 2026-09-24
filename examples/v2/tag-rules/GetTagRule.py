"""
Get a tag rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_rules_api import TagRulesApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_tag_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagRulesApi(api_client)
    response = api_instance.get_tag_rule(
        rule_id="rule_id",
    )

    print(response)
