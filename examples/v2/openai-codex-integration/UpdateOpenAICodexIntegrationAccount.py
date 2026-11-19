"""
Update an OpenAI Codex integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.open_ai_codex_integration_api import OpenAICodexIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.open_ai_codex_dora_integration_dataflow_request import (
    OpenAICodexDoraIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_type import (
    OpenAICodexIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_bearer_token_auth_update import (
    OpenAICodexIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_settings_update import (
    OpenAICodexIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_update_attributes import (
    OpenAICodexIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_update_data import (
    OpenAICodexIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.open_ai_codex_integration_account_update_request import (
    OpenAICodexIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.open_ai_codex_integration_dataflows_request import (
    OpenAICodexIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.open_ai_codex_turn_metrics_integration_dataflow_request import (
    OpenAICodexTurnMetricsIntegrationDataflowRequest,
)

body = OpenAICodexIntegrationAccountUpdateRequest(
    data=OpenAICodexIntegrationAccountUpdateData(
        attributes=OpenAICodexIntegrationAccountUpdateAttributes(
            authentication=OpenAICodexIntegrationAccountBearerTokenAuthUpdate(
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
            settings=OpenAICodexIntegrationAccountSettingsUpdate(
                codex_workspace_id="your-workspace-id",
            ),
        ),
        id="7d2f9c4e-3a1b-4c8e-9f6d-2b5a8e1c0d47",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_open_ai_codex_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = OpenAICodexIntegrationApi(api_client)
    response = api_instance.update_open_ai_codex_integration_account(account_id="account_id", body=body)

    print(response)
