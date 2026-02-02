"""
Evaluate policy result returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.policy_management_api import PolicyManagementApi

configuration = Configuration()
configuration.unstable_operations["evaluate_policy_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = PolicyManagementApi(api_client)
    response = api_instance.evaluate_policy_result(
        policy_type="SAML",
    )

    print(response)
