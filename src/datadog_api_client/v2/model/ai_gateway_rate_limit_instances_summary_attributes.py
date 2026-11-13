# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


class AiGatewayRateLimitInstancesSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_count": (int,),
            "limited_requests": (int,),
            "limiting_count": (int,),
            "max_utilization": (float,),
            "near_limit_count": (int,),
            "rate_limit_id": (UUID,),
            "scope_restricted": (bool,),
            "truncated": (bool,),
            "would_limit_requests": (int,),
        }

    attribute_map = {
        "instance_count": "instance_count",
        "limited_requests": "limited_requests",
        "limiting_count": "limiting_count",
        "max_utilization": "max_utilization",
        "near_limit_count": "near_limit_count",
        "rate_limit_id": "rate_limit_id",
        "scope_restricted": "scope_restricted",
        "truncated": "truncated",
        "would_limit_requests": "would_limit_requests",
    }

    def __init__(
        self_,
        instance_count: int,
        limiting_count: int,
        max_utilization: float,
        near_limit_count: int,
        rate_limit_id: UUID,
        truncated: bool,
        limited_requests: Union[int, UnsetType] = unset,
        scope_restricted: Union[bool, UnsetType] = unset,
        would_limit_requests: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregate of a template rate limit's counters.

        :param instance_count: Number of counters.
        :type instance_count: int

        :param limited_requests: Requests the counters rejected in the last 15 minutes (ENFORCE), totaled over the counters whose usage was read.
        :type limited_requests: int, optional

        :param limiting_count: Counters that limited, or would have limited, a request in the last 15 minutes.
        :type limiting_count: int

        :param max_utilization: Utilization of the fullest counter.
        :type max_utilization: float

        :param near_limit_count: Counters at 80% or more of a limit in the rolling window.
        :type near_limit_count: int

        :param rate_limit_id: Rate limit UUID.
        :type rate_limit_id: UUID

        :param scope_restricted: True when the caller can't see the template's selector because it lists a provider or model the caller can't access. The counters are then hidden, and every count is zero.
        :type scope_restricted: bool, optional

        :param truncated: True when some recently active counters' usage wasn't read, so the counts may be low.
        :type truncated: bool

        :param would_limit_requests: Requests the counters would have rejected in the last 15 minutes (ALERT), totaled over the counters whose usage was read.
        :type would_limit_requests: int, optional
        """
        if limited_requests is not unset:
            kwargs["limited_requests"] = limited_requests
        if scope_restricted is not unset:
            kwargs["scope_restricted"] = scope_restricted
        if would_limit_requests is not unset:
            kwargs["would_limit_requests"] = would_limit_requests
        super().__init__(kwargs)

        self_.instance_count = instance_count
        self_.limiting_count = limiting_count
        self_.max_utilization = max_utilization
        self_.near_limit_count = near_limit_count
        self_.rate_limit_id = rate_limit_id
        self_.truncated = truncated
