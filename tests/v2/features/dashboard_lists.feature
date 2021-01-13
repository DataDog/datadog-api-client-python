@endpoint(dashboard-lists)
Feature: Dashboard Lists
  Interact with your dashboard lists through the API to make it easier to
  organize, find, and share all of your dashboards with your team and
  organization. Note that you can add API v1 Dashboards to Dashboard Lists
  that you create with API v2.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardLists" API
    And request contains "dashboard_list_id" parameter from "<PATH>"

  @generated @skip
  Scenario: Delete items from a dashboard list returns "OK" response
    Given new "DeleteDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a Dashboard List returns "OK" response
    Given new "GetDashboardListItems" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Add Items to a Dashboard List returns "OK" response
    Given new "CreateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update items of a dashboard list returns "OK" response
    Given new "UpdateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete items from a dashboard list returns "Bad Request" response
    Given new "DeleteDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete items from a dashboard list returns "Not Found" response
    Given new "DeleteDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get a Dashboard List returns "Not Found" response
    Given new "GetDashboardListItems" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Add Items to a Dashboard List returns "Bad Request" response
    Given new "CreateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Add Items to a Dashboard List returns "Not Found" response
    Given new "CreateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update items of a dashboard list returns "Bad Request" response
    Given new "UpdateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update items of a dashboard list returns "Not Found" response
    Given new "UpdateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 404 Not Found
