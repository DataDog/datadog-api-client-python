@endpoint(dashboard-lists) @endpoint(dashboard-lists-v1)
Feature: Dashboard Lists
  Interact with your dashboard lists through the API to organize, find, and
  share all of your dashboards with your team and organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardLists" API

  @generated @skip @team:DataDog/dashboards
  Scenario: Create a dashboard list returns "Bad Request" response
    Given new "CreateDashboardList" request
    And body with value {"name": "My Dashboard"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards
  Scenario: Create a dashboard list returns "OK" response
    Given new "CreateDashboardList" request
    And body with value {"name": "{{ unique }}"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"

  @team:DataDog/dashboards
  Scenario: Delete a dashboard list returns "Not Found" response
    Given new "DeleteDashboardList" request
    And request contains "list_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Delete a dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And new "DeleteDashboardList" request
    And request contains "list_id" parameter from "dashboard_list.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "deleted_dashboard_list_id" has the same value as "dashboard_list.id"

  @team:DataDog/dashboards
  Scenario: Get a dashboard list returns "Not Found" response
    Given new "GetDashboardList" request
    And request contains "list_id" parameter with value 0
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Get a dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And new "GetDashboardList" request
    And request contains "list_id" parameter from "dashboard_list.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "id" has the same value as "dashboard_list.id"
    And the response "name" has the same value as "dashboard_list.name"

  @team:DataDog/dashboards
  Scenario: Get all dashboard lists returns "OK" response
    Given new "ListDashboardLists" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dashboards
  Scenario: Update a dashboard list returns "Bad Request" response
    Given new "UpdateDashboardList" request
    And request contains "list_id" parameter from "REPLACE.ME"
    And body with value {"name": "My Dashboard"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/dashboards
  Scenario: Update a dashboard list returns "Not Found" response
    Given new "UpdateDashboardList" request
    And request contains "list_id" parameter with value 0
    And body with value {"name": "Not found"}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/dashboards
  Scenario: Update a dashboard list returns "OK" response
    Given there is a valid "dashboard_list" in the system
    And new "UpdateDashboardList" request
    And request contains "list_id" parameter from "dashboard_list.id"
    And body with value {"name": "updated {{unique}}"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "updated {{ unique }}"
