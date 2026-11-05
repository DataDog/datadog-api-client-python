# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
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
        from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_request import AiGatewayRoutingRuleTierRequest

        return {
            "slug": (str,),
            "tiers": ([AiGatewayRoutingRuleTierRequest],),
        }

    attribute_map = {
        "slug": "slug",
        "tiers": "tiers",
    }

    def __init__(self_, slug: str, tiers: List[AiGatewayRoutingRuleTierRequest], **kwargs):
        """
        Attributes used to create an AI Gateway routing rule.

        :param slug: Organization-unique resource slug.
        :type slug: str

        :param tiers:
        :type tiers: [AiGatewayRoutingRuleTierRequest]
        """
        super().__init__(kwargs)

        self_.slug = slug
        self_.tiers = tiers
