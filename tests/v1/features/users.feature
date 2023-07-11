@endpoint(users) @endpoint(users-v1)
Feature: Users
  Create, edit, and disable users.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Create a user returns "Bad Request" response
    Given new "CreateUser" request
    And body with value {"access_role": "ro", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Create a user returns "Conflict" response
    Given new "CreateUser" request
    And body with value {"access_role": "ro", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Create a user returns "User created" response
    Given new "CreateUser" request
    And body with value {"access_role": "ro", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 200 User created

  @replay-only @team:DataDog/team-aaa-identity
  Scenario: Create a user returns null access role
    Given new "CreateUser" request
    And body with value {"access_role": null, "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 200 User created
    And the response "user.access_role" is equal to null

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Disable a user returns "Bad Request" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Disable a user returns "Not Found" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Disable a user returns "User disabled" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 User disabled

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Get user details returns "Not Found" response
    Given new "GetUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Get user details returns "OK for get user" response
    Given new "GetUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK for get user

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: List all users returns "OK" response
    Given new "ListUsers" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Update a user returns "Bad Request" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    And body with value {"access_role": "ro", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Update a user returns "Not Found" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    And body with value {"access_role": "ro", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa-identity
  Scenario: Update a user returns "User updated" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "REPLACE.ME"
    And body with value {"access_role": "ro", "disabled": false, "email": "test@datadoghq.com", "handle": "test@datadoghq.com", "name": "test user"}
    When the request is sent
    Then the response status is 200 User updated
