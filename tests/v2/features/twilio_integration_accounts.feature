@endpoint(twilio-integration-accounts) @endpoint(twilio-integration-accounts-v2)
Feature: Twilio Integration Accounts
  Manage your Datadog Twilio integration accounts directly through the
  Datadog API. Create, update, and delete accounts, configure authentication
  and settings, and enable or disable dataflows such as message logs, event
  logs, alerts, call summaries, and Cloud Cost Management metrics. See the
  [Twilio integration page](https://docs.datadoghq.com/integrations/twilio/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TwilioIntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Bad Request" response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Created" response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "Not Found" response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Twilio integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateTwilioIntegrationAccount" enabled
    And new "CreateTwilioIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "Bad Request" response
    Given operation "DeleteTwilioIntegrationAccount" enabled
    And new "DeleteTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "Not Found" response
    Given operation "DeleteTwilioIntegrationAccount" enabled
    And new "DeleteTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Twilio integration account returns "OK" response
    Given operation "DeleteTwilioIntegrationAccount" enabled
    And new "DeleteTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "Bad Request" response
    Given operation "GetTwilioIntegrationAccount" enabled
    And new "GetTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "Not Found" response
    Given operation "GetTwilioIntegrationAccount" enabled
    And new "GetTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Twilio integration account returns "OK" response
    Given operation "GetTwilioIntegrationAccount" enabled
    And new "GetTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "Bad Request" response
    Given operation "ListTwilioIntegrationAccounts" enabled
    And new "ListTwilioIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "Not Found" response
    Given operation "ListTwilioIntegrationAccounts" enabled
    And new "ListTwilioIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Twilio integration accounts returns "OK" response
    Given operation "ListTwilioIntegrationAccounts" enabled
    And new "ListTwilioIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "Bad Request" response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "Not Found" response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "OK" response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Twilio integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateTwilioIntegrationAccount" enabled
    And new "UpdateTwilioIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "basic", "password": "your-password", "username": "datadog"}, "dataflows": {"twilio-alerts-logs": {"enabled": true}, "twilio-call-summaries-logs": {"enabled": true}, "twilio-cloud-cost-metrics": {"enabled": true}, "twilio-events-logs": {"enabled": true}, "twilio-messages-logs": {"enabled": true}}, "name": "twilio-prod", "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "censor_logs": true}}, "id": "953a0060-81ec-4221-aed4-d4733b59cd96", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
