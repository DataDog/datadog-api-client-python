# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayRateLimitInstanceSort(ModelSimple):
    """
    Sort order for rate limit counters.

    :param value: If omitted defaults to "utilization_desc". Must be one of ["utilization_desc", "last_seen_desc", "key_asc"].
    :type value: str
    """

    allowed_values = {
        "utilization_desc",
        "last_seen_desc",
        "key_asc",
    }
    UTILIZATION_DESC: ClassVar["AiGatewayRateLimitInstanceSort"]
    LAST_SEEN_DESC: ClassVar["AiGatewayRateLimitInstanceSort"]
    KEY_ASC: ClassVar["AiGatewayRateLimitInstanceSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayRateLimitInstanceSort.UTILIZATION_DESC = AiGatewayRateLimitInstanceSort("utilization_desc")
AiGatewayRateLimitInstanceSort.LAST_SEEN_DESC = AiGatewayRateLimitInstanceSort("last_seen_desc")
AiGatewayRateLimitInstanceSort.KEY_ASC = AiGatewayRateLimitInstanceSort("key_asc")
