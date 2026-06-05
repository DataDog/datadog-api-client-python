# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRateLimitWindowType(ModelSimple):
    """
    The window type over which the session limit is enforced.

    :param value: If omitted defaults to "daily". Must be one of ["daily"].
    :type value: str
    """

    allowed_values = {
        "daily",
    }
    DAILY: ClassVar["RumRateLimitWindowType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRateLimitWindowType.DAILY = RumRateLimitWindowType("daily")
