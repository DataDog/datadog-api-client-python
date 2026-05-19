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
    from datadog_api_client.v2.model.maintenance_window_update_attributes import MaintenanceWindowUpdateAttributes
    from datadog_api_client.v2.model.maintenance_window_resource_type import MaintenanceWindowResourceType


class MaintenanceWindowUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_window_update_attributes import MaintenanceWindowUpdateAttributes
        from datadog_api_client.v2.model.maintenance_window_resource_type import MaintenanceWindowResourceType

        return {
            "attributes": (MaintenanceWindowUpdateAttributes,),
            "type": (MaintenanceWindowResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: MaintenanceWindowResourceType,
        attributes: Union[MaintenanceWindowUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating a maintenance window.

        :param attributes: Attributes that can be updated on a maintenance window. All fields are optional; only provided fields are changed.
        :type attributes: MaintenanceWindowUpdateAttributes, optional

        :param type: JSON:API resource type for maintenance windows.
        :type type: MaintenanceWindowResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
