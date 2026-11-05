# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_nullable_max_reasoning_level import AiGatewayNullableMaxReasoningLevel
    from datadog_api_client.v2.model.ai_gateway_model_group_model import AiGatewayModelGroupModel
    from datadog_api_client.v2.model.ai_gateway_model_group_provider import AiGatewayModelGroupProvider
    from datadog_api_client.v2.model.ai_gateway_model_group_routing_rule import AiGatewayModelGroupRoutingRule


class AiGatewayModelGroupAttributes(ModelNormal):
    validations = {
        "revision": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_nullable_max_reasoning_level import (
            AiGatewayNullableMaxReasoningLevel,
        )
        from datadog_api_client.v2.model.ai_gateway_model_group_model import AiGatewayModelGroupModel
        from datadog_api_client.v2.model.ai_gateway_model_group_provider import AiGatewayModelGroupProvider
        from datadog_api_client.v2.model.ai_gateway_model_group_routing_rule import AiGatewayModelGroupRoutingRule

        return {
            "allow_fast_mode": (bool,),
            "created_at": (datetime,),
            "max_reasoning_level": (AiGatewayNullableMaxReasoningLevel,),
            "model_ids": ([int],),
            "models": ([AiGatewayModelGroupModel],),
            "name": (str,),
            "provider_ids": ([int],),
            "providers": ([AiGatewayModelGroupProvider],),
            "revision": (int,),
            "routing_rules": ([AiGatewayModelGroupRoutingRule],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "allow_fast_mode": "allow_fast_mode",
        "created_at": "created_at",
        "max_reasoning_level": "max_reasoning_level",
        "model_ids": "model_ids",
        "models": "models",
        "name": "name",
        "provider_ids": "provider_ids",
        "providers": "providers",
        "revision": "revision",
        "routing_rules": "routing_rules",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        allow_fast_mode: bool,
        created_at: datetime,
        max_reasoning_level: Union[AiGatewayNullableMaxReasoningLevel, none_type],
        model_ids: List[int],
        models: List[AiGatewayModelGroupModel],
        name: str,
        provider_ids: List[int],
        providers: List[AiGatewayModelGroupProvider],
        routing_rules: List[AiGatewayModelGroupRoutingRule],
        updated_at: datetime,
        revision: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Complete AI Gateway model group configuration.

        :param allow_fast_mode: Whether fast mode is allowed for models and routing rules in the group.
        :type allow_fast_mode: bool

        :param created_at: Time when the resource was created.
        :type created_at: datetime

        :param max_reasoning_level: Maximum reasoning level permitted by a model group.
        :type max_reasoning_level: AiGatewayNullableMaxReasoningLevel, none_type

        :param model_ids: All saved model catalog IDs, including selections whose provider metadata is hidden. Preserve these IDs independently of the visible catalog.
        :type model_ids: [int]

        :param models: Metadata for saved model selections whose providers the caller can view. Missing metadata does not remove a saved ID.
        :type models: [AiGatewayModelGroupModel]

        :param name: Human-readable resource name.
        :type name: str

        :param provider_ids: All explicitly selected provider IDs, including hidden providers. Embedded provider metadata includes only viewable providers.
        :type provider_ids: [int]

        :param providers: Viewable explicitly selected providers, separate from individually selected models. Use provider_ids to retain all selections.
        :type providers: [AiGatewayModelGroupProvider]

        :param revision: Revision of the organization-wide policy. Present for the default model group and absent for named policies.
        :type revision: int, optional

        :param routing_rules:
        :type routing_rules: [AiGatewayModelGroupRoutingRule]

        :param updated_at: Time when the resource was last updated.
        :type updated_at: datetime
        """
        if revision is not unset:
            kwargs["revision"] = revision
        super().__init__(kwargs)

        self_.allow_fast_mode = allow_fast_mode
        self_.created_at = created_at
        self_.max_reasoning_level = max_reasoning_level
        self_.model_ids = model_ids
        self_.models = models
        self_.name = name
        self_.provider_ids = provider_ids
        self_.providers = providers
        self_.routing_rules = routing_rules
        self_.updated_at = updated_at
