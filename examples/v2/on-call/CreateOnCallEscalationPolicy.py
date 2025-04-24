"""
Create on-call escalation policy returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.escalation_policy_create_request import EscalationPolicyCreateRequest
from datadog_api_client.v2.model.escalation_policy_create_request_data import EscalationPolicyCreateRequestData
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes import (
    EscalationPolicyCreateRequestDataAttributes,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items import (
    EscalationPolicyCreateRequestDataAttributesStepsItems,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items_assignment import (
    EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items_targets_items import (
    EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItems,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items_targets_items_type import (
    EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships import (
    EscalationPolicyCreateRequestDataRelationships,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams import (
    EscalationPolicyCreateRequestDataRelationshipsTeams,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams_data_items import (
    EscalationPolicyCreateRequestDataRelationshipsTeamsDataItems,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships_teams_data_items_type import (
    EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_type import EscalationPolicyCreateRequestDataType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = EscalationPolicyCreateRequest(
    data=EscalationPolicyCreateRequestData(
        attributes=EscalationPolicyCreateRequestDataAttributes(
            description="Escalation Policy 1 description",
            name="Example-On-Call",
            resolve_page_on_policy_end=True,
            retries=2,
            steps=[
                EscalationPolicyCreateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment.DEFAULT,
                    escalate_after_seconds=3600,
                    targets=[
                        EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItems(
                            id=USER_DATA_ID,
                            type=EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType.USERS,
                        ),
                        EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItems(
                            id=SCHEDULE_DATA_ID,
                            type=EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType.SCHEDULES,
                        ),
                        EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItems(
                            id=DD_TEAM_DATA_ID,
                            type=EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType.TEAMS,
                        ),
                    ],
                ),
                EscalationPolicyCreateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyCreateRequestDataAttributesStepsItemsAssignment.ROUND_ROBIN,
                    escalate_after_seconds=3600,
                    targets=[
                        EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItems(
                            id=DD_TEAM_DATA_ID,
                            type=EscalationPolicyCreateRequestDataAttributesStepsItemsTargetsItemsType.TEAMS,
                        ),
                    ],
                ),
            ],
        ),
        relationships=EscalationPolicyCreateRequestDataRelationships(
            teams=EscalationPolicyCreateRequestDataRelationshipsTeams(
                data=[
                    EscalationPolicyCreateRequestDataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=EscalationPolicyCreateRequestDataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=EscalationPolicyCreateRequestDataType.POLICIES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.create_on_call_escalation_policy(body=body)

    print(response)
