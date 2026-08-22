"""
Bulk create and remove teams ownership mappings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_teams_ownership_api import RumTeamsOwnershipApi
from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation import TeamsOwnershipMappingBatchOperation
from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_data import (
    TeamsOwnershipMappingBatchOperationData,
)
from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_data_attributes import (
    TeamsOwnershipMappingBatchOperationDataAttributes,
)
from datadog_api_client.v2.model.teams_ownership_mapping_batch_operation_op import TeamsOwnershipMappingBatchOperationOp
from datadog_api_client.v2.model.teams_ownership_mapping_batch_request import TeamsOwnershipMappingBatchRequest
from datadog_api_client.v2.model.teams_ownership_mapping_type import TeamsOwnershipMappingType
from datadog_api_client.v2.model.teams_ownership_match_type import TeamsOwnershipMatchType

body = TeamsOwnershipMappingBatchRequest(
    atomic_operations=[
        TeamsOwnershipMappingBatchOperation(
            op=TeamsOwnershipMappingBatchOperationOp.ADD,
            data=TeamsOwnershipMappingBatchOperationData(
                type=TeamsOwnershipMappingType.TEAMS_OWNERSHIP_MAPPINGS,
                attributes=TeamsOwnershipMappingBatchOperationDataAttributes(
                    team_handle="team-rum",
                    view_name="/checkout-examplerumteamsownership",
                    service="web-checkout-examplerumteamsownership",
                    match_type=TeamsOwnershipMatchType.EXACT,
                ),
            ),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumTeamsOwnershipApi(api_client)
    response = api_instance.create_teams_ownership_mappings_batch(body=body)

    print(response)
