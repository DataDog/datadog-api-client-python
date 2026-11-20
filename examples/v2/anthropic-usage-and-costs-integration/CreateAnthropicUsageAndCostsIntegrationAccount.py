"""
Create an Anthropic Usage and Costs account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.anthropic_usage_and_costs_integration_api import AnthropicUsageAndCostsIntegrationApi
from datadog_api_client.v2.model.anthropic_usage_and_costs_cloud_cost_metrics_integration_dataflow_request import (
    AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_bearer_token_auth_request import (
    AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_bearer_token_auth_type import (
    AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_create_attributes import (
    AnthropicUsageAndCostsIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_create_data import (
    AnthropicUsageAndCostsIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_create_request import (
    AnthropicUsageAndCostsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_dataflows_request import (
    AnthropicUsageAndCostsIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = AnthropicUsageAndCostsIntegrationAccountCreateRequest(
    data=AnthropicUsageAndCostsIntegrationAccountCreateData(
        attributes=AnthropicUsageAndCostsIntegrationAccountCreateAttributes(
            authentication=AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthRequest(
                auth_type=AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=AnthropicUsageAndCostsIntegrationDataflowsRequest(
                anthropic_cloud_cost_metrics=AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="anthropic-acme",
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_anthropic_usage_and_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnthropicUsageAndCostsIntegrationApi(api_client)
    response = api_instance.create_anthropic_usage_and_costs_integration_account(body=body)

    print(response)
