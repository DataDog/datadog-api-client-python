"""
Create a GitHub personal access token Action Connection
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.github_integration import GithubIntegration
from datadog_api_client.v2.model.github_integration_type import GithubIntegrationType
from datadog_api_client.v2.model.github_personal_access_token import GithubPersonalAccessToken
from datadog_api_client.v2.model.github_personal_access_token_type import GithubPersonalAccessTokenType

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="GitHub personal access token Connection exampleactionconnection",
            integration=GithubIntegration(
                type=GithubIntegrationType.GITHUB,
                credentials=GithubPersonalAccessToken(
                    type=GithubPersonalAccessTokenType.GITHUBPERSONALACCESSTOKEN,
                    access_token="example-token",
                    hostname="github.example.com",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.create_action_connection(body=body)

    print(response)
