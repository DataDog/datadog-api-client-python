# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_routing_rule_replace_attributes import (
        AiGatewayRoutingRuleReplaceAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_routing_rule_type import AiGatewayRoutingRuleType


class AiGatewayRoutingRuleReplaceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_rule_replace_attributes import (
            AiGatewayRoutingRuleReplaceAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_routing_rule_type import AiGatewayRoutingRuleType

        return {
            "attributes": (AiGatewayRoutingRuleReplaceAttributes,),
            "id": (str,),
            "type": (AiGatewayRoutingRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayRoutingRuleReplaceAttributes, id: str, type: AiGatewayRoutingRuleType, **kwargs
    ):
        """
        Data used to replace an AI Gateway routing rule.

        :param attributes: Partial route update. Omit tiers to preserve the entire graph, including hidden selections. Saved target IDs retain omitted settings. Replacing tiers must explicitly retain or remove every hidden occurrence.
        :type attributes: AiGatewayRoutingRuleReplaceAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: AI Gateway routing rule resource type.
        :type type: AiGatewayRoutingRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
