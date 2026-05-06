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
    from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request_data import (
        UpsertCloudInventorySyncConfigRequestData,
    )


class UpsertCloudInventorySyncConfigRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_cloud_inventory_sync_config_request_data import (
            UpsertCloudInventorySyncConfigRequestData,
        )

        return {
            "data": (UpsertCloudInventorySyncConfigRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpsertCloudInventorySyncConfigRequestData, **kwargs):
        """
        Request body for creating or updating a cloud inventory sync configuration.

        :param data: Storage Management configuration data for the create or update request.
        :type data: UpsertCloudInventorySyncConfigRequestData
        """
        super().__init__(kwargs)

        self_.data = data
