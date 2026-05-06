# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus(ModelSimple):
    """
    The status of a backfilled maintenance update.

    :param value: Must be one of ["in_progress", "completed"].
    :type value: str
    """

    allowed_values = {
        "in_progress",
        "completed",
    }
    IN_PROGRESS: ClassVar["CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus"]
    COMPLETED: ClassVar["CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus.IN_PROGRESS = (
    CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus("in_progress")
)
CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus.COMPLETED = (
    CreateBackfilledMaintenanceRequestDataAttributesUpdatesItemsStatus("completed")
)
