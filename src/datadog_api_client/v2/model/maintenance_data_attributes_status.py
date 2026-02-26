# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MaintenanceDataAttributesStatus(ModelSimple):
    """
    The status of the maintenance.

    :param value: Must be one of ["scheduled", "in_progress", "completed"].
    :type value: str
    """

    allowed_values = {
        "scheduled",
        "in_progress",
        "completed",
    }
    SCHEDULED: ClassVar["MaintenanceDataAttributesStatus"]
    IN_PROGRESS: ClassVar["MaintenanceDataAttributesStatus"]
    COMPLETED: ClassVar["MaintenanceDataAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MaintenanceDataAttributesStatus.SCHEDULED = MaintenanceDataAttributesStatus("scheduled")
MaintenanceDataAttributesStatus.IN_PROGRESS = MaintenanceDataAttributesStatus("in_progress")
MaintenanceDataAttributesStatus.COMPLETED = MaintenanceDataAttributesStatus("completed")
