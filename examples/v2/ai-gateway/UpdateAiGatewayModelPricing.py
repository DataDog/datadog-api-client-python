"""
Set a model pricing override returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_gateway_api import AIGatewayApi
from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_config import (
    AiGatewayModelPricingCustomRequestConfig,
)
from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_source import (
    AiGatewayModelPricingCustomRequestSource,
)
from datadog_api_client.v2.model.ai_gateway_model_pricing_custom_request_source_type import (
    AiGatewayModelPricingCustomRequestSourceType,
)
from datadog_api_client.v2.model.ai_gateway_model_pricing_request import AiGatewayModelPricingRequest
from datadog_api_client.v2.model.ai_gateway_model_pricing_request_attributes import (
    AiGatewayModelPricingRequestAttributes,
)
from datadog_api_client.v2.model.ai_gateway_model_pricing_request_data import AiGatewayModelPricingRequestData
from datadog_api_client.v2.model.ai_gateway_model_pricing_required_rates import AiGatewayModelPricingRequiredRates
from datadog_api_client.v2.model.ai_gateway_model_pricing_type import AiGatewayModelPricingType

body = AiGatewayModelPricingRequest(
    data=AiGatewayModelPricingRequestData(
        attributes=AiGatewayModelPricingRequestAttributes(
            pricing_config=AiGatewayModelPricingCustomRequestConfig(
                rates=AiGatewayModelPricingRequiredRates(
                    cache_read_cost_per_mtok=0.0,
                    cache_write_cost_per_mtok=0.0,
                    non_cached_input_cost_per_mtok=0.0,
                    output_cost_per_mtok=0.0,
                ),
                source=AiGatewayModelPricingCustomRequestSource(
                    type=AiGatewayModelPricingCustomRequestSourceType.CUSTOM,
                ),
                version=1,
            ),
        ),
        id="gpt-4o",
        type=AiGatewayModelPricingType.MODEL_PRICING,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_ai_gateway_model_pricing"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGatewayApi(api_client)
    response = api_instance.update_ai_gateway_model_pricing(
        provider_id=9223372036854775807, canonical="canonical", body=body
    )

    print(response)
