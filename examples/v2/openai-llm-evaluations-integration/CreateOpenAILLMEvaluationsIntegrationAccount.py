"""
Create an OpenAI LLM Evaluations account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_aillm_evaluations_integration_api import OpenAILLMEvaluationsIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_request import (
    OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_bearer_token_auth_type import (
    OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_create_attributes import (
    OpenAILLMEvaluationsIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_create_data import (
    OpenAILLMEvaluationsIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_create_request import (
    OpenAILLMEvaluationsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.open_aillm_evaluations_integration_account_settings_request import (
    OpenAILLMEvaluationsIntegrationAccountSettingsRequest,
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

body = OpenAILLMEvaluationsIntegrationAccountCreateRequest(
    data=OpenAILLMEvaluationsIntegrationAccountCreateData(
        attributes=OpenAILLMEvaluationsIntegrationAccountCreateAttributes(
            authentication=OpenAILLMEvaluationsIntegrationAccountBearerTokenAuthRequest(
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
            settings=OpenAILLMEvaluationsIntegrationAccountSettingsRequest(
                custom_tags="team:ai,env:prod",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_open_aillm_evaluations_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAILLMEvaluationsIntegrationApi(api_client)
    response = api_instance.create_open_aillm_evaluations_integration_account(body=body)

    print(response)
