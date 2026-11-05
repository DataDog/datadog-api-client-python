# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode


class AiGatewayRateLimitUpdateAttributes(ModelNormal):
    validations = {
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
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode

        return {
            "enabled": (bool,),
            "input_tokens_per_minute": (int, none_type),
            "mode": (AiGatewayRateLimitMode,),
            "name": (str,),
            "output_tokens_per_minute": (int, none_type),
            "requests_per_minute": (int, none_type),
            "tags": ({str: (str,)}, none_type),
            "team_id": (str, none_type),
            "user_id": (str, none_type),
        }

    attribute_map = {
        "enabled": "enabled",
        "input_tokens_per_minute": "input_tokens_per_minute",
        "mode": "mode",
        "name": "name",
        "output_tokens_per_minute": "output_tokens_per_minute",
        "requests_per_minute": "requests_per_minute",
        "tags": "tags",
        "team_id": "team_id",
        "user_id": "user_id",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        input_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        mode: Union[AiGatewayRateLimitMode, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        output_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        requests_per_minute: Union[int, none_type, UnsetType] = unset,
        tags: Union[Dict[str, str], none_type, UnsetType] = unset,
        team_id: Union[str, none_type, UnsetType] = unset,
        user_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to update an AI Gateway rate limit. Only sent fields are changed.

        :param enabled: Whether this rate limit is active.
        :type enabled: bool, optional

        :param input_tokens_per_minute: Set to 0 to remove the request limit. Null is ignored. At least one limit must remain.
        :type input_tokens_per_minute: int, none_type, optional

        :param mode: Action taken when request rate exceeds the limit.
        :type mode: AiGatewayRateLimitMode, optional

        :param name: Rate limit name.
        :type name: str, optional

        :param output_tokens_per_minute: Set to 0 to remove the request limit. Null is ignored. At least one limit must remain.
        :type output_tokens_per_minute: int, none_type, optional

        :param requests_per_minute: Set to 0 to remove the request limit. Null is ignored. At least one limit must remain.
        :type requests_per_minute: int, none_type, optional

        :param tags: Replaces all scope tags. An empty object clears them. Null is ignored.
        :type tags: {str: (str,)}, none_type, optional

        :param team_id: Replaces the Team scope. An empty string clears it. Null is ignored.
        :type team_id: str, none_type, optional

        :param user_id: Replaces the user scope. An empty string clears it. Null is ignored.
        :type user_id: str, none_type, optional
        """
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
        super().__init__(kwargs)
