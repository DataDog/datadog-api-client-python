@v2 @roles @todo
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
    When I execute the request
    Then the status is 200 OK

  Scenario: List roles leading to OK
    Given new "ListRoles" request
    When I execute the request
    Then the status is 200 OK

  Scenario: Create role leading to OK
    Given new "CreateRole" request
    And body {}
    When I execute the request
    Then the status is 200 OK

  Scenario: Delete role leading to OK
    Given new "DeleteRole" request
    When I execute the request
    Then the status is 204 OK

  Scenario: Get a role leading to OK for get role
    Given new "GetRole" request
    When I execute the request
    Then the status is 200 OK for get role

  Scenario: Update a role leading to OK
    Given new "UpdateRole" request
    And body {}
    When I execute the request
    Then the status is 200 OK

  Scenario: Revoke permission leading to OK
    Given new "RemovePermissionFromRole" request
    And body {}
    When I execute the request
    Then the status is 200 OK

  Scenario: List permissions for a role leading to OK
    Given new "ListRolePermissions" request
    When I execute the request
    Then the status is 200 OK

  Scenario: Grant permission to a role leading to OK
    Given new "AddPermissionToRole" request
    And body {}
    When I execute the request
    Then the status is 200 OK

  Scenario: Remove a user from a role leading to OK
    Given new "RemoveUserFromRole" request
    And body {}
    When I execute the request
    Then the status is 200 OK

  Scenario: Get all users of a role leading to OK
    Given new "ListRoleUsers" request
    When I execute the request
    Then the status is 200 OK

  Scenario: Add a user to a role leading to OK
    Given new "AddUserToRole" request
    And body {}
    When I execute the request
    Then the status is 200 OK
