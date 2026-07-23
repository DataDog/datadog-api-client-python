@endpoint(rum-operations) @endpoint(rum-operations-v2)
Feature: RUM Operations
  Manage [RUM Operations](https://docs.datadoghq.com/real_user_monitoring/),
  business transactions detected from RUM events through a configurable
  journey, and their strong links to features. See the [RUM & Session Replay
  page](https://docs.datadoghq.com/real_user_monitoring/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMOperations" API

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation returns "Bad Request" response
    Given operation "CreateRUMOperation" enabled
    And new "CreateRUMOperation" request
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "type": "operations"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation returns "Conflict. An operation with this name already exists." response
    Given operation "CreateRUMOperation" enabled
    And new "CreateRUMOperation" request
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "type": "operations"}}
    When the request is sent
    Then the response status is 409 Conflict. An operation with this name already exists.

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation returns "OK" response
    Given operation "CreateRUMOperation" enabled
    And new "CreateRUMOperation" request
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "type": "operations"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation strong link returns "Bad Request" response
    Given operation "CreateRUMOperationStrongLink" enabled
    And new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"attributes": {"description": null, "feature_id": "feature-123", "operation_id": "abc12345-1234-5678-abcd-ef1234567890", "status": "CONFIRMED", "tags": []}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation strong link returns "Conflict. A strong link between this operation and feature already exists." response
    Given operation "CreateRUMOperationStrongLink" enabled
    And new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"attributes": {"description": null, "feature_id": "feature-123", "operation_id": "abc12345-1234-5678-abcd-ef1234567890", "status": "CONFIRMED", "tags": []}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 409 Conflict. A strong link between this operation and feature already exists.

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation strong link returns "Created" response
    Given operation "CreateRUMOperationStrongLink" enabled
    And new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"attributes": {"description": null, "feature_id": "feature-123", "operation_id": "abc12345-1234-5678-abcd-ef1234567890", "status": "CONFIRMED", "tags": []}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/rum-backend
  Scenario: Create a RUM operation strong link returns "Not Found. The referenced `operation_id` does not exist." response
    Given operation "CreateRUMOperationStrongLink" enabled
    And new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"attributes": {"description": null, "feature_id": "feature-123", "operation_id": "abc12345-1234-5678-abcd-ef1234567890", "status": "CONFIRMED", "tags": []}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 404 Not Found. The referenced `operation_id` does not exist.

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM operation returns "No Content" response
    Given operation "DeleteRUMOperation" enabled
    And new "DeleteRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM operation returns "Not Found" response
    Given operation "DeleteRUMOperation" enabled
    And new "DeleteRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM operation strong link returns "No Content" response
    Given operation "DeleteRUMOperationStrongLink" enabled
    And new "DeleteRUMOperationStrongLink" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And request contains "feature_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/rum-backend
  Scenario: Delete a RUM operation strong link returns "Not Found" response
    Given operation "DeleteRUMOperationStrongLink" enabled
    And new "DeleteRUMOperationStrongLink" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And request contains "feature_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM operation by name returns "Bad Request" response
    Given operation "GetRUMOperationByName" enabled
    And new "GetRUMOperationByName" request
    And request contains "name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM operation by name returns "Not Found" response
    Given operation "GetRUMOperationByName" enabled
    And new "GetRUMOperationByName" request
    And request contains "name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM operation by name returns "OK" response
    Given operation "GetRUMOperationByName" enabled
    And new "GetRUMOperationByName" request
    And request contains "name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM operation returns "Not Found" response
    Given operation "GetRUMOperation" enabled
    And new "GetRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Get a RUM operation returns "OK" response
    Given operation "GetRUMOperation" enabled
    And new "GetRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: List RUM operation strong links returns "Bad Request" response
    Given operation "ListRUMOperationStrongLinks" enabled
    And new "ListRUMOperationStrongLinks" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: List RUM operation strong links returns "OK" response
    Given operation "ListRUMOperationStrongLinks" enabled
    And new "ListRUMOperationStrongLinks" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Search RUM operations returns "Bad Request" response
    Given operation "ListRUMOperations" enabled
    And new "ListRUMOperations" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Search RUM operations returns "OK" response
    Given operation "ListRUMOperations" enabled
    And new "ListRUMOperations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation returns "Bad Request" response
    Given operation "UpdateRUMOperation" enabled
    And new "UpdateRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "operations"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation returns "Conflict. An operation with this name already exists." response
    Given operation "UpdateRUMOperation" enabled
    And new "UpdateRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "operations"}}
    When the request is sent
    Then the response status is 409 Conflict. An operation with this name already exists.

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation returns "Not Found" response
    Given operation "UpdateRUMOperation" enabled
    And new "UpdateRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "operations"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation returns "OK" response
    Given operation "UpdateRUMOperation" enabled
    And new "UpdateRUMOperation" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"application_id": null, "category": null, "description": null, "display_name": "Checkout completed", "feature_ids": [], "journey_rum": {"rum_steps": [{"composite": {"kind": "all_of", "max_window_ms": 30000, "predicates": [{"query": "@type:action @action.type:click"}]}, "nodes": [{"query": "@type:action @action.type:click"}], "type": "start"}]}, "name": "checkout_completed", "tags": ["team:checkout"]}, "id": "abc12345-1234-5678-abcd-ef1234567890", "type": "operations"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation strong link returns "Bad Request" response
    Given operation "UpdateRUMOperationStrongLink" enabled
    And new "UpdateRUMOperationStrongLink" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And request contains "feature_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "CONFIRMED"}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation strong link returns "Not Found" response
    Given operation "UpdateRUMOperationStrongLink" enabled
    And new "UpdateRUMOperationStrongLink" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And request contains "feature_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "CONFIRMED"}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/rum-backend
  Scenario: Update a RUM operation strong link returns "OK" response
    Given operation "UpdateRUMOperationStrongLink" enabled
    And new "UpdateRUMOperationStrongLink" request
    And request contains "operation_id" parameter from "REPLACE.ME"
    And request contains "feature_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "CONFIRMED"}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 200 OK
