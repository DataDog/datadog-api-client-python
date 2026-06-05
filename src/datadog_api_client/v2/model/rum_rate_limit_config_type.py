# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRateLimitConfigType(ModelSimple):
    """
    The type of the resource, always `rum_rate_limit_config`.

    :param value: If omitted defaults to "rum_rate_limit_config". Must be one of ["rum_rate_limit_config"].
    :type value: str
    """

    allowed_values = {
        "rum_rate_limit_config",
    }
    RUM_RATE_LIMIT_CONFIG: ClassVar["RumRateLimitConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRateLimitConfigType.RUM_RATE_LIMIT_CONFIG = RumRateLimitConfigType("rum_rate_limit_config")
