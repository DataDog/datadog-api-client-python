"""
Add a model to an AI Gateway provider returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_type import AiGatewayModelCatalogEntryType
from datadog_api_client.v2.model.ai_gateway_model_create_attributes import AiGatewayModelCreateAttributes
from datadog_api_client.v2.model.ai_gateway_model_create_data import AiGatewayModelCreateData
from datadog_api_client.v2.model.ai_gateway_model_create_request import AiGatewayModelCreateRequest
from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation

body = AiGatewayModelCreateRequest(
    data=AiGatewayModelCreateData(
        attributes=AiGatewayModelCreateAttributes(
            model_id_canonical="gpt-5.2-codex",
            model_id_wire="gpt-5.2-codex-20260801",
            supported_operations=[
                AiGatewaySupportedOperation.OPENAI_CHAT_COMPLETIONS,
            ],
        ),
        type=AiGatewayModelCatalogEntryType.MODEL_CATALOG_ENTRIES,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_gateway_model"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.create_ai_gateway_model(provider_id=9223372036854775807, body=body)

    print(response)
