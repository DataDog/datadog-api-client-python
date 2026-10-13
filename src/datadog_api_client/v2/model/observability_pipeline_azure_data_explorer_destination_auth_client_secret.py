# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_secret_kind import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind,
    )


class ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecret(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_secret_kind import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind,
        )

        return {
            "azure_client_id": (str,),
            "azure_client_secret_key": (str,),
            "azure_credential_kind": (ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind,),
            "azure_tenant_id": (str,),
        }

    attribute_map = {
        "azure_client_id": "azure_client_id",
        "azure_client_secret_key": "azure_client_secret_key",
        "azure_credential_kind": "azure_credential_kind",
        "azure_tenant_id": "azure_tenant_id",
    }

    def __init__(
        self_,
        azure_client_id: str,
        azure_client_secret_key: str,
        azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind,
        azure_tenant_id: str,
        **kwargs,
    ):
        """
        Authenticate using a Microsoft Entra application client secret.

        :param azure_client_id: The Microsoft Entra application (client) ID.
        :type azure_client_id: str

        :param azure_client_secret_key: Name of the environment variable or secret that holds the Microsoft Entra application client secret.
        :type azure_client_secret_key: str

        :param azure_credential_kind: The Azure credential kind. The value should always be ``client_secret_credential``.
        :type azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthClientSecretKind

        :param azure_tenant_id: The Microsoft Entra tenant ID.
        :type azure_tenant_id: str
        """
        super().__init__(kwargs)

        self_.azure_client_id = azure_client_id
        self_.azure_client_secret_key = azure_client_secret_key
        self_.azure_credential_kind = azure_credential_kind
        self_.azure_tenant_id = azure_tenant_id
