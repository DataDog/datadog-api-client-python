# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MaintenanceWindowResourceType(ModelSimple):
    """
    JSON:API resource type for maintenance windows.

    :param value: If omitted defaults to "maintenance_window". Must be one of ["maintenance_window"].
    :type value: str
    """

    allowed_values = {
        "maintenance_window",
    }
    MAINTENANCE_WINDOW: ClassVar["MaintenanceWindowResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MaintenanceWindowResourceType.MAINTENANCE_WINDOW = MaintenanceWindowResourceType("maintenance_window")
