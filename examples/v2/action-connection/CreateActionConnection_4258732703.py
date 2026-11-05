"""
Create an Anthropic Action Connection with an AWS Secrets Manager API token
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
from datadog_api_client.v2.model.anthropic_api_key import AnthropicAPIKey
from datadog_api_client.v2.model.anthropic_api_key_type import AnthropicAPIKeyType
from datadog_api_client.v2.model.anthropic_integration import AnthropicIntegration
from datadog_api_client.v2.model.anthropic_integration_type import AnthropicIntegrationType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = environ["ACTION_CONNECTION_DATA_ID"]

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="Anthropic Secrets Manager Connection exampleactionconnection",
            external_secrets_manager=ActionConnectionAWSSecretsManager(
                type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                connection_id=ACTION_CONNECTION_DATA_ID,
                region="us-east-1",
            ),
            integration=AnthropicIntegration(
                type=AnthropicIntegrationType.ANTHROPIC,
                credentials=AnthropicAPIKey(
                    type=AnthropicAPIKeyType.ANTHROPICAPIKEY,
                    api_token=ActionConnectionAWSSecretsManagerReference(
                        type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                        secret_id="example/anthropic",
                        key="api_token",
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
