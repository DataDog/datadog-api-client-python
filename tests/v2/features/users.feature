@endpoint(users) @endpoint(users-v2)
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create a service account returns "Bad Request" response
    Given new "CreateServiceAccount" request
    And body with value {"data": {"attributes": {"email": "jane.doe@example.com", "service_account": true}, "relationships": {"roles": {"data": [{"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}]}}, "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: Create a service account returns "OK" response
    Given there is a valid "role" in the system
    And new "CreateServiceAccount" request
    And body with value {"data": {"type": "users", "attributes": {"name": "Test API Client", "email": "{{ unique }}@datadoghq.com", "service_account": true}, "relationships": {"roles": {"data": [{"id": "{{ role.data.id }}", "type": "roles"}]}}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.email" is equal to "{{ unique_lower }}@datadoghq.com"
    And the response "data.attributes.name" is equal to "Test API Client"
    And the response "data.attributes.disabled" is false
    And the response "data.attributes.service_account" is equal to true
    And the response "data.relationships.roles.data[0].id" is equal to "{{ role.data.id }}"

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create a user returns "Bad Request" response
    Given new "CreateUser" request
    And body with value {"data": {"attributes": {"email": "jane.doe@example.com"}, "relationships": {"roles": {"data": [{"id": "3653d3c6-0c75-11ea-ad28-fb5701eabc7d", "type": "roles"}]}}, "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: Create a user returns "OK" response
    Given new "CreateUser" request
    And body with value {"data": {"type": "users", "attributes": {"name": "Datadog API Client Python", "email": "{{ unique }}@datadoghq.com"}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.email" is equal to "{{ unique_lower }}@datadoghq.com"
    And the response "data.attributes.name" is equal to "Datadog API Client Python"
    And the response "data.attributes.disabled" is false
    And the response "data.attributes.service_account" is false

  @generated @skip @team:DataDog/team-aaa
  Scenario: Disable a user returns "Not found" response
    Given new "DisableUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/team-aaa
  Scenario: Disable a user returns "OK" response
    Given there is a valid "user" in the system
    And new "DisableUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get a user invitation returns "Not found" response
    Given new "GetInvitation" request
    And request contains "user_invitation_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/team-aaa
  Scenario: Get a user invitation returns "OK" response
    Given there is a valid "user" in the system
    And the "user" has a "user_invitation"
    And new "GetInvitation" request
    And request contains "user_invitation_uuid" parameter from "user_invitation.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get a user organization returns "Not found" response
    Given new "ListUserOrganizations" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get a user organization returns "OK" response
    Given new "ListUserOrganizations" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get a user permissions returns "Not found" response
    Given new "ListUserPermissions" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/team-aaa
  Scenario: Get a user permissions returns "OK" response
    Given there is a valid "user" in the system
    And new "ListUserPermissions" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/team-aaa
  Scenario: Get a user returns "OK" response
    Given there is a valid "user" in the system
    And new "GetUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK for get user

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get user details returns "Not found" response
    Given new "GetUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get user details returns "OK for get user" response
    Given new "GetUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK for get user

  @generated @skip @team:DataDog/team-aaa
  Scenario: List all users returns "Bad Request" response
    Given new "ListUsers" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: List all users returns "OK" response
    Given there is a valid "user" in the system
    And new "ListUsers" request
    And request contains "filter" parameter from "user.data.attributes.email"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_filtered_count" is equal to 1
    And the response "data[0].attributes.email" has the same value as "user.data.attributes.email"

  @generated @skip @team:DataDog/team-aaa
  Scenario: Send invitation emails returns "Bad Request" response
    Given new "SendInvitations" request
    And body with value {"data": []}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: Send invitation emails returns "OK" response
    Given there is a valid "user" in the system
    And new "SendInvitations" request
    And body with value {"data": [{"type": "user_invitations", "relationships": {"user": {"data": {"type": "{{ user.data.type }}", "id": "{{ user.data.id }}"}}}}]}
    When the request is sent
    Then the response status is 201 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Update a user returns "Bad Request" response
    Given new "UpdateUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "id": "00000000-0000-feed-0000-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: Update a user returns "Bad User ID in Request" response
    Given there is a valid "user" in the system
    And new "UpdateUser" request
    And request contains "user_id" parameter from "user.data.id"
    And body with value {"data": {"id": "00000000-mismatch-body-id-ffffffffffff", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 422 Bad User ID in Request

  @team:DataDog/team-aaa
  Scenario: Update a user returns "Not found" response
    Given new "UpdateUser" request
    And request contains "user_id" parameter with value "00000000-dead-beef-dead-ffffffffffff"
    And body with value {"data": {"id": "00000000-dead-beef-dead-ffffffffffff", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/team-aaa
  Scenario: Update a user returns "OK" response
    Given there is a valid "user" in the system
    And new "UpdateUser" request
    And request contains "user_id" parameter from "user.data.id"
    And body with value {"data": {"id": "{{ user.data.id }}", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.email" has the same value as "user.data.attributes.email"
    And the response "data.attributes.title" has the same value as "user.data.attributes.title"
    And the response "data.attributes.name" is equal to "updated"
    And the response "data.attributes.disabled" is equal to true

  @generated @skip @team:DataDog/team-aaa
  Scenario: Update a user returns "Unprocessable Entity" response
    Given new "UpdateUser" request
    And request contains "user_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "id": "00000000-0000-feed-0000-000000000000", "type": "users"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
