@endpoint(ci-visibility-github-accounts) @endpoint(ci-visibility-github-accounts-v2)
Feature: CI Visibility GitHub Accounts
  Manage CI Visibility opt-in status for your GitHub accounts and
  repositories. See the [CI Visibility GitHub Actions setup
  page](https://docs.datadoghq.com/continuous_integration/pipelines/github/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CIVisibilityGitHubAccounts" API

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: List GitHub CI Visibility status returns "Bad Request" response
    Given new "ListCIAppGitHubAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: List GitHub CI Visibility status returns "Not Found" response
    Given new "ListCIAppGitHubAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: List GitHub CI Visibility status returns "OK" response
    Given new "ListCIAppGitHubAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update GitHub CI Visibility status returns "Bad Request" response
    Given new "UpdateCIAppGitHubAccount" request
    And body with value {"data": {"attributes": {"account": "datadog", "enabled": true, "host": "github.com", "repository": {"enabled": true, "name": "shopist"}}, "type": "ci_github_account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update GitHub CI Visibility status returns "Conflict" response
    Given new "UpdateCIAppGitHubAccount" request
    And body with value {"data": {"attributes": {"account": "datadog", "enabled": true, "host": "github.com", "repository": {"enabled": true, "name": "shopist"}}, "type": "ci_github_account"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update GitHub CI Visibility status returns "Not Found" response
    Given new "UpdateCIAppGitHubAccount" request
    And body with value {"data": {"attributes": {"account": "datadog", "enabled": true, "host": "github.com", "repository": {"enabled": true, "name": "shopist"}}, "type": "ci_github_account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ci-app-backend
  Scenario: Update GitHub CI Visibility status returns "OK" response
    Given new "UpdateCIAppGitHubAccount" request
    And body with value {"data": {"attributes": {"account": "datadog", "enabled": true, "host": "github.com", "repository": {"enabled": true, "name": "shopist"}}, "type": "ci_github_account"}}
    When the request is sent
    Then the response status is 200 OK
