"""
Update a GitHub Costs integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.git_hub_costs_integration_api import GitHubCostsIntegrationApi
from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_type import (
    GitHubCostsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_bearer_token_auth_update import (
    GitHubCostsIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_settings_update import (
    GitHubCostsIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_update_attributes import (
    GitHubCostsIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_update_data import (
    GitHubCostsIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.git_hub_costs_integration_account_update_request import (
    GitHubCostsIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = GitHubCostsIntegrationAccountUpdateRequest(
    data=GitHubCostsIntegrationAccountUpdateData(
        attributes=GitHubCostsIntegrationAccountUpdateAttributes(
            authentication=GitHubCostsIntegrationAccountBearerTokenAuthUpdate(
                auth_type=GitHubCostsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            name="github-costs-acme",
            settings=GitHubCostsIntegrationAccountSettingsUpdate(
                enterprise_name="acme",
                tags="env:prod,team:finops",
            ),
        ),
        id="4b7c2e1a-6f3d-4e8b-9a52-1d0c8f7e3b64",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_git_hub_costs_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = GitHubCostsIntegrationApi(api_client)
    response = api_instance.update_git_hub_costs_integration_account(account_id="account_id", body=body)

    print(response)
