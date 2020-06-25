@v2 @endpoint(users)
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key
    And a valid "appKeyAuth" key
    And an instance of "Users" API

  @todo
  Scenario: Send invitation emails leading to OK
    Given new "SendInvitations" request
    And body {}
    When the request is sent
    Then the status is 201 OK

  @todo
  Scenario: Get a user invitation leading to OK
    Given new "GetInvitation" request
    When the request is sent
    Then the status is 200 OK

  Scenario: List all users leading to OK
    Given new "ListUsers" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Create a user leading to OK
    Given new "CreateUser" request
    And body {"data": {"type": "users", "attributes": {"name": "Datadog API Client Python", "email": "{{ unique }}@datadoghq.com"}}}
    When the request is sent
    Then the status is 201 OK

  Scenario: Disable a user leading to OK
    Given there is a valid user in the system
    And new "DisableUser" request
    And parameter user_id from user.data.id
    When the request is sent
    Then the status is 204 OK

  Scenario: Get a user leading to OK for get user
    Given there is a valid user in the system
    And new "GetUser" request
    And parameter user_id from user.data.id
    When the request is sent
    Then the status is 200 OK for get user

  Scenario: Update a user leading to OK
    Given there is a valid user in the system
    And new "UpdateUser" request
    And parameter user_id from user.data.id
    And body {"data": {"id": "{{ user.data.id }}", "type": "users", "attributes": {"name": "updated"}}}
    When the request is sent
    Then the status is 204 OK

  ## NOTE: to test getting a user organization, we'd need to have a "whoami" API endpoint
  ## to get the UUID of the current user, but there's no such stable endpoint right now
	## (a user can only get organization for itself, never for a different user)
  # Scenario: Get a user organization leading to OK
  #   Given there is a valid user in the system
  #   And new "ListUserOrganizations" request
  #   And parameter user_id from user.data.id
  #   When the request is sent
  #   Then the status is 200 OK

  Scenario: Get a user permissions leading to OK
    Given there is a valid user in the system
    And new "ListUserPermissions" request
    And parameter user_id from user.data.id
    When the request is sent
    Then the status is 200 OK
