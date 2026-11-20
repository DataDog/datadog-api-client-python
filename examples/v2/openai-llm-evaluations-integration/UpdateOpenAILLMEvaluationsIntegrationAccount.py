"""
Update an OpenAI LLM Evaluations account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_aillm_evaluations_integration_api import OpenAILLMEvaluationsIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_type import (
    OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_update import (
    OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_settings_update import (
    OpenAILLMEvaluationsIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_update_attributes import (
    OpenAILLMEvaluationsIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_update_data import (
    OpenAILLMEvaluationsIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_update_request import (
    OpenAILLMEvaluationsIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_dataflows_request import (
    OpenAILLMEvaluationsIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.open_aillm_evaluations_llm_completions_integration_dataflow_request import (
    OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.open_aillm_evaluations_project_cloud_cost_data_integration_dataflow_request import (
    OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest,
)

body = OpenAILLMEvaluationsIntegrationAccountUpdateRequest(
    data=OpenAILLMEvaluationsIntegrationAccountUpdateData(
        attributes=OpenAILLMEvaluationsIntegrationAccountUpdateAttributes(
            authentication=OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthUpdate(
                auth_type=OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=OpenAILLMEvaluationsIntegrationDataflowsRequest(
                openai_llm_completions=OpenAILLMEvaluationsLLMCompletionsIntegrationDataflowRequest(
                    enabled=True,
                ),
                openai_project_cloud_cost_data=OpenAILLMEvaluationsProjectCloudCostDataIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="openai-llm-evaluations-acme",
            settings=OpenAILLMEvaluationsIntegrationAccountSettingsUpdate(
                custom_tags="team:ai,env:prod",
            ),
        ),
        id="3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_open_aillm_evaluations_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAILLMEvaluationsIntegrationApi(api_client)
    response = api_instance.update_open_aillm_evaluations_integration_account(account_id="account_id", body=body)

    print(response)
