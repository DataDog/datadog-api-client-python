"""
Create a GCP Action Connection with AWS Secrets Manager references
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
from datadog_api_client.v2.model.gcp_integration import GCPIntegration
from datadog_api_client.v2.model.gcp_integration_type import GCPIntegrationType
from datadog_api_client.v2.model.gcp_service_account import GCPServiceAccount
from datadog_api_client.v2.model.gcp_service_account_credential_type import GCPServiceAccountCredentialType

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = environ["ACTION_CONNECTION_DATA_ID"]

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributes(
            name="GCP Secrets Manager Connection exampleactionconnection",
            external_secrets_manager=ActionConnectionAWSSecretsManager(
                type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                connection_id=ACTION_CONNECTION_DATA_ID,
                region="us-east-1",
            ),
            integration=GCPIntegration(
                type=GCPIntegrationType.GCP,
                credentials=GCPServiceAccount(
                    type=GCPServiceAccountCredentialType.GCPSERVICEACCOUNT,
                    private_key=ActionConnectionAWSSecretsManagerReference(
                        type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                        secret_id="example/gcp/service-account",
                        key="private_key",
                    ),
                    service_account_email=ActionConnectionAWSSecretsManagerReference(
                        type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                        secret_id="example/gcp/service-account",
                        key="client_email",
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
