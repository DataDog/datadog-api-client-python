"""
Create an AI Gateway provider returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_custom_provider_supported_operation import (
    AiGatewayCustomProviderSupportedOperation,
)
from datadog_api_client.v2.model.ai_gateway_known_provider import AiGatewayKnownProvider
from datadog_api_client.v2.model.ai_gateway_model_input import AiGatewayModelInput
from datadog_api_client.v2.model.ai_gateway_provider_create_attributes import AiGatewayProviderCreateAttributes
from datadog_api_client.v2.model.ai_gateway_provider_create_data import AiGatewayProviderCreateData
from datadog_api_client.v2.model.ai_gateway_provider_create_request import AiGatewayProviderCreateRequest
from datadog_api_client.v2.model.ai_gateway_provider_initial_binding import AiGatewayProviderInitialBinding
from datadog_api_client.v2.model.ai_gateway_provider_initial_binding_relation import (
    AiGatewayProviderInitialBindingRelation,
)
from datadog_api_client.v2.model.ai_gateway_provider_integration_config import AiGatewayProviderIntegrationConfig
from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType
from datadog_api_client.v2.model.ai_gateway_supported_operation import AiGatewaySupportedOperation

body = AiGatewayProviderCreateRequest(
    data=AiGatewayProviderCreateData(
        attributes=AiGatewayProviderCreateAttributes(
            cost_multiplier=1.0,
            initial_bindings=[
                AiGatewayProviderInitialBinding(
                    principals=[
                        "org:11111111-1111-1111-1111-111111111111",
                    ],
                    relation=AiGatewayProviderInitialBindingRelation.VIEWER,
                ),
            ],
            integration_account_id="account-123",
            integration_config=AiGatewayProviderIntegrationConfig(
                bedrock_region="us-east-1",
                foundry_project="my-project",
                foundry_resource_id="/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/ai/providers/Microsoft.CognitiveServices/accounts/my-foundry",
                location="us-central1",
                project_id="my-gcp-project",
                supported_operations=[
                    AiGatewayCustomProviderSupportedOperation.OPENAI_CHAT_COMPLETIONS,
                ],
            ),
            known_provider=AiGatewayKnownProvider.OPENAI,
            models=[
                AiGatewayModelInput(
                    model_id_canonical="gpt-5.2-codex",
                    model_id_wire="gpt-5.2-codex-20260801",
                    supported_operations=[
                        AiGatewaySupportedOperation.OPENAI_CHAT_COMPLETIONS,
                    ],
                ),
            ],
            name="production-us",
            slug="prod-us",
        ),
        type=AiGatewayProviderType.PROVIDERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_ai_gateway_provider"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.create_ai_gateway_provider(body=body)

    print(response)
