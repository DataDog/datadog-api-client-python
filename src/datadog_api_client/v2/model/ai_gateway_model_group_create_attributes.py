# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_group_binding import AiGatewayModelGroupBinding
    from datadog_api_client.v2.model.ai_gateway_max_reasoning_level import AiGatewayMaxReasoningLevel


class AiGatewayModelGroupCreateAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_group_binding import AiGatewayModelGroupBinding
        from datadog_api_client.v2.model.ai_gateway_max_reasoning_level import AiGatewayMaxReasoningLevel

        return {
            "allow_fast_mode": (bool,),
            "bindings": ([AiGatewayModelGroupBinding],),
            "max_reasoning_level": (AiGatewayMaxReasoningLevel,),
            "model_ids": ([int],),
            "name": (str,),
            "provider_ids": ([int],),
            "routing_rule_slugs": ([str],),
        }

    attribute_map = {
        "allow_fast_mode": "allow_fast_mode",
        "bindings": "bindings",
        "max_reasoning_level": "max_reasoning_level",
        "model_ids": "model_ids",
        "name": "name",
        "provider_ids": "provider_ids",
        "routing_rule_slugs": "routing_rule_slugs",
    }

    def __init__(
        self_,
        name: str,
        allow_fast_mode: Union[bool, UnsetType] = unset,
        bindings: Union[List[AiGatewayModelGroupBinding], UnsetType] = unset,
        max_reasoning_level: Union[AiGatewayMaxReasoningLevel, UnsetType] = unset,
        model_ids: Union[List[int], UnsetType] = unset,
        provider_ids: Union[List[int], UnsetType] = unset,
        routing_rule_slugs: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to create an AI Gateway model group.

        :param allow_fast_mode: Whether fast mode is allowed for models and routing rules in the group.
        :type allow_fast_mode: bool, optional

        :param bindings: Optional initial model-group access bindings.
        :type bindings: [AiGatewayModelGroupBinding], optional

        :param max_reasoning_level: Maximum reasoning level permitted by a model group.
        :type max_reasoning_level: AiGatewayMaxReasoningLevel, optional

        :param model_ids: Model catalog IDs to select. New selections require provider View.
        :type model_ids: [int], optional

        :param name: Human-readable resource name.
        :type name: str

        :param provider_ids: Explicit provider selections, including current and future models. Omit to preserve selections on update; an empty array clears them. Null is invalid. New selections require provider View; saved hidden IDs can be retained or removed.
        :type provider_ids: [int], optional

        :param routing_rule_slugs: Organization-unique routing rule slugs, such as coding-route.
        :type routing_rule_slugs: [str], optional
        """
        if allow_fast_mode is not unset:
            kwargs["allow_fast_mode"] = allow_fast_mode
        if bindings is not unset:
            kwargs["bindings"] = bindings
        if max_reasoning_level is not unset:
            kwargs["max_reasoning_level"] = max_reasoning_level
        if model_ids is not unset:
            kwargs["model_ids"] = model_ids
        if provider_ids is not unset:
            kwargs["provider_ids"] = provider_ids
        if routing_rule_slugs is not unset:
            kwargs["routing_rule_slugs"] = routing_rule_slugs
        super().__init__(kwargs)

        self_.name = name
