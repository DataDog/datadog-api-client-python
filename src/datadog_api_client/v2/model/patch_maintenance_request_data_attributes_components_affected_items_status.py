# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus(ModelSimple):
    """
    The status of the component.

    :param value: Must be one of ["operational", "maintenance"].
    :type value: str
    """

    allowed_values = {
        "operational",
        "maintenance",
    }
    OPERATIONAL: ClassVar["PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus"]
    MAINTENANCE: ClassVar["PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus.OPERATIONAL = (
    PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus("operational")
)
PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus.MAINTENANCE = (
    PatchMaintenanceRequestDataAttributesComponentsAffectedItemsStatus("maintenance")
)
