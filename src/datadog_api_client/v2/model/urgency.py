# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Urgency(ModelSimple):
    """
    Specifies the level of urgency for a routing rule (low, high, or dynamic).

    :param value: Must be one of ["low", "high", "dynamic"].
    :type value: str
    """

    allowed_values = {
        "low",
        "high",
        "dynamic",
    }
    LOW: ClassVar["Urgency"]
    HIGH: ClassVar["Urgency"]
    DYNAMIC: ClassVar["Urgency"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Urgency.LOW = Urgency("low")
Urgency.HIGH = Urgency("high")
Urgency.DYNAMIC = Urgency("dynamic")
