@endpoint(users) @v2
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  Scenario: Send invitation emails returns "OK" response
    Given there is a valid "user" in the system
    And new "SendInvitations" request
    And body {"data": [{"type": "user_invitations", "relationships": {"user": {"data": {"type": "{{ user.data.type }}", "id": "{{ user.data.id }}"}}}}]}
    When the request is sent
    Then the response status is 201 OK

  Scenario: Get a user invitation returns "OK" response
    Given there is a valid "user" in the system
    And the "user" has a "user_invitation"
    And new "GetInvitation" request
    And request contains "user_invitation_uuid" parameter from "user_invitation.id"
    When the request is sent
    Then the response status is 200 OK

  Scenario: List all users returns "OK" response
    Given there is a valid "user" in the system
    And new "ListUsers" request
    And request contains "filter" parameter from "user.data.attributes.email"
    When the request is sent
    Then the response status is 200 OK
    And the response "meta.page.total_filtered_count" is equal to 1
    And the response "data[0].attributes.email" has the same value as "user.data.attributes.email"

  Scenario: Create a user returns "OK" response
    Given new "CreateUser" request
    And body {"data": {"type": "users", "attributes": {"name": "Datadog API Client Python", "email": "{{ unique }}@datadoghq.com"}}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.email" is equal to "{{ unique_lower }}@datadoghq.com"
    And the response "data.attributes.name" is equal to "Datadog API Client Python"
    And the response "data.attributes.disabled" is false

  Scenario: Disable a user returns "OK" response
    Given there is a valid "user" in the system
    And new "DisableUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get a user returns "OK" response
    Given there is a valid "user" in the system
    And new "GetUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK for get user

  Scenario: Update a user returns "OK" response
    Given there is a valid "user" in the system
    And new "UpdateUser" request
    And request contains "user_id" parameter from "user.data.id"
    And body {"data": {"id": "{{ user.data.id }}", "type": "users", "attributes": {"name": "updated", "disabled": true}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.email" has the same value as "user.data.attributes.email"
    And the response "data.attributes.title" has the same value as "user.data.attributes.title"
    And the response "data.attributes.name" is equal to "updated"
    And the response "data.attributes.disabled" is equal to true

  Scenario: Get a user permissions returns "OK" response
    Given there is a valid "user" in the system
    And new "ListUserPermissions" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a user returns "OK for get user" response
    Given new "GetUser" request
    And request contains "user_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK for get user

  @generated @skip
  Scenario: Get a user organization returns "OK" response
    Given new "ListUserOrganizations" request
    And request contains "user_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK
