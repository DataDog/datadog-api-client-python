# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DowntimeNotifyEndStateTypes(ModelSimple):
    """
    State that will trigger a monitor notification when the `notify_end_types` action occurs.

    :param value: Must be one of ["alert", "no data", "warn"].
    :type value: str
    """

    allowed_values = {
        "alert",
        "no data",
        "warn",
    }
    ALERT: ClassVar["DowntimeNotifyEndStateTypes"]
    NO_DATA: ClassVar["DowntimeNotifyEndStateTypes"]
    WARN: ClassVar["DowntimeNotifyEndStateTypes"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DowntimeNotifyEndStateTypes.ALERT = DowntimeNotifyEndStateTypes("alert")
DowntimeNotifyEndStateTypes.NO_DATA = DowntimeNotifyEndStateTypes("no data")
DowntimeNotifyEndStateTypes.WARN = DowntimeNotifyEndStateTypes("warn")
