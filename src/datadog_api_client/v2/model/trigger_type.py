# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TriggerType(ModelSimple):
    """
    The type of trigger for the investigation.

    :param value: If omitted defaults to "monitor_alert_trigger". Must be one of ["monitor_alert_trigger"].
    :type value: str
    """

    allowed_values = {
        "monitor_alert_trigger",
    }
    MONITOR_ALERT_TRIGGER: ClassVar["TriggerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TriggerType.MONITOR_ALERT_TRIGGER = TriggerType("monitor_alert_trigger")
