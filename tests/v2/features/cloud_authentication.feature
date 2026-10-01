@endpoint(cloud-authentication) @endpoint(cloud-authentication-v2)
Feature: Cloud Authentication
  Configure AWS and GitHub cloud authentication mappings for persona and
  intake authentication through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudAuthentication" API

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create a GitHub cloud auth intake mapping returns "Bad Request" response
    Given operation "CreateGitHubCloudAuthIntakeMapping" enabled
    And new "CreateGitHubCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create a GitHub cloud auth intake mapping returns "Conflict" response
    Given operation "CreateGitHubCloudAuthIntakeMapping" enabled
    And new "CreateGitHubCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create a GitHub cloud auth intake mapping returns "Created" response
    Given operation "CreateGitHubCloudAuthIntakeMapping" enabled
    And new "CreateGitHubCloudAuthIntakeMapping" request
    And body with value {"data": {"attributes": {"claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_intake_mapping"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create a GitHub cloud auth persona mapping returns "Bad Request" response
    Given operation "CreateGitHubCloudAuthPersonaMapping" enabled
    And new "CreateGitHubCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@example.com", "claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create a GitHub cloud auth persona mapping returns "Conflict" response
    Given operation "CreateGitHubCloudAuthPersonaMapping" enabled
    And new "CreateGitHubCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@example.com", "claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create a GitHub cloud auth persona mapping returns "Created" response
    Given operation "CreateGitHubCloudAuthPersonaMapping" enabled
    And new "CreateGitHubCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@example.com", "claim_matchers": {"actor": "octocat", "actor_id": "1234567", "enterprise": "test_enterprise", "enterprise_id": "42", "environment": "production", "event_name": "push", "job_workflow_ref": "test_owner/test_repo/.github/workflows/jobs.yml@refs/heads/main", "ref": "refs/heads/main", "ref_type": "branch", "repository": "test_owner/test_repo", "repository_id": "123456789", "repository_owner": "test_owner", "repository_owner_id": "987654321", "repository_visibility": "public", "runner_environment": "github-hosted", "sub": "repo:test_owner/test_repo:(ref:refs/heads/main|pull_request)", "workflow": "CI", "workflow_ref": "test_owner/test_repo/.github/workflows/ci.yml@refs/heads/main"}}, "type": "github_oidc_auth_config"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create an AWS cloud authentication persona mapping returns "Bad Request" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create an AWS cloud authentication persona mapping returns "Conflict" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create an AWS cloud authentication persona mapping returns "Created" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete a GitHub cloud auth intake mapping returns "No Content" response
    Given operation "DeleteGitHubCloudAuthIntakeMapping" enabled
    And new "DeleteGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete a GitHub cloud auth intake mapping returns "Not Found" response
    Given operation "DeleteGitHubCloudAuthIntakeMapping" enabled
    And new "DeleteGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete a GitHub cloud auth persona mapping returns "No Content" response
    Given operation "DeleteGitHubCloudAuthPersonaMapping" enabled
    And new "DeleteGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete a GitHub cloud auth persona mapping returns "Not Found" response
    Given operation "DeleteGitHubCloudAuthPersonaMapping" enabled
    And new "DeleteGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete an AWS cloud authentication persona mapping returns "No Content" response
    Given operation "DeleteAWSCloudAuthPersonaMapping" enabled
    And new "DeleteAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete an AWS cloud authentication persona mapping returns "Not Found" response
    Given operation "DeleteAWSCloudAuthPersonaMapping" enabled
    And new "DeleteAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get a GitHub cloud authentication intake mapping returns "Not Found" response
    Given operation "GetGitHubCloudAuthIntakeMapping" enabled
    And new "GetGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get a GitHub cloud authentication intake mapping returns "OK" response
    Given operation "GetGitHubCloudAuthIntakeMapping" enabled
    And new "GetGitHubCloudAuthIntakeMapping" request
    And request contains "intake_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get a GitHub cloud authentication persona mapping returns "Not Found" response
    Given operation "GetGitHubCloudAuthPersonaMapping" enabled
    And new "GetGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get a GitHub cloud authentication persona mapping returns "OK" response
    Given operation "GetGitHubCloudAuthPersonaMapping" enabled
    And new "GetGitHubCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get an AWS cloud authentication persona mapping returns "Not Found" response
    Given operation "GetAWSCloudAuthPersonaMapping" enabled
    And new "GetAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get an AWS cloud authentication persona mapping returns "OK" response
    Given operation "GetAWSCloudAuthPersonaMapping" enabled
    And new "GetAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List AWS cloud authentication persona mappings returns "Bad Request" response
    Given operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List AWS cloud authentication persona mappings returns "OK" response
    Given operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List GitHub cloud authentication intake mappings returns "Bad Request" response
    Given operation "ListGitHubCloudAuthIntakeMappings" enabled
    And new "ListGitHubCloudAuthIntakeMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List GitHub cloud authentication intake mappings returns "OK" response
    Given operation "ListGitHubCloudAuthIntakeMappings" enabled
    And new "ListGitHubCloudAuthIntakeMappings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List GitHub cloud authentication persona mappings returns "Bad Request" response
    Given operation "ListGitHubCloudAuthPersonaMappings" enabled
    And new "ListGitHubCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List GitHub cloud authentication persona mappings returns "OK" response
    Given operation "ListGitHubCloudAuthPersonaMappings" enabled
    And new "ListGitHubCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK
