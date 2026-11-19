@endpoint(openai-codex-integration) @endpoint(openai-codex-integration-v2)
Feature: OpenAI Codex Integration
  Manage your Datadog OpenAI Codex integration accounts and account
  resources directly through the Datadog API. See the [OpenAI Codex
  integration page](https://docs.datadoghq.com/integrations/openai-codex/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OpenAICodexIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Codex integration account returns "Bad Request" response
    Given operation "CreateOpenAICodexIntegrationAccount" enabled
    And new "CreateOpenAICodexIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Codex integration account returns "Created" response
    Given operation "CreateOpenAICodexIntegrationAccount" enabled
    And new "CreateOpenAICodexIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Codex integration account returns "Not Found" response
    Given operation "CreateOpenAICodexIntegrationAccount" enabled
    And new "CreateOpenAICodexIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Codex integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateOpenAICodexIntegrationAccount" enabled
    And new "CreateOpenAICodexIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Codex integration account returns "Bad Request" response
    Given operation "DeleteOpenAICodexIntegrationAccount" enabled
    And new "DeleteOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Codex integration account returns "Not Found" response
    Given operation "DeleteOpenAICodexIntegrationAccount" enabled
    And new "DeleteOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Codex integration account returns "OK" response
    Given operation "DeleteOpenAICodexIntegrationAccount" enabled
    And new "DeleteOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Codex integration account returns "Bad Request" response
    Given operation "GetOpenAICodexIntegrationAccount" enabled
    And new "GetOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Codex integration account returns "Not Found" response
    Given operation "GetOpenAICodexIntegrationAccount" enabled
    And new "GetOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Codex integration account returns "OK" response
    Given operation "GetOpenAICodexIntegrationAccount" enabled
    And new "GetOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Codex integration accounts returns "Bad Request" response
    Given operation "ListOpenAICodexIntegrationAccounts" enabled
    And new "ListOpenAICodexIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Codex integration accounts returns "Not Found" response
    Given operation "ListOpenAICodexIntegrationAccounts" enabled
    And new "ListOpenAICodexIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Codex integration accounts returns "OK" response
    Given operation "ListOpenAICodexIntegrationAccounts" enabled
    And new "ListOpenAICodexIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Codex integration account returns "Bad Request" response
    Given operation "UpdateOpenAICodexIntegrationAccount" enabled
    And new "UpdateOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "id": "7d2f9c4e-3a1b-4c8e-9f6d-2b5a8e1c0d47", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Codex integration account returns "Not Found" response
    Given operation "UpdateOpenAICodexIntegrationAccount" enabled
    And new "UpdateOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "id": "7d2f9c4e-3a1b-4c8e-9f6d-2b5a8e1c0d47", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Codex integration account returns "OK" response
    Given operation "UpdateOpenAICodexIntegrationAccount" enabled
    And new "UpdateOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "id": "7d2f9c4e-3a1b-4c8e-9f6d-2b5a8e1c0d47", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Codex integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateOpenAICodexIntegrationAccount" enabled
    And new "UpdateOpenAICodexIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-codex-dora": {"enabled": true}, "openai-codex-turn-metrics": {"enabled": true}}, "name": "openai-codex-acme", "settings": {"codex_workspace_id": "your-workspace-id"}}, "id": "7d2f9c4e-3a1b-4c8e-9f6d-2b5a8e1c0d47", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
