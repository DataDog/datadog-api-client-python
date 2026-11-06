# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRateLimitInstancesSummaryType(ModelSimple):
    """
    AI Gateway rate limit counter summary resource type.

    :param value: If omitted defaults to "rate-limit-instances-summary". Must be one of ["rate-limit-instances-summary"].
    :type value: str
    """

    allowed_values = {
        "rate-limit-instances-summary",
    }
    RATE_LIMIT_INSTANCES_SUMMARY: ClassVar["AiGatewayRateLimitInstancesSummaryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRateLimitInstancesSummaryType.RATE_LIMIT_INSTANCES_SUMMARY = AiGatewayRateLimitInstancesSummaryType(
    "rate-limit-instances-summary"
)
