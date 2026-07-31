@endpoint(twilio-integration-accounts) @endpoint(twilio-integration-accounts-v2)
Feature: Twilio Integration Accounts
  Manage Twilio accounts for the Twilio integration, served by the Account
  Management Service (AMS). The account payload is strongly typed to Twilio;
  the Twilio interface and its authentication are modeled inline.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TwilioIntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Bad Request" response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Created" response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Not Found" response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "Bad Request" response
    Given operation "DeleteTwilioIntegrationAccount" enabled
    And new "DeleteTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "No Content" response
    Given operation "DeleteTwilioIntegrationAccount" enabled
    And new "DeleteTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "Not Found" response
    Given operation "DeleteTwilioIntegrationAccount" enabled
    And new "DeleteTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "Bad Request" response
    Given operation "GetTwilioIntegrationAccount" enabled
    And new "GetTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "Not Found" response
    Given operation "GetTwilioIntegrationAccount" enabled
    And new "GetTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "OK" response
    Given operation "GetTwilioIntegrationAccount" enabled
    And new "GetTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "Bad Request" response
    Given operation "ListTwilioIntegrationAccounts" enabled
    And new "ListTwilioIntegrationAccounts" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "Not Found" response
    Given operation "ListTwilioIntegrationAccounts" enabled
    And new "ListTwilioIntegrationAccounts" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "OK" response
    Given operation "ListTwilioIntegrationAccounts" enabled
    And new "ListTwilioIntegrationAccounts" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "Bad Request" response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "Not Found" response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "OK" response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "interface_id" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"interface": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}, "type": "twilio"}, "name": "twilio-prod"}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK
