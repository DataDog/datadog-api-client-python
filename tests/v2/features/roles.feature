@endpoint(roles) @v2
Feature: Roles
  The Roles API is used to create and manage Datadog roles, what [global
  permissions](https://docs.datadoghq.com/account_management/rbac/) they
  grant, and which users belong to them.  Permissions related to specific
  account assets can be granted to roles in the Datadog application without
  using this API. For example, granting read access on a specific log index
  to a role can be done in Datadog from the [Pipelines
  page](https://app.datadoghq.com/logs/pipelines).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Roles" API

  Scenario: List permissions returns "OK" response
    Given new "ListPermissions" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: List roles returns "OK" response
    Given there is a valid "role" in the system
    And new "ListRoles" request
    And request contains "filter" parameter from "role.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_filtered_count" is equal to 1
    And the response "data[0].id" has the same value as "role.data.id"
    And the response "data[0].attributes.name" has the same value as "role.data.attributes.name"

  Scenario: Create role returns "OK" response
    Given new "CreateRole" request
    And body {"data": {"type": "roles", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ unique }}"

  Scenario: Delete role returns "OK" response
    Given there is a valid "role" in the system
    And new "DeleteRole" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get a role returns "OK" response
    Given there is a valid "role" in the system
    And new "GetRole" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK for get role
    And the response "data.attributes.name" has the same value as "role.data.attributes.name"

  Scenario: Update a role returns "OK" response
    Given there is a valid "role" in the system
    And new "UpdateRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body {"data": {"id": "{{ role.data.id }}", "type": "roles", "attributes": {"name" : "{{ role.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ role.data.attributes.name }}-updated"

  Scenario: Revoke permission returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And the "permission" is granted to the "role"
    And new "RemovePermissionFromRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the response status is 200 OK

  Scenario: List permissions for a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And the "permission" is granted to the "role"
    And new "ListRolePermissions" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK

  Scenario: Grant permission to a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "permission" in the system
    And new "AddPermissionToRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body {"data": {"id": "{{ permission.id }}", "type": "{{ permission.type }}"}}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Remove a user from a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And the "user" has the "role"
    And new "RemoveUserFromRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body {"data": {"id": "{{ user.data.id}}", "type": "{{ user.data.type }}"}}
    When the request is sent
    Then the response status is 200 OK

  Scenario: Get all users of a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And the "user" has the "role"
    And new "ListRoleUsers" request
    And request contains "role_id" parameter from "role.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_count" is equal to 1

  Scenario: Add a user to a role returns "OK" response
    Given there is a valid "role" in the system
    And there is a valid "user" in the system
    And new "AddUserToRole" request
    And request contains "role_id" parameter from "role.data.id"
    And body {"data": {"id": "{{ user.data.id}}", "type": "{{ user.data.type }}"}}
    When the request is sent
    Then the response status is 200 OK
