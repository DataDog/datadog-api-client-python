"""
Create a ChatGPT Enterprise integration account returns "Created" response
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
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_request import (
    ChatGPTEnterpriseIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_bearer_token_auth_type import (
    ChatGPTEnterpriseIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_create_attributes import (
    ChatGPTEnterpriseIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_create_data import (
    ChatGPTEnterpriseIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_create_request import (
    ChatGPTEnterpriseIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_account_settings_request import (
    ChatGPTEnterpriseIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.chat_gpt_enterprise_integration_dataflows_request import (
    ChatGPTEnterpriseIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ChatGPTEnterpriseIntegrationAccountCreateRequest(
    data=ChatGPTEnterpriseIntegrationAccountCreateData(
        attributes=ChatGPTEnterpriseIntegrationAccountCreateAttributes(
            authentication=ChatGPTEnterpriseIntegrationAccountBearerTokenAuthRequest(
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
            settings=ChatGPTEnterpriseIntegrationAccountSettingsRequest(
                openai_org_id="org-AbC123dEf456",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_chat_gpt_enterprise_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChatGPTEnterpriseIntegrationApi(api_client)
    response = api_instance.create_chat_gpt_enterprise_integration_account(body=body)

    print(response)
