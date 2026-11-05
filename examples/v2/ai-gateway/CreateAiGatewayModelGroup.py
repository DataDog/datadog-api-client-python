"""
Create an AI Gateway model group returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_max_reasoning_level import AiGatewayMaxReasoningLevel
from datadog_api_client.v2.model.ai_gateway_model_group_binding import AiGatewayModelGroupBinding
from datadog_api_client.v2.model.ai_gateway_model_group_binding_relation import AiGatewayModelGroupBindingRelation
from datadog_api_client.v2.model.ai_gateway_model_group_create_attributes import AiGatewayModelGroupCreateAttributes
from datadog_api_client.v2.model.ai_gateway_model_group_create_data import AiGatewayModelGroupCreateData
from datadog_api_client.v2.model.ai_gateway_model_group_create_request import AiGatewayModelGroupCreateRequest
from datadog_api_client.v2.model.ai_gateway_model_group_type import AiGatewayModelGroupType

body = AiGatewayModelGroupCreateRequest(
    data=AiGatewayModelGroupCreateData(
        attributes=AiGatewayModelGroupCreateAttributes(
            allow_fast_mode=True,
            bindings=[
                AiGatewayModelGroupBinding(
                    principals=[
                        "user:55555555-5555-5555-5555-555555555555",
                    ],
                    relation=AiGatewayModelGroupBindingRelation.RUNNER,
                ),
            ],
            max_reasoning_level=AiGatewayMaxReasoningLevel.HIGH,
            model_ids=[
                101,
            ],
            name="Coding models",
            provider_ids=[],
            routing_rule_slugs=[
                "coding-route",
            ],
        ),
        type=AiGatewayModelGroupType.MODEL_GROUPS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_gateway_model_group"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.create_ai_gateway_model_group(body=body)

    print(response)
