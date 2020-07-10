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
  Scenario: Get all dashboards returns "OK" response
    Given new "ListDashboards" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a new dashboard returns "OK" response
    Given new "CreateDashboard" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a dashboard returns "OK" response
    Given new "DeleteDashboard" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a dashboard returns "OK" response
    Given new "GetDashboard" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a dashboard returns "OK" response
    Given new "UpdateDashboard" request
    And body {}
    When the request is sent
    Then the response status is 200 OK
