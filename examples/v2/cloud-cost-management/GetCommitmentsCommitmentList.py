"""
Get commitments list returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.commitments_commitment_type import CommitmentsCommitmentType
from datadog_api_client.v2.model.commitments_provider import CommitmentsProvider

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_commitments_commitment_list"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.get_commitments_commitment_list(
        provider=CommitmentsProvider.AWS,
        product="ec2",
        start=1788220800000,
        end=1790812799000,
        commitment_type=CommitmentsCommitmentType.RESERVED_INSTANCES,
    )

    print(response)
