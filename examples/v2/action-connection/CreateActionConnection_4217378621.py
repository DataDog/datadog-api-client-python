"""
Create an HTTP Action Connection with an AWS Secrets Manager token
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_aws_secrets_manager import ActionConnectionAWSSecretsManager
from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
    ActionConnectionAWSSecretsManagerReference,
)
from datadog_api_client.v2.model.action_connection_aws_secrets_manager_type import ActionConnectionAWSSecretsManagerType
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest
from datadog_api_client.v2.model.http_body import HTTPBody
from datadog_api_client.v2.model.http_header import HTTPHeader
from datadog_api_client.v2.model.http_integration import HTTPIntegration
from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType
from datadog_api_client.v2.model.http_token import HTTPToken
from datadog_api_client.v2.model.http_token_auth import HTTPTokenAuth
from datadog_api_client.v2.model.http_token_auth_type import HTTPTokenAuthType
from datadog_api_client.v2.model.token_type import TokenType
from datadog_api_client.v2.model.url_param import UrlParam

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = environ["ACTION_CONNECTION_DATA_ID"]

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="HTTP Secrets Manager Connection exampleactionconnection",
            external_secrets_manager=ActionConnectionAWSSecretsManager(
                type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                connection_id=ACTION_CONNECTION_DATA_ID,
                region="us-east-1",
            ),
            integration=HTTPIntegration(
                type=HTTPIntegrationType.HTTP,
                base_url="https://example.com",
                credentials=HTTPTokenAuth(
                    type=HTTPTokenAuthType.HTTPTOKENAUTH,
                    tokens=[
                        HTTPToken(
                            name="token",
                            type=TokenType.SECRET,
                            value=ActionConnectionAWSSecretsManagerReference(
                                type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                                secret_id="example/http",
                                key="token",
                            ),
                        ),
                    ],
                    headers=[
                        HTTPHeader(
                            name="ApiKey",
                            value="literal-value",
                        ),
                    ],
                    url_parameters=[
                        UrlParam(
                            name="apiKey",
                            value="literal-value",
                        ),
                    ],
                    body=HTTPBody(
                        content_type="application/json",
                        content='{"example":"literal"}',
                    ),
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
