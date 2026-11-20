@endpoint(anthropic-usage-and-costs-integration) @endpoint(anthropic-usage-and-costs-integration-v2)
Feature: Anthropic Usage And Costs Integration
  Manage your Datadog Anthropic Usage and Costs integration accounts and
  account resources directly through the Datadog API. See the [Anthropic
  Usage and Costs integration
  page](https://docs.datadoghq.com/integrations/anthropic-usage-and-costs/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AnthropicUsageAndCostsIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an Anthropic Usage and Costs account returns "Bad Request" response
    Given operation "CreateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "CreateAnthropicUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an Anthropic Usage and Costs account returns "Created" response
    Given operation "CreateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "CreateAnthropicUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an Anthropic Usage and Costs account returns "Not Found" response
    Given operation "CreateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "CreateAnthropicUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an Anthropic Usage and Costs account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "CreateAnthropicUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an Anthropic Usage and Costs account returns "Bad Request" response
    Given operation "DeleteAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "DeleteAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an Anthropic Usage and Costs account returns "Not Found" response
    Given operation "DeleteAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "DeleteAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an Anthropic Usage and Costs account returns "OK" response
    Given operation "DeleteAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "DeleteAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an Anthropic Usage and Costs account returns "Bad Request" response
    Given operation "GetAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "GetAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an Anthropic Usage and Costs account returns "Not Found" response
    Given operation "GetAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "GetAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an Anthropic Usage and Costs account returns "OK" response
    Given operation "GetAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "GetAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Anthropic Usage and Costs accounts returns "Bad Request" response
    Given operation "ListAnthropicUsageAndCostsIntegrationAccounts" enabled
    And new "ListAnthropicUsageAndCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Anthropic Usage and Costs accounts returns "Not Found" response
    Given operation "ListAnthropicUsageAndCostsIntegrationAccounts" enabled
    And new "ListAnthropicUsageAndCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List Anthropic Usage and Costs accounts returns "OK" response
    Given operation "ListAnthropicUsageAndCostsIntegrationAccounts" enabled
    And new "ListAnthropicUsageAndCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an Anthropic Usage and Costs account returns "Bad Request" response
    Given operation "UpdateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "UpdateAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "id": "9b4c7e2a-1d6f-4a3b-8e5c-0f2d7a9b6c18", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an Anthropic Usage and Costs account returns "Not Found" response
    Given operation "UpdateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "UpdateAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "id": "9b4c7e2a-1d6f-4a3b-8e5c-0f2d7a9b6c18", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an Anthropic Usage and Costs account returns "OK" response
    Given operation "UpdateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "UpdateAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "id": "9b4c7e2a-1d6f-4a3b-8e5c-0f2d7a9b6c18", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an Anthropic Usage and Costs account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateAnthropicUsageAndCostsIntegrationAccount" enabled
    And new "UpdateAnthropicUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"anthropic-cloud-cost-metrics": {"enabled": true}}, "name": "anthropic-acme"}, "id": "9b4c7e2a-1d6f-4a3b-8e5c-0f2d7a9b6c18", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
