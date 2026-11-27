"""
Update an OpenAI Model Inference account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_model_inference_integration_api import OpenAIModelInferenceIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_bearer_token_auth_type import (
    OpenAIModelInferenceIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_bearer_token_auth_update import (
    OpenAIModelInferenceIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_settings_update import (
    OpenAIModelInferenceIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_update_attributes import (
    OpenAIModelInferenceIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_update_data import (
    OpenAIModelInferenceIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.open_ai_model_inference_integration_account_update_request import (
    OpenAIModelInferenceIntegrationAccountUpdateRequest,
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

body = OpenAIModelInferenceIntegrationAccountUpdateRequest(
    data=OpenAIModelInferenceIntegrationAccountUpdateData(
        attributes=OpenAIModelInferenceIntegrationAccountUpdateAttributes(
            authentication=OpenAIModelInferenceIntegrationAccountBearerTokenAuthUpdate(
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
            settings=OpenAIModelInferenceIntegrationAccountSettingsUpdate(
                custom_tags="team:ai,env:prod",
            ),
        ),
        id="3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_open_ai_model_inference_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAIModelInferenceIntegrationApi(api_client)
    response = api_instance.update_open_ai_model_inference_integration_account(account_id="account_id", body=body)

    print(response)
