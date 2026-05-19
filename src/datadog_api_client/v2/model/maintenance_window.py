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
    from datadog_api_client.v2.model.maintenance_window_attributes import MaintenanceWindowAttributes
    from datadog_api_client.v2.model.maintenance_window_resource_type import MaintenanceWindowResourceType


class MaintenanceWindow(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.maintenance_window_attributes import MaintenanceWindowAttributes
        from datadog_api_client.v2.model.maintenance_window_resource_type import MaintenanceWindowResourceType

        return {
            "attributes": (MaintenanceWindowAttributes,),
            "id": (str,),
            "type": (MaintenanceWindowResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: MaintenanceWindowAttributes, id: str, type: MaintenanceWindowResourceType, **kwargs
    ):
        """
        A maintenance window that defines a scheduled time period during which case-related notifications and automation rules are suppressed. Each maintenance window applies to cases matching a specified query.

        :param attributes: Attributes of a maintenance window, including its schedule and the query that determines which cases are affected.
        :type attributes: MaintenanceWindowAttributes

        :param id: The maintenance window's identifier.
        :type id: str

        :param type: JSON:API resource type for maintenance windows.
        :type type: MaintenanceWindowResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
