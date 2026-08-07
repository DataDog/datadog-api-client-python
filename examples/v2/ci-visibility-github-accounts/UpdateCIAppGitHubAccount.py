"""
Update GitHub CI Visibility status returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_git_hub_accounts_api import CIVisibilityGitHubAccountsApi
from datadog_api_client.v2.model.ci_app_git_hub_account_type import CIAppGitHubAccountType
from datadog_api_client.v2.model.ci_app_git_hub_account_update_request import CIAppGitHubAccountUpdateRequest
from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_attributes import (
    CIAppGitHubAccountUpdateRequestAttributes,
)
from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_data import CIAppGitHubAccountUpdateRequestData
from datadog_api_client.v2.model.ci_app_git_hub_account_update_request_repository import (
    CIAppGitHubAccountUpdateRequestRepository,
)

body = CIAppGitHubAccountUpdateRequest(
    data=CIAppGitHubAccountUpdateRequestData(
        attributes=CIAppGitHubAccountUpdateRequestAttributes(
            account="datadog",
            enabled=True,
            host="github.com",
            repository=CIAppGitHubAccountUpdateRequestRepository(
                enabled=True,
                name="shopist",
            ),
        ),
        type=CIAppGitHubAccountType.CI_GITHUB_ACCOUNT,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityGitHubAccountsApi(api_client)
    response = api_instance.update_ci_app_git_hub_account(body=body)

    print(response)
