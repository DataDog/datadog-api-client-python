# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_managed_identity_client_assertion_kind import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind,
    )
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_managed_identity_id_type import (
        ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType,
    )


class ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_managed_identity_client_assertion_kind import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind,
        )
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_managed_identity_id_type import (
            ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType,
        )

        return {
            "azure_credential_kind": (
                ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind,
            ),
            "client_assertion_client_id": (str,),
            "client_assertion_tenant_id": (str,),
            "user_assigned_managed_identity_id": (str, none_type),
            "user_assigned_managed_identity_id_type": (
                ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType,
            ),
        }

    attribute_map = {
        "azure_credential_kind": "azure_credential_kind",
        "client_assertion_client_id": "client_assertion_client_id",
        "client_assertion_tenant_id": "client_assertion_tenant_id",
        "user_assigned_managed_identity_id": "user_assigned_managed_identity_id",
        "user_assigned_managed_identity_id_type": "user_assigned_managed_identity_id_type",
    }

    def __init__(
        self_,
        azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind,
        client_assertion_client_id: str,
        client_assertion_tenant_id: str,
        user_assigned_managed_identity_id: Union[str, none_type, UnsetType] = unset,
        user_assigned_managed_identity_id_type: Union[
            ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Authenticate using a managed identity as a client assertion for a Microsoft Entra application.

        :param azure_credential_kind: The Azure credential kind. The value should always be ``managed_identity_client_assertion``.
        :type azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthManagedIdentityClientAssertionKind

        :param client_assertion_client_id: The client ID of the Microsoft Entra application that trusts the managed identity.
        :type client_assertion_client_id: str

        :param client_assertion_tenant_id: The tenant ID of the Microsoft Entra application that trusts the managed identity.
        :type client_assertion_tenant_id: str

        :param user_assigned_managed_identity_id: The ID of the user-assigned managed identity. If omitted, the system-assigned managed identity is used.
        :type user_assigned_managed_identity_id: str, none_type, optional

        :param user_assigned_managed_identity_id_type: The type of the user-assigned managed identity ID.
        :type user_assigned_managed_identity_id_type: ObservabilityPipelineAzureDataExplorerDestinationManagedIdentityIdType, optional
        """
        if user_assigned_managed_identity_id is not unset:
            kwargs["user_assigned_managed_identity_id"] = user_assigned_managed_identity_id
        if user_assigned_managed_identity_id_type is not unset:
            kwargs["user_assigned_managed_identity_id_type"] = user_assigned_managed_identity_id_type
        super().__init__(kwargs)

        self_.azure_credential_kind = azure_credential_kind
        self_.client_assertion_client_id = client_assertion_client_id
        self_.client_assertion_tenant_id = client_assertion_tenant_id
