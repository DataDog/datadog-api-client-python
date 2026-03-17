@endpoint(integration-accounts) @endpoint(integration-accounts-v2)
Feature: Integration Accounts
  Configure and manage third-party integrations with Datadog. This API
  provides a unified interface for managing integration accounts across
  various external services.  Each integration has its own unique schema
  that defines the required settings and secrets. Before creating or
  updating an account, use the schema endpoint to retrieve the specific
  requirements, field types, validation rules, and available configuration
  options for your integration.  **Note**: This API manages integration
  account configurations only. It does not support Grace Resources,
  Reference Tables, or Custom Queries CRUD operations. For those features,
  refer to each integration's dedicated documentation.  Supported
  Integrations:   -
  [Twilio](https://docs.datadoghq.com/integrations/twilio/)   -
  [Snowflake](https://docs.datadoghq.com/integrations/snowflake-web/)   -
  [Databricks](https://docs.datadoghq.com/integrations/databricks/)

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "IntegrationAccounts" API

  @generated @skip @team:DataDog/web-integrations
  Scenario: Create integration account returns "Bad Request: The request body is malformed or the integration name format is invalid." response
    Given new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account", "secrets": {"api_key_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}, "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "alerts": true, "api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "call_summaries": true, "ccm_enabled": true, "censor_logs": true, "events": true, "messages": true}}, "type": "Account"}}
    When the request is sent
    Then the response status is 400 Bad Request: The request body is malformed or the integration name format is invalid.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Create integration account returns "Created: The account was successfully created." response
    Given new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account", "secrets": {"api_key_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}, "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "alerts": true, "api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "call_summaries": true, "ccm_enabled": true, "censor_logs": true, "events": true, "messages": true}}, "type": "Account"}}
    When the request is sent
    Then the response status is 201 Created: The account was successfully created.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Create integration account returns "Not Found: The integration does not exist." response
    Given new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account", "secrets": {"api_key_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}, "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "alerts": true, "api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "call_summaries": true, "ccm_enabled": true, "censor_logs": true, "events": true, "messages": true}}, "type": "Account"}}
    When the request is sent
    Then the response status is 404 Not Found: The integration does not exist.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Create integration account returns "Unprocessable Entity: The account configuration does not match the integration schema." response
    Given new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account", "secrets": {"api_key_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}, "settings": {"account_sid": "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "alerts": true, "api_key": "SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "call_summaries": true, "ccm_enabled": true, "censor_logs": true, "events": true, "messages": true}}, "type": "Account"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity: The account configuration does not match the integration schema.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Delete integration account returns "Bad Request: The integration name or account ID format is invalid." response
    Given new "DeleteWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request: The integration name or account ID format is invalid.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Delete integration account returns "Not Found: The integration or account does not exist." response
    Given new "DeleteWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found: The integration or account does not exist.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Delete integration account returns "OK: The account was successfully deleted." response
    Given new "DeleteWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK: The account was successfully deleted.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Get account schema for an integration returns "Bad Request: The integration name format is invalid." response
    Given new "GetWebIntegrationAccountSchema" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request: The integration name format is invalid.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Get account schema for an integration returns "Not Found: The integration does not exist or has no schema available." response
    Given new "GetWebIntegrationAccountSchema" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found: The integration does not exist or has no schema available.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Get account schema for an integration returns "OK: The JSON schema for the integration's account configuration." response
    Given new "GetWebIntegrationAccountSchema" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK: The JSON schema for the integration's account configuration.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Get integration account returns "Bad Request: The integration name or account ID format is invalid." response
    Given new "GetWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request: The integration name or account ID format is invalid.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Get integration account returns "Not Found: The integration or account does not exist." response
    Given new "GetWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found: The integration or account does not exist.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Get integration account returns "OK: The account details for the specified integration." response
    Given new "GetWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK: The account details for the specified integration.

  @generated @skip @team:DataDog/web-integrations
  Scenario: List integration accounts returns "Bad Request: The integration name format is invalid." response
    Given new "ListWebIntegrationAccounts" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request: The integration name format is invalid.

  @generated @skip @team:DataDog/web-integrations
  Scenario: List integration accounts returns "Not Found: The integration does not exist." response
    Given new "ListWebIntegrationAccounts" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found: The integration does not exist.

  @generated @skip @team:DataDog/web-integrations
  Scenario: List integration accounts returns "OK: List of all accounts for the specified integration." response
    Given new "ListWebIntegrationAccounts" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK: List of all accounts for the specified integration.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Update integration account returns "Bad Request: The request body is malformed or the integration name/account ID format is invalid." response
    Given new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account (Updated)", "secrets": {"api_key_token": "new_secret_token_value"}, "settings": {"ccm_enabled": true, "events": true, "messages": false}}, "type": "Account"}}
    When the request is sent
    Then the response status is 400 Bad Request: The request body is malformed or the integration name/account ID format is invalid.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Update integration account returns "Not Found: The integration or account does not exist." response
    Given new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account (Updated)", "secrets": {"api_key_token": "new_secret_token_value"}, "settings": {"ccm_enabled": true, "events": true, "messages": false}}, "type": "Account"}}
    When the request is sent
    Then the response status is 404 Not Found: The integration or account does not exist.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Update integration account returns "OK: The account was successfully updated." response
    Given new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account (Updated)", "secrets": {"api_key_token": "new_secret_token_value"}, "settings": {"ccm_enabled": true, "events": true, "messages": false}}, "type": "Account"}}
    When the request is sent
    Then the response status is 200 OK: The account was successfully updated.

  @generated @skip @team:DataDog/web-integrations
  Scenario: Update integration account returns "Unprocessable Entity: The account configuration does not match the integration schema." response
    Given new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "My Production Account (Updated)", "secrets": {"api_key_token": "new_secret_token_value"}, "settings": {"ccm_enabled": true, "events": true, "messages": false}}, "type": "Account"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity: The account configuration does not match the integration schema.
