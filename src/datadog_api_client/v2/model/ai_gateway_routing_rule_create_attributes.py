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
    from datadog_api_client.v2.model.ai_gateway_provider_initial_binding import AiGatewayProviderInitialBinding
    from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_request import AiGatewayRoutingRuleTierRequest


class AiGatewayRoutingRuleCreateAttributes(ModelNormal):
    validations = {
        "slug": {
            "max_length": 128,
            "min_length": 1,
        },
        "tiers": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_initial_binding import AiGatewayProviderInitialBinding
        from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_request import AiGatewayRoutingRuleTierRequest

        return {
            "initial_bindings": ([AiGatewayProviderInitialBinding],),
            "slug": (str,),
            "tiers": ([AiGatewayRoutingRuleTierRequest],),
        }

    attribute_map = {
        "initial_bindings": "initial_bindings",
        "slug": "slug",
        "tiers": "tiers",
    }

    def __init__(
        self_,
        slug: str,
        tiers: List[AiGatewayRoutingRuleTierRequest],
        initial_bindings: Union[List[AiGatewayProviderInitialBinding], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes used to create an AI Gateway routing rule.

        :param initial_bindings: Reserved for initial View and Edit permissions. Supplying this attribute returns HTTP 400 and doesn't
            create the route. Create the route, then set its permissions through the restriction policy API.
        :type initial_bindings: [AiGatewayProviderInitialBinding], optional

        :param slug: Organization-unique resource slug.
        :type slug: str

        :param tiers:
        :type tiers: [AiGatewayRoutingRuleTierRequest]
        """
        if initial_bindings is not unset:
            kwargs["initial_bindings"] = initial_bindings
        super().__init__(kwargs)

        self_.slug = slug
        self_.tiers = tiers
