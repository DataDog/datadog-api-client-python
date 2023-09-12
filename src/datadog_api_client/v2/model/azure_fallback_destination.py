# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.azure_fallback_destination_integration import AzureFallbackDestinationIntegration
    from datadog_api_client.v2.model.azure_fallback_destination_type import AzureFallbackDestinationType


class AzureFallbackDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_fallback_destination_integration import (
            AzureFallbackDestinationIntegration,
        )
        from datadog_api_client.v2.model.azure_fallback_destination_type import AzureFallbackDestinationType

        return {
            "container": (str,),
            "integration": (AzureFallbackDestinationIntegration,),
            "path": (str,),
            "region": (str,),
            "storage_account": (str,),
            "type": (AzureFallbackDestinationType,),
        }

    attribute_map = {
        "container": "container",
        "integration": "integration",
        "path": "path",
        "region": "region",
        "storage_account": "storageAccount",
        "type": "type",
    }

    def __init__(
        self_,
        container: str,
        integration: AzureFallbackDestinationIntegration,
        storage_account: str,
        type: AzureFallbackDestinationType,
        path: Union[str, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Azure archive destination.

        :param container: The container where the archive will be stored.
        :type container: str

        :param integration: The Azure archive's integration destination.
        :type integration: AzureFallbackDestinationIntegration

        :param path: The archive path.
        :type path: str, optional

        :param region: The region where the archive will be stored.
        :type region: str, optional

        :param storage_account: The associated storage account.
        :type storage_account: str

        :param type: Type of the Azure archive destination.
        :type type: AzureFallbackDestinationType
        """
        if path is not unset:
            kwargs["path"] = path
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)

        self_.container = container
        self_.integration = integration
        self_.storage_account = storage_account
        self_.type = type
