@endpoint(actions-datastores) @endpoint(actions-datastores-v2)
Feature: Actions Datastores
  Leverage the Actions Datastore API to create, modify, and delete items in
  datastores owned by your organization.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ActionsDatastores" API

  @team:DataDog/app-builder-backend
  Scenario: Bulk put datastore items returns "Bad Request" response
    Given new "BulkPutDatastoreItems" request
    And a "datastore" is created in the system
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"values": [{"{{datastore.data.attributes.primary_column_name}}": "key1", "value": {"data": "example data 1", "key": "value"}}, {"badPrimaryKey": "key2", "value": {"data": "example data 2", "key": "value"}}]}, "type": "items", "id": "{{datastore.data.id}}"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "item key missing or invalid"

  @team:DataDog/app-builder-backend
  Scenario: Bulk put datastore items returns "Not Found" response
    Given new "BulkPutDatastoreItems" request
    And request contains "datastore_id" parameter with value "70b87c26-886f-497a-bd9d-09f53bc9b40c"
    And body with value {"data": {"attributes": {"values": [{"primaryKey": "key1", "value": {"data": "example data 1", "key": "value"}}, {"primaryKey": "key2", "value": {"data": "example data 2", "key": "value"}}]}, "type": "items", "id": "70b87c26-886f-497a-bd9d-09f53bc9b40c"}}
    When the request is sent
    Then the response status is 404 Not Found
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "datastore not found"

  @team:DataDog/app-builder-backend
  Scenario: Bulk put datastore items returns "OK" response
    Given new "BulkPutDatastoreItems" request
    And a "datastore" is created in the system
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"values": [{"{{datastore.data.attributes.primary_column_name}}": "key1", "value": {"data": "example data 1", "key": "value"}}, {"{{datastore.data.attributes.primary_column_name}}": "key2", "value": {"data": "example data 2", "key": "value"}}]}, "type": "items"}}
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
    And the response "errors[0].title" is equal to "invalid column name"

  @team:DataDog/app-builder-backend
  Scenario: Create datastore from import returns "OK" response
    Given new "CreateDatastoreFromImport" request
    And body with value {"data": {"attributes": {"name": "datastore-name", "primary_column_name": "primaryKey", "values": [{"primaryKey": "key1", "value": {"data": "example data 1", "key": "value"}}, {"primaryKey": "key2", "value": {"data": "example data 2", "key": "value"}}]}, "type": "datastores"}}
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
    And the response "errors[0].title" is equal to "invalid column name"

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

  @team:DataDog/app-builder-backend
  Scenario: Delete datastore item returns "OK" response
    Given new "DeleteDatastoreItem" request
    And a "datastore" is created in the system
    And there is a valid "datastore" in the system
    And a "datastore item" is created in the system
    And there are valid "datastore items" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"id": "{{datastore_items.data[0].id}}", "item_key": "test-key"}, "type": "items", "id": "{{datastore.data.id}}"}}
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

  @skip @team:DataDog/app-builder-backend
  Scenario: Delete datastore returns "Not Found" response
    Given new "DeleteDatastore" request
    And request contains "datastore_id" parameter with value "f4822dc6-3c79-4963-8980-291a65d3b196"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/app-builder-backend
  Scenario: Delete datastore returns "OK" response
    Given new "DeleteDatastore" request
    And a "datastore" is created in the system
    And request contains "datastore_id" parameter from "created_datastore.data.id"
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
    And a "datastore" is created in the system
    And request contains "datastore_id" parameter from "created_datastore.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{created_datastore.data.id}}"

  @team:DataDog/app-builder-backend
  Scenario: List datastore items returns "Bad Request" response
    Given new "ListDatastoreItems" request
    And a "datastore" is created in the system
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

  @team:DataDog/app-builder-backend
  Scenario: List datastore items returns "OK" response
    Given new "ListDatastoreItems" request
    And a "datastore" is created in the system
    And there is a valid "datastore" in the system
    And a "datastore item" is created in the system
    And there are valid "datastore items" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].id" is equal to "{{datastore_items.data[0].id}}"

  @team:DataDog/app-builder-backend
  Scenario: List datastores returns "OK" response
    Given new "ListDatastores" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/app-builder-backend
  Scenario: Put datastore item returns "Bad Request" response
    Given new "PutDatastoreItem" request
    And a "datastore" is created in the system
    And request contains "datastore_id" parameter from "created_datastore.data.id"
    And body with value {"data": {"attributes": {"value": {"missing": "item-key"}}, "type": "items"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].title" is equal to "item key missing or invalid"

  @team:DataDog/app-builder-backend
  Scenario: Put datastore item returns "OK" response
    Given new "PutDatastoreItem" request
    And a "datastore" is created in the system
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"value": {"{{datastore.data.attributes.primary_column_name}}": "new-item-key", "data": "example data", "key": "value"}}, "type": "items", "id": "e7e64418-b60c-4789-9612-895ac8423207"}}
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
    And a "datastore" is created in the system
    And there is a valid "datastore" in the system
    And request contains "datastore_id" parameter from "datastore.data.id"
    And body with value {"data": {"attributes": {"name": "updated name"}, "type": "datastores", "id": "{{datastore.data.id}}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "updated name"
