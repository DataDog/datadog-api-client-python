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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode


class AiGatewayRateLimitCreateAttributes(ModelNormal):
    validations = {
        "input_tokens_per_minute": {
            "inclusive_maximum": 100000000000,
            "inclusive_minimum": 1,
        },
        "output_tokens_per_minute": {
            "inclusive_maximum": 100000000000,
            "inclusive_minimum": 1,
        },
        "requests_per_minute": {
            "inclusive_maximum": 10000000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_mode import AiGatewayRateLimitMode

        return {
            "input_tokens_per_minute": (int, none_type),
            "mode": (AiGatewayRateLimitMode,),
            "name": (str,),
            "output_tokens_per_minute": (int, none_type),
            "requests_per_minute": (int, none_type),
            "tags": ({str: (str,)},),
            "team_id": (UUID,),
            "user_id": (UUID,),
        }

    attribute_map = {
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
        name: str,
        input_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        mode: Union[AiGatewayRateLimitMode, UnsetType] = unset,
        output_tokens_per_minute: Union[int, none_type, UnsetType] = unset,
        requests_per_minute: Union[int, none_type, UnsetType] = unset,
        tags: Union[Dict[str, str], UnsetType] = unset,
        team_id: Union[UUID, UnsetType] = unset,
        user_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to create an AI Gateway rate limit.

        :param input_tokens_per_minute: Maximum input tokens per rolling minute.
        :type input_tokens_per_minute: int, none_type, optional

        :param mode: Action taken when request rate exceeds the limit.
        :type mode: AiGatewayRateLimitMode, optional

        :param name: Rate limit name. Must not be empty.
        :type name: str

        :param output_tokens_per_minute: Maximum output tokens per rolling minute.
        :type output_tokens_per_minute: int, none_type, optional

        :param requests_per_minute: Maximum requests per rolling minute. At least one of ``requests_per_minute`` , ``input_tokens_per_minute`` , and ``output_tokens_per_minute`` is required.
        :type requests_per_minute: int, none_type, optional

        :param tags: Optional scope tags, such as ``provider`` , ``model`` , ``ml_app`` , or custom dimensions. A request matches when it has all of these tags. The reserved metadata keys ``name`` , ``budget_name`` , and ``span_filter`` are rejected.
        :type tags: {str: (str,)}, optional

        :param team_id: Optional UUID. Count only requests attributed to this Datadog Team.
        :type team_id: UUID, optional

        :param user_id: Optional UUID. Count only this user's requests.
        :type user_id: UUID, optional
        """
        if input_tokens_per_minute is not unset:
            kwargs["input_tokens_per_minute"] = input_tokens_per_minute
        if mode is not unset:
            kwargs["mode"] = mode
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

        self_.name = name
