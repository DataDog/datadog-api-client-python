@endpoint(dashboard-lists)
Feature: Dashboard Lists
  This endpoint is deprecated. Use the [new dashboard list
  endpoint](https://docs.datadoghq.com/api/v2/dashboard-lists/) instead.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardLists" API

  @generated @skip
  Scenario: Get all dashboard lists returns "OK" response
    Given new "ListDashboardLists" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a dashboard list returns "OK" response
    Given new "CreateDashboardList" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a dashboard list returns "OK" response
    Given new "DeleteDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a dashboard list returns "OK" response
    Given new "GetDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a dashboard list returns "OK" response
    Given new "UpdateDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
