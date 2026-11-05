"""
Update a GCP Action Connection with a versioned AWS Secrets Manager reference
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
from datadog_api_client.v2.model.action_connection_aws_secrets_manager import ActionConnectionAWSSecretsManager
from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
    ActionConnectionAWSSecretsManagerReference,
)
from datadog_api_client.v2.model.action_connection_aws_secrets_manager_type import ActionConnectionAWSSecretsManagerType
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.action_connection_data_update import ActionConnectionDataUpdate
from datadog_api_client.v2.model.gcp_integration_type import GCPIntegrationType
from datadog_api_client.v2.model.gcp_integration_update import GCPIntegrationUpdate
from datadog_api_client.v2.model.gcp_service_account_credential_type import GCPServiceAccountCredentialType
from datadog_api_client.v2.model.gcp_service_account_update import GCPServiceAccountUpdate
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest

# there is a valid "gcp_action_connection" in the system
GCP_ACTION_CONNECTION_DATA_ID = environ["GCP_ACTION_CONNECTION_DATA_ID"]

# there is a valid "action_connection" in the system
ACTION_CONNECTION_DATA_ID = environ["ACTION_CONNECTION_DATA_ID"]

body = UpdateActionConnectionRequest(
    data=ActionConnectionDataUpdate(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributesUpdate(
            external_secrets_manager=ActionConnectionAWSSecretsManager(
                type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                connection_id=ACTION_CONNECTION_DATA_ID,
                region="us-east-1",
            ),
            integration=GCPIntegrationUpdate(
                type=GCPIntegrationType.GCP,
                credentials=GCPServiceAccountUpdate(
                    type=GCPServiceAccountCredentialType.GCPSERVICEACCOUNT,
                    private_key=ActionConnectionAWSSecretsManagerReference(
                        type=ActionConnectionAWSSecretsManagerType.AWS_SECRETS_MANAGER,
                        secret_id="example/gcp/service-account",
                        key="private_key",
                        version_stage="AWSCURRENT",
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
    response = api_instance.update_action_connection(connection_id=GCP_ACTION_CONNECTION_DATA_ID, body=body)

    print(response)
