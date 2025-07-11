@endpoint(datasets) @endpoint(datasets-v2)
Feature: Datasets
  Data Access Controls in Datadog is a feature that allows administrators
  and access managers to regulate access to sensitive data. By defining
  Restricted Datasets, you can ensure that only specific teams or roles can
  view certain types of telemetry (for example, logs, traces, metrics, and
  RUM data).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Datasets" API

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Create a dataset returns "Bad Request" response
    Given new "CreateDataset" request
    And body with value {"data": {"attributes": {"created_at": null, "name": "Security Audit Dataset", "principals": ["role:86245fce-0a4e-11f0-92bd-da7ad0900002"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "id": "123e4567-e89b-12d3-a456-426614174000", "type": "dataset"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Create a dataset returns "Conflict" response
    Given new "CreateDataset" request
    And body with value {"data": {"attributes": {"created_at": null, "name": "Security Audit Dataset", "principals": ["role:86245fce-0a4e-11f0-92bd-da7ad0900002"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "id": "123e4567-e89b-12d3-a456-426614174000", "type": "dataset"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Create a dataset returns "OK" response
    Given new "CreateDataset" request
    And body with value {"data": {"attributes": {"created_at": null, "name": "Security Audit Dataset", "principals": ["role:86245fce-0a4e-11f0-92bd-da7ad0900002"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "id": "123e4567-e89b-12d3-a456-426614174000", "type": "dataset"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a dataset returns "Bad Request" response
    Given new "DeleteDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a dataset returns "No Content" response
    Given new "DeleteDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a dataset returns "Not Found" response
    Given new "DeleteDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a single dataset by ID returns "Bad Request" response
    Given new "GetDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a single dataset by ID returns "Not Found" response
    Given new "GetDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a single dataset by ID returns "OK" response
    Given new "GetDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get all datasets returns "OK" response
    Given new "GetAllDatasets" request
    When the request is sent
    Then the response status is 200 OK
