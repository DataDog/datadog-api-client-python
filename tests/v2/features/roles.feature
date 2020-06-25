@v2 @endpoint(roles)
Feature: Roles
  The Roles API is used to create and manage Datadog roles, what [global
  permissions](https://docs.datadoghq.com/account_management/rbac/) they
  grant, and which users belong to them.  Permissions related to specific
  account assets can be granted to roles in the Datadog application without
  using this API. For example, granting read access on a specific log index
  to a role can be done in Datadog from the [Pipelines
  page](https://app.datadoghq.com/logs/pipelines).

  Background:
    Given a valid "apiKeyAuth" key
    And a valid "appKeyAuth" key
    And an instance of "Roles" API

  Scenario: List permissions leading to OK
    Given new "ListPermissions" request
    When the request is sent
    Then the status is 200 OK

  Scenario: List roles leading to OK
    Given new "ListRoles" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Create role leading to OK
    Given new "CreateRole" request
    And body {"data": {"type": "roles", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the status is 200 OK

  Scenario: Delete role leading to OK
    Given there is a valid role in the system
    And new "DeleteRole" request
    And parameter role_id from role.data.id
    When the request is sent
    Then the status is 204 OK

  Scenario: Get a role leading to OK for get role
    Given there is a valid role in the system
    And new "GetRole" request
    And parameter role_id from role.data.id
    When the request is sent
    Then the status is 200 OK for get role

  Scenario: Update a role leading to OK
    Given there is a valid role in the system
    And new "UpdateRole" request
    And parameter role_id from role.data.id
    And body {"data": {"id": "{{ role.data.id }}", "type": "roles", "attributes": {"name" : "{{ role.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the status is 200 OK

  Scenario: Revoke permission leading to OK
    Given there is a valid role in the system
    And there is a valid permission in the system
    And the permission is granted to the role
    And new "RemovePermissionFromRole" request
    And parameter role_id from role.data.id
    And body {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the status is 200 OK

  Scenario: List permissions for a role leading to OK
    Given there is a valid role in the system
    And there is a valid permission in the system
    And the permission is granted to the role
    And new "ListRolePermissions" request
    And parameter role_id from role.data.id
    When the request is sent
    Then the status is 200 OK

  Scenario: Grant permission to a role leading to OK
    Given there is a valid role in the system
    And there is a valid permission in the system
    And new "AddPermissionToRole" request
    And parameter role_id from role.data.id
    And body {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the status is 200 OK

  Scenario: Remove a user from a role leading to OK
    Given there is a valid role in the system
    And there is a valid user in the system
    And the user has the role
    And new "RemoveUserFromRole" request
    And parameter role_id from role.data.id
    And body {"data": {"id": "{{ user.data.id}}", "type": "{{ user.data.type }}"}}
    When the request is sent
    Then the status is 200 OK

  Scenario: Get all users of a role leading to OK
    Given there is a valid role in the system
    And there is a valid user in the system
    And the user has the role
    And new "ListRoleUsers" request
    And parameter role_id from role.data.id
    When the request is sent
    Then the status is 200 OK

  Scenario: Add a user to a role leading to OK
    Given there is a valid role in the system
    And there is a valid user in the system
    And new "AddUserToRole" request
    And parameter role_id from role.data.id
    And body {"data": {"id": "{{ user.data.id}}", "type": "{{ user.data.type }}"}}
    When the request is sent
    Then the status is 200 OK
