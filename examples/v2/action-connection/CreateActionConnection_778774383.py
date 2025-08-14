"""
Create a new Action Connection with HTTPBasicAuth returns "Successfully created Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.http_basic_auth import HTTPBasicAuth
from datadog_api_client.v2.model.http_basic_auth_type import HTTPBasicAuthType
from datadog_api_client.v2.model.http_integration import HTTPIntegration
from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="HTTP Basic Auth Connection exampleactionconnection",
            integration=HTTPIntegration(
                type=HTTPIntegrationType.HTTP,
                base_url="https://api.example.com",
                credentials=HTTPBasicAuth(
                    type=HTTPBasicAuthType.HTTPBASICAUTH,
                    username="test-user",
                    password="test-password",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.create_action_connection(body=body)

    print(response)
