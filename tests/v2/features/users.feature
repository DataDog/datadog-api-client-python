@v2 @endpoint(users)
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  @todo
  Scenario: Send invitation emails returns "OK" response
    Given new "SendInvitations" request
    And body {}
    When the request is sent
    Then the response status is 201 OK

  @todo
  Scenario: Get a user invitation returns "OK" response
    Given new "GetInvitation" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: List all users returns "OK" response
    Given new "ListUsers" request
    When the request is sent
    Then the response status is 200 OK

  Scenario: Create a user returns "OK" response
    Given new "CreateUser" request
    And body {"data": {"type": "users", "attributes": {"name": "Datadog API Client Python", "email": "{{ unique }}@datadoghq.com"}}}
    When the request is sent
    Then the response status is 201 OK

  Scenario: Disable a user returns "OK" response
    Given there is a valid user in the system
    And new "DisableUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 204 OK

  Scenario: Get a user returns "OK" response
    Given there is a valid user in the system
    And new "GetUser" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK for get user

  Scenario: Update a user returns "OK" response
    Given there is a valid user in the system
    And new "UpdateUser" request
    And request contains "user_id" parameter from "user.data.id"
    And body {"data": {"id": "{{ user.data.id }}", "type": "users", "attributes": {"name": "updated"}}}
    When the request is sent
    Then the response status is 204 OK

  ## NOTE: to test getting a user organization, we'd need to have a "whoami" API endpoint
  ## to get the UUID of the current user, but there's no such stable endpoint right now
	## (a user can only get organization for itself, never for a different user)
  # Scenario: Get a user organization returns "OK" response
  #   Given there is a valid user in the system
  #   And new "ListUserOrganizations" request
  #   And request contains "user_id" parameter from "user.data.id"
  #   When the request is sent
  #   Then the response status is 200 OK

  Scenario: Get a user permissions returns "OK" response
    Given there is a valid user in the system
    And new "ListUserPermissions" request
    And request contains "user_id" parameter from "user.data.id"
    When the request is sent
    Then the response status is 200 OK
