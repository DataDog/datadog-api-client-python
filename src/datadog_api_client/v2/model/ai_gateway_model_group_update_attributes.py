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
    from datadog_api_client.v2.model.ai_gateway_nullable_max_reasoning_level import AiGatewayNullableMaxReasoningLevel


class AiGatewayModelGroupUpdateAttributes(ModelNormal):
    validations = {
        "expected_revision": {
            "inclusive_minimum": 0,
        },
        "name": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_nullable_max_reasoning_level import (
            AiGatewayNullableMaxReasoningLevel,
        )

        return {
            "allow_fast_mode": (bool,),
            "expected_revision": (int,),
            "max_reasoning_level": (AiGatewayNullableMaxReasoningLevel,),
            "model_ids": ([int],),
            "name": (str,),
            "provider_ids": ([int],),
            "routing_rule_slugs": ([str],),
        }

    attribute_map = {
        "allow_fast_mode": "allow_fast_mode",
        "expected_revision": "expected_revision",
        "max_reasoning_level": "max_reasoning_level",
        "model_ids": "model_ids",
        "name": "name",
        "provider_ids": "provider_ids",
        "routing_rule_slugs": "routing_rule_slugs",
    }

    def __init__(
        self_,
        allow_fast_mode: Union[bool, UnsetType] = unset,
        expected_revision: Union[int, UnsetType] = unset,
        max_reasoning_level: Union[AiGatewayNullableMaxReasoningLevel, none_type, UnsetType] = unset,
        model_ids: Union[List[int], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        provider_ids: Union[List[int], UnsetType] = unset,
        routing_rule_slugs: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to update an AI Gateway model group.

        :param allow_fast_mode: Whether fast mode is allowed for models and routing rules in the group.
        :type allow_fast_mode: bool, optional

        :param expected_revision: Required when updating the default model group. Must match its current revision; a stale revision returns HTTP 409. Omit for named policies.
        :type expected_revision: int, optional

        :param max_reasoning_level: Maximum reasoning level permitted by a model group.
        :type max_reasoning_level: AiGatewayNullableMaxReasoningLevel, none_type, optional

        :param model_ids: Individually selected model catalog IDs. Replaces this selection only. Omit to preserve it; an empty array clears it. Null is invalid. Individual selections do not include future models. New selections require provider View; retaining or removing saved hidden selections requires only parent Edit.
        :type model_ids: [int], optional

        :param name: Human-readable resource name.
        :type name: str, optional

        :param provider_ids: Explicit provider selections, including current and future models. Omit to preserve selections on update; an empty array clears them. Null is invalid. New selections require provider View; saved hidden IDs can be retained or removed.
        :type provider_ids: [int], optional

        :param routing_rule_slugs: Organization-unique routing rule slugs. Replaces route selections only. Omit to preserve them; an empty array clears them. Null is invalid.
        :type routing_rule_slugs: [str], optional
        """
        if allow_fast_mode is not unset:
            kwargs["allow_fast_mode"] = allow_fast_mode
        if expected_revision is not unset:
            kwargs["expected_revision"] = expected_revision
        if max_reasoning_level is not unset:
            kwargs["max_reasoning_level"] = max_reasoning_level
        if model_ids is not unset:
            kwargs["model_ids"] = model_ids
        if name is not unset:
            kwargs["name"] = name
        if provider_ids is not unset:
            kwargs["provider_ids"] = provider_ids
        if routing_rule_slugs is not unset:
            kwargs["routing_rule_slugs"] = routing_rule_slugs
        super().__init__(kwargs)
