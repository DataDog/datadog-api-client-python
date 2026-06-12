"""
Create a target audience returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi
from datadog_api_client.v2.model.google_chat_target_audience_create_request import GoogleChatTargetAudienceCreateRequest
from datadog_api_client.v2.model.google_chat_target_audience_create_request_attributes import (
    GoogleChatTargetAudienceCreateRequestAttributes,
)
from datadog_api_client.v2.model.google_chat_target_audience_create_request_data import (
    GoogleChatTargetAudienceCreateRequestData,
)
from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType

body = GoogleChatTargetAudienceCreateRequest(
    data=GoogleChatTargetAudienceCreateRequestData(
        attributes=GoogleChatTargetAudienceCreateRequestAttributes(
            audience_id="fake-audience-id-1",
            audience_name="fake audience name 1",
        ),
        type=GoogleChatTargetAudienceType.GOOGLE_CHAT_TARGET_AUDIENCE_TYPE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.create_google_chat_target_audience(
        organization_binding_id="organization_binding_id", body=body
    )

    print(response)
