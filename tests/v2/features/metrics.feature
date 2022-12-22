@endpoint(metrics) @endpoint(metrics-v2)
Feature: Metrics
  The metrics endpoint allows you to:  - Post metrics data so it can be
  graphed on Datadog’s dashboards - Query metrics from any time period
  (timeseries and scalar) - Modify tag configurations for metrics - View
  tags and volumes for metrics  **Note**: A graph can only contain a set
  number of points and as the timeframe over which a metric is viewed
  increases, aggregation between points occurs to stay below that set
  number.  The Post, Patch, and Delete `manage_tags` API methods can only be
  performed by a user who has the `Manage Tags for Metrics` permission.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And an instance of "Metrics" API

  @skip-typescript @team:DataDog/points-aggregation
  Scenario: Configure tags for multiple metrics returns "Accepted" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "user" in the system
    And new "CreateBulkTagsMetricsConfiguration" request
    And body with value {"data": {"attributes": {"emails": ["{{ user.data.attributes.email }}"], "tags": ["test", "{{ unique_lower_alnum }}"]}, "id": "system.load.1", "type": "metric_bulk_configure_tags"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Configure tags for multiple metrics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "CreateBulkTagsMetricsConfiguration" request
    And body with value {"data": {"attributes": {"emails": ["sue@example.com", "bob@example.com"], "tags": ["host", "pod_name", "is_shadow"]}, "id": "kafka.lag", "type": "metric_bulk_configure_tags"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Configure tags for multiple metrics returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "CreateBulkTagsMetricsConfiguration" request
    And body with value {"data": {"attributes": {"emails": ["sue@example.com", "bob@example.com"], "tags": ["host", "pod_name", "is_shadow"]}, "id": "kafka.lag", "type": "metric_bulk_configure_tags"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Create a tag configuration returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "CreateTagConfiguration" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"include_percentiles": false, "metric_type": "distribution", "tags": ["app", "datacenter"]}, "id": "http.endpoint.request", "type": "manage_tags"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Create a tag configuration returns "Conflict" response
    Given a valid "appKeyAuth" key in the system
    And new "CreateTagConfiguration" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"include_percentiles": false, "metric_type": "distribution", "tags": ["app", "datacenter"]}, "id": "http.endpoint.request", "type": "manage_tags"}}
    When the request is sent
    Then the response status is 409 Conflict

  @replay-only @team:DataDog/points-aggregation
  Scenario: Create a tag configuration returns "Created" response
    Given a valid "appKeyAuth" key in the system
    And new "CreateTagConfiguration" request
    And there is a valid "metric" in the system
    And request contains "metric_name" parameter with value "{{ unique_alnum }}"
    And body with value {"data": {"type": "manage_tags", "id": "{{ unique_alnum }}", "attributes": {"tags": ["app","datacenter"], "metric_type": "gauge"}}}
    When the request is sent
    Then the response status is 201 Created

  @replay-only @team:DataDog/points-aggregation
  Scenario: Delete a tag configuration returns "No Content" response
    Given there is a valid "metric" in the system
    And there is a valid "metric_tag_configuration" in the system
    And a valid "appKeyAuth" key in the system
    And new "DeleteTagConfiguration" request
    And request contains "metric_name" parameter with value "{{ unique_alnum }}"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Delete a tag configuration returns "Not found" response
    Given a valid "appKeyAuth" key in the system
    And new "DeleteTagConfiguration" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Get a list of metrics returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListTagConfigurations" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/points-aggregation
  Scenario: Get a list of metrics returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "metric_tag_configuration" in the system
    And new "ListTagConfigurations" request
    When the request is sent
    Then the response status is 200 Success

  @team:DataDog/points-aggregation
  Scenario: Get a list of metrics with a tag filter returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And new "ListTagConfigurations" request
    And request contains "filter[tags]" parameter with value "{{ unique_alnum }}"
    When the request is sent
    Then the response status is 200 Success

  @team:DataDog/points-aggregation
  Scenario: Get a list of metrics with configured filter returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And new "ListTagConfigurations" request
    And request contains "filter[configured]" parameter with value true
    When the request is sent
    Then the response status is 200 Success

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List active tags and aggregations returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListActiveMetricConfigurations" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List active tags and aggregations returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "ListActiveMetricConfigurations" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/points-aggregation
  Scenario: List active tags and aggregations returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "metric" in the system
    And new "ListActiveMetricConfigurations" request
    And request contains "metric_name" parameter with value "{{ unique_alnum }}"
    When the request is sent
    Then the response status is 200 Success
    And the response "data.type" is equal to "actively_queried_configurations"

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List distinct metric volumes by metric name returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListVolumesByMetricName" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List distinct metric volumes by metric name returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "ListVolumesByMetricName" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/points-aggregation
  Scenario: List distinct metric volumes by metric name returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "metric" in the system
    And there is a valid "metric_tag_configuration" in the system
    And new "ListVolumesByMetricName" request
    And request contains "metric_name" parameter with value "{{ unique_alnum }}"
    When the request is sent
    Then the response status is 200 Success
    And the response "data.type" is equal to "metric_volumes"

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List tag configuration by name returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "ListTagConfigurationByName" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/points-aggregation
  Scenario: List tag configuration by name returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "metric" in the system
    And there is a valid "metric_tag_configuration" in the system
    And new "ListTagConfigurationByName" request
    And request contains "metric_name" parameter from "metric_tag_configuration.data.id"
    When the request is sent
    Then the response status is 200 Success
    And the response "data.id" has the same value as "metric_tag_configuration.data.id"

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List tags by metric name returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "ListTagsByMetricName" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/points-aggregation
  Scenario: List tags by metric name returns "Not Found" response
    Given a valid "appKeyAuth" key in the system
    And new "ListTagsByMetricName" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/points-aggregation
  Scenario: List tags by metric name returns "Success" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "metric" in the system
    And there is a valid "metric_tag_configuration" in the system
    And new "ListTagsByMetricName" request
    And request contains "metric_name" parameter from "metric_tag_configuration.data.id"
    When the request is sent
    Then the response status is 200 Success
    And the response "data.id" has the same value as "metric_tag_configuration.data.id"

  @team:DataDog/metrics-query
  Scenario: Scalar cross product query returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryScalarData" enabled
    And new "QueryScalarData" request
    And body with value {"data": {"attributes": {"formulas": [{"formula": "a+b", "limit": {"count": 10, "order": "desc"}}], "from": 1568899800000, "queries": [{"aggregator": "avg", "data_source": "metrics", "query": "avg:system.cpu.user{*}", "name": "a"}], "to": 1568923200000}, "type": "scalar_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/metrics-query
  Scenario: Scalar cross product query returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryScalarData" enabled
    And new "QueryScalarData" request
    And body with value {"data": {"attributes": {"formulas": [{"formula": "a", "limit": {"count": 10, "order": "desc"}}], "from": 1671612804000, "queries": [{"aggregator": "avg", "data_source": "metrics", "query": "avg:system.cpu.user{*}", "name": "a"}], "to": 1671620004000}, "type": "scalar_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Bad Request" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [{"timestamp": 1475317847, "value": 0.7}], "resources": [{"name": "dummyhost", "type": "host"}]}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Payload accepted" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "type": 0, "points": [{"timestamp": {{ timestamp('now') }}, "value": 0.7}], "resources": [{"name": "dummyhost", "type": "host"}]}]}
    When the request is sent
    Then the response status is 202 Payload accepted

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Payload too large" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [{"timestamp": 1475317847, "value": 0.7}], "resources": [{"name": "dummyhost", "type": "host"}]}]}
    When the request is sent
    Then the response status is 413 Payload too large

  @generated @skip @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics returns "Request timeout" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "points": [{"timestamp": 1475317847, "value": 0.7}], "resources": [{"name": "dummyhost", "type": "host"}]}]}
    When the request is sent
    Then the response status is 408 Request timeout

  @integration-only @skip-terraform-config @skip-validation @team:DataDog/metrics-intake @team:DataDog/metrics-query
  Scenario: Submit metrics with compression returns "Payload accepted" response
    Given new "SubmitMetrics" request
    And body with value {"series": [{"metric": "system.load.1", "type": 0, "points": [{"timestamp": {{ timestamp('now') }}, "value": 0.7}]}]}
    And request contains "Content-Encoding" parameter with value "zstd1"
    When the request is sent
    Then the response status is 202 Payload accepted

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Tag Configuration Cardinality Estimator returns "API error response." response
    Given a valid "appKeyAuth" key in the system
    And new "EstimateMetricsOutputSeries" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response.

  @replay-only @team:DataDog/points-aggregation
  Scenario: Tag Configuration Cardinality Estimator returns "Success" response
    Given new "EstimateMetricsOutputSeries" request
    And request contains "metric_name" parameter with value "system.cpu.idle"
    And request contains "filter[groups]" parameter with value "app,host"
    And request contains "filter[num_aggregations]" parameter with value 4
    When the request is sent
    Then the response status is 200 Success

  @team:DataDog/metrics-query
  Scenario: Timeseries cross product query returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryTimeseriesData" enabled
    And new "QueryTimeseriesData" request
    And body with value {"data": {"attributes": {"formulas": [{"formula": "a+b", "limit": {"count": 10, "order": "desc"}}], "from": {{ timestamp('now - 1h') }}, "interval": 5000, "queries": [{"data_source": "metrics", "query": "avg:system.cpu.user{*}"}], "to": {{ timestamp('now') }}}, "type": "timeseries_rquest"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/metrics-query
  Scenario: Timeseries cross product query returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And operation "QueryTimeseriesData" enabled
    And new "QueryTimeseriesData" request
    And body with value {"data": {"attributes": {"formulas": [{"formula": "a", "limit": {"count": 10, "order": "desc"}}], "from": 1671612804000, "interval": 5000, "queries": [{"data_source": "metrics", "query": "avg:system.cpu.user{*}", "name": "a"}], "to": 1671620004000}, "type": "timeseries_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Update a tag configuration returns "Bad Request" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"group_by": ["app", "datacenter"], "include_percentiles": false}, "id": "http.endpoint.request", "type": "manage_tags"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/points-aggregation
  Scenario: Update a tag configuration returns "OK" response
    Given a valid "appKeyAuth" key in the system
    And there is a valid "metric" in the system
    And there is a valid "metric_tag_configuration" in the system
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "metric_tag_configuration.data.id"
    And body with value {"data": {"type": "manage_tags", "id": "{{ metric_tag_configuration.data.id }}", "attributes": {"tags": ["app"]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.tags[0]" is equal to "app"

  @generated @skip @team:DataDog/points-aggregation
  Scenario: Update a tag configuration returns "Unprocessable Entity" response
    Given a valid "appKeyAuth" key in the system
    And new "UpdateTagConfiguration" request
    And request contains "metric_name" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"group_by": ["app", "datacenter"], "include_percentiles": false}, "id": "http.endpoint.request", "type": "manage_tags"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
