@endpoint(claude-compliance-integration) @endpoint(claude-compliance-integration-v2)
Feature: Claude Compliance Integration
  Manage your Datadog Claude Compliance integration accounts and account
  resources directly through the Datadog API. See the [Claude Compliance
  integration page](https://docs.datadoghq.com/integrations/anthropic-
  compliance-logs/) for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ClaudeComplianceIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Claude Compliance integration account returns "Bad Request" response
    Given operation "CreateClaudeComplianceIntegrationAccount" enabled
    And new "CreateClaudeComplianceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Claude Compliance integration account returns "Created" response
    Given operation "CreateClaudeComplianceIntegrationAccount" enabled
    And new "CreateClaudeComplianceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Claude Compliance integration account returns "Not Found" response
    Given operation "CreateClaudeComplianceIntegrationAccount" enabled
    And new "CreateClaudeComplianceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a Claude Compliance integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateClaudeComplianceIntegrationAccount" enabled
    And new "CreateClaudeComplianceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a Claude Compliance integration account returns "Bad Request" response
    Given operation "DeleteClaudeComplianceIntegrationAccount" enabled
    And new "DeleteClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a Claude Compliance integration account returns "Not Found" response
    Given operation "DeleteClaudeComplianceIntegrationAccount" enabled
    And new "DeleteClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a Claude Compliance integration account returns "OK" response
    Given operation "DeleteClaudeComplianceIntegrationAccount" enabled
    And new "DeleteClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a Claude Compliance integration account returns "Bad Request" response
    Given operation "GetClaudeComplianceIntegrationAccount" enabled
    And new "GetClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a Claude Compliance integration account returns "Not Found" response
    Given operation "GetClaudeComplianceIntegrationAccount" enabled
    And new "GetClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a Claude Compliance integration account returns "OK" response
    Given operation "GetClaudeComplianceIntegrationAccount" enabled
    And new "GetClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Claude Compliance integration accounts returns "Bad Request" response
    Given operation "ListClaudeComplianceIntegrationAccounts" enabled
    And new "ListClaudeComplianceIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Claude Compliance integration accounts returns "Not Found" response
    Given operation "ListClaudeComplianceIntegrationAccounts" enabled
    And new "ListClaudeComplianceIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Claude Compliance integration accounts returns "OK" response
    Given operation "ListClaudeComplianceIntegrationAccounts" enabled
    And new "ListClaudeComplianceIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Claude Compliance integration account returns "Bad Request" response
    Given operation "UpdateClaudeComplianceIntegrationAccount" enabled
    And new "UpdateClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "id": "5f1a8d3c-7e2b-4f9a-b6c4-8d0e3a7f1b52", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Claude Compliance integration account returns "Not Found" response
    Given operation "UpdateClaudeComplianceIntegrationAccount" enabled
    And new "UpdateClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "id": "5f1a8d3c-7e2b-4f9a-b6c4-8d0e3a7f1b52", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Claude Compliance integration account returns "OK" response
    Given operation "UpdateClaudeComplianceIntegrationAccount" enabled
    And new "UpdateClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "id": "5f1a8d3c-7e2b-4f9a-b6c4-8d0e3a7f1b52", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a Claude Compliance integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateClaudeComplianceIntegrationAccount" enabled
    And new "UpdateClaudeComplianceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "name": "claude-compliance-acme"}, "id": "5f1a8d3c-7e2b-4f9a-b6c4-8d0e3a7f1b52", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
