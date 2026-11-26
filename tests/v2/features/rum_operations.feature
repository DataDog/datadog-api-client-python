@endpoint(rum-operations) @endpoint(rum-operations-v2)
Feature: RUM Operations
  Manage [RUM Operations](https://docs.datadoghq.com/real_user_monitoring/),
  business transactions detected from RUM events through a configurable
  journey, and their links to journeys. See the [RUM & Session Replay
  page](https://docs.datadoghq.com/real_user_monitoring/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "RUMOperations" API

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation link returns "Bad Request" response
    Given new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"type": "strong_links", "attributes": {"feature_id": "bdd-{{ unique_lower_alnum }}"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation link returns "Conflict. A link between this operation and journey already exists." response
    Given there is a valid "rum_operation" in the system
    And there is a valid "rum_operation_strong_link" in the system
    And new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"type": "strong_links", "attributes": {"operation_id": "{{ rum_operation_strong_link.data.attributes.operation_id }}", "feature_id": "{{ rum_operation_strong_link.data.attributes.feature_id }}", "status": "DRAFT", "tags": []}}}
    When the request is sent
    Then the response status is 409 Conflict. A link between this operation and journey already exists.

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation link returns "Created" response
    Given there is a valid "rum_operation" in the system
    And new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"type": "strong_links", "attributes": {"operation_id": "{{ rum_operation.data.id }}", "feature_id": "bdd-{{ unique_lower_alnum }}", "status": "DRAFT", "tags": ["team:rum-backend"]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "strong_links"
    And the response "data.attributes.operation_id" is equal to "{{ rum_operation.data.id }}"
    And the response "data.attributes.feature_id" is equal to "bdd-{{ unique_lower_alnum }}"
    And the response "data.attributes.status" is equal to "DRAFT"

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation link returns "Not Found. The referenced `operation_id` does not exist." response
    Given new "CreateRUMOperationStrongLink" request
    And body with value {"data": {"type": "strong_links", "attributes": {"operation_id": "00000000-0000-0000-0000-000000000000", "feature_id": "bdd-{{ unique_lower_alnum }}", "status": "DRAFT", "tags": []}}}
    When the request is sent
    Then the response status is 404 Not Found. The referenced `operation_id` does not exist.

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation returns "Bad Request" response
    Given new "CreateRUMOperation" request
    And body with value {"data": {"type": "operations", "attributes": {"name": "bdd_{{ unique_lower_alnum }}", "display_name": "BDD operation", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "composite": {"kind": "all_of", "predicates": [{"query": "@type:action"}]}}]}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation returns "Conflict. An operation with this name already exists." response
    Given there is a valid "rum_operation" in the system
    And new "CreateRUMOperation" request
    And body with value {"data": {"type": "operations", "attributes": {"name": "{{ rum_operation.data.attributes.name }}", "display_name": "BDD operation", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "nodes": [{"query": "@type:action @action.type:click"}]}, {"type": "stop", "nodes": [{"query": "@type:view"}]}]}}}}
    When the request is sent
    Then the response status is 409 Conflict. An operation with this name already exists.

  @team:ddoghq/rum-backend
  Scenario: Create a RUM operation returns "OK" response
    Given new "CreateRUMOperation" request
    And body with value {"data": {"type": "operations", "attributes": {"name": "bdd_{{ unique_lower_alnum }}", "display_name": "BDD operation", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "nodes": [{"query": "@type:action @action.type:click"}]}, {"type": "stop", "nodes": [{"query": "@type:view"}]}]}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "operations"
    And the response "data.attributes.name" is equal to "bdd_{{ unique_lower_alnum }}"
    And the response "data.attributes.display_name" is equal to "BDD operation"

  @team:ddoghq/rum-backend
  Scenario: Delete a RUM operation link returns "No Content" response
    Given there is a valid "rum_operation" in the system
    And there is a valid "rum_operation_strong_link" in the system
    And new "DeleteRUMOperationStrongLink" request
    And request contains "rum_operation_id" parameter from "rum_operation_strong_link.data.attributes.operation_id"
    And request contains "feature_id" parameter from "rum_operation_strong_link.data.attributes.feature_id"
    When the request is sent
    Then the response status is 204 No Content

  @team:ddoghq/rum-backend
  Scenario: Delete a RUM operation link returns "Not Found" response
    Given new "DeleteRUMOperationStrongLink" request
    And request contains "rum_operation_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "feature_id" parameter with value "bdd-{{ unique_lower_alnum }}"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/rum-backend
  Scenario: Delete a RUM operation returns "No Content" response
    Given there is a valid "rum_operation" in the system
    And new "DeleteRUMOperation" request
    And request contains "rum_operation_id" parameter from "rum_operation.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:ddoghq/rum-backend
  Scenario: Delete a RUM operation returns "Not Found" response
    Given new "DeleteRUMOperation" request
    And request contains "rum_operation_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Get a RUM operation by name returns "Bad Request" response
    Given new "GetRUMOperationByName" request
    And request contains "name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: Get a RUM operation by name returns "Not Found" response
    Given new "GetRUMOperationByName" request
    And request contains "name" parameter with value "bdd_missing_{{ unique_lower_alnum }}"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/rum-backend
  Scenario: Get a RUM operation by name returns "OK" response
    Given there is a valid "rum_operation" in the system
    And new "GetRUMOperationByName" request
    And request contains "name" parameter from "rum_operation.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ rum_operation.data.id }}"

  @team:ddoghq/rum-backend
  Scenario: Get a RUM operation returns "Not Found" response
    Given new "GetRUMOperation" request
    And request contains "rum_operation_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/rum-backend
  Scenario: Get a RUM operation returns "OK" response
    Given there is a valid "rum_operation" in the system
    And new "GetRUMOperation" request
    And request contains "rum_operation_id" parameter from "rum_operation.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ rum_operation.data.id }}"
    And the response "data.attributes.name" is equal to "{{ rum_operation.data.attributes.name }}"

  @team:ddoghq/rum-backend
  Scenario: List RUM operation links returns "Bad Request" response
    Given new "ListRUMOperationStrongLinks" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: List RUM operation links returns "OK" response
    Given there is a valid "rum_operation" in the system
    And there is a valid "rum_operation_strong_link" in the system
    And new "ListRUMOperationStrongLinks" request
    And request contains "operation_id" parameter from "rum_operation.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.feature_id" is equal to "{{ rum_operation_strong_link.data.attributes.feature_id }}"

  @skip-go @skip-java @skip-python @team:ddoghq/rum-backend
  Scenario: Search RUM operations returns "Bad Request" response
    Given new "ListRUMOperations" request
    And request contains "application_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: Search RUM operations returns "OK" response
    Given there is a valid "rum_operation" in the system
    And new "ListRUMOperations" request
    And request contains "query" parameter from "rum_operation.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].id" is equal to "{{ rum_operation.data.id }}"

  @generated @skip @team:ddoghq/rum-backend
  Scenario: Update a RUM operation link returns "Bad Request" response
    Given new "UpdateRUMOperationStrongLink" request
    And request contains "rum_operation_id" parameter from "REPLACE.ME"
    And request contains "feature_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"status": "CONFIRMED"}, "type": "strong_links"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: Update a RUM operation link returns "Not Found" response
    Given new "UpdateRUMOperationStrongLink" request
    And request contains "rum_operation_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "feature_id" parameter with value "bdd-{{ unique_lower_alnum }}"
    And body with value {"data": {"type": "strong_links", "attributes": {"status": "REJECTED"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/rum-backend
  Scenario: Update a RUM operation link returns "OK" response
    Given there is a valid "rum_operation" in the system
    And there is a valid "rum_operation_strong_link" in the system
    And new "UpdateRUMOperationStrongLink" request
    And request contains "rum_operation_id" parameter from "rum_operation_strong_link.data.attributes.operation_id"
    And request contains "feature_id" parameter from "rum_operation_strong_link.data.attributes.feature_id"
    And body with value {"data": {"type": "strong_links", "attributes": {"status": "REJECTED"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.status" is equal to "REJECTED"

  @team:ddoghq/rum-backend
  Scenario: Update a RUM operation returns "Bad Request" response
    Given there is a valid "rum_operation" in the system
    And new "UpdateRUMOperation" request
    And request contains "rum_operation_id" parameter from "rum_operation.data.id"
    And body with value {"data": {"id": "{{ rum_operation.data.id }}", "type": "operations", "attributes": {"name": "{{ rum_operation.data.attributes.name }}", "display_name": "BDD operation", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "composite": {"kind": "all_of", "predicates": [{"query": "@type:action"}]}}]}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:ddoghq/rum-backend
  Scenario: Update a RUM operation returns "Conflict. An operation with this name already exists." response
    Given there is a valid "rum_operation" in the system
    And there is a valid "rum_operation_b" in the system
    And new "UpdateRUMOperation" request
    And request contains "rum_operation_id" parameter from "rum_operation.data.id"
    And body with value {"data": {"id": "{{ rum_operation.data.id }}", "type": "operations", "attributes": {"name": "{{ rum_operation_b.data.attributes.name }}", "display_name": "BDD operation", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "nodes": [{"query": "@type:action @action.type:click"}]}, {"type": "stop", "nodes": [{"query": "@type:view"}]}]}}}}
    When the request is sent
    Then the response status is 409 Conflict. An operation with this name already exists.

  @team:ddoghq/rum-backend
  Scenario: Update a RUM operation returns "Not Found" response
    Given new "UpdateRUMOperation" request
    And request contains "rum_operation_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "operations", "attributes": {"name": "bdd_{{ unique_lower_alnum }}", "display_name": "BDD operation", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "nodes": [{"query": "@type:action @action.type:click"}]}, {"type": "stop", "nodes": [{"query": "@type:view"}]}]}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:ddoghq/rum-backend
  Scenario: Update a RUM operation returns "OK" response
    Given there is a valid "rum_operation" in the system
    And new "UpdateRUMOperation" request
    And request contains "rum_operation_id" parameter from "rum_operation.data.id"
    And body with value {"data": {"id": "{{ rum_operation.data.id }}", "type": "operations", "attributes": {"name": "{{ rum_operation.data.attributes.name }}", "display_name": "BDD operation updated", "tags": ["team:rum-backend"], "journey_rum": {"rum_steps": [{"type": "start", "nodes": [{"query": "@type:action @action.type:click"}]}, {"type": "stop", "nodes": [{"query": "@type:view"}]}]}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.display_name" is equal to "BDD operation updated"
