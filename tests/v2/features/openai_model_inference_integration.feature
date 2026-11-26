@endpoint(openai-model-inference-integration) @endpoint(openai-model-inference-integration-v2)
Feature: OpenAI Model Inference Integration
  Manage your Datadog OpenAI Model Inference integration accounts and
  account resources directly through the Datadog API. See the [OpenAI
  integration page](https://docs.datadoghq.com/integrations/openai/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OpenAIModelInferenceIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Model Inference account returns "Bad Request" response
    Given operation "CreateOpenAIModelInferenceIntegrationAccount" enabled
    And new "CreateOpenAIModelInferenceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Model Inference account returns "Created" response
    Given operation "CreateOpenAIModelInferenceIntegrationAccount" enabled
    And new "CreateOpenAIModelInferenceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Model Inference account returns "Not Found" response
    Given operation "CreateOpenAIModelInferenceIntegrationAccount" enabled
    And new "CreateOpenAIModelInferenceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create an OpenAI Model Inference account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateOpenAIModelInferenceIntegrationAccount" enabled
    And new "CreateOpenAIModelInferenceIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Model Inference account returns "Bad Request" response
    Given operation "DeleteOpenAIModelInferenceIntegrationAccount" enabled
    And new "DeleteOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Model Inference account returns "Not Found" response
    Given operation "DeleteOpenAIModelInferenceIntegrationAccount" enabled
    And new "DeleteOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete an OpenAI Model Inference account returns "OK" response
    Given operation "DeleteOpenAIModelInferenceIntegrationAccount" enabled
    And new "DeleteOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Model Inference account returns "Bad Request" response
    Given operation "GetOpenAIModelInferenceIntegrationAccount" enabled
    And new "GetOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Model Inference account returns "Not Found" response
    Given operation "GetOpenAIModelInferenceIntegrationAccount" enabled
    And new "GetOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get an OpenAI Model Inference account returns "OK" response
    Given operation "GetOpenAIModelInferenceIntegrationAccount" enabled
    And new "GetOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Model Inference accounts returns "Bad Request" response
    Given operation "ListOpenAIModelInferenceIntegrationAccounts" enabled
    And new "ListOpenAIModelInferenceIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Model Inference accounts returns "Not Found" response
    Given operation "ListOpenAIModelInferenceIntegrationAccounts" enabled
    And new "ListOpenAIModelInferenceIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List OpenAI Model Inference accounts returns "OK" response
    Given operation "ListOpenAIModelInferenceIntegrationAccounts" enabled
    And new "ListOpenAIModelInferenceIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Model Inference account returns "Bad Request" response
    Given operation "UpdateOpenAIModelInferenceIntegrationAccount" enabled
    And new "UpdateOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Model Inference account returns "Not Found" response
    Given operation "UpdateOpenAIModelInferenceIntegrationAccount" enabled
    And new "UpdateOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Model Inference account returns "OK" response
    Given operation "UpdateOpenAIModelInferenceIntegrationAccount" enabled
    And new "UpdateOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update an OpenAI Model Inference account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateOpenAIModelInferenceIntegrationAccount" enabled
    And new "UpdateOpenAIModelInferenceIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"openai-llm-completions": {"enabled": true}, "openai-project-cloud-cost-data": {"enabled": true}}, "name": "openai-model-inference-acme", "settings": {"custom_tags": "team:ai,env:prod"}}, "id": "3f8b2c1d-6e4a-4b9f-8c2d-1a7e5b9c0f63", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
