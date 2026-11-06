# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class AiGatewayRateLimitInstancesSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_count": (int,),
            "limiting_count": (int,),
            "max_utilization": (float,),
            "near_limit_count": (int,),
            "rate_limit_id": (UUID,),
            "truncated": (bool,),
        }

    attribute_map = {
        "instance_count": "instance_count",
        "limiting_count": "limiting_count",
        "max_utilization": "max_utilization",
        "near_limit_count": "near_limit_count",
        "rate_limit_id": "rate_limit_id",
        "truncated": "truncated",
    }

    def __init__(
        self_,
        instance_count: int,
        limiting_count: int,
        max_utilization: float,
        near_limit_count: int,
        rate_limit_id: UUID,
        truncated: bool,
        **kwargs,
    ):
        """
        Aggregate of a template rate limit's counters.

        :param instance_count: Number of counters.
        :type instance_count: int

        :param limiting_count: Counters that limited, or would have limited, a request in the last 15 minutes.
        :type limiting_count: int

        :param max_utilization: Utilization of the fullest counter.
        :type max_utilization: float

        :param near_limit_count: Counters at 80% or more of a limit in the rolling window.
        :type near_limit_count: int

        :param rate_limit_id: Rate limit UUID.
        :type rate_limit_id: UUID

        :param truncated: True when some recently active counters' usage wasn't read, so the counts may be low.
        :type truncated: bool
        """
        super().__init__(kwargs)

        self_.instance_count = instance_count
        self_.limiting_count = limiting_count
        self_.max_utilization = max_utilization
        self_.near_limit_count = near_limit_count
        self_.rate_limit_id = rate_limit_id
        self_.truncated = truncated
