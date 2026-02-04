@endpoint(dashboards) @endpoint(dashboards-v2)
Feature: Dashboards
  Interact with your dashboards through the API to search and retrieve
  dashboards.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Dashboards" API
    And operation "SearchDashboards" enabled
    And new "SearchDashboards" request

  @generated @skip @team:DataDog/notebooks-backend
  Scenario: Search dashboards returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/notebooks-backend
  Scenario: Search dashboards returns "OK" response
    When the request is sent
    Then the response status is 200 OK
