# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRateLimitWindowLimitMetric(ModelSimple):
    """
    The metric that a window limit counts. `cost` counts priced spend in microcents.

    :param value: Must be one of ["requests", "input_tokens", "output_tokens", "cost"].
    :type value: str
    """

    allowed_values = {
        "requests",
        "input_tokens",
        "output_tokens",
        "cost",
    }
    REQUESTS: ClassVar["AiGatewayRateLimitWindowLimitMetric"]
    INPUT_TOKENS: ClassVar["AiGatewayRateLimitWindowLimitMetric"]
    OUTPUT_TOKENS: ClassVar["AiGatewayRateLimitWindowLimitMetric"]
    COST: ClassVar["AiGatewayRateLimitWindowLimitMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRateLimitWindowLimitMetric.REQUESTS = AiGatewayRateLimitWindowLimitMetric("requests")
AiGatewayRateLimitWindowLimitMetric.INPUT_TOKENS = AiGatewayRateLimitWindowLimitMetric("input_tokens")
AiGatewayRateLimitWindowLimitMetric.OUTPUT_TOKENS = AiGatewayRateLimitWindowLimitMetric("output_tokens")
AiGatewayRateLimitWindowLimitMetric.COST = AiGatewayRateLimitWindowLimitMetric("cost")
