@endpoint(dashboard-sharing) @endpoint(dashboard-sharing-v2)
Feature: Dashboard Sharing
  Manage dashboard sharing configurations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DashboardSharing" API
    And operation "ListSharedDashboardsByDashboardId" enabled
    And new "ListSharedDashboardsByDashboardId" request

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List shared dashboards for a dashboard returns "Dashboard Not Found" response
    Given request contains "dashboard_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Dashboard Not Found

  @generated @skip @team:DataDog/reporting-and-sharing
  Scenario: List shared dashboards for a dashboard returns "OK" response
    Given request contains "dashboard_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
