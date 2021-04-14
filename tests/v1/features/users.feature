@endpoint(users)
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  @generated @skip
  Scenario: Create a user returns "Bad Request" response
    Given new "CreateUser" request
    And body {"access_role": "st", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "icon": "/path/to/matching/gravatar/icon", "name": "test user", "verified": true}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a user returns "Conflict" response
    Given new "CreateUser" request
    And body {"access_role": "st", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "icon": "/path/to/matching/gravatar/icon", "name": "test user", "verified": true}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip
  Scenario: Create a user returns "User created" response
    Given new "CreateUser" request
    And body {"access_role": "st", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "icon": "/path/to/matching/gravatar/icon", "name": "test user", "verified": true}
    When the request is sent
    Then the response status is 200 User created

  @generated @skip
  Scenario: Disable a user returns "Bad Request" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Disable a user returns "Not Found" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Disable a user returns "User disabled" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 User disabled

  @generated @skip
  Scenario: Get user details returns "Not Found" response
    Given new "GetUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get user details returns "OK for get user" response
    Given new "GetUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK for get user

  @generated @skip
  Scenario: List all users returns "OK" response
    Given new "ListUsers" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a user returns "Bad Request" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "<PATH>"
    And body {"access_role": "st", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "icon": "/path/to/matching/gravatar/icon", "name": "test user", "verified": true}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a user returns "Not Found" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "<PATH>"
    And body {"access_role": "st", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "icon": "/path/to/matching/gravatar/icon", "name": "test user", "verified": true}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update a user returns "User updated" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "<PATH>"
    And body {"access_role": "st", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "icon": "/path/to/matching/gravatar/icon", "name": "test user", "verified": true}
    When the request is sent
    Then the response status is 200 User updated
