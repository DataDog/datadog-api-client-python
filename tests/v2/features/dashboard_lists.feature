@v2 @@endpoint(dashboard-lists) @todo
Feature: Dashboard Lists
  Interact with your dashboard lists through the API to make it easier to
  organize, find, and share all of your dashboards with your team and
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardLists" API

  Scenario: Delete items from a dashboard list returns "OK" response
    Given new "DeleteDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Get a Dashboard List returns "OK" response
    Given new "GetDashboardListItems" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Add Items to a Dashboard List returns "OK" response
    Given new "CreateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Update items of a dashboard list returns "OK" response
    Given new "UpdateDashboardListItems" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
