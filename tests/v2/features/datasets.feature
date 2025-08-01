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

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/aaa-granular-access
  Scenario: Create a dataset returns "Bad Request" response
    Given new "CreateDataset" request
    And operation "CreateDataset" enabled
    And body with value {"test": "bad_request"}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Create a dataset returns "Conflict" response
    Given there is a valid "dataset" in the system
    And operation "CreateDataset" enabled
    And new "CreateDataset" request
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "metrics"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Create a dataset returns "OK" response
    Given new "CreateDataset" request
    And operation "CreateDataset" enabled
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "metrics"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Delete a dataset returns "Bad Request" response
    Given new "DeleteDataset" request
    And operation "DeleteDataset" enabled
    And request contains "dataset_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Delete a dataset returns "No Content" response
    Given there is a valid "dataset" in the system
    And operation "DeleteDataset" enabled
    And new "DeleteDataset" request
    And request contains "dataset_id" parameter from "dataset.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Delete a dataset returns "Not Found" response
    Given new "DeleteDataset" request
    And operation "DeleteDataset" enabled
    And request contains "dataset_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-terraform-config @skip-typescript @skip-validation @team:DataDog/aaa-granular-access
  Scenario: Edit a dataset returns "Bad Request" response
    Given new "UpdateDataset" request
    And operation "UpdateDataset" enabled
    And request contains "dataset_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Edit a dataset returns "Not Found" response
    Given there is a valid "dataset" in the system
    And operation "UpdateDataset" enabled
    And new "UpdateDataset" request
    And request contains "dataset_id" parameter from "dataset.data.id"
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:1234"], "product": "metrics"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Edit a dataset returns "OK" response
    Given there is a valid "dataset" in the system
    And operation "UpdateDataset" enabled
    And new "UpdateDataset" request
    And request contains "dataset_id" parameter from "dataset.data.id"
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:1234"], "product": "metrics"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get a single dataset by ID returns "Bad Request" response
    Given new "GetDataset" request
    And operation "GetDataset" enabled
    And request contains "dataset_id" parameter with value "malformed_id"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get a single dataset by ID returns "Not Found" response
    Given operation "GetDataset" enabled
    And new "GetDataset" request
    And request contains "dataset_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get a single dataset by ID returns "OK" response
    Given there is a valid "dataset" in the system
    And operation "GetDataset" enabled
    And new "GetDataset" request
    And request contains "dataset_id" parameter from "dataset.data.id"
    When the request is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/aaa-granular-access
  Scenario: Get all datasets returns "OK" response
    Given there is a valid "dataset" in the system
    And operation "GetAllDatasets" enabled
    And new "GetAllDatasets" request
    When the request is sent
    Then the response status is 200 OK
