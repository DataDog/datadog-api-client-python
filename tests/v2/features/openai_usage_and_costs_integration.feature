@endpoint(openai-usage-and-costs-integration) @endpoint(openai-usage-and-costs-integration-v2)
Feature: OpenAI Usage and Costs Integration
  Manage your Datadog OpenAI Usage and Costs integration accounts and
  account resources directly through the Datadog API. See the [OpenAI
  integration page](https://docs.datadoghq.com/integrations/openai/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OpenAIUsageandCostsIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Usage and Costs account returns "Bad Request" response
    Given operation "CreateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "CreateOpenAIUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Usage and Costs account returns "Created" response
    Given operation "CreateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "CreateOpenAIUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Usage and Costs account returns "Not Found" response
    Given operation "CreateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "CreateOpenAIUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Usage and Costs account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "CreateOpenAIUsageAndCostsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Usage and Costs account returns "Bad Request" response
    Given operation "DeleteOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "DeleteOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Usage and Costs account returns "Not Found" response
    Given operation "DeleteOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "DeleteOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Usage and Costs account returns "OK" response
    Given operation "DeleteOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "DeleteOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Usage and Costs account returns "Bad Request" response
    Given operation "GetOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "GetOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Usage and Costs account returns "Not Found" response
    Given operation "GetOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "GetOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Usage and Costs account returns "OK" response
    Given operation "GetOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "GetOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Usage and Costs accounts returns "Bad Request" response
    Given operation "ListOpenAIUsageAndCostsIntegrationAccounts" enabled
    And new "ListOpenAIUsageAndCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Usage and Costs accounts returns "Not Found" response
    Given operation "ListOpenAIUsageAndCostsIntegrationAccounts" enabled
    And new "ListOpenAIUsageAndCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Usage and Costs accounts returns "OK" response
    Given operation "ListOpenAIUsageAndCostsIntegrationAccounts" enabled
    And new "ListOpenAIUsageAndCostsIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Usage and Costs account returns "Bad Request" response
    Given operation "UpdateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "UpdateOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "9c4e7a2b-1d5f-4e8a-b3c6-0f2d8a6e4b17", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Usage and Costs account returns "Not Found" response
    Given operation "UpdateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "UpdateOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "9c4e7a2b-1d5f-4e8a-b3c6-0f2d8a6e4b17", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Usage and Costs account returns "OK" response
    Given operation "UpdateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "UpdateOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "9c4e7a2b-1d5f-4e8a-b3c6-0f2d8a6e4b17", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Usage and Costs account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateOpenAIUsageAndCostsIntegrationAccount" enabled
    And new "UpdateOpenAIUsageAndCostsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-cloud-cost-data": {"enabled": true}}, "name": "openai-usage-and-costs-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "9c4e7a2b-1d5f-4e8a-b3c6-0f2d8a6e4b17", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
