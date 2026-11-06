@endpoint(cloud-authentication) @endpoint(cloud-authentication-v2)
Feature: Cloud Authentication
  Configure AWS, GitHub, and Custom OIDC cloud authentication for persona
  and intake authentication through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudAuthentication" API

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a Custom OIDC persona mapping returns "Bad Request" response
    Given operation "CreateOIDCCloudAuthPersonaMapping" enabled
    And new "CreateOIDCCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_uuid": "00000000-0000-0000-0000-000000000003", "claim_matchers": [{"claim": "sub", "mode": "exact", "values": ["system:serviceaccount:controllers:example-controller"]}], "identity_pattern": "system:serviceaccount:controllers:example-controller", "provider_id": "00000000-0000-0000-0000-000000000002"}, "type": "custom_oidc_identity_mapping"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a Custom OIDC persona mapping returns "Conflict" response
    Given operation "CreateOIDCCloudAuthPersonaMapping" enabled
    And new "CreateOIDCCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_uuid": "00000000-0000-0000-0000-000000000003", "claim_matchers": [{"claim": "sub", "mode": "exact", "values": ["system:serviceaccount:controllers:example-controller"]}], "identity_pattern": "system:serviceaccount:controllers:example-controller", "provider_id": "00000000-0000-0000-0000-000000000002"}, "type": "custom_oidc_identity_mapping"}}
    When the request is sent
    Then the response status is 409 Conflict

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a Custom OIDC persona mapping returns "Created" response
    Given there is a valid "role" in the system
    And there is a valid "service_account_user_with_role" in the system
    And there is a valid "oidc_cloud_auth_provider" in the system
    And operation "CreateOIDCCloudAuthPersonaMapping" enabled
    And new "CreateOIDCCloudAuthPersonaMapping" request
    And body with value {"data": {"type": "custom_oidc_identity_mapping", "attributes": {"provider_id": "{{ oidc_cloud_auth_provider.data.id }}", "account_uuid": "{{ service_account_user_with_role.data.id }}", "claim_matchers": [{"claim": "sub", "mode": "exact", "values": ["system:serviceaccount:controllers:example-controller"]}]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "custom_oidc_identity_mapping"
    And the response "data" has field "id"
    And the response "data.attributes.claim_matchers[0].mode" is equal to "exact"
    And the response "data.attributes.account_uuid" is equal to "{{ service_account_user_with_role.data.id }}"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a Custom OIDC provider returns "Bad Request" response
    Given operation "CreateOIDCCloudAuthProvider" enabled
    And new "CreateOIDCCloudAuthProvider" request
    And body with value {"data": {"attributes": {"audiences": ["datadog/00000000-0000-0000-0000-000000000001"], "discovery_type": "oidc_discovery", "identity_claim_name": "sub", "issuer_url": "https://issuer.example.com", "jwks_url": "https://issuer.example.com/keys", "org_uuid_claim_name": "dd_org_uuid", "org_uuid_source": "dd_org_uuid", "provider_name": "example-cluster", "required_claims": [{"claim": "sub", "mode": "exact", "values": ["system:serviceaccount:controllers:example-controller"]}]}, "type": "custom_oidc_provider_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a Custom OIDC provider returns "Conflict" response
    Given operation "CreateOIDCCloudAuthProvider" enabled
    And new "CreateOIDCCloudAuthProvider" request
    And body with value {"data": {"attributes": {"audiences": ["datadog/00000000-0000-0000-0000-000000000001"], "discovery_type": "oidc_discovery", "identity_claim_name": "sub", "issuer_url": "https://issuer.example.com", "jwks_url": "https://issuer.example.com/keys", "org_uuid_claim_name": "dd_org_uuid", "org_uuid_source": "dd_org_uuid", "provider_name": "example-cluster", "required_claims": [{"claim": "sub", "mode": "exact", "values": ["system:serviceaccount:controllers:example-controller"]}]}, "type": "custom_oidc_provider_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a Custom OIDC provider returns "Created" response
    Given operation "CreateOIDCCloudAuthProvider" enabled
    And new "CreateOIDCCloudAuthProvider" request
    And body with value {"data": {"type": "custom_oidc_provider_config", "attributes": {"provider_name": "oidc-{{ unique_hash }}", "issuer_url": "https://oidc-{{ unique_hash }}.example.com", "discovery_type": "oidc_discovery", "audiences": ["sdk-test"]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "custom_oidc_provider_config"
    And the response "data" has field "id"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a GitHub cloud auth intake mapping returns "Bad Request" response
    Given operation "CreateGitHubCloudAuthIntakeMapping" enabled
    And new "CreateGitHubCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a GitHub cloud auth intake mapping returns "Conflict" response
    Given operation "CreateGitHubCloudAuthIntakeMapping" enabled
    And new "CreateGitHubCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a GitHub cloud auth intake mapping returns "Created" response
    Given operation "CreateGitHubCloudAuthIntakeMapping" enabled
    And new "CreateGitHubCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a GitHub cloud auth persona mapping returns "Bad Request" response
    Given operation "CreateGitHubCloudAuthPersonaMapping" enabled
    And new "CreateGitHubCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@example.com", "claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a GitHub cloud auth persona mapping returns "Conflict" response
    Given operation "CreateGitHubCloudAuthPersonaMapping" enabled
    And new "CreateGitHubCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@example.com", "claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create a GitHub cloud auth persona mapping returns "Created" response
    Given operation "CreateGitHubCloudAuthPersonaMapping" enabled
    And new "CreateGitHubCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@example.com", "claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_config"}}
    When the request is sent
    Then the response status is 201 Created

  @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create an AWS cloud authentication intake mapping returns "Bad Request" response
    Given operation "CreateAWSCloudAuthIntakeMapping" enabled
    And new "CreateAWSCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"arn_pattern": "not-an-arn"}, "type": "aws_cloud_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create an AWS cloud authentication intake mapping returns "Conflict" response
    Given there is an integrated AWS test account for WIF
    And there is a valid "aws_cloud_auth_intake_mapping" in the system
    And operation "CreateAWSCloudAuthIntakeMapping" enabled
    And new "CreateAWSCloudAuthIntakeMapping" request
    And body with value {"data":{"type":"aws_cloud_auth_intake_mapping","attributes":{"arn_pattern":"arn:aws:sts::{{ aws_wif_account_v2.data[0].attributes.aws_account_id }}:assumed-role/DatadogAgent-{{ unique_hash }}/*"}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create an AWS cloud authentication intake mapping returns "Created" response
    Given there is an integrated AWS test account for WIF
    And operation "CreateAWSCloudAuthIntakeMapping" enabled
    And new "CreateAWSCloudAuthIntakeMapping" request
    And body with value {"data":{"type":"aws_cloud_auth_intake_mapping","attributes":{"arn_pattern":"arn:aws:sts::{{ aws_wif_account_v2.data[0].attributes.aws_account_id }}:assumed-role/DatadogAgent-{{ unique_hash }}/*"}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "aws_cloud_auth_intake_mapping"
    And the response "data" has field "id"
    And the response "data.attributes.arn_pattern" is equal to "arn:aws:sts::{{ aws_wif_account_v2.data[0].attributes.aws_account_id }}:assumed-role/DatadogAgent-{{ unique_hash }}/*"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create an AWS cloud authentication persona mapping returns "Bad Request" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create an AWS cloud authentication persona mapping returns "Conflict" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Create an AWS cloud authentication persona mapping returns "Created" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC persona mapping returns "Bad Request" response
    Given operation "DeleteOIDCCloudAuthPersonaMapping" enabled
    And new "DeleteOIDCCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC persona mapping returns "No Content" response
    Given there is a valid "role" in the system
    And there is a valid "service_account_user_with_role" in the system
    And there is a valid "oidc_cloud_auth_provider" in the system
    And there is a valid "oidc_cloud_auth_persona_mapping" in the system
    And operation "DeleteOIDCCloudAuthPersonaMapping" enabled
    And new "DeleteOIDCCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "oidc_cloud_auth_persona_mapping.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC persona mapping returns "Not Found" response
    Given operation "DeleteOIDCCloudAuthPersonaMapping" enabled
    And new "DeleteOIDCCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC provider returns "Bad Request" response
    Given operation "DeleteOIDCCloudAuthProvider" enabled
    And new "DeleteOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC provider returns "Conflict" response
    Given operation "DeleteOIDCCloudAuthProvider" enabled
    And new "DeleteOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC provider returns "No Content" response
    Given there is a valid "oidc_cloud_auth_provider" in the system
    And operation "DeleteOIDCCloudAuthProvider" enabled
    And new "DeleteOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "oidc_cloud_auth_provider.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a Custom OIDC provider returns "Not Found" response
    Given operation "DeleteOIDCCloudAuthProvider" enabled
    And new "DeleteOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a GitHub cloud auth intake mapping returns "No Content" response
    Given operation "DeleteGitHubCloudAuthIntakeMapping" enabled
    And new "DeleteGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a GitHub cloud auth intake mapping returns "Not Found" response
    Given operation "DeleteGitHubCloudAuthIntakeMapping" enabled
    And new "DeleteGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a GitHub cloud auth persona mapping returns "No Content" response
    Given operation "DeleteGitHubCloudAuthPersonaMapping" enabled
    And new "DeleteGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete a GitHub cloud auth persona mapping returns "Not Found" response
    Given operation "DeleteGitHubCloudAuthPersonaMapping" enabled
    And new "DeleteGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete an AWS cloud authentication intake mapping returns "No Content" response
    Given there is an integrated AWS test account for WIF
    And there is a valid "aws_cloud_auth_intake_mapping" in the system
    And operation "DeleteAWSCloudAuthIntakeMapping" enabled
    And new "DeleteAWSCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "aws_cloud_auth_intake_mapping.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete an AWS cloud authentication intake mapping returns "Not Found" response
    Given operation "DeleteAWSCloudAuthIntakeMapping" enabled
    And new "DeleteAWSCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete an AWS cloud authentication persona mapping returns "No Content" response
    Given operation "DeleteAWSCloudAuthPersonaMapping" enabled
    And new "DeleteAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Delete an AWS cloud authentication persona mapping returns "Not Found" response
    Given operation "DeleteAWSCloudAuthPersonaMapping" enabled
    And new "DeleteAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a Custom OIDC persona mapping returns "Bad Request" response
    Given operation "GetOIDCCloudAuthPersonaMapping" enabled
    And new "GetOIDCCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a Custom OIDC persona mapping returns "Not Found" response
    Given operation "GetOIDCCloudAuthPersonaMapping" enabled
    And new "GetOIDCCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a Custom OIDC persona mapping returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "service_account_user_with_role" in the system
    And there is a valid "oidc_cloud_auth_provider" in the system
    And there is a valid "oidc_cloud_auth_persona_mapping" in the system
    And operation "GetOIDCCloudAuthPersonaMapping" enabled
    And new "GetOIDCCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "oidc_cloud_auth_persona_mapping.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_oidc_identity_mapping"
    And the response "data" has field "id"
    And the response "data.attributes.claim_matchers[0].mode" is equal to "exact"
    And the response "data.attributes.account_uuid" is equal to "{{ service_account_user_with_role.data.id }}"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a Custom OIDC provider returns "Bad Request" response
    Given operation "GetOIDCCloudAuthProvider" enabled
    And new "GetOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a Custom OIDC provider returns "Not Found" response
    Given operation "GetOIDCCloudAuthProvider" enabled
    And new "GetOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a Custom OIDC provider returns "OK" response
    Given there is a valid "oidc_cloud_auth_provider" in the system
    And operation "GetOIDCCloudAuthProvider" enabled
    And new "GetOIDCCloudAuthProvider" request
    And request contains "provider_id" parameter from "oidc_cloud_auth_provider.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "custom_oidc_provider_config"
    And the response "data" has field "id"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a GitHub cloud authentication intake mapping returns "Not Found" response
    Given operation "GetGitHubCloudAuthIntakeMapping" enabled
    And new "GetGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a GitHub cloud authentication intake mapping returns "OK" response
    Given operation "GetGitHubCloudAuthIntakeMapping" enabled
    And new "GetGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a GitHub cloud authentication persona mapping returns "Not Found" response
    Given operation "GetGitHubCloudAuthPersonaMapping" enabled
    And new "GetGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get a GitHub cloud authentication persona mapping returns "OK" response
    Given operation "GetGitHubCloudAuthPersonaMapping" enabled
    And new "GetGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get an AWS cloud authentication intake mapping returns "Not Found" response
    Given operation "GetAWSCloudAuthIntakeMapping" enabled
    And new "GetAWSCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get an AWS cloud authentication intake mapping returns "OK" response
    Given there is an integrated AWS test account for WIF
    And there is a valid "aws_cloud_auth_intake_mapping" in the system
    And operation "GetAWSCloudAuthIntakeMapping" enabled
    And new "GetAWSCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "aws_cloud_auth_intake_mapping.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "aws_cloud_auth_intake_mapping.data.id"
    And the response "data.attributes.arn_pattern" is equal to "arn:aws:sts::{{ aws_wif_account_v2.data[0].attributes.aws_account_id }}:assumed-role/DatadogAgent-{{ unique_hash }}/*"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get an AWS cloud authentication persona mapping returns "Not Found" response
    Given operation "GetAWSCloudAuthPersonaMapping" enabled
    And new "GetAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: Get an AWS cloud authentication persona mapping returns "OK" response
    Given operation "GetAWSCloudAuthPersonaMapping" enabled
    And new "GetAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List AWS cloud authentication intake mappings returns "Bad Request" response
    Given operation "ListAWSCloudAuthIntakeMappings" enabled
    And new "ListAWSCloudAuthIntakeMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List AWS cloud authentication intake mappings returns "OK" response
    Given there is an integrated AWS test account for WIF
    And there is a valid "aws_cloud_auth_intake_mapping" in the system
    And operation "ListAWSCloudAuthIntakeMappings" enabled
    And new "ListAWSCloudAuthIntakeMappings" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ aws_cloud_auth_intake_mapping.data.id }}"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List AWS cloud authentication persona mappings returns "Bad Request" response
    Given operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List AWS cloud authentication persona mappings returns "OK" response
    Given operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List GitHub cloud authentication intake mappings returns "Bad Request" response
    Given operation "ListGitHubCloudAuthIntakeMappings" enabled
    And new "ListGitHubCloudAuthIntakeMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List GitHub cloud authentication intake mappings returns "OK" response
    Given operation "ListGitHubCloudAuthIntakeMappings" enabled
    And new "ListGitHubCloudAuthIntakeMappings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List GitHub cloud authentication persona mappings returns "Bad Request" response
    Given operation "ListGitHubCloudAuthPersonaMappings" enabled
    And new "ListGitHubCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List GitHub cloud authentication persona mappings returns "OK" response
    Given operation "ListGitHubCloudAuthPersonaMappings" enabled
    And new "ListGitHubCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List all Custom OIDC persona mappings returns "Bad Request" response
    Given operation "ListOIDCCloudAuthPersonaMappings" enabled
    And new "ListOIDCCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List all Custom OIDC persona mappings returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "service_account_user_with_role" in the system
    And there is a valid "oidc_cloud_auth_provider" in the system
    And there is a valid "oidc_cloud_auth_persona_mapping" in the system
    And operation "ListOIDCCloudAuthPersonaMappings" enabled
    And new "ListOIDCCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ oidc_cloud_auth_persona_mapping.data.id }}"

  @generated @skip @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List all Custom OIDC providers returns "Bad Request" response
    Given operation "ListOIDCCloudAuthProviders" enabled
    And new "ListOIDCCloudAuthProviders" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:ddoghq/credential-management @team:ddoghq/delegated-auth-login
  Scenario: List all Custom OIDC providers returns "OK" response
    Given there is a valid "oidc_cloud_auth_provider" in the system
    And operation "ListOIDCCloudAuthProviders" enabled
    And new "ListOIDCCloudAuthProviders" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ oidc_cloud_auth_provider.data.id }}"
