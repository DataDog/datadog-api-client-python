@endpoint(chatgpt-enterprise-integration) @endpoint(chatgpt-enterprise-integration-v2)
Feature: ChatGPT Enterprise Integration
  Manage your Datadog ChatGPT Enterprise integration accounts and account
  resources directly through the Datadog API. See the [ChatGPT Enterprise
  integration page](https://docs.datadoghq.com/integrations/chatgpt-
  enterprise/) for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ChatGPTEnterpriseIntegration" API

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a ChatGPT Enterprise integration account returns "Bad Request" response
    Given operation "CreateChatGPTEnterpriseIntegrationAccount" enabled
    And new "CreateChatGPTEnterpriseIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a ChatGPT Enterprise integration account returns "Created" response
    Given operation "CreateChatGPTEnterpriseIntegrationAccount" enabled
    And new "CreateChatGPTEnterpriseIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a ChatGPT Enterprise integration account returns "Not Found" response
    Given operation "CreateChatGPTEnterpriseIntegrationAccount" enabled
    And new "CreateChatGPTEnterpriseIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Create a ChatGPT Enterprise integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateChatGPTEnterpriseIntegrationAccount" enabled
    And new "CreateChatGPTEnterpriseIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a ChatGPT Enterprise integration account returns "Bad Request" response
    Given operation "DeleteChatGPTEnterpriseIntegrationAccount" enabled
    And new "DeleteChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a ChatGPT Enterprise integration account returns "Not Found" response
    Given operation "DeleteChatGPTEnterpriseIntegrationAccount" enabled
    And new "DeleteChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Delete a ChatGPT Enterprise integration account returns "OK" response
    Given operation "DeleteChatGPTEnterpriseIntegrationAccount" enabled
    And new "DeleteChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a ChatGPT Enterprise integration account returns "Bad Request" response
    Given operation "GetChatGPTEnterpriseIntegrationAccount" enabled
    And new "GetChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a ChatGPT Enterprise integration account returns "Not Found" response
    Given operation "GetChatGPTEnterpriseIntegrationAccount" enabled
    And new "GetChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Get a ChatGPT Enterprise integration account returns "OK" response
    Given operation "GetChatGPTEnterpriseIntegrationAccount" enabled
    And new "GetChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List ChatGPT Enterprise integration accounts returns "Bad Request" response
    Given operation "ListChatGPTEnterpriseIntegrationAccounts" enabled
    And new "ListChatGPTEnterpriseIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List ChatGPT Enterprise integration accounts returns "Not Found" response
    Given operation "ListChatGPTEnterpriseIntegrationAccounts" enabled
    And new "ListChatGPTEnterpriseIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: List ChatGPT Enterprise integration accounts returns "OK" response
    Given operation "ListChatGPTEnterpriseIntegrationAccounts" enabled
    And new "ListChatGPTEnterpriseIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a ChatGPT Enterprise integration account returns "Bad Request" response
    Given operation "UpdateChatGPTEnterpriseIntegrationAccount" enabled
    And new "UpdateChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "id": "3e8a1f6b-9c2d-4b7e-8a5f-6d1c4e9b2a03", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a ChatGPT Enterprise integration account returns "Not Found" response
    Given operation "UpdateChatGPTEnterpriseIntegrationAccount" enabled
    And new "UpdateChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "id": "3e8a1f6b-9c2d-4b7e-8a5f-6d1c4e9b2a03", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a ChatGPT Enterprise integration account returns "OK" response
    Given operation "UpdateChatGPTEnterpriseIntegrationAccount" enabled
    And new "UpdateChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "id": "3e8a1f6b-9c2d-4b7e-8a5f-6d1c4e9b2a03", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/saas-integrations
  Scenario: Update a ChatGPT Enterprise integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateChatGPTEnterpriseIntegrationAccount" enabled
    And new "UpdateChatGPTEnterpriseIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "bearer_token", "token": "your-token"}, "dataflows": {"chatgpt-enterprise-agent-console": {"enabled": true}, "chatgpt-enterprise-cloud-cost-data": {"enabled": true}}, "name": "chatgpt-enterprise-acme", "settings": {"openai_org_id": "org-AbC123dEf456"}}, "id": "3e8a1f6b-9c2d-4b7e-8a5f-6d1c4e9b2a03", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
