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
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_certificate_kind import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind,
    )


class ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_client_certificate_kind import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind,
        )

        return {
            "azure_client_id": (str,),
            "azure_credential_kind": (ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind,),
            "azure_tenant_id": (str,),
            "certificate_password_key": (str, none_type),
            "certificate_path": (str,),
        }

    attribute_map = {
        "azure_client_id": "azure_client_id",
        "azure_credential_kind": "azure_credential_kind",
        "azure_tenant_id": "azure_tenant_id",
        "certificate_password_key": "certificate_password_key",
        "certificate_path": "certificate_path",
    }

    def __init__(
        self_,
        azure_client_id: str,
        azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind,
        azure_tenant_id: str,
        certificate_path: str,
        certificate_password_key: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Authenticate using a Microsoft Entra application client certificate.

        :param azure_client_id: The Microsoft Entra application (client) ID.
        :type azure_client_id: str

        :param azure_credential_kind: The Azure credential kind. The value should always be ``client_certificate_credential``.
        :type azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthClientCertificateKind

        :param azure_tenant_id: The Microsoft Entra tenant ID.
        :type azure_tenant_id: str

        :param certificate_password_key: Name of the environment variable or secret that holds the password for the client certificate.
        :type certificate_password_key: str, none_type, optional

        :param certificate_path: Path to the ``.pfx`` client certificate file on the Worker.
        :type certificate_path: str
        """
        if certificate_password_key is not unset:
            kwargs["certificate_password_key"] = certificate_password_key
        super().__init__(kwargs)

        self_.azure_client_id = azure_client_id
        self_.azure_credential_kind = azure_credential_kind
        self_.azure_tenant_id = azure_tenant_id
        self_.certificate_path = certificate_path
