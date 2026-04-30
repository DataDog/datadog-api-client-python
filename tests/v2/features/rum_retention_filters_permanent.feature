@endpoint(rum-retention-filters-permanent) @endpoint(rum-retention-filters-permanent-v2)
Feature: Rum Retention Filters Permanent
  Manage permanent retention filters through [Manage
  Applications](https://app.datadoghq.com/rum/list) in RUM for your
  organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RumRetentionFiltersPermanent" API

  @team:DataDog/rum-backend
  Scenario: Get a permanent retention filter returns "Not Found" response
    Given new "GetPermanentRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/rum-backend
  Scenario: Get a permanent retention filter returns "OK" response
    Given new "GetPermanentRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "default_synthetics"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "default_synthetics"
    And the response "data.type" is equal to "permanent_retention_filters"

  @replay-only @team:DataDog/rum-backend
  Scenario: Get all permanent retention filters returns "OK" response
    Given new "ListPermanentRetentionFilters" request
    And request contains "app_id" parameter with value "1d4b9c34-7ac4-423a-91cf-9902d926e9b3"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/rum-backend
  Scenario: Update a permanent retention filter returns "Bad Request" response
    Given new "UpdatePermanentRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data":{"id":"{{ unique }}","type":"invalid_type","attributes":{"cross_product_sampling":{"trace_sample_rate":25}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/rum-backend
  Scenario: Update a permanent retention filter returns "Bad Request" response for unknown rf_id
    Given new "UpdatePermanentRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data":{"id":"{{ unique }}","type":"permanent_retention_filters","attributes":{"cross_product_sampling":{"trace_sample_rate":25}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a permanent retention filter returns "Not Found" response
    Given new "UpdatePermanentRetentionFilter" request
    And request contains "app_id" parameter from "REPLACE.ME"
    And request contains "rf_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cross_product_sampling": {"trace_sample_rate": 25.0}}, "id": "4b95d361-f65d-4515-9824-c9aaeba5ac2a", "type": "permanent_retention_filters"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/rum-backend
  Scenario: Update a permanent retention filter returns "Updated" response
    Given new "UpdatePermanentRetentionFilter" request
    And request contains "app_id" parameter with value "a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"
    And request contains "rf_id" parameter with value "default_replays"
    And body with value {"data":{"id":"default_replays","type":"permanent_retention_filters","attributes":{"cross_product_sampling":{"trace_sample_rate":100}}}}
    When the request is sent
    Then the response status is 200 Updated
    And the response "data.id" is equal to "default_replays"
    And the response "data.type" is equal to "permanent_retention_filters"
