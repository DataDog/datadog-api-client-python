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
    from datadog_api_client.v2.model.ai_gateway_routing_rule_create_data import AiGatewayRoutingRuleCreateData


class AiGatewayRoutingRuleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_routing_rule_create_data import AiGatewayRoutingRuleCreateData

        return {
            "data": (AiGatewayRoutingRuleCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayRoutingRuleCreateData, **kwargs):
        """
        Request to create an AI Gateway routing rule.

        :param data: Data used to create an AI Gateway routing rule.
        :type data: AiGatewayRoutingRuleCreateData
        """
        super().__init__(kwargs)

        self_.data = data
