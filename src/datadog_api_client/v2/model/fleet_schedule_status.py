# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetScheduleStatus(ModelSimple):
    """
    The status of the schedule.
        - `active`: The schedule is active and will create deployments according to its recurrence rule.
        - `inactive`: The schedule is inactive and will not create any deployments.

    :param value: Must be one of ["active", "inactive"].
    :type value: str
    """

    allowed_values = {
        "active",
        "inactive",
    }
    ACTIVE: ClassVar["FleetScheduleStatus"]
    INACTIVE: ClassVar["FleetScheduleStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetScheduleStatus.ACTIVE = FleetScheduleStatus("active")
FleetScheduleStatus.INACTIVE = FleetScheduleStatus("inactive")
