# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineAzureDataExplorerDestinationAuth(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication configuration for Azure Data Explorer. The ``azure_credential_kind`` field selects the credential type.

        :param azure_credential_kind: The Azure credential kind. The value should always be `azure_cli`.
        :type azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind

        :param azure_client_id: The Microsoft Entra application (client) ID.
        :type azure_client_id: str

        :param azure_client_secret_key: Name of the environment variable or secret that holds the Microsoft Entra application client secret.
        :type azure_client_secret_key: str

        :param azure_tenant_id: The Microsoft Entra tenant ID.
        :type azure_tenant_id: str

        :param certificate_password_key: Name of the environment variable or secret that holds the password for the client certificate.
        :type certificate_password_key: str, none_type, optional

        :param certificate_path: Path to the `.pfx` client certificate file on the Worker.
        :type certificate_path: str

        :param user_assigned_managed_identity_id: The ID of the user-assigned managed identity. If omitted, the system-assigned managed identity is used.
        :type user_assigned_managed_identity_id: str, none_type, optional

        :param user_assigned_managed_identity_id_type: The type of the user-assigned managed identity ID.
        :type user_assigned_managed_identity_id_type: ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType, optional

        :param client_assertion_client_id: The client ID of the Microsoft Entra application that trusts the managed identity.
        :type client_assertion_client_id: str

        :param client_assertion_tenant_id: The tenant ID of the Microsoft Entra application that trusts the managed identity.
        :type client_assertion_tenant_id: str

        :param client_id: The client ID of the Microsoft Entra application. If omitted, it is read from the environment.
        :type client_id: str, none_type, optional

        :param tenant_id: The Microsoft Entra tenant ID. If omitted, it is read from the environment.
        :type tenant_id: str, none_type, optional

        :param token_file_path: Path to the federated token file. If omitted, it is read from the environment.
        :type token_file_path: str, none_type, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_azure_cli import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCli,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_secret import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecret,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_certificate import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificate,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_managed_identity import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentity,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_managed_identity_client_assertion import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertion,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_workload_identity import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentity,
        )

        return {
            "oneOf": [
                ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCli,
                ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecret,
                ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificate,
                ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentity,
                ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertion,
                ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentity,
            ],
        }
