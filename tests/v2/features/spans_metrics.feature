@endpoint(spans-metrics) @endpoint(spans-metrics-v2)
Feature: Spans Metrics
  Manage configuration of [span-based
  metrics](https://app.datadoghq.com/apm/traces/generate-metrics) for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SpansMetrics" API

  @generated @skip @team:DataDog/apm
  Scenario: Create a span-based metric returns "Bad Request" response
    Given new "CreateSpansMetric" request
    And body with value {"data": {"attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": false, "path": "@duration"}, "filter": {"query": "@http.status_code:200 service:my-service"}, "group_by": [{"path": "resource_name", "tag_name": "resource_name"}]}, "id": "my.metric", "type": "spans_metrics"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/apm
  Scenario: Create a span-based metric returns "Conflict" response
    Given new "CreateSpansMetric" request
    And body with value {"data": {"attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": false, "path": "@duration"}, "filter": {"query": "@http.status_code:200 service:my-service"}, "group_by": [{"path": "resource_name", "tag_name": "resource_name"}]}, "id": "my.metric", "type": "spans_metrics"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/apm
  Scenario: Create a span-based metric returns "OK" response
    Given new "CreateSpansMetric" request
    And body with value {"data": {"attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": false, "path": "@duration"}, "filter": {"query": "@http.status_code:200 service:my-service"}, "group_by": [{"path": "resource_name", "tag_name": "resource_name"}]}, "id": "{{ unique_alnum }}", "type": "spans_metrics"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "unique_alnum"
    And the response "data.type" is equal to "spans_metrics"
    And the response "data.attributes.compute.aggregation_type" is equal to "distribution"

  @generated @skip @team:DataDog/apm
  Scenario: Delete a span-based metric returns "Not Found" response
    Given new "DeleteSpansMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/apm
  Scenario: Delete a span-based metric returns "OK" response
    Given there is a valid "spans_metric" in the system
    And new "DeleteSpansMetric" request
    And request contains "metric_id" parameter from "spans_metric.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/apm
  Scenario: Get a span-based metric returns "Not Found" response
    Given new "GetSpansMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/apm
  Scenario: Get a span-based metric returns "OK" response
    Given there is a valid "spans_metric" in the system
    And new "GetSpansMetric" request
    And request contains "metric_id" parameter from "spans_metric.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.filter.query" has the same value as "spans_metric.data.attributes.filter.query"

  @team:DataDog/apm
  Scenario: Get all span-based metrics returns "OK" response
    Given there is a valid "spans_metric" in the system
    And new "ListSpansMetrics" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "spans_metrics"

  @generated @skip @team:DataDog/apm
  Scenario: Update a span-based metric returns "Bad Request" response
    Given new "UpdateSpansMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"compute": {"include_percentiles": false}, "filter": {"query": "@http.status_code:200 service:my-service"}, "group_by": [{"path": "resource_name", "tag_name": "resource_name"}]}, "type": "spans_metrics"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/apm
  Scenario: Update a span-based metric returns "Not Found" response
    Given new "UpdateSpansMetric" request
    And request contains "metric_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"compute": {"include_percentiles": false}, "filter": {"query": "@http.status_code:200 service:my-service"}, "group_by": [{"path": "resource_name", "tag_name": "resource_name"}]}, "type": "spans_metrics"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/apm
  Scenario: Update a span-based metric returns "OK" response
    Given there is a valid "spans_metric" in the system
    And new "UpdateSpansMetric" request
    And request contains "metric_id" parameter from "spans_metric.data.id"
    And body with value {"data": {"attributes": {"compute": {"include_percentiles": false}, "filter": {"query": "{{ spans_metric.data.attributes.filter.query }}-updated"}, "group_by": [{"path": "resource_name", "tag_name": "resource_name"}]}, "type": "spans_metrics"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.filter.query" is equal to "{{ spans_metric.data.attributes.filter.query }}-updated"
