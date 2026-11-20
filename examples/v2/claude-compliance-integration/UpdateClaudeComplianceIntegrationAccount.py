"""
Update a Claude Compliance integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.claude_compliance_integration_api import ClaudeComplianceIntegrationApi
from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_type import (
    ClaudeComplianceIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_bearer_token_auth_update import (
    ClaudeComplianceIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_update_attributes import (
    ClaudeComplianceIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_update_data import (
    ClaudeComplianceIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.claude_compliance_integration_account_update_request import (
    ClaudeComplianceIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = ClaudeComplianceIntegrationAccountUpdateRequest(
    data=ClaudeComplianceIntegrationAccountUpdateData(
        attributes=ClaudeComplianceIntegrationAccountUpdateAttributes(
            authentication=ClaudeComplianceIntegrationAccountBearerTokenAuthUpdate(
                auth_type=ClaudeComplianceIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            name="claude-compliance-acme",
        ),
        id="5f1a8d3c-7e2b-4f9a-b6c4-8d0e3a7f1b52",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_claude_compliance_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = ClaudeComplianceIntegrationApi(api_client)
    response = api_instance.update_claude_compliance_integration_account(account_id="account_id", body=body)

    print(response)
