"""
Get tag policy score returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi

configuration = Configuration()
configuration.unstable_operations["get_tag_policy_score"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    response = api_instance.get_tag_policy_score(
        policy_id="123",
    )

    print(response)
