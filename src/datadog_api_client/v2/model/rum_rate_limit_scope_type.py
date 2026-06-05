# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRateLimitScopeType(ModelSimple):
    """
    The type of scope the rate limit configuration applies to.

    :param value: If omitted defaults to "application". Must be one of ["application"].
    :type value: str
    """

    allowed_values = {
        "application",
    }
    APPLICATION: ClassVar["RumRateLimitScopeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRateLimitScopeType.APPLICATION = RumRateLimitScopeType("application")
