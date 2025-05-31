"""
Update On-Call escalation policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datadog_api_client.v2.model.data_relationships_teams import DataRelationshipsTeams
from datadog_api_client.v2.model.data_relationships_teams_data_items import DataRelationshipsTeamsDataItems
from datadog_api_client.v2.model.data_relationships_teams_data_items_type import DataRelationshipsTeamsDataItemsType
from datadog_api_client.v2.model.escalation_policy_step_attributes_assignment import (
    EscalationPolicyStepAttributesAssignment,
)
from datadog_api_client.v2.model.escalation_policy_step_target import EscalationPolicyStepTarget
from datadog_api_client.v2.model.escalation_policy_step_target_type import EscalationPolicyStepTargetType
from datadog_api_client.v2.model.escalation_policy_update_request import EscalationPolicyUpdateRequest
from datadog_api_client.v2.model.escalation_policy_update_request_data import EscalationPolicyUpdateRequestData
from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes import (
    EscalationPolicyUpdateRequestDataAttributes,
)
from datadog_api_client.v2.model.escalation_policy_update_request_data_attributes_steps_items import (
    EscalationPolicyUpdateRequestDataAttributesStepsItems,
)
from datadog_api_client.v2.model.escalation_policy_update_request_data_relationships import (
    EscalationPolicyUpdateRequestDataRelationships,
)
from datadog_api_client.v2.model.escalation_policy_update_request_data_type import EscalationPolicyUpdateRequestDataType

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]
ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID = environ["ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID"]

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

# there is a valid "dd_team" in the system
DD_TEAM_DATA_ID = environ["DD_TEAM_DATA_ID"]

body = EscalationPolicyUpdateRequest(
    data=EscalationPolicyUpdateRequestData(
        attributes=EscalationPolicyUpdateRequestDataAttributes(
            name="Example-On-Call-updated",
            resolve_page_on_policy_end=False,
            retries=0,
            steps=[
                EscalationPolicyUpdateRequestDataAttributesStepsItems(
                    assignment=EscalationPolicyStepAttributesAssignment.DEFAULT,
                    escalate_after_seconds=3600,
                    id=ESCALATION_POLICY_DATA_RELATIONSHIPS_STEPS_DATA_0_ID,
                    targets=[
                        EscalationPolicyStepTarget(
                            id=USER_DATA_ID,
                            type=EscalationPolicyStepTargetType.USERS,
                        ),
                    ],
                ),
            ],
        ),
        id=ESCALATION_POLICY_DATA_ID,
        relationships=EscalationPolicyUpdateRequestDataRelationships(
            teams=DataRelationshipsTeams(
                data=[
                    DataRelationshipsTeamsDataItems(
                        id=DD_TEAM_DATA_ID,
                        type=DataRelationshipsTeamsDataItemsType.TEAMS,
                    ),
                ],
            ),
        ),
        type=EscalationPolicyUpdateRequestDataType.POLICIES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.update_on_call_escalation_policy(policy_id=ESCALATION_POLICY_DATA_ID, body=body)

    print(response)
