"""
Update an OpenAI Usage and Costs account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_usageand_costs_integration_api import OpenAIUsageandCostsIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_ai_usage_and_costs_cloud_cost_data_integration_dataflow_request import (
    OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_type import (
    OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_bearer_token_auth_update import (
    OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_settings_update import (
    OpenAIUsageAndCostsIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_update_attributes import (
    OpenAIUsageAndCostsIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_update_data import (
    OpenAIUsageAndCostsIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_account_update_request import (
    OpenAIUsageAndCostsIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.open_ai_usage_and_costs_integration_dataflows_request import (
    OpenAIUsageAndCostsIntegrationDataflowsRequest,
)

body = OpenAIUsageAndCostsIntegrationAccountUpdateRequest(
    data=OpenAIUsageAndCostsIntegrationAccountUpdateData(
        attributes=OpenAIUsageAndCostsIntegrationAccountUpdateAttributes(
            authentication=OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthUpdate(
                auth_type=OpenAIUsageAndCostsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=OpenAIUsageAndCostsIntegrationDataflowsRequest(
                openai_cloud_cost_data=OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="openai-usage-and-costs-acme",
            settings=OpenAIUsageAndCostsIntegrationAccountSettingsUpdate(
                custom_tags="team:ai,env:prod",
            ),
        ),
        id="9c4e7a2b-1d5f-4e8a-b3c6-0f2d8a6e4b17",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_open_ai_usage_and_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAIUsageandCostsIntegrationApi(api_client)
    response = api_instance.update_open_ai_usage_and_costs_integration_account(account_id="account_id", body=body)

    print(response)
