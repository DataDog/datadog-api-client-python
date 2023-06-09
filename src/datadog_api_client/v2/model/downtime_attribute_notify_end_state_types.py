# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DowntimeAttributeNotifyEndStateTypes(ModelSimple):
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
    ALERT: ClassVar["DowntimeAttributeNotifyEndStateTypes"]
    NO_DATA: ClassVar["DowntimeAttributeNotifyEndStateTypes"]
    WARN: ClassVar["DowntimeAttributeNotifyEndStateTypes"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DowntimeAttributeNotifyEndStateTypes.ALERT = DowntimeAttributeNotifyEndStateTypes("alert")
DowntimeAttributeNotifyEndStateTypes.NO_DATA = DowntimeAttributeNotifyEndStateTypes("no data")
DowntimeAttributeNotifyEndStateTypes.WARN = DowntimeAttributeNotifyEndStateTypes("warn")
