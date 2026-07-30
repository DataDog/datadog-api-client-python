@endpoint(integration-accounts) @endpoint(integration-accounts-v2)
Feature: Integration Accounts
  Manage accounts for Datadog integrations served by the Account Management
  Service (AMS). The account payload is strongly typed per integration and
  interface.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an integration account returns "Bad Request" response
    Given operation "CreateIntegrationAccount" enabled
    And new "CreateIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an integration account returns "Created" response
    Given operation "CreateIntegrationAccount" enabled
    And new "CreateIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create an integration account returns "Not Found" response
    Given operation "CreateIntegrationAccount" enabled
    And new "CreateIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an integration account returns "Bad Request" response
    Given operation "DeleteIntegrationAccount" enabled
    And new "DeleteIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an integration account returns "No Content" response
    Given operation "DeleteIntegrationAccount" enabled
    And new "DeleteIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete an integration account returns "Not Found" response
    Given operation "DeleteIntegrationAccount" enabled
    And new "DeleteIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an integration account returns "Bad Request" response
    Given operation "GetIntegrationAccount" enabled
    And new "GetIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an integration account returns "Not Found" response
    Given operation "GetIntegrationAccount" enabled
    And new "GetIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get an integration account returns "OK" response
    Given operation "GetIntegrationAccount" enabled
    And new "GetIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List integration accounts returns "Bad Request" response
    Given operation "ListIntegrationAccounts" enabled
    And new "ListIntegrationAccounts" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List integration accounts returns "Not Found" response
    Given operation "ListIntegrationAccounts" enabled
    And new "ListIntegrationAccounts" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List integration accounts returns "OK" response
    Given operation "ListIntegrationAccounts" enabled
    And new "ListIntegrationAccounts" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an integration account returns "Bad Request" response
    Given operation "UpdateIntegrationAccount" enabled
    And new "UpdateIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an integration account returns "Not Found" response
    Given operation "UpdateIntegrationAccount" enabled
    And new "UpdateIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update an integration account returns "OK" response
    Given operation "UpdateIntegrationAccount" enabled
    And new "UpdateIntegrationAccount" request
    And request contains "integration_id" parameter from "REPLACE.ME"
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK
