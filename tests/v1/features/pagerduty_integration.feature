@endpoint(pagerduty-integration)
Feature: PagerDuty Integration
  Configure your [Datadog-PagerDuty
  integration](https://docs.datadoghq.com/api/?lang=bash#integration-
  pagerduty) directly through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "PagerDutyIntegration" API

  @generated @skip
  Scenario: Create a new service object returns "Bad Request" response
    Given new "CreatePagerDutyIntegrationService" request
    And body {"service_key": "", "service_name": ""}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a new service object returns "OK" response
    Given new "CreatePagerDutyIntegrationService" request
    And body {"service_key": "", "service_name": ""}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip
  Scenario: Delete a single service object returns "Item Not Found" response
    Given new "DeletePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Delete a single service object returns "OK" response
    Given new "DeletePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a single service object returns "Item Not Found" response
    Given new "GetPagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Get a single service object returns "OK" response
    Given new "GetPagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a single service object returns "Bad Request" response
    Given new "UpdatePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    And body {"service_key": ""}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a single service object returns "Item Not Found" response
    Given new "UpdatePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    And body {"service_key": ""}
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Update a single service object returns "OK" response
    Given new "UpdatePagerDutyIntegrationService" request
    And request contains "service_name" parameter from "<PATH>"
    And body {"service_key": ""}
    When the request is sent
    Then the response status is 200 OK
