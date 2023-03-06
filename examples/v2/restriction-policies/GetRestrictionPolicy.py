"""
Get a restriction policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.restriction_policies_api import RestrictionPoliciesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RestrictionPoliciesApi(api_client)
    response = api_instance.get_restriction_policy(
        resource_id="dashboard:test-get",
    )

    print(response)
