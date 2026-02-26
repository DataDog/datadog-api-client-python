# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.patch_maintenance_request_data_attributes import (
        PatchMaintenanceRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType


class PatchMaintenanceRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_maintenance_request_data_attributes import (
            PatchMaintenanceRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType

        return {
            "attributes": (PatchMaintenanceRequestDataAttributes,),
            "id": (UUID,),
            "type": (PatchMaintenanceRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: PatchMaintenanceRequestDataAttributes,
        id: UUID,
        type: PatchMaintenanceRequestDataType,
        **kwargs,
    ):
        """


        :param attributes: The supported attributes for updating a maintenance.
        :type attributes: PatchMaintenanceRequestDataAttributes

        :param id: The ID of the maintenance.
        :type id: UUID

        :param type: Maintenances resource type.
        :type type: PatchMaintenanceRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
