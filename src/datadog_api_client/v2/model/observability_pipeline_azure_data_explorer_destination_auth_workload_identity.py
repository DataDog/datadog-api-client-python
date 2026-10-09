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
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_workload_identity_kind import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind,
    )


class ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentity(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_workload_identity_kind import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind,
        )

        return {
            "azure_credential_kind": (ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind,),
            "client_id": (str, none_type),
            "tenant_id": (str, none_type),
            "token_file_path": (str, none_type),
        }

    attribute_map = {
        "azure_credential_kind": "azure_credential_kind",
        "client_id": "client_id",
        "tenant_id": "tenant_id",
        "token_file_path": "token_file_path",
    }

    def __init__(
        self_,
        azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind,
        client_id: Union[str, none_type, UnsetType] = unset,
        tenant_id: Union[str, none_type, UnsetType] = unset,
        token_file_path: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Authenticate using Azure Workload Identity (for example, on Kubernetes).

        :param azure_credential_kind: The Azure credential kind. The value should always be ``workload_identity``.
        :type azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthWorkloadIdentityKind

        :param client_id: The client ID of the Microsoft Entra application. If omitted, it is read from the environment.
        :type client_id: str, none_type, optional

        :param tenant_id: The Microsoft Entra tenant ID. If omitted, it is read from the environment.
        :type tenant_id: str, none_type, optional

        :param token_file_path: Path to the federated token file. If omitted, it is read from the environment.
        :type token_file_path: str, none_type, optional
        """
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id
        if token_file_path is not unset:
            kwargs["token_file_path"] = token_file_path
        super().__init__(kwargs)

        self_.azure_credential_kind = azure_credential_kind
