"""
Replace an AI Gateway routing rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_nullable_routing_rule_tier_ordering import (
    AiGatewayNullableRoutingRuleTierOrdering,
)
from datadog_api_client.v2.model.ai_gateway_routing_reasoning_level import AiGatewayRoutingReasoningLevel
from datadog_api_client.v2.model.ai_gateway_routing_rule_classifier_request import AiGatewayRoutingRuleClassifierRequest
from datadog_api_client.v2.model.ai_gateway_routing_rule_replace_attributes import AiGatewayRoutingRuleReplaceAttributes
from datadog_api_client.v2.model.ai_gateway_routing_rule_replace_data import AiGatewayRoutingRuleReplaceData
from datadog_api_client.v2.model.ai_gateway_routing_rule_replace_request import AiGatewayRoutingRuleReplaceRequest
from datadog_api_client.v2.model.ai_gateway_routing_rule_target_request import AiGatewayRoutingRuleTargetRequest
from datadog_api_client.v2.model.ai_gateway_routing_rule_target_type import AiGatewayRoutingRuleTargetType
from datadog_api_client.v2.model.ai_gateway_routing_rule_tier_request import AiGatewayRoutingRuleTierRequest
from datadog_api_client.v2.model.ai_gateway_routing_rule_type import AiGatewayRoutingRuleType

body = AiGatewayRoutingRuleReplaceRequest(
    data=AiGatewayRoutingRuleReplaceData(
        attributes=AiGatewayRoutingRuleReplaceAttributes(
            tiers=[
                AiGatewayRoutingRuleTierRequest(
                    classifier=AiGatewayRoutingRuleClassifierRequest(
                        confidence_threshold=0.6,
                        context="Requests come from the internal coding assistant.",
                        model="gpt-6-luna",
                        provider="prod-us",
                    ),
                    ordering=AiGatewayNullableRoutingRuleTierOrdering.CONFIGURED,
                    targets=[
                        AiGatewayRoutingRuleTargetRequest(
                            default=False,
                            id=901,
                            model="gpt-5.2-codex",
                            model_id=101,
                            provider="prod-us",
                            reasoning_level=AiGatewayRoutingReasoningLevel.MEDIUM,
                            rubric="Writing, reviewing, or debugging code.",
                            slug="coding-fallback",
                            type=AiGatewayRoutingRuleTargetType.MODEL,
                            weight=70,
                        ),
                    ],
                ),
            ],
        ),
        id="coding",
        type=AiGatewayRoutingRuleType.ROUTING_RULES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_routing_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_routing_rule(slug="slug", body=body)

    print(response)
