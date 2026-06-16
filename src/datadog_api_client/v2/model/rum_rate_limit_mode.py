# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRateLimitMode(ModelSimple):
    """
    The rate limit mode. `custom` enforces a fixed session limit, while
        `adaptive` dynamically adjusts retention.

    :param value: Must be one of ["custom", "adaptive"].
    :type value: str
    """

    allowed_values = {
        "custom",
        "adaptive",
    }
    CUSTOM: ClassVar["RumRateLimitMode"]
    ADAPTIVE: ClassVar["RumRateLimitMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRateLimitMode.CUSTOM = RumRateLimitMode("custom")
RumRateLimitMode.ADAPTIVE = RumRateLimitMode("adaptive")
