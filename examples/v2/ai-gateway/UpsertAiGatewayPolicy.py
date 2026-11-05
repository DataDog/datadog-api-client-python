"""
Create or replace an AI Gateway routing policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_policy_request import AiGatewayPolicyRequest
from datadog_api_client.v2.model.ai_gateway_policy_request_attributes import AiGatewayPolicyRequestAttributes
from datadog_api_client.v2.model.ai_gateway_policy_request_data import AiGatewayPolicyRequestData
from datadog_api_client.v2.model.ai_gateway_policy_target_request import AiGatewayPolicyTargetRequest
from datadog_api_client.v2.model.ai_gateway_policy_tier_request import AiGatewayPolicyTierRequest
from datadog_api_client.v2.model.ai_gateway_policy_type import AiGatewayPolicyType

body = AiGatewayPolicyRequest(
    data=AiGatewayPolicyRequestData(
        attributes=AiGatewayPolicyRequestAttributes(
            inbound="coding-agent",
            priority=1,
            tiers=[
                AiGatewayPolicyTierRequest(
                    priority=1,
                    targets=[
                        AiGatewayPolicyTargetRequest(
                            id=901,
                            model="gpt-5.2-codex",
                            provider="prod-us",
                        ),
                    ],
                ),
            ],
        ),
        type=AiGatewayPolicyType.ROUTING_DOCUMENTS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["upsert_ai_gateway_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.upsert_ai_gateway_policy(body=body)

    print(response)
