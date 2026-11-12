# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_routing_rule_tier import AiGatewayRoutingRuleTier


class AiGatewayRoutingRuleAttributes(ModelNormal):
    validations = {
        "tiers": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_rule_tier import AiGatewayRoutingRuleTier

        return {
            "created_at": (datetime,),
            "route_id": (int,),
            "tiers": ([AiGatewayRoutingRuleTier],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "route_id": "route_id",
        "tiers": "tiers",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        route_id: int,
        tiers: List[AiGatewayRoutingRuleTier],
        updated_at: datetime,
        **kwargs,
    ):
        """
        Routing rule configuration and metadata.

        :param created_at: Time when the resource was created.
        :type created_at: datetime

        :param route_id: Stable numeric route identifier used by scoped policies and ``ai-gateway-route`` restriction policies.
        :type route_id: int

        :param tiers:
        :type tiers: [AiGatewayRoutingRuleTier]

        :param updated_at: Time when the resource was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.route_id = route_id
        self_.tiers = tiers
        self_.updated_at = updated_at
