@endpoint(dashboard-lists)
Feature: Dashboard Lists
  Interact with your dashboard lists through the API to organize, find, and
  share all of your dashboards with your team and organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardLists" API

  @generated @skip
  Scenario: Create a dashboard list returns "Bad Request" response
    Given new "CreateDashboardList" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a dashboard list returns "OK" response
    Given new "CreateDashboardList" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a dashboard list returns "Not Found" response
    Given new "DeleteDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Delete a dashboard list returns "OK" response
    Given new "DeleteDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a dashboard list returns "Not Found" response
    Given new "GetDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get a dashboard list returns "OK" response
    Given new "GetDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all dashboard lists returns "OK" response
    Given new "ListDashboardLists" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a dashboard list returns "Bad Request" response
    Given new "UpdateDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a dashboard list returns "Not Found" response
    Given new "UpdateDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update a dashboard list returns "OK" response
    Given new "UpdateDashboardList" request
    And request contains "list_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
