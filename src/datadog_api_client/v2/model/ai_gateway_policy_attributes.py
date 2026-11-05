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
    from datadog_api_client.v2.model.ai_gateway_policy_tier import AiGatewayPolicyTier


class AiGatewayPolicyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_policy_tier import AiGatewayPolicyTier

        return {
            "priority": (int,),
            "tiers": ([AiGatewayPolicyTier],),
        }

    attribute_map = {
        "priority": "priority",
        "tiers": "tiers",
    }

    def __init__(self_, priority: int, tiers: List[AiGatewayPolicyTier], **kwargs):
        """
        Routing policy configuration.

        :param priority: Routing priority.
        :type priority: int

        :param tiers:
        :type tiers: [AiGatewayPolicyTier]
        """
        super().__init__(kwargs)

        self_.priority = priority
        self_.tiers = tiers
