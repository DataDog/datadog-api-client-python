"""
Create an Application key for current user returns "Created" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi
from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes
from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequest
from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

body = ApplicationKeyCreateRequest(
    data=ApplicationKeyCreateData(
        type=ApplicationKeysType("application_keys"),
        attributes=ApplicationKeyCreateAttributes(
            name="Test-Example-Create_an_Application_key_for_current_user_returns_Created_response"
        ),
    )
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    response = api_instance.create_current_user_application_key(body=body)

    print(response)
