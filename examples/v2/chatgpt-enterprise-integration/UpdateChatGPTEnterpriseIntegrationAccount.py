"""
Update a ChatGPT Enterprise integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.chat_gpt_enterprise_integration_api import ChatGPTEnterpriseIntegrationApi
from datadog_api_client.v2.model.chat_gpt_enterprise_agent_console_integration_dataflow_request import (
    ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_cloud_cost_data_integration_dataflow_request import (
    ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_type import (
    ChatGPTEnterpriseIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_update import (
    ChatGPTEnterpriseIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_update import (
    ChatGPTEnterpriseIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_update_attributes import (
    ChatGPTEnterpriseIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_update_data import (
    ChatGPTEnterpriseIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_update_request import (
    ChatGPTEnterpriseIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_request import (
    ChatGPTEnterpriseIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ChatGPTEnterpriseIntegrationAccountUpdateRequest(
    data=ChatGPTEnterpriseIntegrationAccountUpdateData(
        attributes=ChatGPTEnterpriseIntegrationAccountUpdateAttributes(
            authentication=ChatGPTEnterpriseIntegrationAccountBearerTokenAuthUpdate(
                auth_type=ChatGPTEnterpriseIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            dataflows=ChatGPTEnterpriseIntegrationDataflowsRequest(
                chatgpt_enterprise_agent_console=ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest(
                    enabled=True,
                ),
                chatgpt_enterprise_cloud_cost_data=ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="chatgpt-enterprise-acme",
            settings=ChatGPTEnterpriseIntegrationAccountSettingsUpdate(
                openai_org_id="org-AbC123dEf456",
            ),
        ),
        id="3e8a1f6b-9c2d-4b7e-8a5f-6d1c4e9b2a03",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_chat_gpt_enterprise_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChatGPTEnterpriseIntegrationApi(api_client)
    response = api_instance.update_chat_gpt_enterprise_integration_account(account_id="account_id", body=body)

    print(response)
