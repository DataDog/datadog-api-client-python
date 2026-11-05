# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_reasoning_control_type import AiGatewayModelReasoningControlType


class AiGatewayModelReasoningControl(ModelNormal):
    validations = {
        "max_budget_tokens": {
            "inclusive_minimum": 0,
        },
        "min_budget_tokens": {
            "inclusive_minimum": -1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_reasoning_control_type import (
            AiGatewayModelReasoningControlType,
        )

        return {
            "effort_levels": ([str, none_type],),
            "max_budget_tokens": (int,),
            "min_budget_tokens": (int,),
            "type": (AiGatewayModelReasoningControlType,),
        }

    attribute_map = {
        "effort_levels": "effort_levels",
        "max_budget_tokens": "max_budget_tokens",
        "min_budget_tokens": "min_budget_tokens",
        "type": "type",
    }

    def __init__(
        self_,
        type: AiGatewayModelReasoningControlType,
        effort_levels: Union[List[str], UnsetType] = unset,
        max_budget_tokens: Union[int, UnsetType] = unset,
        min_budget_tokens: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        One supported mechanism for configuring model reasoning.

        :param effort_levels: Supported effort values in provider order for an effort control.
        :type effort_levels: [str, none_type], optional

        :param max_budget_tokens: Maximum reasoning-token budget.
        :type max_budget_tokens: int, optional

        :param min_budget_tokens: Minimum reasoning-token budget.
        :type min_budget_tokens: int, optional

        :param type: Reasoning-control mechanism.
        :type type: AiGatewayModelReasoningControlType
        """
        if effort_levels is not unset:
            kwargs["effort_levels"] = effort_levels
        if max_budget_tokens is not unset:
            kwargs["max_budget_tokens"] = max_budget_tokens
        if min_budget_tokens is not unset:
            kwargs["min_budget_tokens"] = min_budget_tokens
        super().__init__(kwargs)

        self_.type = type
