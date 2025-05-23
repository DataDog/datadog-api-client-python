@endpoint(rum-metrics) @endpoint(rum-metrics-v2)
Feature: Rum Metrics
  Manage configuration of [rum-based
  metrics](https://app.datadoghq.com/rum/generate-metrics) for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumMetrics" API

  @team:DataDog/rum-backend
  Scenario: Create a rum-based metric returns "Bad Request" response
    Given new "CreateRumMetric" request
    And body with value {"data": {"id": "rum.actions.invalid", "type": "rum_metrics", "attributes": {"event_type": "action", "compute": {"aggregation_type": "count"}, "uniqueness":{"when": "match"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Create a rum-based metric returns "Conflict" response
    Given there is a valid "rum_metric" in the system
    And new "CreateRumMetric" request
    And body with value {"data": {"id": "{{ rum_metric.data.id }}", "type": "rum_metrics", "attributes": {"compute": {"aggregation_type": "count"}, "event_type": "action"}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/rum-backend
  Scenario: Create a rum-based metric returns "Created" response
    Given new "CreateRumMetric" request
    And body with value {"data": {"attributes": {"compute": {"aggregation_type": "distribution", "include_percentiles": true, "path": "@duration"}, "event_type": "session", "filter": {"query": "@service:web-ui"}, "group_by": [{"path": "@browser.name", "tag_name": "browser_name"}], "uniqueness": {"when": "match"}}, "id": "{{ unique_lower_alnum }}", "type": "rum_metrics"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.id" is equal to "{{ unique_lower_alnum }}"
    And the response "data.type" is equal to "rum_metrics"
    And the response "data.attributes.event_type" is equal to "session"
    And the response "data.attributes.compute.aggregation_type" is equal to "distribution"
    And the response "data.attributes.compute.include_percentiles" is equal to true
    And the response "data.attributes.compute.path" is equal to "@duration"
    And the response "data.attributes.filter.query" is equal to "@service:web-ui"
    And the response "data.attributes.group_by[0].path" is equal to "@browser.name"
    And the response "data.attributes.group_by[0].tag_name" is equal to "browser_name"
    And the response "data.attributes.uniqueness.when" is equal to "match"

  @team:DataDog/rum-backend
  Scenario: Delete a rum-based metric returns "No Content" response
    Given there is a valid "rum_metric" in the system
    And new "DeleteRumMetric" request
    And request contains "metric_id" parameter from "rum_metric.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/rum-backend
  Scenario: Delete a rum-based metric returns "Not Found" response
    Given new "DeleteRumMetric" request
    And request contains "metric_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/rum-backend
  Scenario: Get a rum-based metric returns "Not Found" response
    Given new "GetRumMetric" request
    And request contains "metric_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/rum-backend
  Scenario: Get a rum-based metric returns "OK" response
    Given there is a valid "rum_metric" in the system
    And new "GetRumMetric" request
    And request contains "metric_id" parameter from "rum_metric.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "rum_metric.data.id"
    And the response "data.type" has the same value as "rum_metric.data.type"
    And the response "data.attributes.event_type" has the same value as "rum_metric.data.attributes.event_type"
    And the response "data.attributes.compute.aggregation_type" has the same value as "rum_metric.data.attributes.compute.aggregation_type"
    And the response "data.attributes.compute.include_percentiles" has the same value as "rum_metric.data.attributes.compute.include_percentiles"
    And the response "data.attributes.compute.path" has the same value as "rum_metric.data.attributes.compute.path"
    And the response "data.attributes.filter.query" has the same value as "rum_metric.data.attributes.filter.query"
    And the response "data.attributes.group_by[0].path" has the same value as "rum_metric.data.attributes.group_by[0].path"
    And the response "data.attributes.group_by[0].tag_name" has the same value as "rum_metric.data.attributes.group_by[0].tag_name"
    And the response "data.attributes.uniqueness.when" has the same value as "rum_metric.data.attributes.uniqueness.when"

  @team:DataDog/rum-backend
  Scenario: Get all rum-based metrics returns "OK" response
    Given new "ListRumMetrics" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/rum-backend
  Scenario: Update a rum-based metric returns "Bad Request" response
    Given there is a valid "rum_metric" in the system
    And new "UpdateRumMetric" request
    And request contains "metric_id" parameter from "rum_metric.data.id"
    And body with value {"data": {"id": "rum.sessions.webui.count", "type": "unknown_metrics", "attributes": {"compute": {"include_percentiles": true}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Update a rum-based metric returns "Conflict" response
    Given there is a valid "rum_metric" in the system
    And new "UpdateRumMetric" request
    And request contains "metric_id" parameter from "rum_metric.data.id"
    And body with value {"data": {"id": "conflicting.id", "type": "rum_metrics", "attributes": {"compute": {"include_percentiles": true}}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/rum-backend
  Scenario: Update a rum-based metric returns "Not Found" response
    Given there is a valid "rum_metric" in the system
    And new "UpdateRumMetric" request
    And request contains "metric_id" parameter with value "8fc991bf-967e-4652-8a5b-0711a985abe3"
    And body with value {"data": {"id": "8fc991bf-967e-4652-8a5b-0711a985abe3", "type": "rum_metrics", "attributes": {"compute": {"include_percentiles": true}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/rum-backend
  Scenario: Update a rum-based metric returns "OK" response
    Given there is a valid "rum_metric" in the system
    And new "UpdateRumMetric" request
    And request contains "metric_id" parameter from "rum_metric.data.id"
    And body with value {"data": {"id": "{{ rum_metric.data.id }}", "type": "rum_metrics", "attributes": {"compute": {"include_percentiles": false}, "filter": {"query": "@service:rum-config"}, "group_by": [{"path": "@browser.version", "tag_name": "browser_version"}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "rum_metric.data.id"
    And the response "data.type" has the same value as "rum_metric.data.type"
    And the response "data.attributes.event_type" has the same value as "rum_metric.data.attributes.event_type"
    And the response "data.attributes.compute.aggregation_type" has the same value as "rum_metric.data.attributes.compute.aggregation_type"
    And the response "data.attributes.compute.include_percentiles" is equal to false
    And the response "data.attributes.compute.path" has the same value as "rum_metric.data.attributes.compute.path"
    And the response "data.attributes.filter.query" is equal to "@service:rum-config"
    And the response "data.attributes.group_by[0].path" is equal to "@browser.version"
    And the response "data.attributes.group_by[0].tag_name" is equal to "browser_version"
    And the response "data.attributes.uniqueness.when" has the same value as "rum_metric.data.attributes.uniqueness.when"
