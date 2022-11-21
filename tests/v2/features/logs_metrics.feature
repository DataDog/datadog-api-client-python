@endpoint(logs-metrics) @endpoint(logs-metrics-v2)
Feature: Logs Metrics
  Manage configuration of [log-based
  metrics](https://app.datadoghq.com/logs/pipelines/generate-metrics) for
  your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsMetrics" API

  @generated @skip @team:DataDog/logs-backend
  Scenario: Create a log-based metric returns "Bad Request" response
    Given new "CreateLogsMetric" request
    And body with value {"data": {"attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": true, "path": "@duration"}, "filter": {"query": "service:web* AND @http.status_code:[200 TO 299]"}, "group_by": [{"path": "@http.status_code", "tag_name": "status_code"}]}, "id": "logs.page.load.count", "type": "logs_metrics"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Create a log-based metric returns "Conflict" response
    Given new "CreateLogsMetric" request
    And body with value {"data": {"attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": true, "path": "@duration"}, "filter": {"query": "service:web* AND @http.status_code:[200 TO 299]"}, "group_by": [{"path": "@http.status_code", "tag_name": "status_code"}]}, "id": "logs.page.load.count", "type": "logs_metrics"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/logs-backend
  Scenario: Create a log-based metric returns "OK" response
    Given new "CreateLogsMetric" request
    And body with value {"data": {"id": "{{ unique }}", "type": "logs_metrics", "attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": true, "path":"@duration"}}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Delete a log-based metric returns "Not Found" response
    Given new "DeleteLogsMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-backend
  Scenario: Delete a log-based metric returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "DeleteLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Get a log-based metric returns "Not Found" response
    Given new "GetLogsMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-backend
  Scenario: Get a log-based metric returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "GetLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.filter.query" has the same value as "logs_metric.data.attributes.filter.query"

  @team:DataDog/logs-backend
  Scenario: Get all log-based metrics returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "ListLogsMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update a log-based metric returns "Bad Request" response
    Given new "UpdateLogsMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"compute": {"include_percentiles": true}, "filter": {"query": "service:web* AND @http.status_code:[200 TO 299]"}, "group_by": [{"path": "@http.status_code", "tag_name": "status_code"}]}, "type": "logs_metrics"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/logs-backend
  Scenario: Update a log-based metric returns "Not Found" response
    Given new "UpdateLogsMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"compute": {"include_percentiles": true}, "filter": {"query": "service:web* AND @http.status_code:[200 TO 299]"}, "group_by": [{"path": "@http.status_code", "tag_name": "status_code"}]}, "type": "logs_metrics"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/logs-backend
  Scenario: Update a log-based metric returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "UpdateLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric.data.id"
    And body with value {"data": {"type": "logs_metrics", "attributes": {"filter" : {"query": "{{ logs_metric.data.attributes.filter.query }}-updated"}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.filter.query" is equal to "{{ logs_metric.data.attributes.filter.query }}-updated"

  @team:DataDog/logs-backend
  Scenario: Update a log-based metric with include_percentiles field returns "OK" response
    Given there is a valid "logs_metric_percentile" in the system
    And new "UpdateLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric_percentile.data.id"
    And body with value {"data": {"type": "logs_metrics", "attributes": {"compute": {"include_percentiles": false}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.compute.include_percentiles" is false
