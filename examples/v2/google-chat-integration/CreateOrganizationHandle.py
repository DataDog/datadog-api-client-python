"""
Create organization handle returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi
from datadog_api_client.v2.model.google_chat_create_organization_handle_request import (
    GoogleChatCreateOrganizationHandleRequest,
)
from datadog_api_client.v2.model.google_chat_create_organization_handle_request_attributes import (
    GoogleChatCreateOrganizationHandleRequestAttributes,
)
from datadog_api_client.v2.model.google_chat_create_organization_handle_request_data import (
    GoogleChatCreateOrganizationHandleRequestData,
)
from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType

body = GoogleChatCreateOrganizationHandleRequest(
    data=GoogleChatCreateOrganizationHandleRequestData(
        attributes=GoogleChatCreateOrganizationHandleRequestAttributes(
            name="Example-Google-Chat-Integration",
            space_resource_name="spaces/AAQA-zFIks8",
        ),
    ),
    type=GoogleChatOrganizationHandleType.GOOGLE_CHAT_ORGANIZATION_HANDLE_TYPE,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.create_organization_handle(
        organization_binding_id="e54cb570-c674-529c-769d-84b312288ed7", body=body
    )

    print(response)
