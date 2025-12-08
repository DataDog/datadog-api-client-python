@endpoint(reference-tables) @endpoint(reference-tables-v2)
Feature: Reference Tables
  View and manage Reference Tables in your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ReferenceTables" API

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Create reference table returns "Bad Request" response
    Given new "CreateReferenceTable" request
    And body with value {"data": {"attributes": {"file_metadata": {"access_details": {"aws_detail": {"aws_account_id": "123456789000", "aws_bucket_name": "example-data-bucket", "file_path": "reference-tables/users.csv"}, "azure_detail": {"azure_client_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb", "azure_container_name": "reference-data", "azure_storage_account_name": "examplestorageaccount", "azure_tenant_id": "cccccccc-4444-5555-6666-dddddddddddd", "file_path": "tables/users.csv"}, "gcp_detail": {"file_path": "data/reference_tables/users.csv", "gcp_bucket_name": "example-data-bucket", "gcp_project_id": "example-gcp-project-12345", "gcp_service_account_email": "example-service@example-gcp-project-12345.iam.gserviceaccount.com"}}, "sync_enabled": false}, "schema": {"fields": [{"name": "field_1", "type": "STRING"}], "primary_keys": ["field_1"]}, "source": "LOCAL_FILE", "table_name": "table_1", "tags": ["tag_1", "tag_2"]}, "type": "reference_table"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Create reference table returns "Created" response
    Given new "CreateReferenceTable" request
    And body with value {"data": {"attributes": {"file_metadata": {"access_details": {"aws_detail": {"aws_account_id": "123456789000", "aws_bucket_name": "example-data-bucket", "file_path": "reference-tables/users.csv"}, "azure_detail": {"azure_client_id": "aaaaaaaa-1111-2222-3333-bbbbbbbbbbbb", "azure_container_name": "reference-data", "azure_storage_account_name": "examplestorageaccount", "azure_tenant_id": "cccccccc-4444-5555-6666-dddddddddddd", "file_path": "tables/users.csv"}, "gcp_detail": {"file_path": "data/reference_tables/users.csv", "gcp_bucket_name": "example-data-bucket", "gcp_project_id": "example-gcp-project-12345", "gcp_service_account_email": "example-service@example-gcp-project-12345.iam.gserviceaccount.com"}}, "sync_enabled": false}, "schema": {"fields": [{"name": "field_1", "type": "STRING"}], "primary_keys": ["field_1"]}, "source": "LOCAL_FILE", "table_name": "table_1", "tags": ["tag_1", "tag_2"]}, "type": "reference_table"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Create reference table upload returns "Bad Request" response
    Given new "CreateReferenceTableUpload" request
    And body with value {"data": {"attributes": {"headers": ["product_id", "product_name", "price"], "part_count": 3, "part_size": 10000000, "table_name": "my_products_table"}, "type": "upload"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/redapl-experiences
  Scenario: Create reference table upload returns "Created" response
    Given new "CreateReferenceTableUpload" request
    And body with value {"data": {"attributes": {"headers": ["id", "name", "value"], "table_name": "test_upload_table_{{ unique }}", "part_count": 1, "part_size": 1024}, "type": "upload"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "upload"
    And the response "data.attributes.table_name" is equal to "test_upload_table_{{ unique }}"

  @skip @team:DataDog/redapl-experiences
  Scenario: Create reference table with upload returns "Created" response
    Given new "CreateReferenceTable" request
    And body with value {"data": {"attributes": {"description": "Test reference table created via BDD test {{ unique }}", "source": "LOCAL_FILE", "file_metadata": {"upload_id": "test-upload-id-{{ unique }}"}, "schema": {"fields": [{"name": "id", "type": "STRING"}, {"name": "name", "type": "STRING"}, {"name": "value", "type": "INT32"}], "primary_keys": ["id"]}, "table_name": "test_reference_table_{{ unique }}", "tags": ["test_tag"]}, "type": "reference_table"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "reference_table"
    And the response "data.attributes.table_name" is equal to "test_reference_table_{{ unique }}"

  @team:DataDog/redapl-experiences
  Scenario: Create reference table without upload or access details returns "Bad Request" response
    Given new "CreateReferenceTable" request
    And body with value {"data": {"attributes": {"description": "Test reference table without upload or access details", "source": "LOCAL_FILE", "schema": {"fields": [{"name": "id", "type": "STRING"}], "primary_keys": ["id"]}, "table_name": "test_invalid_table_{{ unique }}", "tags": ["test_tag"]}, "type": "reference_table"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Delete rows returns "Bad Request" response
    Given new "DeleteRows" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": [{"id": "primary_key_value", "type": "row"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Delete rows returns "Not Found" response
    Given new "DeleteRows" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": [{"id": "primary_key_value", "type": "row"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Delete rows returns "Rows deleted successfully" response
    Given new "DeleteRows" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": [{"id": "primary_key_value", "type": "row"}]}
    When the request is sent
    Then the response status is 200 Rows deleted successfully

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Delete table returns "Not Found" response
    Given new "DeleteTable" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Delete table returns "OK" response
    Given new "DeleteTable" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Get rows by id returns "Not Found" response
    Given new "GetRowsByID" request
    And request contains "id" parameter from "REPLACE.ME"
    And request contains "row_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Get rows by id returns "Some or all requested rows were found." response
    Given new "GetRowsByID" request
    And request contains "id" parameter from "REPLACE.ME"
    And request contains "row_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Some or all requested rows were found.

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Get table returns "Not Found" response
    Given new "GetTable" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Get table returns "OK" response
    Given new "GetTable" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/redapl-experiences
  Scenario: List tables returns "OK" response
    Given new "ListTables" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Update reference table returns "Bad Request" response
    Given new "UpdateReferenceTable" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "this is a cloud table generated via a cloud bucket sync", "file_metadata": {"access_details": {"aws_detail": {"aws_account_id": "test-account-id", "aws_bucket_name": "test-bucket", "file_path": "test_rt.csv"}}, "sync_enabled": true}, "schema": {"fields": [{"name": "id", "type": "INT32"}, {"name": "name", "type": "STRING"}], "primary_keys": ["id"]}, "sync_enabled": false, "tags": ["test_tag"]}, "type": "reference_table"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Update reference table returns "OK" response
    Given new "UpdateReferenceTable" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "this is a cloud table generated via a cloud bucket sync", "file_metadata": {"access_details": {"aws_detail": {"aws_account_id": "test-account-id", "aws_bucket_name": "test-bucket", "file_path": "test_rt.csv"}}, "sync_enabled": true}, "schema": {"fields": [{"name": "id", "type": "INT32"}, {"name": "name", "type": "STRING"}], "primary_keys": ["id"]}, "sync_enabled": false, "tags": ["test_tag"]}, "type": "reference_table"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Upsert rows returns "Bad Request" response
    Given new "UpsertRows" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"values": {"example_key_value": "primary_key_value", "name": "row_name"}}, "id": "primary_key_value", "type": "row"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Upsert rows returns "Not Found" response
    Given new "UpsertRows" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"values": {"example_key_value": "primary_key_value", "name": "row_name"}}, "id": "primary_key_value", "type": "row"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/redapl-experiences
  Scenario: Upsert rows returns "Rows created or updated successfully" response
    Given new "UpsertRows" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": [{"attributes": {"values": {"example_key_value": "primary_key_value", "name": "row_name"}}, "id": "primary_key_value", "type": "row"}]}
    When the request is sent
    Then the response status is 200 Rows created or updated successfully
