@endpoint(pagerduty-integration) @endpoint(pagerduty-integration-v1)
Feature: PagerDuty Integration
  Configure your [Datadog-PagerDuty
  integration](https://docs.datadoghq.com/integrations/pagerduty/) directly
  through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "PagerDutyIntegration" API

  @generated @skip @team:Datadog/web-integrations
  Scenario: Create a new service object returns "Bad Request" response
    Given new "CreatePagerDutyIntegrationService" request
    And body with value {"service_key": "", "service_name": ""}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Create a new service object returns "OK" response
    Given new "CreatePagerDutyIntegrationService" request
    And body with value {"service_key": "", "service_name": ""}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete a single service object returns "Item Not Found" response
    Given new "DeletePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Delete a single service object returns "No Content" response
    Given new "DeletePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get a single service object returns "Item Not Found" response
    Given new "GetPagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Get a single service object returns "OK" response
    Given new "GetPagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update a single service object returns "Bad Request" response
    Given new "UpdatePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    And body with value {"service_key": ""}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update a single service object returns "Item Not Found" response
    Given new "UpdatePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    And body with value {"service_key": ""}
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip @team:Datadog/web-integrations
  Scenario: Update a single service object returns "OK" response
    Given new "UpdatePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "REPLACE.ME"
    And body with value {"service_key": ""}
    When the request is sent
    Then the response status is 200 OK
