# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MaintenanceUpdateDataAttributesStatus(ModelSimple):
    """
    The status of the maintenance update.

    :param value: Must be one of ["scheduled", "in_progress", "completed", "canceled"].
    :type value: str
    """

    allowed_values = {
        "scheduled",
        "in_progress",
        "completed",
        "canceled",
    }
    SCHEDULED: ClassVar["MaintenanceUpdateDataAttributesStatus"]
    IN_PROGRESS: ClassVar["MaintenanceUpdateDataAttributesStatus"]
    COMPLETED: ClassVar["MaintenanceUpdateDataAttributesStatus"]
    CANCELED: ClassVar["MaintenanceUpdateDataAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MaintenanceUpdateDataAttributesStatus.SCHEDULED = MaintenanceUpdateDataAttributesStatus("scheduled")
MaintenanceUpdateDataAttributesStatus.IN_PROGRESS = MaintenanceUpdateDataAttributesStatus("in_progress")
MaintenanceUpdateDataAttributesStatus.COMPLETED = MaintenanceUpdateDataAttributesStatus("completed")
MaintenanceUpdateDataAttributesStatus.CANCELED = MaintenanceUpdateDataAttributesStatus("canceled")
