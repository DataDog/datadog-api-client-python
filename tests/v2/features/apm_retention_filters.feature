@endpoint(apm-retention-filters) @endpoint(apm-retention-filters-v2)
Feature: APM Retention Filters
  Manage configuration of [APM retention
  filters](https://app.datadoghq.com/apm/traces/retention-filters) for your
  organization. You need an API and application key with Admin rights to
  interact with this endpoint.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "APMRetentionFilters" API

  @team:DataDog/apm-trace-intake
  Scenario: Create a retention filter returns "Bad Request" response
    Given new "CreateApmRetentionFilter" request
    And body with value {"data": {"attributes": {"enabled": true, "filter": {"query": "@http.status_code:200 service:my-service"}, "filter_type": "spans-sampling-processor", "name": "my retention filter", "rate": 2.0}, "type": "apm_retention_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/apm-trace-intake
  Scenario: Create a retention filter returns "Conflict" response
    Given new "CreateApmRetentionFilter" request
    And body with value {"data": {"attributes": {"enabled": true, "filter": {"query": "@http.status_code:200 service:my-service"}, "filter_type": "spans-sampling-processor", "name": "my retention filter", "rate": 1.0}, "type": "apm_retention_filter"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/apm-trace-intake
  Scenario: Create a retention filter returns "OK" response
    Given new "CreateApmRetentionFilter" request
    And body with value {"data": {"attributes": {"enabled": true, "filter": {"query": "@http.status_code:200 service:my-service"}, "filter_type": "spans-sampling-processor", "name": "my retention filter", "rate": 1.0}, "type": "apm_retention_filter"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "my retention filter"

  @team:DataDog/apm-trace-intake
  Scenario: Delete a retention filter returns "Not Found" response
    Given new "DeleteApmRetentionFilter" request
    And request contains "filter_id" parameter with value "not_found"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/apm-trace-intake
  Scenario: Delete a retention filter returns "OK" response
    Given there is a valid "retention_filter" in the system
    And new "DeleteApmRetentionFilter" request
    And request contains "filter_id" parameter from "retention_filter.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/apm-trace-intake
  Scenario: Get a given APM retention filter returns "Not Found" response
    Given new "GetApmRetentionFilter" request
    And request contains "filter_id" parameter with value "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/apm-trace-intake
  Scenario: Get a given APM retention filter returns "OK" response
    Given there is a valid "retention_filter" in the system
    And new "GetApmRetentionFilter" request
    And request contains "filter_id" parameter from "retention_filter.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/apm-trace-intake
  Scenario: List all APM retention filters returns "OK" response
    Given there is a valid "retention_filter" in the system
    And new "ListApmRetentionFilters" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "id" with value "{{ retention_filter.data.id }}"

  @generated @skip @team:DataDog/apm-trace-intake
  Scenario: Re-order retention filters returns "Bad Request" response
    Given new "ReorderApmRetentionFilters" request
    And body with value {"data": [{"id": "7RBOb7dLSYWI01yc3pIH8w", "type": "apm_retention_filter"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/apm-trace-intake
  Scenario: Re-order retention filters returns "OK" response
    Given new "ReorderApmRetentionFilters" request
    And body with value {"data":[{"id":"jdZrilSJQLqzb6Cu7aub9Q","type":"apm_retention_filter"},{"id":"7RBOb7dLSYWI01yc3pIH8w","type":"apm_retention_filter"}]}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/apm-trace-intake
  Scenario: Update a retention filter returns "Bad Request" response
    Given there is a valid "retention_filter" in the system
    And new "UpdateApmRetentionFilter" request
    And request contains "filter_id" parameter from "retention_filter.data.id"
    And body with value {"data": { "attributes": { "name": "test","rate": 1.90, "filter": {"query": "@_top_level:1 test:service-demo"},"enabled": true,"filter_type": "spans-sampling-processor"}, "id":"test-id", "type": "apm_retention_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/apm-trace-intake
  Scenario: Update a retention filter returns "Not Found" response
    Given new "UpdateApmRetentionFilter" request
    And request contains "filter_id" parameter with value "not_found"
    And body with value {"data": { "attributes": { "name": "test", "rate": 0.90, "filter": {"query": "@_top_level:1 test:service-demo"},"enabled": true,"filter_type": "spans-sampling-processor"}, "id":"not_found", "type": "apm_retention_filter"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/apm-trace-intake
  Scenario: Update a retention filter returns "OK" response
    Given there is a valid "retention_filter" in the system
    And new "UpdateApmRetentionFilter" request
    And request contains "filter_id" parameter from "retention_filter.data.id"
    And body with value {"data": { "attributes": { "name": "test", "rate": 0.90, "filter": {"query": "@_top_level:1 test:service-demo"},"enabled": true,"filter_type": "spans-sampling-processor"}, "id":"test-id", "type": "apm_retention_filter"}}
    When the request is sent
    Then the response status is 200 OK
