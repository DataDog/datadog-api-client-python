@endpoint(data-access-controls) @endpoint(data-access-controls-v2)
Feature: Data Access Controls
  Manage [Data Access
  Controls](https://docs.datadoghq.com/account_management/rbac/data_access/)
  programmatically using Datasets.  Data Access Controls in Datadog allows
  administrators and access managers to regulate access to sensitive data.
  By defining Restricted Datasets, you can ensure that only specific teams
  or roles can view certain types of telemetry (for example, logs, traces,
  metrics, and RUM data).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DataAccessControls" API

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Create a Data Access Control dataset returns "Bad Request" response
    Given operation "CreateDataset" enabled
    And new "CreateDataset" request
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Create a Data Access Control dataset returns "Conflict" response
    Given operation "CreateDataset" enabled
    And new "CreateDataset" request
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Create a Data Access Control dataset returns "OK" response
    Given operation "CreateDataset" enabled
    And new "CreateDataset" request
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a Data Access Control dataset returns "Bad Request" response
    Given operation "DeleteDataset" enabled
    And new "DeleteDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a Data Access Control dataset returns "No Content" response
    Given operation "DeleteDataset" enabled
    And new "DeleteDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Delete a Data Access Control dataset returns "Not Found" response
    Given operation "DeleteDataset" enabled
    And new "DeleteDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Edit a Data Access Control dataset returns "Bad Request" response
    Given operation "UpdateDataset" enabled
    And new "UpdateDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Edit a Data Access Control dataset returns "Not Found" response
    Given operation "UpdateDataset" enabled
    And new "UpdateDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Edit a Data Access Control dataset returns "OK" response
    Given operation "UpdateDataset" enabled
    And new "UpdateDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Security Audit Dataset", "principals": ["role:94172442-be03-11e9-a77a-3b7612558ac1"], "product_filters": [{"filters": ["@application.id:ABCD"], "product": "logs"}]}, "type": "dataset"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a Data Access Control dataset by ID returns "Bad Request" response
    Given operation "GetDataset" enabled
    And new "GetDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a Data Access Control dataset by ID returns "Not Found" response
    Given operation "GetDataset" enabled
    And new "GetDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get a Data Access Control dataset by ID returns "OK" response
    Given operation "GetDataset" enabled
    And new "GetDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/aaa-granular-access
  Scenario: Get all Data Access Control datasets returns "OK" response
    Given operation "GetAllDatasets" enabled
    And new "GetAllDatasets" request
    When the request is sent
    Then the response status is 200 OK
