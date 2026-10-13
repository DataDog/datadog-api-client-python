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
    from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_azure_cli_kind import (
        ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind,
    )


class ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCli(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_azure_data_explorer_destination_auth_azure_cli_kind import (
            ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind,
        )

        return {
            "azure_credential_kind": (ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind,),
        }

    attribute_map = {
        "azure_credential_kind": "azure_credential_kind",
    }

    def __init__(
        self_, azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind, **kwargs
    ):
        """
        Authenticate using the Azure CLI credentials available in the environment.

        :param azure_credential_kind: The Azure credential kind. The value should always be ``azure_cli``.
        :type azure_credential_kind: ObservabilityPipelineAzureDataExplorerDestinationAuthAzureCliKind
        """
        super().__init__(kwargs)

        self_.azure_credential_kind = azure_credential_kind
