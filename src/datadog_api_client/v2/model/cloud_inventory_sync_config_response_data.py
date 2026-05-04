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
    from datadog_api_client.v2.model.cloud_inventory_sync_config_attributes import CloudInventorySyncConfigAttributes
    from datadog_api_client.v2.model.cloud_inventory_sync_config_resource_type import (
        CloudInventorySyncConfigResourceType,
    )


class CloudInventorySyncConfigResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_inventory_sync_config_attributes import (
            CloudInventorySyncConfigAttributes,
        )
        from datadog_api_client.v2.model.cloud_inventory_sync_config_resource_type import (
            CloudInventorySyncConfigResourceType,
        )

        return {
            "attributes": (CloudInventorySyncConfigAttributes,),
            "id": (str,),
            "type": (CloudInventorySyncConfigResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CloudInventorySyncConfigAttributes,
        id: str,
        type: CloudInventorySyncConfigResourceType,
        **kwargs,
    ):
        """
        JSON:API data object for a sync configuration.

        :param attributes: Attributes for a cloud inventory sync configuration. Values beyond ``id`` may be omitted immediately after upsert.
        :type attributes: CloudInventorySyncConfigAttributes

        :param id: Unique identifier for the recurring sync configuration.
        :type id: str

        :param type: JSON:API type for sync configuration resources.
        :type type: CloudInventorySyncConfigResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
