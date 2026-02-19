"""
Update a change request returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.change_management_api import ChangeManagementApi
from datadog_api_client.v2.model.change_request_change_type import ChangeRequestChangeType
from datadog_api_client.v2.model.change_request_decision_create_attributes import ChangeRequestDecisionCreateAttributes
from datadog_api_client.v2.model.change_request_decision_create_item import ChangeRequestDecisionCreateItem
from datadog_api_client.v2.model.change_request_decision_create_relationships import (
    ChangeRequestDecisionCreateRelationships,
)
from datadog_api_client.v2.model.change_request_decision_relationship_data import ChangeRequestDecisionRelationshipData
from datadog_api_client.v2.model.change_request_decision_resource_type import ChangeRequestDecisionResourceType
from datadog_api_client.v2.model.change_request_decision_status_type import ChangeRequestDecisionStatusType
from datadog_api_client.v2.model.change_request_decisions_relationship import ChangeRequestDecisionsRelationship
from datadog_api_client.v2.model.change_request_resource_type import ChangeRequestResourceType
from datadog_api_client.v2.model.change_request_risk_level import ChangeRequestRiskLevel
from datadog_api_client.v2.model.change_request_update_attributes import ChangeRequestUpdateAttributes
from datadog_api_client.v2.model.change_request_update_data import ChangeRequestUpdateData
from datadog_api_client.v2.model.change_request_update_relationships import ChangeRequestUpdateRelationships
from datadog_api_client.v2.model.change_request_update_request import ChangeRequestUpdateRequest
from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship
from datadog_api_client.v2.model.change_request_user_relationship_data import ChangeRequestUserRelationshipData
from datetime import datetime
from dateutil.tz import tzutc

body = ChangeRequestUpdateRequest(
    data=ChangeRequestUpdateData(
        attributes=ChangeRequestUpdateAttributes(
            change_request_plan="Updated deployment plan",
            change_request_risk=ChangeRequestRiskLevel.LOW,
            change_request_type=ChangeRequestChangeType.NORMAL,
            end_date=datetime(2024, 1, 2, 15, 0, tzinfo=tzutc()),
            id="CHM-1234",
            start_date=datetime(2024, 1, 1, 3, 0, tzinfo=tzutc()),
        ),
        relationships=ChangeRequestUpdateRelationships(
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
configuration.unstable_operations["update_change_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChangeManagementApi(api_client)
    response = api_instance.update_change_request(change_request_id="change_request_id", body=body)

    print(response)
