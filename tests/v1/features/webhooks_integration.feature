@endpoint(webhooks-integration) @endpoint(webhooks-integration-v1)
Feature: Webhooks Integration
  Configure your Datadog-Webhooks integration directly through the Datadog
  API. For more information about the Datadog-Webhooks integration, see the
  [integration page](https://docs.datadoghq.com/integrations/webhooks).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "WebhooksIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a custom variable returns "Bad Request" response
    Given new "CreateWebhooksIntegrationCustomVariable" request
    And body with value {"is_secret": true, "name": "CUSTOM_VARIABLE_NAME", "value": "CUSTOM_VARIABLE_VALUE"}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Create a custom variable returns "OK" response
    Given new "CreateWebhooksIntegrationCustomVariable" request
    And body with value {"is_secret": true, "name": "{{ unique_upper_alnum }}", "value": "CUSTOM_VARIABLE_VALUE"}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create a webhooks integration returns "Bad Request" response
    Given new "CreateWebhooksIntegration" request
    And body with value {"custom_headers": null, "encode_as": "json", "name": "WEBHOOK_NAME", "payload": null, "url": "https://example.com/webhook"}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Create a webhooks integration returns "OK" response
    Given new "CreateWebhooksIntegration" request
    And body with value {"name": "{{ unique }}", "url": "https://example.com/webhook"}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a custom variable returns "Item Not Found" response
    Given new "DeleteWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Delete a custom variable returns "OK" response
    Given there is a valid "webhook_custom_variable" in the system
    And new "DeleteWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "webhook_custom_variable.name"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete a webhook returns "Item Not Found" response
    Given new "DeleteWebhooksIntegration" request
    And request contains "webhook_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Delete a webhook returns "OK" response
    Given there is a valid "webhook" in the system
    And new "DeleteWebhooksIntegration" request
    And request contains "webhook_name" parameter from "webhook.name"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a custom variable returns "Bad Request" response
    Given new "GetWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a custom variable returns "Item Not Found" response
    Given new "GetWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a custom variable returns "OK" response
    Given new "GetWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a webhook integration returns "Bad Request" response
    Given new "GetWebhooksIntegration" request
    And request contains "webhook_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get a webhook integration returns "Item Not Found" response
    Given new "GetWebhooksIntegration" request
    And request contains "webhook_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Get a webhook integration returns "OK" response
    Given there is a valid "webhook" in the system
    And new "GetWebhooksIntegration" request
    And request contains "webhook_name" parameter from "webhook.name"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a custom variable returns "Bad Request" response
    Given new "UpdateWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "REPLACE.ME"
    And body with value {"name": "CUSTOM_VARIABLE_NAME", "value": "CUSTOM_VARIABLE_VALUE"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a custom variable returns "Item Not Found" response
    Given new "UpdateWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "REPLACE.ME"
    And body with value {"name": "CUSTOM_VARIABLE_NAME", "value": "CUSTOM_VARIABLE_VALUE"}
    When the request is sent
    Then the response status is 404 Item Not Found

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Update a custom variable returns "OK" response
    Given there is a valid "webhook_custom_variable" in the system
    And new "UpdateWebhooksIntegrationCustomVariable" request
    And request contains "custom_variable_name" parameter from "webhook_custom_variable.name"
    And body with value {"value": "variable-updated"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a webhook returns "Bad Request" response
    Given new "UpdateWebhooksIntegration" request
    And request contains "webhook_name" parameter from "REPLACE.ME"
    And body with value {"encode_as": "json", "name": "WEBHOOK_NAME", "payload": null, "url": "https://example.com/webhook"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update a webhook returns "Item Not Found" response
    Given new "UpdateWebhooksIntegration" request
    And request contains "webhook_name" parameter from "REPLACE.ME"
    And body with value {"encode_as": "json", "name": "WEBHOOK_NAME", "payload": null, "url": "https://example.com/webhook"}
    When the request is sent
    Then the response status is 404 Item Not Found

  @skip-terraform-config @team:Datadog/collaboration-integrations
  Scenario: Update a webhook returns "OK" response
    Given there is a valid "webhook" in the system
    And new "UpdateWebhooksIntegration" request
    And request contains "webhook_name" parameter from "webhook.name"
    And body with value {"url": "https://example.com/webhook-updated"}
    When the request is sent
    Then the response status is 200 OK
