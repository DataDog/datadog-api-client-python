@endpoint(actions-datastores) @endpoint(actions-datastores-v2)
Feature: Actions Datastores
  Leverage the Actions Datastore API to create, modify, and delete items in
  datastores owned by your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ActionsDatastores" API

  @team:DataDog/app-builder-backend
  Scenario: Bulk write datastore items returns "Bad Request" response
    Given new "BulkWriteDatastoreItems" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"values": [{"id": "cust_3141", "name": "Johnathan"}, {"badPrimaryKey": "key2", "name": "Johnathan"}]}, "type": "items", "id": "{{datastore.data.id}}"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "item key missing or invalid"

  @team:DataDog/app-builder-backend
  Scenario: Bulk write datastore items returns "Not Found" response
    Given new "BulkWriteDatastoreItems" request
    And request contains "datastore_id" parameter with value "70b87c26-886f-497a-bd9d-09f53bc9b40c"
    And body with value {"data": {"attributes": {"values": [{"id": "cust_3141", "name": "Johnathan"}, {"id": "cust_3142", "name": "Mary"}]}, "type": "items", "id": "70b87c26-886f-497a-bd9d-09f53bc9b40c"}}
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore not found"

  @team:DataDog/app-builder-backend
  Scenario: Bulk write datastore items returns "OK" response
    Given new "BulkWriteDatastoreItems" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"values": [{"id": "cust_3141", "name": "Johnathan"}, {"id": "cust_3142", "name": "Mary"}]}, "type": "items"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 2

  @team:DataDog/app-builder-backend
  Scenario: Create datastore from import returns "Bad Request" response
    Given new "CreateDatastoreFromImport" request
    And body with value {"data": {"attributes": {"name": "datastore-name", "primary_column_name": "0invalid_name", "values": [{"primaryKey": "key1", "value": {"data": "example data 1", "key": "value"}}, {"primaryKey": "key2", "value": {"data": "example data 2", "key": "value"}}]}, "type": "datastores"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore configuration invalid"

  @team:DataDog/app-builder-backend
  Scenario: Create datastore from import returns "OK" response
    Given new "CreateDatastoreFromImport" request
    And body with value {"data": {"attributes": {"name": "datastore-name", "primary_column_name": "primaryKey", "values": [{"primaryKey": "key1", "value": "Newton"}, {"primaryKey": "key2", "value": "Leibniz"}]}, "type": "datastores"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.item_count" is equal to 2

  @team:DataDog/app-builder-backend
  Scenario: Create datastore returns "Bad Request" response
    Given new "CreateDatastore" request
    And body with value {"data": {"attributes": {"name": "datastore-name", "primary_column_name": "0invalid_key"}, "type": "datastores"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore configuration invalid"

  @team:DataDog/app-builder-backend
  Scenario: Create datastore returns "OK" response
    Given new "CreateDatastore" request
    And body with value {"data": {"attributes": {"name": "datastore-name", "primary_column_name": "primaryKey"}, "type": "datastores"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/app-builder-backend
  Scenario: Delete datastore item returns "Bad Request" response
    Given new "DeleteDatastoreItem" request
    And request contains "datastore_id" parameter with value "invalid-uuid"
    And body with value {"data": {"attributes": {"item_key": "primaryKey"}, "type": "items", "id": "invalid-uuid"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "invalid path parameter"

  @team:DataDog/app-builder-backend
  Scenario: Delete datastore item returns "Not Found" response
    Given new "DeleteDatastoreItem" request
    And request contains "datastore_id" parameter with value "70b87c26-886f-497a-bd9d-09f53bc9b40c"
    And body with value {"data": {"attributes": {"item_key": "primaryKey"}, "type": "items", "id": "70b87c26-886f-497a-bd9d-09f53bc9b40c"}}
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore not found"

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Delete datastore item returns "OK" response
    Given new "DeleteDatastoreItem" request
    And there is a valid "datastore" in the system
    And there is a valid "datastore_item" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"item_key": "test-key"}, "type": "items", "id": "{{datastore.data.id}}"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/app-builder-backend
  Scenario: Delete datastore returns "Bad Request" response
    Given new "DeleteDatastore" request
    And request contains "datastore_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "invalid path parameter"

  @skip-typescript @skip-validation @team:DataDog/app-builder-backend
  Scenario: Delete datastore returns "OK" response
    Given new "DeleteDatastore" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/app-builder-backend
  Scenario: Get datastore returns "Bad Request" response
    Given new "GetDatastore" request
    And request contains "datastore_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "invalid path parameter"

  @team:DataDog/app-builder-backend
  Scenario: Get datastore returns "Not Found" response
    Given new "GetDatastore" request
    And request contains "datastore_id" parameter with value "5bf53b3f-b230-4b35-ab1a-b39f2633eb22"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore not found"

  @team:DataDog/app-builder-backend
  Scenario: Get datastore returns "OK" response
    Given new "GetDatastore" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{datastore.data.id}}"

  @team:DataDog/app-builder-backend
  Scenario: List datastore items returns "Bad Request" response
    Given new "ListDatastoreItems" request
    And request contains "datastore_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "invalid path parameter"

  @team:DataDog/app-builder-backend
  Scenario: List datastore items returns "Not Found" response
    Given new "ListDatastoreItems" request
    And request contains "datastore_id" parameter with value "3cfdd0b8-c490-4969-8d51-69add64a70ea"
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore not found"

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: List datastore items returns "OK" response
    Given new "ListDatastoreItems" request
    And there is a valid "datastore" in the system
    And there is a valid "datastore_item" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" is equal to "{{datastore_item.data.id}}"

  @team:DataDog/app-builder-backend
  Scenario: List datastores returns "OK" response
    Given new "ListDatastores" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/app-builder-backend
  Scenario: Update datastore returns "Bad Request" response
    Given new "UpdateDatastore" request
    And request contains "datastore_id" parameter with value "invalid-uuid"
    And body with value {"data": {"attributes": {}, "type": "datastores", "id": "invalid-uuid"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "invalid path parameter"

  @team:DataDog/app-builder-backend
  Scenario: Update datastore returns "Not Found" response
    Given new "UpdateDatastore" request
    And request contains "datastore_id" parameter with value "c1eb5bb8-726a-4e59-9a61-ccbb26f95329"
    And body with value {"data": {"attributes": {"name": "updated name"}, "type": "datastores", "id": "c1eb5bb8-726a-4e59-9a61-ccbb26f95329"}}
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore not found"

  @team:DataDog/app-builder-backend
  Scenario: Update datastore returns "OK" response
    Given new "UpdateDatastore" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"name": "updated name"}, "type": "datastores", "id": "{{datastore.data.id}}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "updated name"

  @team:DataDog/app-builder-backend
  Scenario: Write datastore item returns "Bad Request" response
    Given new "WriteDatastoreItem" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"value": {"missing": "item-key"}}, "type": "items"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "item key missing or invalid"

  @skip-typescript @team:DataDog/app-builder-backend
  Scenario: Write datastore item returns "OK" response
    Given new "WriteDatastoreItem" request
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"value": {"id": "new-item-key", "data": "example data", "key": "value"}}, "type": "items", "id": "e7e64418-b60c-4789-9612-895ac8423207"}}
    When the request is sent
    Then the response status is 200 OK
