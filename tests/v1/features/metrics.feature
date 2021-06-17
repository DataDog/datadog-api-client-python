@endpoint(metrics) @endpoint(metrics-v1)
Feature: Metrics
  The metrics endpoint allows you to:  - Post metrics data so it can be
  graphed on Datadog’s dashboards - Query metrics from any time period -
  Modify tag configurations for metrics - View tags and volumes for metrics
  **Note**: A graph can only contain a set number of points and as the
  timeframe over which a metric is viewed increases, aggregation between
  points occurs to stay below that set number.  The Post, Patch, and Delete
  `manage_tags` API methods can only be performed by a user who has the
  `Manage Tags for Metrics` permission.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "Metrics" API

  @generated @skip
  Scenario: Edit metric metadata returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body with value {"description": null, "per_unit": "second", "short_name": null, "statsd_interval": null, "type": "count", "unit": "byte"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Edit metric metadata returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body with value {"description": null, "per_unit": "second", "short_name": null, "statsd_interval": null, "type": "count", "unit": "byte"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Edit metric metadata returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    And body with value {"description": null, "per_unit": "second", "short_name": null, "statsd_interval": null, "type": "count", "unit": "byte"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get active metrics list returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListActiveMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get active metrics list returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListActiveMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get metric metadata returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get metric metadata returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Query timeseries points returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-python
  Scenario: Query timeseries points returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryMetrics" request
    And request contains "from" parameter with value {{ timestamp("now - 1d") }}
    And request contains "to" parameter with value {{ timestamp("now") }}
    And request contains "query" parameter with value "system.cpu.idle{*}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Search metrics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListMetrics" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Search metrics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @skip
  Scenario: Submit metrics returns "Bad Request" response
    Given new "SubmitMetrics" request
    And body with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  Scenario: Submit metrics returns "Payload accepted" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "type": "gauge", "points": [[{{ timestamp("now") }}, 1.1]], "tags": ["test:{{ unique_alnum }}"]}]}
    When the request is sent
    Then the response status is 202 Payload accepted

  @generated @skip
  Scenario: Submit metrics returns "Payload too large" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [[1475317847, 0.7]]}]}
    When the request is sent
    Then the response status is 413 Payload too large

  @generated @skip
  Scenario: Submit metrics returns "Request timeout" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [[1475317847, 0.7]]}]}
    When the request is sent
    Then the response status is 408 Request timeout
