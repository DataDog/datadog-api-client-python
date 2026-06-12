"""
Update a target audience returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi
from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType
from datadog_api_client.v2.model.google_chat_target_audience_update_request import GoogleChatTargetAudienceUpdateRequest
from datadog_api_client.v2.model.google_chat_target_audience_update_request_attributes import (
    GoogleChatTargetAudienceUpdateRequestAttributes,
)
from datadog_api_client.v2.model.google_chat_target_audience_update_request_data import (
    GoogleChatTargetAudienceUpdateRequestData,
)

body = GoogleChatTargetAudienceUpdateRequest(
    data=GoogleChatTargetAudienceUpdateRequestData(
        attributes=GoogleChatTargetAudienceUpdateRequestAttributes(
            audience_id="fake-audience-id-1",
            audience_name="fake audience name 1",
        ),
        type=GoogleChatTargetAudienceType.GOOGLE_CHAT_TARGET_AUDIENCE_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.update_google_chat_target_audience(
        organization_binding_id="organization_binding_id", target_audience_id="target_audience_id", body=body
    )

    print(response)
