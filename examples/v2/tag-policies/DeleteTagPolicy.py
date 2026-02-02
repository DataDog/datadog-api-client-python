"""
Delete a tag policy returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.tag_policies_api import TagPoliciesApi

configuration = Configuration()
configuration.unstable_operations["delete_tag_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = TagPoliciesApi(api_client)
    api_instance.delete_tag_policy(
        policy_id="123",
    )
