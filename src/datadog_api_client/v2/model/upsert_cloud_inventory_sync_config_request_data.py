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
    from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request_attributes import (
        UpsertCloudInventorySyncConfigRequestAttributes,
    )
    from datadog_api_client.v2.model.cloud_inventory_cloud_provider_id import CloudInventoryCloudProviderId
    from datadog_api_client.v2.model.cloud_inventory_cloud_provider_request_type import (
        CloudInventoryCloudProviderRequestType,
    )


class UpsertCloudInventorySyncConfigRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request_attributes import (
            UpsertCloudInventorySyncConfigRequestAttributes,
        )
        from datadog_api_client.v2.model.cloud_inventory_cloud_provider_id import CloudInventoryCloudProviderId
        from datadog_api_client.v2.model.cloud_inventory_cloud_provider_request_type import (
            CloudInventoryCloudProviderRequestType,
        )

        return {
            "attributes": (UpsertCloudInventorySyncConfigRequestAttributes,),
            "id": (CloudInventoryCloudProviderId,),
            "type": (CloudInventoryCloudProviderRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: UpsertCloudInventorySyncConfigRequestAttributes,
        id: CloudInventoryCloudProviderId,
        type: CloudInventoryCloudProviderRequestType,
        **kwargs,
    ):
        """
        Storage Management configuration data for the create or update request.

        :param attributes: Settings for the cloud provider specified in ``data.id``. Include only the matching provider object ( ``aws`` , ``gcp`` , or ``azure`` ).
        :type attributes: UpsertCloudInventorySyncConfigRequestAttributes

        :param id: Cloud provider for this sync configuration ( ``aws`` , ``gcp`` , or ``azure`` ). For requests, must match the provider block supplied under ``attributes``.
        :type id: CloudInventoryCloudProviderId

        :param type: Always ``cloud_provider``.
        :type type: CloudInventoryCloudProviderRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
