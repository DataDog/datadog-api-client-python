"""
Update a model for an AI Gateway provider returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_type import AiGatewayModelCatalogEntryType
from datadog_api_client.v2.model.ai_gateway_model_update_attributes import AiGatewayModelUpdateAttributes
from datadog_api_client.v2.model.ai_gateway_model_update_data import AiGatewayModelUpdateData
from datadog_api_client.v2.model.ai_gateway_model_update_request import AiGatewayModelUpdateRequest
from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation

body = AiGatewayModelUpdateRequest(
    data=AiGatewayModelUpdateData(
        attributes=AiGatewayModelUpdateAttributes(
            model_id_wire="gpt-5.2-codex-20260801",
            supported_operations=[
                AiGatewaySupportedOperation.OPENAI_CHAT_COMPLETIONS,
            ],
        ),
        id="101",
        type=AiGatewayModelCatalogEntryType.MODEL_CATALOG_ENTRIES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_model"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_model(provider_id=9223372036854775807, canonical="canonical", body=body)

    print(response)
