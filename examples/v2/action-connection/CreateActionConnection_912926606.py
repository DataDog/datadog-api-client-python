"""
Create a new Action Connection with HTTPTokenAuth returns "Successfully created Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.http_header import HTTPHeader
from datadog_api_client.v2.model.http_integration import HTTPIntegration
from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType
from datadog_api_client.v2.model.http_token import HTTPToken
from datadog_api_client.v2.model.http_token_auth import HTTPTokenAuth
from datadog_api_client.v2.model.http_token_auth_type import HTTPTokenAuthType
from datadog_api_client.v2.model.token_type import TokenType

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="HTTP Token Connection exampleactionconnection",
            integration=HTTPIntegration(
                type=HTTPIntegrationType.HTTP,
                base_url="https://api.example.com",
                credentials=HTTPTokenAuth(
                    type=HTTPTokenAuthType.HTTPTOKENAUTH,
                    tokens=[
                        HTTPToken(
                            name="ApiKey",
                            type=TokenType.SECRET,
                            value="secret-token-value",
                        ),
                    ],
                    headers=[
                        HTTPHeader(
                            name="Authorization",
                            value="Bearer token-value",
                        ),
                    ],
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
