@endpoint(users)
Feature: Users
  Create, edit, and disable users. [Read more about team management][1].
  [1]: https://docs.datadoghq.com/account_management/team

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Users" API

  @generated @skip
  Scenario: Get all users returns "OK" response
    Given new "ListUsers" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a user returns "User created" response
    Given new "CreateUser" request
    And body {}
    When the request is sent
    Then the response status is 200 User created

  @generated @skip
  Scenario: Disable a user returns "User disabled" response
    Given new "DisableUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 User disabled

  @generated @skip
  Scenario: Get user details returns "OK for get user" response
    Given new "GetUser" request
    And request contains "user_handle" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK for get user

  @generated @skip
  Scenario: Update a user returns "User updated" response
    Given new "UpdateUser" request
    And request contains "user_handle" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 User updated
