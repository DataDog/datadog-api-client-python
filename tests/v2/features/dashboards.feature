@endpoint(dashboards) @endpoint(dashboards-v2)
Feature: Dashboards
  Get usage statistics for the dashboards in your organization, including
  view counts, last-edit times, widget counts, and quality scores. See the
  [Dashboards documentation](https://docs.datadoghq.com/dashboards/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Dashboards" API

  @generated @skip @team:DataDog/dashboards-backend
  Scenario: Get usage stats for a dashboard returns "Bad Request" response
    Given operation "GetDashboardUsage" enabled
    And new "GetDashboardUsage" request
    And request contains "dashboard_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get usage stats for a dashboard returns "Not Found" response
    Given operation "GetDashboardUsage" enabled
    And new "GetDashboardUsage" request
    And request contains "dashboard_id" parameter with value "xxx-xxx-xxx"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get usage stats for a dashboard returns "OK" response
    Given operation "GetDashboardUsage" enabled
    And there is a valid "dashboard" in the system
    And new "GetDashboardUsage" request
    And request contains "dashboard_id" parameter from "dashboard.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "dashboard.id"
    And the response "data.type" is equal to "dashboards-usages"
    And the response "data.attributes.title" has the same value as "dashboard.title"
    And the response "data.attributes" has field "org_id"
    And the response "data.attributes" has field "total_views"
    And the response "data.attributes.author" has field "handle"

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get usage stats for all dashboards returns "Bad Request" response
    Given operation "ListDashboardsUsage" enabled
    And new "ListDashboardsUsage" request
    And request contains "page[limit]" parameter with value 10000
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/dashboards-backend
  Scenario: Get usage stats for all dashboards returns "OK" response
    Given operation "ListDashboardsUsage" enabled
    And there is a valid "dashboard" in the system
    And new "ListDashboardsUsage" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "dashboards-usages"
    And the response "data[0]" has field "id"
    And the response "data[0].attributes" has field "org_id"
    And the response "meta.page.type" is equal to "offset_limit"
    And the response "meta.page" has field "total"
    And the response "links" has field "self"

  @replay-only @skip-validation @team:DataDog/dashboards-backend @with-pagination
  Scenario: Get usage stats for all dashboards returns "OK" response with pagination
    Given operation "ListDashboardsUsage" enabled
    And new "ListDashboardsUsage" request
    And request contains "page[limit]" parameter with value 500
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 590 items
