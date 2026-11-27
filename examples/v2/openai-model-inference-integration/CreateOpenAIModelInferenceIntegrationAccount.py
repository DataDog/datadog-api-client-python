"""
Create an OpenAI Model Inference account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_model_inference_integration_api import OpenAIModelInferenceIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_bearer_token_auth_request import (
    OpenAIModelInferenceIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_bearer_token_auth_type import (
    OpenAIModelInferenceIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_create_attributes import (
    OpenAIModelInferenceIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_create_data import (
    OpenAIModelInferenceIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_create_request import (
    OpenAIModelInferenceIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_settings_request import (
    OpenAIModelInferenceIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_dataflows_request import (
    OpenAIModelInferenceIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.open_ai_model_inference_llm_completions_integration_dataflow_request import (
    OpenAIModelInferenceLLMCompletionsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.open_ai_model_inference_project_cloud_cost_data_integration_dataflow_request import (
    OpenAIModelInferenceProjectCloudCostDataIntegrationDataflowRequest,
)

body = OpenAIModelInferenceIntegrationAccountCreateRequest(
    data=OpenAIModelInferenceIntegrationAccountCreateData(
        attributes=OpenAIModelInferenceIntegrationAccountCreateAttributes(
            authentication=OpenAIModelInferenceIntegrationAccountBearerTokenAuthRequest(
                auth_type=OpenAIModelInferenceIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=OpenAIModelInferenceIntegrationDataflowsRequest(
                openai_llm_completions=OpenAIModelInferenceLLMCompletionsIntegrationDataflowRequest(
                    enabled=True,
                ),
                openai_project_cloud_cost_data=OpenAIModelInferenceProjectCloudCostDataIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="openai-model-inference-acme",
            settings=OpenAIModelInferenceIntegrationAccountSettingsRequest(
                custom_tags="team:ai,env:prod",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_open_ai_model_inference_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAIModelInferenceIntegrationApi(api_client)
    response = api_instance.create_open_ai_model_inference_integration_account(body=body)

    print(response)
