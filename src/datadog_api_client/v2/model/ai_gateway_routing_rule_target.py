# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_routing_reasoning_level import AiGatewayRoutingReasoningLevel
    from datadog_api_client.v2.model.ai_gateway_routing_rule_target_type import AiGatewayRoutingRuleTargetType


class AiGatewayRoutingRuleTarget(ModelNormal):
    validations = {
        "id": {
            "inclusive_minimum": 1,
        },
        "model_id": {
            "inclusive_minimum": 1,
        },
        "weight": {
            "inclusive_maximum": 10000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_reasoning_level import AiGatewayRoutingReasoningLevel
        from datadog_api_client.v2.model.ai_gateway_routing_rule_target_type import AiGatewayRoutingRuleTargetType

        return {
            "default": (bool,),
            "id": (int,),
            "model": (str,),
            "model_id": (int,),
            "provider": (str,),
            "reasoning_level": (AiGatewayRoutingReasoningLevel,),
            "rubric": (str,),
            "slug": (str,),
            "type": (AiGatewayRoutingRuleTargetType,),
            "weight": (int,),
        }

    attribute_map = {
        "default": "default",
        "id": "id",
        "model": "model",
        "model_id": "model_id",
        "provider": "provider",
        "reasoning_level": "reasoning_level",
        "rubric": "rubric",
        "slug": "slug",
        "type": "type",
        "weight": "weight",
    }

    def __init__(
        self_,
        type: AiGatewayRoutingRuleTargetType,
        default: Union[bool, UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        model: Union[str, UnsetType] = unset,
        model_id: Union[int, UnsetType] = unset,
        provider: Union[str, UnsetType] = unset,
        reasoning_level: Union[AiGatewayRoutingReasoningLevel, none_type, UnsetType] = unset,
        rubric: Union[str, UnsetType] = unset,
        slug: Union[str, UnsetType] = unset,
        weight: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Model target or reference to another routing rule.

        :param default: Present and true for the default classified destination.
        :type default: bool, optional

        :param id: Saved target row ID. On replacement, retain this ID only within its original route and at most once. A stale or foreign ID is rejected.
        :type id: int, optional

        :param model: Model name or pattern. Omitted when the caller cannot view its provider.
        :type model: str, optional

        :param model_id: Opaque model catalog ID for a concrete model target. New selections require provider View; saved selections can be retained without metadata.
        :type model_id: int, optional

        :param provider: Provider slug. Omitted for dynamic resolution and when the caller cannot view its provider.
        :type provider: str, optional

        :param reasoning_level: Optional reasoning effort preference for this model destination. Must be supported by the selected model and provider. For provider "*", every eligible provider must support the level. An explicit value overrides the request's reasoning setting, subject to model-group policy. Omitted or null preserves request and provider behavior; none is an explicit level, not the default. On update, omission preserves a saved target override; null explicitly clears it. Routing-rule references cannot set this field; each referenced model destination owns its override. If an override cannot be applied at runtime, the gateway keeps the destination and restores the caller's original reasoning settings, or preserves the provider default when omitted. It rechecks all applicable route and model-group policies against those settings before sending. Model-group max_reasoning_level enforces hard limits; the override is not an additional cap. Normal fallback applies if governance denies the resulting request or the destination cannot otherwise serve it. Metrics and span tags record the override outcome and incompatibility reason. When response headers have not already been committed, ``X-Ai-Gateway-Reasoning-Override`` reports applied or not_applied for the returned attempt, and ``X-Ai-Gateway-Reasoning-Override-Reason`` reports the reason when not applied.
        :type reasoning_level: AiGatewayRoutingReasoningLevel, none_type, optional

        :param rubric: Destination rubric, present only for non-default targets in classified tiers.
        :type rubric: str, optional

        :param slug: Referenced route slug. Omitted when the caller lacks View; only the parent-local occurrence ID remains.
        :type slug: str, optional

        :param type: Type of routing target.
        :type type: AiGatewayRoutingRuleTargetType

        :param weight: Effective relative weight. Returned only for targets in weighted_affinity tiers.
        :type weight: int, optional
        """
        if default is not unset:
            kwargs["default"] = default
        if id is not unset:
            kwargs["id"] = id
        if model is not unset:
            kwargs["model"] = model
        if model_id is not unset:
            kwargs["model_id"] = model_id
        if provider is not unset:
            kwargs["provider"] = provider
        if reasoning_level is not unset:
            kwargs["reasoning_level"] = reasoning_level
        if rubric is not unset:
            kwargs["rubric"] = rubric
        if slug is not unset:
            kwargs["slug"] = slug
        if weight is not unset:
            kwargs["weight"] = weight
        super().__init__(kwargs)

        self_.type = type
