"""
Update an Anthropic Usage and Costs account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.anthropic_usage_and_costs_integration_api import AnthropicUsageAndCostsIntegrationApi
from datadog_api_client.v2.model.anthropic_usage_and_costs_cloud_cost_metrics_integration_dataflow_request import (
    AnthropicUsageAndCostsCloudCostMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_bearer_token_auth_type import (
    AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_bearer_token_auth_update import (
    AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_update_attributes import (
    AnthropicUsageAndCostsIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_update_data import (
    AnthropicUsageAndCostsIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_account_update_request import (
    AnthropicUsageAndCostsIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.anthropic_usage_and_costs_integration_dataflows_request import (
    AnthropicUsageAndCostsIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = AnthropicUsageAndCostsIntegrationAccountUpdateRequest(
    data=AnthropicUsageAndCostsIntegrationAccountUpdateData(
        attributes=AnthropicUsageAndCostsIntegrationAccountUpdateAttributes(
            authentication=AnthropicUsageAndCostsIntegrationAccountBearerTokenAuthUpdate(
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
        id="9b4c7e2a-1d6f-4a3b-8e5c-0f2d7a9b6c18",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_anthropic_usage_and_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = AnthropicUsageAndCostsIntegrationApi(api_client)
    response = api_instance.update_anthropic_usage_and_costs_integration_account(account_id="account_id", body=body)

    print(response)
