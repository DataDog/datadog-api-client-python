"""
List GitHub CI Visibility status returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_git_hub_accounts_api import CIVisibilityGitHubAccountsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityGitHubAccountsApi(api_client)
    response = api_instance.list_ci_app_git_hub_accounts()

    print(response)
