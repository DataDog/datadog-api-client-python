# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DowntimeStatus(ModelSimple):
    """
    The current status of the downtime.

    :param value: Must be one of ["active", "canceled", "ended", "scheduled"].
    :type value: str
    """

    allowed_values = {
        "active",
        "canceled",
        "ended",
        "scheduled",
    }
    ACTIVE: ClassVar["DowntimeStatus"]
    CANCELED: ClassVar["DowntimeStatus"]
    ENDED: ClassVar["DowntimeStatus"]
    SCHEDULED: ClassVar["DowntimeStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DowntimeStatus.ACTIVE = DowntimeStatus("active")
DowntimeStatus.CANCELED = DowntimeStatus("canceled")
DowntimeStatus.ENDED = DowntimeStatus("ended")
DowntimeStatus.SCHEDULED = DowntimeStatus("scheduled")
