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
    from datadog_api_client.v2.model.create_maintenance_request_data_attributes import (
        CreateMaintenanceRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType


class CreateMaintenanceRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_maintenance_request_data_attributes import (
            CreateMaintenanceRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_maintenance_request_data_type import PatchMaintenanceRequestDataType

        return {
            "attributes": (CreateMaintenanceRequestDataAttributes,),
            "type": (PatchMaintenanceRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: CreateMaintenanceRequestDataAttributes, type: PatchMaintenanceRequestDataType, **kwargs
    ):
        """


        :param attributes: The supported attributes for creating a maintenance.
        :type attributes: CreateMaintenanceRequestDataAttributes

        :param type: Maintenances resource type.
        :type type: PatchMaintenanceRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
