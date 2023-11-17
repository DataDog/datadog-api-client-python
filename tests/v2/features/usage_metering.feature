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

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get Monthly Cost Attribution returns "Bad Request" response
    Given operation "GetMonthlyCostAttribution" enabled
    And new "GetMonthlyCostAttribution" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_month" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "fields" parameter with value "not_a_product"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get Monthly Cost Attribution returns "OK" response
    Given operation "GetMonthlyCostAttribution" enabled
    And new "GetMonthlyCostAttribution" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_month" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "fields" parameter with value "infra_host_total_cost"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get active billing dimensions for cost attribution returns "Bad Request" response
    Given operation "GetActiveBillingDimensions" enabled
    And new "GetActiveBillingDimensions" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get active billing dimensions for cost attribution returns "OK" response
    Given operation "GetActiveBillingDimensions" enabled
    And new "GetActiveBillingDimensions" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get cost across multi-org account returns "Bad Request" response
    Given new "GetCostByOrg" request
    And request contains "start_month" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get cost across multi-org account returns "OK" response
    Given new "GetCostByOrg" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get estimated cost across your account returns "Bad Request" response
    Given new "GetEstimatedCostByOrg" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get estimated cost across your account returns "OK" response
    Given new "GetEstimatedCostByOrg" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get historical cost across your account returns "Bad Request" response
    Given new "GetHistoricalCostByOrg" request
    And request contains "start_month" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get historical cost across your account returns "OK" response
    Given new "GetHistoricalCostByOrg" request
    And request contains "start_month" parameter with value "{{ timeISO('now - 2M') }}"
    And request contains "view" parameter with value "sub-org"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage by product family returns "Bad Request" response
    Given new "GetHourlyUsage" request
    And request contains "filter[timestamp][start]" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "filter[product_families]" parameter with value "infra_hosts"
    And request contains "filter[timestamp][end]" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage by product family returns "OK" response
    Given new "GetHourlyUsage" request
    And request contains "filter[timestamp][start]" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "filter[product_families]" parameter with value "infra_hosts"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "usage_timeseries"
    And the response "data[0].attributes.region" is equal to "us"

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Application Security returns "Bad Request" response
    Given new "GetUsageApplicationSecurityMonitoring" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Lambda Traced Invocations returns "Bad Request" response
    Given new "GetUsageLambdaTracedInvocations" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for Observability Pipelines returns "Bad Request" response
    Given new "GetUsageObservabilityPipelines" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 3d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 5d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for application security returns "Bad Request" response
    Given new "GetUsageApplicationSecurityMonitoring" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for application security returns "OK" response
    Given new "GetUsageApplicationSecurityMonitoring" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "usage_timeseries"
    And the response "data[0].attributes.product_family" is equal to "app-sec"

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for lambda traced invocations returns "Bad Request" response
    Given new "GetUsageLambdaTracedInvocations" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for lambda traced invocations returns "OK" response
    Given new "GetUsageLambdaTracedInvocations" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "usage_timeseries"
    And the response "data[0].attributes.product_family" is equal to "lambda-traced-invocations"

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for observability pipelines returns "Bad Request" response
    Given new "GetUsageObservabilityPipelines" request
    And request contains "start_hr" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/red-zone-revenue-query
  Scenario: Get hourly usage for observability pipelines returns "OK" response
    Given new "GetUsageObservabilityPipelines" request
    And request contains "start_hr" parameter with value "{{ timeISO('now - 5d') }}"
    And request contains "end_hr" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "usage_timeseries"
    And the response "data[0].attributes.product_family" is equal to "observability-pipelines"

  @generated @skip @team:DataDog/red-zone-revenue-query
  Scenario: Get projected cost across your account returns "Bad Request" response
    Given new "GetProjectedCost" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: Get projected cost across your account returns "OK" response
    Given new "GetProjectedCost" request
    And request contains "view" parameter with value "sub-org"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/red-zone-revenue-query
  Scenario: GetEstimatedCostByOrg with both start_month and start_date returns "Bad Request" response
    Given new "GetEstimatedCostByOrg" request
    And request contains "view" parameter with value "sub-org"
    And request contains "start_month" parameter with value "{{ timeISO('now') }}"
    And request contains "start_date" parameter with value "{{ timeISO('now - 3d') }}"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/red-zone-revenue-query
  Scenario: GetEstimatedCostByOrg with start_month returns "OK" response
    Given new "GetEstimatedCostByOrg" request
    And request contains "view" parameter with value "sub-org"
    And request contains "start_month" parameter with value "{{ timeISO('now') }}"
    When the request is sent
    Then the response status is 200 OK
