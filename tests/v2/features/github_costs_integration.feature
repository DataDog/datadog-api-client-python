@endpoint(github-costs-integration) @endpoint(github-costs-integration-v2)
Feature: GitHub Costs Integration
  Manage your Datadog GitHub Costs integration accounts and account
  resources directly through the Datadog API. See the [GitHub Costs
  integration page](https://docs.datadoghq.com/integrations/github-costs/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GitHubCostsIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a GitHub Costs integration account returns "Bad Request" response
    Given operation "CreateGitHubCostsIntegrationAccount" enabled
    And new "CreateGitHubCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a GitHub Costs integration account returns "Created" response
    Given operation "CreateGitHubCostsIntegrationAccount" enabled
    And new "CreateGitHubCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a GitHub Costs integration account returns "Not Found" response
    Given operation "CreateGitHubCostsIntegrationAccount" enabled
    And new "CreateGitHubCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a GitHub Costs integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateGitHubCostsIntegrationAccount" enabled
    And new "CreateGitHubCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a GitHub Costs integration account returns "Bad Request" response
    Given operation "DeleteGitHubCostsIntegrationAccount" enabled
    And new "DeleteGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a GitHub Costs integration account returns "Not Found" response
    Given operation "DeleteGitHubCostsIntegrationAccount" enabled
    And new "DeleteGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a GitHub Costs integration account returns "OK" response
    Given operation "DeleteGitHubCostsIntegrationAccount" enabled
    And new "DeleteGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a GitHub Costs integration account returns "Bad Request" response
    Given operation "GetGitHubCostsIntegrationAccount" enabled
    And new "GetGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a GitHub Costs integration account returns "Not Found" response
    Given operation "GetGitHubCostsIntegrationAccount" enabled
    And new "GetGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a GitHub Costs integration account returns "OK" response
    Given operation "GetGitHubCostsIntegrationAccount" enabled
    And new "GetGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List GitHub Costs integration accounts returns "Bad Request" response
    Given operation "ListGitHubCostsIntegrationAccounts" enabled
    And new "ListGitHubCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List GitHub Costs integration accounts returns "Not Found" response
    Given operation "ListGitHubCostsIntegrationAccounts" enabled
    And new "ListGitHubCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List GitHub Costs integration accounts returns "OK" response
    Given operation "ListGitHubCostsIntegrationAccounts" enabled
    And new "ListGitHubCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a GitHub Costs integration account returns "Bad Request" response
    Given operation "UpdateGitHubCostsIntegrationAccount" enabled
    And new "UpdateGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "id": "4b7c2e1a-6f3d-4e8b-9a52-1d0c8f7e3b64", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a GitHub Costs integration account returns "Not Found" response
    Given operation "UpdateGitHubCostsIntegrationAccount" enabled
    And new "UpdateGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "id": "4b7c2e1a-6f3d-4e8b-9a52-1d0c8f7e3b64", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a GitHub Costs integration account returns "OK" response
    Given operation "UpdateGitHubCostsIntegrationAccount" enabled
    And new "UpdateGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "id": "4b7c2e1a-6f3d-4e8b-9a52-1d0c8f7e3b64", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a GitHub Costs integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateGitHubCostsIntegrationAccount" enabled
    And new "UpdateGitHubCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "github-costs-acme", "settings": {"enterprise_name": "acme", "tags": "env:prod,team:finops"}}, "id": "4b7c2e1a-6f3d-4e8b-9a52-1d0c8f7e3b64", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
