@endpoint(metrics)
Feature: Metrics
  The metrics endpoint allows you to:  - Post metrics data so it can be
  graphed on Datadog’s dashboards - Query metrics from any time period -
  Modify tag configurations for metrics  **Note**: A graph can only contain
  a set number of points and as the timeframe over which a metric is viewed
  increases, aggregation between points occurs to stay below that set
  number.  The Post, Patch, and Delete `manage_tags` API methods can only be
  performed by a user who has the `Manage Tags for Metrics` permission.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Metrics" API

  @generated @skip
  Scenario: Edit metric metadata returns "Bad Request" response
    Given new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Edit metric metadata returns "Not Found" response
    Given new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Edit metric metadata returns "OK" response
    Given new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get active metrics list returns "Bad Request" response
    Given new "ListActiveMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get active metrics list returns "OK" response
    Given new "ListActiveMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get metric metadata returns "Not Found" response
    Given new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get metric metadata returns "OK" response
    Given new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Query timeseries points returns "Bad Request" response
    Given new "QueryMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Query timeseries points returns "OK" response
    Given new "QueryMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Search metrics returns "Bad Request" response
    Given new "ListMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Search metrics returns "OK" response
    Given new "ListMetrics" request
    When the request is sent
    Then the response status is 200 OK
