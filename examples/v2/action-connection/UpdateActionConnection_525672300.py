"""
Update a GitHub personal access token Action Connection without replacing its secret
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.action_connection_data_update import ActionConnectionDataUpdate
from datadog_api_client.v2.model.github_integration_type import GithubIntegrationType
from datadog_api_client.v2.model.github_integration_update import GithubIntegrationUpdate
from datadog_api_client.v2.model.github_personal_access_token_type import GithubPersonalAccessTokenType
from datadog_api_client.v2.model.github_personal_access_token_update import GithubPersonalAccessTokenUpdate
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest

# there is a valid "github_pat_action_connection" in the system
GITHUB_PAT_ACTION_CONNECTION_DATA_ID = environ["GITHUB_PAT_ACTION_CONNECTION_DATA_ID"]

body = UpdateActionConnectionRequest(
    data=ActionConnectionDataUpdate(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributesUpdate(
            name="GitHub personal access token Updated exampleactionconnection",
            integration=GithubIntegrationUpdate(
                type=GithubIntegrationType.GITHUB,
                credentials=GithubPersonalAccessTokenUpdate(
                    type=GithubPersonalAccessTokenType.GITHUBPERSONALACCESSTOKEN,
                    hostname="github.updated.example.com",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.update_action_connection(connection_id=GITHUB_PAT_ACTION_CONNECTION_DATA_ID, body=body)

    print(response)
