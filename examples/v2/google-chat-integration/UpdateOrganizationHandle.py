"""
Update organization handle returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.google_chat_integration_api import GoogleChatIntegrationApi
from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType
from datadog_api_client.v2.model.google_chat_update_organization_handle_request import (
    GoogleChatUpdateOrganizationHandleRequest,
)
from datadog_api_client.v2.model.google_chat_update_organization_handle_request_attributes import (
    GoogleChatUpdateOrganizationHandleRequestAttributes,
)
from datadog_api_client.v2.model.google_chat_update_organization_handle_request_data import (
    GoogleChatUpdateOrganizationHandleRequestData,
)

# there is a valid "organization_handle" in the system
ORGANIZATION_HANDLE_DATA_ATTRIBUTES_NAME = environ["ORGANIZATION_HANDLE_DATA_ATTRIBUTES_NAME"]
ORGANIZATION_HANDLE_DATA_ID = environ["ORGANIZATION_HANDLE_DATA_ID"]

body = GoogleChatUpdateOrganizationHandleRequest(
    data=GoogleChatUpdateOrganizationHandleRequestData(
        attributes=GoogleChatUpdateOrganizationHandleRequestAttributes(
            name="fake-handle-name--updated",
        ),
    ),
    type=GoogleChatOrganizationHandleType.GOOGLE_CHAT_ORGANIZATION_HANDLE_TYPE,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = GoogleChatIntegrationApi(api_client)
    response = api_instance.update_organization_handle(
        organization_binding_id="e54cb570-c674-529c-769d-84b312288ed7", handle_id=ORGANIZATION_HANDLE_DATA_ID, body=body
    )

    print(response)
