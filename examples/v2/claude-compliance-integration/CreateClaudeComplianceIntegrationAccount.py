"""
Create a Claude Compliance integration account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.claude_compliance_integration_api import ClaudeComplianceIntegrationApi
from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_request import (
    ClaudeComplianceIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_type import (
    ClaudeComplianceIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_create_attributes import (
    ClaudeComplianceIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_create_data import (
    ClaudeComplianceIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_create_request import (
    ClaudeComplianceIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ClaudeComplianceIntegrationAccountCreateRequest(
    data=ClaudeComplianceIntegrationAccountCreateData(
        attributes=ClaudeComplianceIntegrationAccountCreateAttributes(
            authentication=ClaudeComplianceIntegrationAccountBearerTokenAuthRequest(
                auth_type=ClaudeComplianceIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            name="claude-compliance-acme",
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_claude_compliance_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ClaudeComplianceIntegrationApi(api_client)
    response = api_instance.create_claude_compliance_integration_account(body=body)

    print(response)
