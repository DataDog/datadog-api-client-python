"""
Create a GitHub cloud auth intake mapping returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_create_attributes import (
    GitHubCloudAuthIntakeMappingCreateAttributes,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_create_data import (
    GitHubCloudAuthIntakeMappingCreateData,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_create_request import (
    GitHubCloudAuthIntakeMappingCreateRequest,
)
from datadog_api_client.v2.model.git_hub_cloud_auth_intake_mapping_type import GitHubCloudAuthIntakeMappingType
from datadog_api_client.v2.model.git_hub_oidc_claim_patterns import GitHubOIDCClaimPatterns

body = GitHubCloudAuthIntakeMappingCreateRequest(
    data=GitHubCloudAuthIntakeMappingCreateData(
        attributes=GitHubCloudAuthIntakeMappingCreateAttributes(
            claim_matchers=GitHubOIDCClaimPatterns(
                actor="octocat",
                actor_id="1234567",
                enterprise="test_enterprise",
                enterprise_id="42",
                environment="production",
                event_name="push",
                job_workflow_ref="test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main",
                ref="refs/heads/main",
                ref_type="branch",
                repository="test_owner/test_repo",
                repository_id="123456789",
                repository_owner="test_owner",
                repository_owner_id="987654321",
                repository_visibility="public",
                runner_environment="github-hosted",
                sub="repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)",
                workflow="CI",
                workflow_ref="test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main",
            ),
        ),
        type=GitHubCloudAuthIntakeMappingType.GITHUB_OIDC_AUTH_INTAKE_MAPPING,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_git_hub_cloud_auth_intake_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.create_git_hub_cloud_auth_intake_mapping(body=body)

    print(response)
