"""
Create a GitHub Costs integration account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.git_hub_costs_integration_api import GitHubCostsIntegrationApi
from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_request import (
    GitHubCostsIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_type import (
    GitHubCostsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_create_attributes import (
    GitHubCostsIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_create_data import (
    GitHubCostsIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_create_request import (
    GitHubCostsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_request import (
    GitHubCostsIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = GitHubCostsIntegrationAccountCreateRequest(
    data=GitHubCostsIntegrationAccountCreateData(
        attributes=GitHubCostsIntegrationAccountCreateAttributes(
            authentication=GitHubCostsIntegrationAccountBearerTokenAuthRequest(
                auth_type=GitHubCostsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            name="github-costs-acme",
            settings=GitHubCostsIntegrationAccountSettingsRequest(
                enterprise_name="acme",
                tags="env:prod,team:finops",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_git_hub_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = GitHubCostsIntegrationApi(api_client)
    response = api_instance.create_git_hub_costs_integration_account(body=body)

    print(response)
