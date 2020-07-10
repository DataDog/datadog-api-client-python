@endpoint(key-management)
Feature: Key Management
  Manage your Datadog API and application keys.  You need an API and
  applications key with Admin rights to interact with this endpoint. The
  full list of keys can be seen on your [Datadog API
  page](https://app.datadoghq.com/account/settings#api).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "KeyManagement" API

  @generated @skip
  Scenario: Get all API keys returns "OK" response
    Given new "ListAPIKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create an API key returns "OK" response
    Given new "CreateAPIKey" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete an API key returns "OK" response
    Given new "DeleteAPIKey" request
    And request contains "key" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get API key returns "OK" response
    Given new "GetAPIKey" request
    And request contains "key" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit an API key returns "OK" response
    Given new "UpdateAPIKey" request
    And request contains "key" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all application keys returns "OK" response
    Given new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create an application key returns "OK" response
    Given new "CreateApplicationKey" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete an application key returns "OK" response
    Given new "DeleteApplicationKey" request
    And request contains "key" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get an application key returns "OK" response
    Given new "GetApplicationKey" request
    And request contains "key" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Edit an application key returns "OK" response
    Given new "UpdateApplicationKey" request
    And request contains "key" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK
