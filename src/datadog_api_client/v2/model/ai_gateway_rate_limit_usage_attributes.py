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
)


class AiGatewayRateLimitUsageAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cost_microcents": (int,),
            "input_tokens": (int,),
            "limited_requests": (int,),
            "output_tokens": (int,),
            "requests": (int,),
            "would_limit_requests": (int,),
        }

    attribute_map = {
        "cost_microcents": "cost_microcents",
        "input_tokens": "input_tokens",
        "limited_requests": "limited_requests",
        "output_tokens": "output_tokens",
        "requests": "requests",
        "would_limit_requests": "would_limit_requests",
    }

    def __init__(
        self_,
        input_tokens: int,
        limited_requests: int,
        output_tokens: int,
        requests: int,
        would_limit_requests: int,
        cost_microcents: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Live consumption of one AI Gateway rate limit.

        :param cost_microcents: Priced spend, in microcents, counted in the rolling one-minute window. Only rules with a cost limit count it, so it is 0 for other rules and for the untracked and total entries.
        :type cost_microcents: int, optional

        :param input_tokens: Input tokens counted in the rolling one-minute window.
        :type input_tokens: int

        :param limited_requests: Requests this rate limit rejected in the last 15 minutes. Applies when mode is ENFORCE.
        :type limited_requests: int

        :param output_tokens: Output tokens counted in the rolling one-minute window.
        :type output_tokens: int

        :param requests: Requests counted in the rolling one-minute window.
        :type requests: int

        :param would_limit_requests: Requests this rate limit would have rejected in the last 15 minutes. Applies when mode is ALERT.
        :type would_limit_requests: int
        """
        if cost_microcents is not unset:
            kwargs["cost_microcents"] = cost_microcents
        super().__init__(kwargs)

        self_.input_tokens = input_tokens
        self_.limited_requests = limited_requests
        self_.output_tokens = output_tokens
        self_.requests = requests
        self_.would_limit_requests = would_limit_requests
