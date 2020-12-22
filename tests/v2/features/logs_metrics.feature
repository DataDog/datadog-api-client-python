@endpoint(logs-metrics)
Feature: Logs Metrics
  Manage configuration of [log-based
  metrics](https://app.datadoghq.com/logs/pipelines/generate-metrics) for
  your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsMetrics" API

  Scenario: Get all log-based metrics returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "ListLogsMetrics" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a log-based metric returns "OK" response
    Given new "CreateLogsMetric" request
    And body {"data": {"id": "{{ unique }}", "type": "logs_metrics", "attributes": {"compute": {"aggregation_type": "count"}}}}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Delete a log-based metric returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "DeleteLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric.data.id"
    When the request is sent
    Then the response status is 200 OK

  Scenario: Get a log-based metric returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "GetLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.filter.query" has the same value as "logs_metric.data.attributes.filter.query"

  Scenario: Update a log-based metric returns "OK" response
    Given there is a valid "logs_metric" in the system
    And new "UpdateLogsMetric" request
    And request contains "metric_id" parameter from "logs_metric.data.id"
    And body {"data": {"id": "{{ logs_metric.data.id }}", "type": "logs_metrics", "attributes": {"filter" : {"query": "{{ logs_metric.data.attributes.filter.query }}-updated"}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.filter.query" is equal to "{{ logs_metric.data.attributes.filter.query }}-updated"
