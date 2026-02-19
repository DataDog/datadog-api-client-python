@endpoint(roles) @endpoint(roles-v2)
Feature: Roles
  The Roles API is used to create and manage Datadog roles, what [global
  permissions](https://docs.datadoghq.com/account_management/rbac/) they
  grant, and which users belong to them.  Permissions related to specific
  account assets can be granted to roles in the Datadog application without
  using this API. For example, granting read access on a specific log index
  to a role can be done in Datadog from the [Pipelines
  page](https://app.datadoghq.com/logs/pipelines).  Roles can also be
  managed in bulk through the Datadog UI, which provides the capability to
  assign a single permission to multiple roles simultaneously.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Roles" API

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Add a user to a role returns "Bad Request" response
    Given new "AddUserToRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-2345-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Add a user to a role returns "Not found" response
    Given new "AddUserToRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-2345-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Add a user to a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And new "AddUserToRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "{{ user.data.id}}", "type": "{{ user.data.type }}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].id" is equal to "{{ user.data.id }}"
    And the response "data[0].type" is equal to "{{ user.data.type }}"
    And the response "data[0].relationships.roles.data" has item with field "id" with value "{{ role.data.id }}"

  @team:DataDog/aaa-core-access
  Scenario: Create a new role by cloning an existing role returns "Bad Request" response
    Given there is a valid "role" in the system
    And new "CloneRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"attributes": {"name": "    "}, "type": "roles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-core-access
  Scenario: Create a new role by cloning an existing role returns "Conflict" response
    Given there is a valid "role" in the system
    And new "CloneRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"attributes": {"name": "{{ role.data.attributes.name }}"}, "type": "roles"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Create a new role by cloning an existing role returns "Not found" response
    Given new "CloneRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "cloned-role", "receives_permissions_from": []}, "type": "roles"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Create a new role by cloning an existing role returns "OK" response
    Given there is a valid "role" in the system
    And new "CloneRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"attributes": {"name": "{{ unique }} clone"}, "type": "roles"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ unique }} clone"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Create role returns "Bad Request" response
    Given new "CreateRole" request
    And body with value {"data": {"attributes": {"name": "developers", "receives_permissions_from": []}, "relationships": {"permissions": {"data": [{"type": "permissions"}]}}, "type": "roles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Create role returns "OK" response
    Given new "CreateRole" request
    And body with value {"data": {"attributes": {"name": "developers", "receives_permissions_from": []}, "relationships": {"permissions": {"data": [{"type": "permissions"}]}}, "type": "roles"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-core-access
  Scenario: Create role with a permission returns "OK" response
    Given new "CreateRole" request
    And there is a valid "permission" in the system
    And body with value {"data": {"type": "roles", "attributes": {"name": "{{ unique }}"}, "relationships": {"permissions": {"data": [{"id": "{{ permission.id }}", "type": "{{ permission.type }}"}]}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.type" is equal to "roles"
    And the response "data.relationships.permissions.data" has item with field "id" with value "{{ permission.id }}"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Delete role returns "Not found" response
    Given new "DeleteRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Delete role returns "OK" response
    Given there is a valid "role" in the system
    And new "DeleteRole" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Get a role returns "Not found" response
    Given new "GetRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Get a role returns "OK" response
    Given there is a valid "role" in the system
    And new "GetRole" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK for get role
    And the response "data.attributes.name" has the same value as "role.data.attributes.name"
    And the response "data.id" has the same value as "role.data.id"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Get all users of a role returns "Not found" response
    Given new "ListRoleUsers" request
    And request contains "role_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Get all users of a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And the "user" has the "role"
    And new "ListRoleUsers" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_count" is equal to 1
    And the response "data" has item with field "id" with value "{{ user.data.id }}"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Grant permission to a role returns "Bad Request" response
    Given new "AddPermissionToRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "permissions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Grant permission to a role returns "Not found" response
    Given new "AddPermissionToRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "permissions"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Grant permission to a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And new "AddPermissionToRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "{{ permission.type }}"
    And the response "data" has item with field "id" with value "{{ permission.id }}"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: List permissions for a role returns "Not found" response
    Given new "ListRolePermissions" request
    And request contains "role_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: List permissions for a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And the "permission" is granted to the "role"
    And new "ListRolePermissions" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "{{ permission.type }}"
    And the response "data" has item with field "id" with value "{{ permission.id }}"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: List permissions returns "Bad Request" response
    Given new "ListPermissions" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-core-access
  Scenario: List permissions returns "OK" response
    Given new "ListPermissions" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "attributes.restricted" with value true
    And the response "data" has item with field "attributes.restricted" with value false
    And the response "data" has item with field "attributes.name" with value "admin"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: List role templates returns "OK" response
    Given operation "ListRoleTemplates" enabled
    And new "ListRoleTemplates" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/aaa-core-access
  Scenario: List roles returns "OK" response
    Given there is a valid "role" in the system
    And new "ListRoles" request
    And request contains "filter" parameter from "role.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_filtered_count" is equal to 1
    And the response "data[0].id" has the same value as "role.data.id"
    And the response "data[0].attributes.name" has the same value as "role.data.attributes.name"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Remove a user from a role returns "Bad Request" response
    Given new "RemoveUserFromRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-2345-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Remove a user from a role returns "Not found" response
    Given new "RemoveUserFromRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-2345-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Remove a user from a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And the "user" has the "role"
    And new "RemoveUserFromRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "{{ user.data.id}}", "type": "{{ user.data.type }}"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/aaa-core-access
  Scenario: Revoke permission returns "Bad Request" response
    Given there is a valid "role" in the system
    And new "RemovePermissionFromRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "11111111-dead-beef-dead-ffffffffffff", "type": "bad_permission_type"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-core-access
  Scenario: Revoke permission returns "Not found" response
    Given there is a valid "permission" in the system
    And new "RemovePermissionFromRole" request
    And request contains "role_id" parameter with value "00000000-dead-beef-dead-ffffffffffff"
    And body with value {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/aaa-core-access
  Scenario: Revoke permission returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And the "permission" is granted to the "role"
    And new "RemovePermissionFromRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "permissions"

  @team:DataDog/aaa-core-access
  Scenario: Update a role returns "Bad Request" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And new "UpdateRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "{{ role.data.id }}", "type": "roles", "attributes": {"name" : "{{ role.data.attributes.name }}-updated"}, "relationships": {"permissions": {"data": [{"id": "11111111-dead-beef-dead-ffffffffffff", "type": "{{ permission.type }}"}]}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aaa-core-access
  Scenario: Update a role returns "Bad Role ID" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And new "UpdateRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "00000000-dead-beef-dead-ffffffffffff", "type": "roles", "attributes": {"name" : "{{ role.data.attributes.name }}-updated"}, "relationships": {"permissions": {"data": [{"type": "{{ permission.type }}", "id": "{{ permission.id }}"}]}}}}
    When the request is sent
    Then the response status is 422 Bad Role ID in Request

  @team:DataDog/aaa-core-access
  Scenario: Update a role returns "Not found" response
    Given there is a valid "permission" in the system
    And new "UpdateRole" request
    And request contains "role_id" parameter with value "00000000-dead-beef-dead-ffffffffffff"
    And body with value {"data": {"id": "00000000-dead-beef-dead-ffffffffffff", "type": "roles", "attributes": {"name" : "updated"}, "relationships": {"permissions": {"data": [{"type": "{{ permission.type }}", "id": "{{ permission.id }}"}]}}}}
    When the request is sent
    Then the response status is 404 Not found

  @skip @team:DataDog/aaa-core-access
  Scenario: Update a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And new "UpdateRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body with value {"data": {"id": "{{ role.data.id }}", "type": "roles", "attributes": {"name" : "{{ role.data.attributes.name }}-updated"}, "relationships": {"permissions": {"data": [{"id": "{{ permission.id }}", "type": "{{ permission.type }}"}]}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ role.data.attributes.name }}-updated"

  @generated @skip @team:DataDog/aaa-core-access
  Scenario: Update a role returns "Unprocessable Entity" response
    Given new "UpdateRole" request
    And request contains "role_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"receives_permissions_from": []}, "id": "00000000-0000-1111-0000-000000000000", "relationships": {"permissions": {"data": [{"type": "permissions"}]}}, "type": "roles"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
