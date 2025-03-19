@endpoint(rum-retention-filters) @endpoint(rum-retention-filters-v2)
Feature: Rum Retention Filters
  Manage retention filters through [Manage
  Applications](https://app.datadoghq.com/rum/list) of RUM for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumRetentionFilters" API

  @team:DataDog/rum-backend
  Scenario: Create a RUM retention filter returns "Bad Request" response
    Given new "CreateRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And body with value {"data":{"type":"invalid_type","attributes":{"name":"Test creating retention filter","event_type":"session","query":"","sample_rate":25,"enabled":true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/rum-backend
  Scenario: Create a RUM retention filter returns "Created" response
    Given new "CreateRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And body with value {"data":{"type":"retention_filters","attributes":{"name":"Test creating retention filter","event_type":"session","query":"custom_query","sample_rate":50,"enabled":true}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "retention_filters"
    And the response "data.attributes.event_type" is equal to "session"
    And the response "data.attributes.name" is equal to "Test creating retention filter"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.query" is equal to "custom_query"
    And the response "data.attributes.sample_rate" is equal to 50

  @replay-only @team:DataDog/rum-backend
  Scenario: Delete a RUM retention filter returns "No Content" response
    Given new "DeleteRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "fe34ee09-14cf-4976-9362-08044c0dea80"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/rum-backend
  Scenario: Delete a RUM retention filter returns "Not Found" response
    Given new "DeleteRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/rum-backend
  Scenario: Get a RUM retention filter returns "Not Found" response
    Given new "GetRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/rum-backend
  Scenario: Get a RUM retention filter returns "OK" response
    Given new "GetRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "4b95d361-f65d-4515-9824-c9aaeba5ac2a"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "4b95d361-f65d-4515-9824-c9aaeba5ac2a"
    And the response "data.type" is equal to "retention_filters"
    And the response "data.attributes.event_type" is equal to "session"
    And the response "data.attributes.name" is equal to "Test retention filter for session"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.query" is equal to "custom_query"
    And the response "data.attributes.sample_rate" is equal to 25

  @replay-only @team:DataDog/rum-backend
  Scenario: Get all RUM retention filters returns "OK" response
    Given new "ListRetentionFilters" request
    And request contains "app_id" parameter with value "1d4b9c34-7ac4-423a-91cf-9902d926e9b3"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 3

  @team:DataDog/rum-backend
  Scenario: Order RUM retention filters returns "Bad Request" response
    Given new "OrderRetentionFilters" request
    And request contains "app_id" parameter with value "1d4b9c34-7ac4-423a-91cf-9902d926e9b3"
    And body with value {"data":[{"type":"retention_filters","id":"325631eb-94c9-49c0-93f9-ab7e4fd24529"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/rum-backend
  Scenario: Order RUM retention filters returns "Ordered" response
    Given new "OrderRetentionFilters" request
    And request contains "app_id" parameter with value "1d4b9c34-7ac4-423a-91cf-9902d926e9b3"
    And body with value {"data":[{"type":"retention_filters","id":"325631eb-94c9-49c0-93f9-ab7e4fd24529"},{"type":"retention_filters","id":"42d89430-5b80-426e-a44b-ba3b417ece25"},{"type":"retention_filters","id":"bff0bc34-99e9-4c16-adce-f47e71948c23"}]}
    When the request is sent
    Then the response status is 200 Ordered
    And the response "data[0].id" is equal to "325631eb-94c9-49c0-93f9-ab7e4fd24529"
    And the response "data[1].id" is equal to "42d89430-5b80-426e-a44b-ba3b417ece25"
    And the response "data[2].id" is equal to "bff0bc34-99e9-4c16-adce-f47e71948c23"

  @team:DataDog/rum-backend
  Scenario: Update a RUM retention filter returns "Bad Request" response
    Given new "UpdateRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data":{"id":"{{ unique }}", "type":"invalid_type","attributes":{"name":"Test updating retention filter","event_type":"view","query":"","sample_rate":100,"enabled":true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Update a RUM retention filter returns "Not Found" response
    Given new "UpdateRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data":{"id":"{{ unique }}","type":"retention_filters","attributes":{"name":"Test updating retention filter","event_type":"view","query":"","sample_rate":100,"enabled":true}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/rum-backend
  Scenario: Update a RUM retention filter returns "Updated" response
    Given new "UpdateRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "4b95d361-f65d-4515-9824-c9aaeba5ac2a"
    And body with value {"data":{"id":"4b95d361-f65d-4515-9824-c9aaeba5ac2a","type":"retention_filters","attributes":{"name":"Test updating retention filter","event_type":"view","query":"view_query","sample_rate":100,"enabled":true}}}
    When the request is sent
    Then the response status is 200 Updated
    And the response "data.id" is equal to "4b95d361-f65d-4515-9824-c9aaeba5ac2a"
    And the response "data.type" is equal to "retention_filters"
    And the response "data.attributes.event_type" is equal to "view"
    And the response "data.attributes.name" is equal to "Test updating retention filter"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.query" is equal to "view_query"
    And the response "data.attributes.sample_rate" is equal to 100
