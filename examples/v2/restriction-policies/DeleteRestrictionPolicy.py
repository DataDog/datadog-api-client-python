"""
Delete a restriction policy returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    api_instance.delete_restriction_policy(
        resource_id="dashboard:test-delete",
    )
