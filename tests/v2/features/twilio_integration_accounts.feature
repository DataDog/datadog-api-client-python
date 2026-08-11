@endpoint(twilio-integration-accounts) @endpoint(twilio-integration-accounts-v2)
Feature: Twilio Integration Accounts
  Manage Twilio accounts for the Twilio `twilio` interface, served by the
  Account Management Service (AMS). Concrete, strongly typed CRUD operations
  for the single Twilio interface.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TwilioIntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Bad Request" response
    Given operation "CreateTwilioAccount" enabled
    And new "CreateTwilioAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Created" response
    Given operation "CreateTwilioAccount" enabled
    And new "CreateTwilioAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Not Found" response
    Given operation "CreateTwilioAccount" enabled
    And new "CreateTwilioAccount" request
    And body with value {"data": {"attributes": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "Bad Request" response
    Given operation "DeleteTwilioAccount" enabled
    And new "DeleteTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "No Content" response
    Given operation "DeleteTwilioAccount" enabled
    And new "DeleteTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "Not Found" response
    Given operation "DeleteTwilioAccount" enabled
    And new "DeleteTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "Bad Request" response
    Given operation "GetTwilioAccount" enabled
    And new "GetTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "Not Found" response
    Given operation "GetTwilioAccount" enabled
    And new "GetTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "OK" response
    Given operation "GetTwilioAccount" enabled
    And new "GetTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "Bad Request" response
    Given operation "ListTwilioAccounts" enabled
    And new "ListTwilioAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "Not Found" response
    Given operation "ListTwilioAccounts" enabled
    And new "ListTwilioAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "OK" response
    Given operation "ListTwilioAccounts" enabled
    And new "ListTwilioAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "Bad Request" response
    Given operation "UpdateTwilioAccount" enabled
    And new "UpdateTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "Not Found" response
    Given operation "UpdateTwilioAccount" enabled
    And new "UpdateTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "OK" response
    Given operation "UpdateTwilioAccount" enabled
    And new "UpdateTwilioAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "api_key_token": "your-api-key-secret", "type": "basic"}, "dataflows": [{"enabled": true, "id": "twilio-messages-logs"}], "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK
