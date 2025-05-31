"""
Create On-Call escalation policy returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.escalation_policy_create_request import EscalationPolicyCreateRequest
from datadog_api_client.v2.model.escalation_policy_create_request_data import EscalationPolicyCreateRequestData
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes import (
    EscalationPolicyCreateRequestDataAttributes,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_attributes_steps_items import (
    EscalationPolicyCreateRequestDataAttributesStepsItems,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_relationships import (
    EscalationPolicyCreateRequestDataRelationships,
)
from datadog_api_client.v2.model.escalation_policy_create_request_data_type import EscalationPolicyCreateRequestDataType
from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
    EscalationPolicyStepAttributesAssignment,
)
from datadog_api_client.v2.model.escalation_policy_step_target import EscalationPolicyStepTarget
from datadog_api_client.v2.model.escalation_policy_step_target_type import EscalationPolicyStepTargetType

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = EscalationPolicyCreateRequest(
    data=EscalationPolicyCreateRequestData(
        attributes=EscalationPolicyCreateRequestDataAttributes(
            name="Example-On-Call",
            resolve_page_on_policy_end=True,
            retries=2,
            steps=[
                EscalationPolicyCreateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyStepAttributesAssignment.DEFAULT,
                    escalate_after_seconds=3600,
                    targets=[
                        EscalationPolicyStepTarget(
                            id=USER_DATA_ID,
                            type=EscalationPolicyStepTargetType.USERS,
                        ),
                        EscalationPolicyStepTarget(
                            id=SCHEDULE_DATA_ID,
                            type=EscalationPolicyStepTargetType.SCHEDULES,
                        ),
                        EscalationPolicyStepTarget(
                            id=DD_TEAM_DATA_ID,
                            type=EscalationPolicyStepTargetType.TEAMS,
                        ),
                    ],
                ),
                EscalationPolicyCreateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyStepAttributesAssignment.ROUND_ROBIN,
                    escalate_after_seconds=3600,
                    targets=[
                        EscalationPolicyStepTarget(
                            id=DD_TEAM_DATA_ID,
                            type=EscalationPolicyStepTargetType.TEAMS,
                        ),
                    ],
                ),
            ],
        ),
        relationships=EscalationPolicyCreateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
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
    response = api_instance.create_on_call_escalation_policy(include="steps.targets", body=body)

    print(response)
