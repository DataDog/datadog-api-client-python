# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRateLimitWindowLimitWindow(ModelSimple):
    """
    The rolling window that a limit applies to. For per-minute limits, use the `*_per_minute` fields instead.

    :param value: Must be one of ["5m", "15m", "30m", "1h", "3h", "6h", "12h", "24h"].
    :type value: str
    """

    allowed_values = {
        "5m",
        "15m",
        "30m",
        "1h",
        "3h",
        "6h",
        "12h",
        "24h",
    }
    FIVE_MINUTES: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    FIFTEEN_MINUTES: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    THIRTY_MINUTES: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    ONE_HOUR: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    THREE_HOURS: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    SIX_HOURS: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    TWELVE_HOURS: ClassVar["AiGatewayRateLimitWindowLimitWindow"]
    TWENTY_FOUR_HOURS: ClassVar["AiGatewayRateLimitWindowLimitWindow"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRateLimitWindowLimitWindow.FIVE_MINUTES = AiGatewayRateLimitWindowLimitWindow("5m")
AiGatewayRateLimitWindowLimitWindow.FIFTEEN_MINUTES = AiGatewayRateLimitWindowLimitWindow("15m")
AiGatewayRateLimitWindowLimitWindow.THIRTY_MINUTES = AiGatewayRateLimitWindowLimitWindow("30m")
AiGatewayRateLimitWindowLimitWindow.ONE_HOUR = AiGatewayRateLimitWindowLimitWindow("1h")
AiGatewayRateLimitWindowLimitWindow.THREE_HOURS = AiGatewayRateLimitWindowLimitWindow("3h")
AiGatewayRateLimitWindowLimitWindow.SIX_HOURS = AiGatewayRateLimitWindowLimitWindow("6h")
AiGatewayRateLimitWindowLimitWindow.TWELVE_HOURS = AiGatewayRateLimitWindowLimitWindow("12h")
AiGatewayRateLimitWindowLimitWindow.TWENTY_FOUR_HOURS = AiGatewayRateLimitWindowLimitWindow("24h")
