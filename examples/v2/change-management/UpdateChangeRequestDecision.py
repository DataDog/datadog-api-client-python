"""
Update a change request decision returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.change_management_api import ChangeManagementApi
from datadog_api_client.v2.model.change_request_decision_create_attributes import ChangeRequestDecisionCreateAttributes
from datadog_api_client.v2.model.change_request_decision_create_item import ChangeRequestDecisionCreateItem
from datadog_api_client.v2.model.change_request_decision_create_relationships import (
    ChangeRequestDecisionCreateRelationships,
)
from datadog_api_client.v2.model.change_request_decision_relationship_data import ChangeRequestDecisionRelationshipData
from datadog_api_client.v2.model.change_request_decision_resource_type import ChangeRequestDecisionResourceType
from datadog_api_client.v2.model.change_request_decision_status_type import ChangeRequestDecisionStatusType
from datadog_api_client.v2.model.change_request_decision_update_data import ChangeRequestDecisionUpdateData
from datadog_api_client.v2.model.change_request_decision_update_data_attributes import (
    ChangeRequestDecisionUpdateDataAttributes,
)
from datadog_api_client.v2.model.change_request_decision_update_data_relationships import (
    ChangeRequestDecisionUpdateDataRelationships,
)
from datadog_api_client.v2.model.change_request_decision_update_request import ChangeRequestDecisionUpdateRequest
from datadog_api_client.v2.model.change_request_decisions_relationship import ChangeRequestDecisionsRelationship
from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType
from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship
from datadog_api_client.v2.model.change_request_user_relationship_data import ChangeRequestUserRelationshipData

body = ChangeRequestDecisionUpdateRequest(
    data=ChangeRequestDecisionUpdateData(
        attributes=ChangeRequestDecisionUpdateDataAttributes(
            id="CHM-1234",
        ),
        relationships=ChangeRequestDecisionUpdateDataRelationships(
            change_request_decisions=ChangeRequestDecisionsRelationship(
                data=[
                    ChangeRequestDecisionRelationshipData(
                        id="decision-id-0",
                        type=ChangeRequestDecisionResourceType.CHANGE_REQUEST_DECISION,
                    ),
                ],
            ),
        ),
        type=ChangeRequestResourceType.CHANGE_REQUEST,
    ),
    included=[
        ChangeRequestDecisionCreateItem(
            attributes=ChangeRequestDecisionCreateAttributes(
                change_request_status=ChangeRequestDecisionStatusType.REQUESTED,
                request_reason="Please review and approve this change",
            ),
            id="decision-id-0",
            relationships=ChangeRequestDecisionCreateRelationships(
                requested_user=ChangeRequestUserRelationship(
                    data=ChangeRequestUserRelationshipData(
                        id="00000000-0000-0000-0000-000000000000",
                        type="user",
                    ),
                ),
            ),
            type=ChangeRequestDecisionResourceType.CHANGE_REQUEST_DECISION,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["update_change_request_decision"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChangeManagementApi(api_client)
    response = api_instance.update_change_request_decision(
        change_request_id="change_request_id", decision_id="decision_id", body=body
    )

    print(response)
