@endpoint(rum-hardcoded-retention-filters) @endpoint(rum-hardcoded-retention-filters-v2)
Feature: RUM Retention Filters Hardcoded
  Manage hardcoded retention filters through [Manage
  Applications](https://app.datadoghq.com/rum/list) in RUM.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMRetentionFiltersHardcoded" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a hardcoded retention filter returns "Not Found" response
    Given new "GetHardcodedRetentionFilter" request
    And request contains "app_id" parameter with value "{{ unique }}"
    And request contains "rf_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a hardcoded retention filter returns "OK" response
    Given new "GetHardcodedRetentionFilter" request
    And request contains "app_id" parameter with value "{{ unique }}"
    And request contains "rf_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get all hardcoded retention filters returns "OK" response
    Given new "ListHardcodedRetentionFilters" request
    And request contains "app_id" parameter with value "{{ unique }}"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a hardcoded retention filter returns "Bad Request" response
    Given new "UpdateHardcodedRetentionFilter" request
    And request contains "app_id" parameter with value "{{ unique }}"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data": {"id": "REPLACE.ME", "type": "hardcoded_retention_filters", "attributes": {"cross_product_sampling": {"session_replay_sample_rate": 50.0}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a hardcoded retention filter returns "Not Found" response
    Given new "UpdateHardcodedRetentionFilter" request
    And request contains "app_id" parameter with value "{{ unique }}"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data": {"id": "REPLACE.ME", "type": "hardcoded_retention_filters", "attributes": {"cross_product_sampling": {"session_replay_sample_rate": 50.0}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a hardcoded retention filter returns "Updated" response
    Given new "UpdateHardcodedRetentionFilter" request
    And request contains "app_id" parameter with value "{{ unique }}"
    And request contains "rf_id" parameter with value "{{ unique }}"
    And body with value {"data": {"id": "REPLACE.ME", "type": "hardcoded_retention_filters", "attributes": {"cross_product_sampling": {"session_replay_sample_rate": 50.0, "session_replay_enabled": true}}}}
    When the request is sent
    Then the response status is 200 OK
