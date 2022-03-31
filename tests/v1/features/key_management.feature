@endpoint(key-management) @endpoint(key-management-v1)
Feature: Key Management
  Manage your Datadog API and application keys. You need an API key and an
  application key for a user with the required permissions to interact with
  these endpoints. The full list of API and application keys can be seen on
  your [Datadog API page](https://app.datadoghq.com/account/settings#api).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "KeyManagement" API

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an API key returns "Bad Request" response
    Given new "CreateAPIKey" request
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an API key returns "OK" response
    Given new "CreateAPIKey" request
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an application key returns "Bad Request" response
    Given new "CreateApplicationKey" request
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an application key returns "Conflict" response
    Given new "CreateApplicationKey" request
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an application key returns "OK" response
    Given new "CreateApplicationKey" request
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an API key returns "Bad Request" response
    Given new "DeleteAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an API key returns "Not Found" response
    Given new "DeleteAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an API key returns "OK" response
    Given new "DeleteAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an application key returns "Not Found" response
    Given new "DeleteApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an application key returns "OK" response
    Given new "DeleteApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an API key returns "Bad Request" response
    Given new "UpdateAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an API key returns "Not Found" response
    Given new "UpdateAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an API key returns "OK" response
    Given new "UpdateAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key returns "Bad Request" response
    Given new "UpdateApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key returns "Conflict" response
    Given new "UpdateApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key returns "Not Found" response
    Given new "UpdateApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key returns "OK" response
    Given new "UpdateApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    And body with value {"name": "example user"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get API key returns "Not Found" response
    Given new "GetAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get API key returns "OK" response
    Given new "GetAPIKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all API keys returns "OK" response
    Given new "ListAPIKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys returns "OK" response
    Given new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get an application key returns "Not Found" response
    Given new "GetApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get an application key returns "OK" response
    Given new "GetApplicationKey" request
    And request contains "key" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
