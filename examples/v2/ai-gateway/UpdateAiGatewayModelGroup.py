"""
Update an AI Gateway model group returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_model_group_type import AiGatewayModelGroupType
from datadog_api_client.v2.model.ai_gateway_model_group_update_attributes import AiGatewayModelGroupUpdateAttributes
from datadog_api_client.v2.model.ai_gateway_model_group_update_data import AiGatewayModelGroupUpdateData
from datadog_api_client.v2.model.ai_gateway_model_group_update_request import AiGatewayModelGroupUpdateRequest
from datadog_api_client.v2.model.ai_gateway_nullable_max_reasoning_level import AiGatewayNullableMaxReasoningLevel

body = AiGatewayModelGroupUpdateRequest(
    data=AiGatewayModelGroupUpdateData(
        attributes=AiGatewayModelGroupUpdateAttributes(
            allow_fast_mode=True,
            max_reasoning_level=AiGatewayNullableMaxReasoningLevel.HIGH,
            model_ids=[
                101,
            ],
            name="Coding models",
            provider_ids=[],
            routing_rule_slugs=[
                "coding-route",
            ],
        ),
        id="7",
        type=AiGatewayModelGroupType.MODEL_GROUPS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_model_group"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_model_group(id="id", body=body)

    print(response)
