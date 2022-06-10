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

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Edit metric metadata returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"per_unit": "second", "type": "count", "unit": "byte"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Edit metric metadata returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"per_unit": "second", "type": "count", "unit": "byte"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Edit metric metadata returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateMetricMetadata" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"per_unit": "second", "type": "count", "unit": "byte"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Get active metrics list returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListActiveMetrics" request
    And request contains "from" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Get active metrics list returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListActiveMetrics" request
    And request contains "from" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Get metric metadata returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Get metric metadata returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "GetMetricMetadata" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Query timeseries points returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryMetrics" request
    And request contains "from" parameter from "REPLACE.ME"
    And request contains "to" parameter from "REPLACE.ME"
    And request contains "query" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Query timeseries points returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "QueryMetrics" request
    And request contains "from" parameter with value {{ timestamp("now - 1d") }}
    And request contains "to" parameter with value {{ timestamp("now") }}
    And request contains "query" parameter with value "system.cpu.idle{*}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Search metrics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListMetrics" request
    And request contains "q" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Search metrics returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And new "ListMetrics" request
    And request contains "q" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/metrics-aggregation
  Scenario: Submit deflate distribution points returns "Payload accepted" response
    Given new "SubmitDistributionPoints" request
    And body with value {"series": [{"metric": "system.load.1.dist", "points": [[{{ timestamp("now") }}, [1.0, 2.0]]]}]}
    And request contains "Content-Encoding" parameter with value "deflate"
    When the request is sent
    Then the response status is 202 Payload accepted

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit deflate metrics returns "Payload accepted" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "type": "gauge", "points": [[{{ timestamp("now") }}, 1.1]], "tags": ["test:{{ unique_alnum }}"]}]}
    And request contains "Content-Encoding" parameter with value "deflate"
    When the request is sent
    Then the response status is 202 Payload accepted

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/metrics-aggregation
  Scenario: Submit distribution points returns "Bad Request" response
    Given new "SubmitDistributionPoints" request
    And body with value {"series": [{"metric": "system.load.1.dist", "points": [[1475317847.0, 1.0]]}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/metrics-aggregation
  Scenario: Submit distribution points returns "Payload accepted" response
    Given new "SubmitDistributionPoints" request
    And body with value {"series": [{"metric": "system.load.1.dist", "points": [[{{ timestamp("now") }}, [1.0, 2.0]]]}]}
    When the request is sent
    Then the response status is 202 Payload accepted

  @generated @skip @team:DataDog/metrics-aggregation
  Scenario: Submit distribution points returns "Payload too large" response
    Given new "SubmitDistributionPoints" request
    And body with value {"series": [{"metric": "system.load.1", "points": [[1475317847.0, [1.0, 2.0]]]}]}
    When the request is sent
    Then the response status is 413 Payload too large

  @generated @skip @team:DataDog/metrics-aggregation
  Scenario: Submit distribution points returns "Request timeout" response
    Given new "SubmitDistributionPoints" request
    And body with value {"series": [{"metric": "system.load.1", "points": [[1475317847.0, [1.0, 2.0]]]}]}
    When the request is sent
    Then the response status is 408 Request timeout

  @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Bad Request" response
    Given new "SubmitMetrics" request
    And body with value "invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Payload accepted" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "type": "gauge", "points": [[{{ timestamp("now") }}, 1.1]], "tags": ["test:{{ unique_alnum }}"]}]}
    When the request is sent
    Then the response status is 202 Payload accepted

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Payload too large" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [[1475317847.0, 0.7]]}]}
    When the request is sent
    Then the response status is 413 Payload too large

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Request timeout" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [[1475317847.0, 0.7]]}]}
    When the request is sent
    Then the response status is 408 Request timeout
