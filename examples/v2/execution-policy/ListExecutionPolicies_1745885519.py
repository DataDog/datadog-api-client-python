"""
List execution policies with query parameters returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.execution_policy_api import ExecutionPolicyApi
from datadog_api_client.v2.model.execution_policy_effect import ExecutionPolicyEffect
from datadog_api_client.v2.model.execution_policy_integration import ExecutionPolicyIntegration

# there is a valid "execution_policy" in the system
EXECUTION_POLICY_DATA_ATTRIBUTES_CREATED_BY = environ["EXECUTION_POLICY_DATA_ATTRIBUTES_CREATED_BY"]
EXECUTION_POLICY_DATA_ATTRIBUTES_NAME = environ["EXECUTION_POLICY_DATA_ATTRIBUTES_NAME"]
EXECUTION_POLICY_DATA_ID = environ["EXECUTION_POLICY_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["list_execution_policies"] = True
with ApiClient(configuration) as api_client:
    api_instance = ExecutionPolicyApi(api_client)
    response = api_instance.list_execution_policies(
        page_size=10,
        page_number=0,
        filter_name=EXECUTION_POLICY_DATA_ATTRIBUTES_NAME,
        filter_ids=[
            EXECUTION_POLICY_DATA_ID,
        ],
        filter_integration=[
            ExecutionPolicyIntegration.INTEGRATION_SCRIPT,
        ],
        filter_effects=[
            ExecutionPolicyEffect.ALLOW,
        ],
        filter_creator_ids=[
            EXECUTION_POLICY_DATA_ATTRIBUTES_CREATED_BY,
        ],
        sort=[
            "-created_at",
        ],
    )

    print(response)
