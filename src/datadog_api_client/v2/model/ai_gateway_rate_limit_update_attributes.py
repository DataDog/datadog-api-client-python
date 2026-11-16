# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode
    from datadog_api_client.v2.model.ai_gateway_rate_limit_window_limit import AiGatewayRateLimitWindowLimit


class AiGatewayRateLimitUpdateAttributes(ModelNormal):
    validations = {
        "cost_microcents_per_minute": {
            "inclusive_minimum": 0,
        },
        "input_tokens_per_minute": {
            "inclusive_maximum": 100000000000,
            "inclusive_minimum": 0,
        },
        "output_tokens_per_minute": {
            "inclusive_maximum": 100000000000,
            "inclusive_minimum": 0,
        },
        "requests_per_minute": {
            "inclusive_maximum": 10000000,
            "inclusive_minimum": 0,
        },
        "window_limits": {
            "max_items": 4,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode
        from datadog_api_client.v2.model.ai_gateway_rate_limit_window_limit import AiGatewayRateLimitWindowLimit

        return {
            "cost_microcents_per_minute": (int, none_type),
            "enabled": (bool,),
            "input_tokens_per_minute": (int, none_type),
            "mode": (AiGatewayRateLimitMode,),
            "name": (str,),
            "output_tokens_per_minute": (int, none_type),
            "requests_per_minute": (int, none_type),
            "tags": ({str: (str,)}, none_type),
            "team_id": (str, none_type),
            "user_id": (str, none_type),
            "window_limits": ([AiGatewayRateLimitWindowLimit], none_type),
        }

    attribute_map = {
        "cost_microcents_per_minute": "cost_microcents_per_minute",
        "enabled": "enabled",
        "input_tokens_per_minute": "input_tokens_per_minute",
        "mode": "mode",
        "name": "name",
        "output_tokens_per_minute": "output_tokens_per_minute",
        "requests_per_minute": "requests_per_minute",
        "tags": "tags",
        "team_id": "team_id",
        "user_id": "user_id",
        "window_limits": "window_limits",
    }

    def __init__(
        self_,
        cost_microcents_per_minute: Union[int, none_type, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        input_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        mode: Union[AiGatewayRateLimitMode, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        output_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        requests_per_minute: Union[int, none_type, UnsetType] = unset,
        tags: Union[Dict[str, str], none_type, UnsetType] = unset,
        team_id: Union[str, none_type, UnsetType] = unset,
        user_id: Union[str, none_type, UnsetType] = unset,
        window_limits: Union[List[AiGatewayRateLimitWindowLimit], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to update an AI Gateway rate limit. Only sent fields are changed.

        :param cost_microcents_per_minute: Spend limit in microcents per rolling minute. Set to 0 to remove the cost limit. Null is ignored. At least one limit, per-minute or in ``window_limits`` , must remain.
        :type cost_microcents_per_minute: int, none_type, optional

        :param enabled: Whether this rate limit is active.
        :type enabled: bool, optional

        :param input_tokens_per_minute: Set to 0 to remove the input token limit. Null is ignored. At least one limit, per-minute or in ``window_limits`` , must remain.
        :type input_tokens_per_minute: int, none_type, optional

        :param mode: Action taken when request rate exceeds the limit.
        :type mode: AiGatewayRateLimitMode, optional

        :param name: Rate limit name.
        :type name: str, optional

        :param output_tokens_per_minute: Set to 0 to remove the output token limit. Null is ignored. At least one limit, per-minute or in ``window_limits`` , must remain.
        :type output_tokens_per_minute: int, none_type, optional

        :param requests_per_minute: Set to 0 to remove the request limit. Null is ignored. At least one limit, per-minute or in ``window_limits`` , must remain.
        :type requests_per_minute: int, none_type, optional

        :param tags: Replaces all scope tags. An empty object clears them. Null is ignored.
        :type tags: {str: (str,)}, none_type, optional

        :param team_id: Replaces the Team scope. An empty string clears it. Null is ignored.
        :type team_id: str, none_type, optional

        :param user_id: Replaces the user scope. An empty string clears it. Null is ignored.
        :type user_id: str, none_type, optional

        :param window_limits: Replaces all limits over rolling windows longer than a minute. If ``window_limits`` is null or omitted, the existing limits are unchanged. An empty array removes them all. This field is available only to organizations with the feature enabled. Other organizations receive a 400 Bad Request response for a non-empty list. The same rules as on create apply. A rule can have at most four limits in total, including any per-minute limits that are set. Each metric and window pair can appear only once, and for the same metric, a longer window must have a larger amount. In ``ENFORCE`` mode, if the list includes a ``cost`` limit, the gateway rejects requests to models with no pricing because their cost can't be counted.
        :type window_limits: [AiGatewayRateLimitWindowLimit], none_type, optional
        """
        if cost_microcents_per_minute is not unset:
            kwargs["cost_microcents_per_minute"] = cost_microcents_per_minute
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if input_tokens_per_minute is not unset:
            kwargs["input_tokens_per_minute"] = input_tokens_per_minute
        if mode is not unset:
            kwargs["mode"] = mode
        if name is not unset:
            kwargs["name"] = name
        if output_tokens_per_minute is not unset:
            kwargs["output_tokens_per_minute"] = output_tokens_per_minute
        if requests_per_minute is not unset:
            kwargs["requests_per_minute"] = requests_per_minute
        if tags is not unset:
            kwargs["tags"] = tags
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if user_id is not unset:
            kwargs["user_id"] = user_id
        if window_limits is not unset:
            kwargs["window_limits"] = window_limits
        super().__init__(kwargs)
