@endpoint(terraform-state-files) @endpoint(terraform-state-files-v2)
Feature: Terraform State Files
  Configure synchronization of Terraform state files from S3 buckets and
  inspect synchronization status.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "TerraformStateFiles" API

  @team:DataDog/iac-platform
  Scenario: Create a Terraform backend sync configuration returns "Bad Request" response
    Given new "CreateTerraformBackendSyncConfig" request
    And body with value {"data":{"type":"terraform-backends","attributes":{"backend_type":"terraform","account_id":" ","region":"us-east-1","bucket_names":["terraform-state-bucket"]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/iac-platform
  Scenario: Create a Terraform backend sync configuration returns "Conflict" response
    Given new "CreateTerraformBackendSyncConfig" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "backend_type": "terraform", "bucket_names": ["terraform-state-bucket"], "region": "us-east-1"}, "type": "terraform-backends"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/iac-platform
  Scenario: Create a Terraform backend sync configuration returns "Created" response
    Given new "CreateTerraformBackendSyncConfig" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "backend_type": "terraform", "bucket_names": ["terraform-state-bucket"], "region": "us-east-1"}, "type": "terraform-backends"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/iac-platform
  Scenario: Delete a Terraform backend sync configuration returns "Bad Request" response
    Given new "DeleteTerraformBackendSyncConfig" request
    And request contains "id" parameter with value "invalid-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/iac-platform
  Scenario: Delete a Terraform backend sync configuration returns "No Content" response
    Given new "DeleteTerraformBackendSyncConfig" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/iac-platform
  Scenario: Delete a Terraform backend sync configuration returns "Not Found" response
    Given new "DeleteTerraformBackendSyncConfig" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/iac-platform
  Scenario: List Terraform backend sync configurations returns "OK" response
    Given new "ListTerraformBackendSyncConfigs" request
    And request contains "account_id" parameter with value "123456789012"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/iac-platform
  Scenario: Update a Terraform backend sync configuration returns "Bad Request" response
    Given new "UpdateTerraformBackendSyncConfig" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bucket_names": ["terraform-state-bucket"]}, "id": "9007199254740993", "type": "terraform-backends"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/iac-platform
  Scenario: Update a Terraform backend sync configuration returns "Conflict" response
    Given new "UpdateTerraformBackendSyncConfig" request
    And request contains "id" parameter with value "1"
    And body with value {"data":{"type":"terraform-backends","id":"2","attributes":{"bucket_names":["terraform-state-bucket"]}}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/iac-platform
  Scenario: Update a Terraform backend sync configuration returns "Not Found" response
    Given new "UpdateTerraformBackendSyncConfig" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bucket_names": ["terraform-state-bucket"]}, "id": "9007199254740993", "type": "terraform-backends"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/iac-platform
  Scenario: Update a Terraform backend sync configuration returns "OK" response
    Given new "UpdateTerraformBackendSyncConfig" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"bucket_names": ["terraform-state-bucket"]}, "id": "9007199254740993", "type": "terraform-backends"}}
    When the request is sent
    Then the response status is 200 OK
