# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRateLimitUsageType(ModelSimple):
    """
    AI Gateway rate limit usage resource type.

    :param value: If omitted defaults to "rate-limit-usage". Must be one of ["rate-limit-usage"].
    :type value: str
    """

    allowed_values = {
        "rate-limit-usage",
    }
    RATE_LIMIT_USAGE: ClassVar["AiGatewayRateLimitUsageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRateLimitUsageType.RATE_LIMIT_USAGE = AiGatewayRateLimitUsageType("rate-limit-usage")
