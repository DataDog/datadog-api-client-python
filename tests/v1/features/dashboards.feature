@endpoint(dashboards)
Feature: Dashboards
  Interact with your dashboard lists through the API to make it easier to
  organize, find, and share all of your dashboards with your team and
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Dashboards" API

  @generated @skip
  Scenario: Create a new dashboard returns "Bad Request" response
    Given new "CreateDashboard" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a new dashboard returns "OK" response
    Given new "CreateDashboard" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a dashboard returns "Dashboards Not Found" response
    Given new "DeleteDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Dashboards Not Found

  @generated @skip
  Scenario: Delete a dashboard returns "OK" response
    Given new "DeleteDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a dashboard returns "Item Not Found" response
    Given new "GetDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Get a dashboard returns "OK" response
    Given new "GetDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all dashboards returns "OK" response
    Given new "ListDashboards" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a dashboard returns "Bad Request" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a dashboard returns "Item Not Found" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Item Not Found

  @generated @skip
  Scenario: Update a dashboard returns "OK" response
    Given new "UpdateDashboard" request
    And request contains "dashboard_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
