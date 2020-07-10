@endpoint(metrics)
Feature: Metrics
  The metrics endpoint allows you to:  - Post metrics data so it can be
  graphed on Datadog’s dashboards - Query metrics from any time period
  **Note**: A graph can only contain a set number of points and as the
  timeframe over which a metric is viewed increases, aggregation between
  points occurs to stay below that set number.  Datadog has a soft limit of
  100 timeseries per host where a timeseries is defined as a unique
  combination of metric name and tag.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Metrics" API

  @generated @skip
  Scenario: Get active metrics list returns "OK" response
    Given new "ListActiveMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get metric metadata returns "OK" response
    Given new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit metric metadata returns "OK" response
    Given new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Query timeseries points returns "OK" response
    Given new "QueryMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Search metrics returns "OK" response
    Given new "ListMetrics" request
    When the request is sent
    Then the response status is 200 OK
