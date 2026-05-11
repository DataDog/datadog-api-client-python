@endpoint(web-integrations) @endpoint(web-integrations-v2)
Feature: Web Integrations
  Manage web integration accounts programmatically through the Datadog API.
  See the [Web Integrations page](https://app.datadoghq.com/integrations)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "WebIntegrations" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a web integration account returns "Bad Request" response
    Given operation "CreateWebIntegrationAccount" enabled
    And new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a web integration account returns "CREATED" response
    Given operation "CreateWebIntegrationAccount" enabled
    And new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a web integration account returns "Not Found" response
    Given operation "CreateWebIntegrationAccount" enabled
    And new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a web integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateWebIntegrationAccount" enabled
    And new "CreateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a web integration account returns "Bad Request" response
    Given operation "DeleteWebIntegrationAccount" enabled
    And new "DeleteWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a web integration account returns "Not Found" response
    Given operation "DeleteWebIntegrationAccount" enabled
    And new "DeleteWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a web integration account returns "OK" response
    Given operation "DeleteWebIntegrationAccount" enabled
    And new "DeleteWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a web integration account returns "Bad Request" response
    Given operation "GetWebIntegrationAccount" enabled
    And new "GetWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a web integration account returns "Not Found" response
    Given operation "GetWebIntegrationAccount" enabled
    And new "GetWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a web integration account returns "OK" response
    Given operation "GetWebIntegrationAccount" enabled
    And new "GetWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List web integration accounts returns "Bad Request" response
    Given operation "ListWebIntegrationAccounts" enabled
    And new "ListWebIntegrationAccounts" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List web integration accounts returns "Not Found" response
    Given operation "ListWebIntegrationAccounts" enabled
    And new "ListWebIntegrationAccounts" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List web integration accounts returns "OK" response
    Given operation "ListWebIntegrationAccounts" enabled
    And new "ListWebIntegrationAccounts" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a web integration account returns "Bad Request" response
    Given operation "UpdateWebIntegrationAccount" enabled
    And new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a web integration account returns "Not Found" response
    Given operation "UpdateWebIntegrationAccount" enabled
    And new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a web integration account returns "OK" response
    Given operation "UpdateWebIntegrationAccount" enabled
    And new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a web integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateWebIntegrationAccount" enabled
    And new "UpdateWebIntegrationAccount" request
    And request contains "integration_name" parameter from "REPLACE.ME"
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "my-databricks-account", "secrets": {"client_secret": "my-client-secret"}, "settings": {"workspace_url": "https://example.azuredatabricks.net"}}, "type": "Account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
