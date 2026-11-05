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
    from datadog_api_client.v2.model.ai_gateway_routing_rule_create_attributes import (
        AiGatewayRoutingRuleCreateAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_routing_rule_type import AiGatewayRoutingRuleType


class AiGatewayRoutingRuleCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_rule_create_attributes import (
            AiGatewayRoutingRuleCreateAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_routing_rule_type import AiGatewayRoutingRuleType

        return {
            "attributes": (AiGatewayRoutingRuleCreateAttributes,),
            "type": (AiGatewayRoutingRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayRoutingRuleCreateAttributes, type: AiGatewayRoutingRuleType, **kwargs):
        """
        Data used to create an AI Gateway routing rule.

        :param attributes: Attributes used to create an AI Gateway routing rule.
        :type attributes: AiGatewayRoutingRuleCreateAttributes

        :param type: AI Gateway routing rule resource type.
        :type type: AiGatewayRoutingRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
