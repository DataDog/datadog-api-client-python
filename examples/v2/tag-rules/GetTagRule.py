"""
Get a tag rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_rules_api import TagRulesApi

configuration = Configuration()
configuration.unstable_operations["get_tag_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagRulesApi(api_client)
    response = api_instance.get_tag_rule(
        policy_id="policy_id",
    )

    print(response)
