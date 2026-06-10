"""
Submit feedback on an ownership inference returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_ownership_api import CSMOwnershipApi
from datadog_api_client.v2.model.ownership_feedback_action import OwnershipFeedbackAction
from datadog_api_client.v2.model.ownership_feedback_request import OwnershipFeedbackRequest
from datadog_api_client.v2.model.ownership_feedback_request_attributes import OwnershipFeedbackRequestAttributes
from datadog_api_client.v2.model.ownership_feedback_request_data import OwnershipFeedbackRequestData
from datadog_api_client.v2.model.ownership_feedback_type import OwnershipFeedbackType
from datadog_api_client.v2.model.ownership_owner_type import OwnershipOwnerType

body = OwnershipFeedbackRequest(
    data=OwnershipFeedbackRequestData(
        attributes=OwnershipFeedbackRequestAttributes(
            action=OwnershipFeedbackAction.CONFIRM,
            actor_handle="user@example.com",
            actor_type="user",
            corrected_owner_handle="team-b",
            corrected_owner_type="team",
            inference_checksum="abc123",
            reason="Confirmed by team lead.",
        ),
        type=OwnershipFeedbackType.OWNERSHIP_FEEDBACK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_ownership_feedback"] = True
with ApiClient(configuration) as api_client:
    api_instance = CSMOwnershipApi(api_client)
    response = api_instance.create_ownership_feedback(
        resource_id="res-1", owner_type=OwnershipOwnerType.TEAM, body=body
    )

    print(response)
