"""
Create an OpenAI Codex integration account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_codex_integration_api import OpenAICodexIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_ai_codex_dora_integration_dataflow_request import (
    OpenAICodexDoraIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_request import (
    OpenAICodexIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_type import (
    OpenAICodexIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_create_attributes import (
    OpenAICodexIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_create_data import (
    OpenAICodexIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_create_request import (
    OpenAICodexIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_request import (
    OpenAICodexIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_request import (
    OpenAICodexIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.open_ai_codex_turn_metrics_integration_dataflow_request import (
    OpenAICodexTurnMetricsIntegrationDataflowRequest,
)

body = OpenAICodexIntegrationAccountCreateRequest(
    data=OpenAICodexIntegrationAccountCreateData(
        attributes=OpenAICodexIntegrationAccountCreateAttributes(
            authentication=OpenAICodexIntegrationAccountBearerTokenAuthRequest(
                auth_type=OpenAICodexIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=OpenAICodexIntegrationDataflowsRequest(
                openai_codex_dora=OpenAICodexDoraIntegrationDataflowRequest(
                    enabled=True,
                ),
                openai_codex_turn_metrics=OpenAICodexTurnMetricsIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="openai-codex-acme",
            settings=OpenAICodexIntegrationAccountSettingsRequest(
                codex_workspace_id="your-workspace-id",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_open_ai_codex_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAICodexIntegrationApi(api_client)
    response = api_instance.create_open_ai_codex_integration_account(body=body)

    print(response)
