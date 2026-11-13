# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class AiGatewayRateLimitInstanceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first_seen": (datetime,),
            "input_tokens": (int,),
            "input_tokens_per_minute": (int, none_type),
            "instance_key": (str,),
            "last_seen": (datetime,),
            "limited_requests": (int,),
            "output_tokens": (int,),
            "output_tokens_per_minute": (int, none_type),
            "rate_limit_id": (UUID,),
            "requests": (int,),
            "requests_per_minute": (int, none_type),
            "split_dims": ({str: (str,)},),
            "usage_known": (bool,),
            "utilization": (float,),
            "would_limit_requests": (int,),
        }

    attribute_map = {
        "first_seen": "first_seen",
        "input_tokens": "input_tokens",
        "input_tokens_per_minute": "input_tokens_per_minute",
        "instance_key": "instance_key",
        "last_seen": "last_seen",
        "limited_requests": "limited_requests",
        "output_tokens": "output_tokens",
        "output_tokens_per_minute": "output_tokens_per_minute",
        "rate_limit_id": "rate_limit_id",
        "requests": "requests",
        "requests_per_minute": "requests_per_minute",
        "split_dims": "split_dims",
        "usage_known": "usage_known",
        "utilization": "utilization",
        "would_limit_requests": "would_limit_requests",
    }

    def __init__(
        self_,
        first_seen: datetime,
        input_tokens: int,
        instance_key: str,
        last_seen: datetime,
        limited_requests: int,
        output_tokens: int,
        rate_limit_id: UUID,
        requests: int,
        split_dims: Dict[str, str],
        usage_known: bool,
        utilization: float,
        would_limit_requests: int,
        input_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        output_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        requests_per_minute: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        One counter of a template rate limit and its live usage.

        :param first_seen: When the gateway first recorded a request for this counter.
        :type first_seen: datetime

        :param input_tokens: Input tokens counted in the rolling one-minute window.
        :type input_tokens: int

        :param input_tokens_per_minute: The rate limit's per-counter input token limit. Null when it doesn't limit input tokens.
        :type input_tokens_per_minute: int, none_type, optional

        :param instance_key: Opaque canonical key identifying the counter.
        :type instance_key: str

        :param last_seen: When the gateway last recorded a request for this counter; up to a few minutes behind live traffic.
        :type last_seen: datetime

        :param limited_requests: Requests this counter rejected in the last 15 minutes (ENFORCE).
        :type limited_requests: int

        :param output_tokens: Output tokens counted in the rolling one-minute window.
        :type output_tokens: int

        :param output_tokens_per_minute: The rate limit's per-counter output token limit. Null when it doesn't limit output tokens.
        :type output_tokens_per_minute: int, none_type, optional

        :param rate_limit_id: Rate limit UUID.
        :type rate_limit_id: UUID

        :param requests: Requests counted in the rolling one-minute window.
        :type requests: int

        :param requests_per_minute: The rate limit's per-counter request limit. Null when it doesn't limit requests.
        :type requests_per_minute: int, none_type, optional

        :param split_dims: The counter's value for each per-value dimension. user_id and team_id values are raw UUIDs.
        :type split_dims: {str: (str,)}

        :param usage_known: False when this counter's usage wasn't read because the request already read the most counters it may. Its usage then reads as zero.
        :type usage_known: bool

        :param utilization: The fullest of the rate limit's limits in the rolling window, as a fraction. 1 or more means the counter is at its limit.
        :type utilization: float

        :param would_limit_requests: Requests this counter would have rejected in the last 15 minutes (ALERT).
        :type would_limit_requests: int
        """
        if input_tokens_per_minute is not unset:
            kwargs["input_tokens_per_minute"] = input_tokens_per_minute
        if output_tokens_per_minute is not unset:
            kwargs["output_tokens_per_minute"] = output_tokens_per_minute
        if requests_per_minute is not unset:
            kwargs["requests_per_minute"] = requests_per_minute
        super().__init__(kwargs)

        self_.first_seen = first_seen
        self_.input_tokens = input_tokens
        self_.instance_key = instance_key
        self_.last_seen = last_seen
        self_.limited_requests = limited_requests
        self_.output_tokens = output_tokens
        self_.rate_limit_id = rate_limit_id
        self_.requests = requests
        self_.split_dims = split_dims
        self_.usage_known = usage_known
        self_.utilization = utilization
        self_.would_limit_requests = would_limit_requests
