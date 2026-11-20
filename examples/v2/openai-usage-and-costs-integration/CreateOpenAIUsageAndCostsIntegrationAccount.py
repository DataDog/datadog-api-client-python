"""
Create an OpenAI Usage and Costs account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_usageand_costs_integration_api import OpenAIUsageandCostsIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_ai_usage_and_costs_cloud_cost_data_integration_dataflow_request import (
    OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_request import (
    OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_type import (
    OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_create_attributes import (
    OpenAIUsageAndCostsIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_create_data import (
    OpenAIUsageAndCostsIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_create_request import (
    OpenAIUsageAndCostsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_request import (
    OpenAIUsageAndCostsIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_request import (
    OpenAIUsageAndCostsIntegrationDataflowsRequest,
)

body = OpenAIUsageAndCostsIntegrationAccountCreateRequest(
    data=OpenAIUsageAndCostsIntegrationAccountCreateData(
        attributes=OpenAIUsageAndCostsIntegrationAccountCreateAttributes(
            authentication=OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthRequest(
                auth_type=OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=OpenAIUsageAndCostsIntegrationDataflowsRequest(
                openai_cloud_cost_data=OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="openai-usage-and-costs-acme",
            settings=OpenAIUsageAndCostsIntegrationAccountSettingsRequest(
                custom_tags="team:ai,env:prod",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_open_ai_usage_and_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAIUsageandCostsIntegrationApi(api_client)
    response = api_instance.create_open_ai_usage_and_costs_integration_account(body=body)

    print(response)
