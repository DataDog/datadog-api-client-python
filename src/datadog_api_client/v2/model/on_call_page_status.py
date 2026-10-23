# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageStatus(ModelSimple):
    """
    The current status of the On-Call Page.

    :param value: Must be one of ["triggered", "acknowledged", "resolved"].
    :type value: str
    """

    allowed_values = {
        "triggered",
        "acknowledged",
        "resolved",
    }
    TRIGGERED: ClassVar["OnCallPageStatus"]
    ACKNOWLEDGED: ClassVar["OnCallPageStatus"]
    RESOLVED: ClassVar["OnCallPageStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageStatus.TRIGGERED = OnCallPageStatus("triggered")
OnCallPageStatus.ACKNOWLEDGED = OnCallPageStatus("acknowledged")
OnCallPageStatus.RESOLVED = OnCallPageStatus("resolved")
