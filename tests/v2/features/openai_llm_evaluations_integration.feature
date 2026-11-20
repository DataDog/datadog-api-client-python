@endpoint(openai-llm-evaluations-integration) @endpoint(openai-llm-evaluations-integration-v2)
Feature: OpenAI LLM Evaluations Integration
  Manage your Datadog OpenAI LLM Evaluations integration accounts and
  account resources directly through the Datadog API. See the [OpenAI
  integration page](https://docs.datadoghq.com/integrations/openai/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OpenAILLMEvaluationsIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI LLM Evaluations account returns "Bad Request" response
    Given operation "CreateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "CreateOpenAILLMEvaluationsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI LLM Evaluations account returns "Created" response
    Given operation "CreateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "CreateOpenAILLMEvaluationsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI LLM Evaluations account returns "Not Found" response
    Given operation "CreateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "CreateOpenAILLMEvaluationsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI LLM Evaluations account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "CreateOpenAILLMEvaluationsIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI LLM Evaluations account returns "Bad Request" response
    Given operation "DeleteOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "DeleteOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI LLM Evaluations account returns "Not Found" response
    Given operation "DeleteOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "DeleteOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI LLM Evaluations account returns "OK" response
    Given operation "DeleteOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "DeleteOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI LLM Evaluations account returns "Bad Request" response
    Given operation "GetOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "GetOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI LLM Evaluations account returns "Not Found" response
    Given operation "GetOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "GetOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI LLM Evaluations account returns "OK" response
    Given operation "GetOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "GetOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI LLM Evaluations accounts returns "Bad Request" response
    Given operation "ListOpenAILLMEvaluationsIntegrationAccounts" enabled
    And new "ListOpenAILLMEvaluationsIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI LLM Evaluations accounts returns "Not Found" response
    Given operation "ListOpenAILLMEvaluationsIntegrationAccounts" enabled
    And new "ListOpenAILLMEvaluationsIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI LLM Evaluations accounts returns "OK" response
    Given operation "ListOpenAILLMEvaluationsIntegrationAccounts" enabled
    And new "ListOpenAILLMEvaluationsIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI LLM Evaluations account returns "Bad Request" response
    Given operation "UpdateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "UpdateOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI LLM Evaluations account returns "Not Found" response
    Given operation "UpdateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "UpdateOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI LLM Evaluations account returns "OK" response
    Given operation "UpdateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "UpdateOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI LLM Evaluations account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateOpenAILLMEvaluationsIntegrationAccount" enabled
    And new "UpdateOpenAILLMEvaluationsIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-llm-evaluations-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
