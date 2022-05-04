@endpoint(usage-metering) @endpoint(usage-metering-v2)
Feature: Usage Metering
  The usage metering API allows you to get hourly, daily, and monthly usage
  across multiple facets of Datadog. This API is available to all Pro and
  Enterprise customers. Usage is only accessible for [parent-level organizat
  ions](https://docs.datadoghq.com/account_management/multi_organization/).
  **Note**: Usage data is delayed by up to 72 hours from when it was
  incurred. It is retained for 15 months.  You can retrieve up to 24 hours
  of hourly usage data for multiple organizations, and up to two months of
  hourly usage data for a single organization in one request.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "UsageMetering" API

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get Cost Across Multi-Org Account returns "Bad Request" response
    Given new "GetCostByOrg" request
    And request contains "start_month" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get Cost Across Multi-Org Account returns "OK" response
    Given new "GetCostByOrg" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Observability Pipelines returns "Bad Request" response
    Given new "GetUsageObservabilityPipelines" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Observability Pipelines returns "OK" response
    Given new "GetUsageObservabilityPipelines" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK
