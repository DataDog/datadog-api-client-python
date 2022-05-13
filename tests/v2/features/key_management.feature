@endpoint(key-management) @endpoint(key-management-v2)
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
    And body with value {"data": {"attributes": {"name": "API Key for submitting metrics"}, "type": "api_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: Create an API key returns "Created" response
    Given new "CreateAPIKey" request
    And body with value {"data": {"type": "api_keys", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/team-aaa
  Scenario: Create an Application key for current user returns "Created" response
    Given new "CreateCurrentUserApplicationKey" request
    And body with value {"data": {"type": "application_keys", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @team:DataDog/team-aaa
  Scenario: Create an Application key with scopes for current user returns "Created" response
    Given new "CreateCurrentUserApplicationKey" request
    And body with value {"data": {"type": "application_keys", "attributes": {"name": "{{ unique }}", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.scopes" is equal to ["dashboards_read", "dashboards_write", "dashboards_public_share"]

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an application key for current user returns "Bad Request" response
    Given new "CreateCurrentUserApplicationKey" request
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "type": "application_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Create an application key for current user returns "Created" response
    Given new "CreateCurrentUserApplicationKey" request
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "type": "application_keys"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/team-aaa
  Scenario: Delete an API key returns "No Content" response
    Given there is a valid "api_key" in the system
    And new "DeleteAPIKey" request
    And request contains "api_key_id" parameter from "api_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an API key returns "Not Found" response
    Given new "DeleteAPIKey" request
    And request contains "api_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Delete an Application key owned by current user returns "No Content" response
    Given there is a valid "application_key" in the system
    And new "DeleteCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/team-aaa
  Scenario: Delete an Application key returns "No Content" response
    Given there is a valid "application_key" in the system
    And new "DeleteApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an application key owned by current user returns "No Content" response
    Given new "DeleteCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an application key owned by current user returns "Not Found" response
    Given new "DeleteCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an application key returns "No Content" response
    Given new "DeleteApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaa
  Scenario: Delete an application key returns "Not Found" response
    Given new "DeleteApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an API key returns "Bad Request" response
    Given new "UpdateAPIKey" request
    And request contains "api_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "API Key for submitting metrics"}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "api_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an API key returns "Not Found" response
    Given new "UpdateAPIKey" request
    And request contains "api_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "API Key for submitting metrics"}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "api_keys"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Edit an API key returns "OK" response
    Given there is a valid "api_key" in the system
    And new "UpdateAPIKey" request
    And request contains "api_key_id" parameter from "api_key.data.id"
    And body with value {"data": {"type": "api_keys", "id": "{{ api_key.data.id }}", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key owned by current user returns "Bad Request" response
    Given new "UpdateCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "application_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key owned by current user returns "Not Found" response
    Given new "UpdateCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "application_keys"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Edit an application key owned by current user returns "OK" response
    Given there is a valid "application_key" in the system
    And new "UpdateCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    And body with value {"data": {"id": "{{ application_key.data.id }}", "type": "application_keys", "attributes": {"name" : "{{ application_key.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ application_key.data.attributes.name }}-updated"

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key returns "Bad Request" response
    Given new "UpdateApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "application_keys"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Edit an application key returns "Not Found" response
    Given new "UpdateApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Application Key for managing dashboards", "scopes": ["dashboards_read", "dashboards_write", "dashboards_public_share"]}, "id": "00112233-4455-6677-8899-aabbccddeeff", "type": "application_keys"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Edit an application key returns "OK" response
    Given there is a valid "application_key" in the system
    And new "UpdateApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    And body with value {"data": {"id": "{{ application_key.data.id }}", "type": "application_keys", "attributes": {"name" : "{{ application_key.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ application_key.data.attributes.name }}-updated"

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get API key returns "Not Found" response
    Given new "GetAPIKey" request
    And request contains "api_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Get API key returns "OK" response
    Given there is a valid "api_key" in the system
    And new "GetAPIKey" request
    And request contains "api_key_id" parameter from "api_key.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all API keys returns "Bad Request" response
    Given new "ListAPIKeys" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/team-aaa
  Scenario: Get all API keys returns "OK" response
    Given there is a valid "api_key" in the system
    And new "ListAPIKeys" request
    And request contains "filter" parameter from "api_key.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/team-aaa
  Scenario: Get all Application keys owned by current user returns "OK" response
    Given new "ListCurrentUserApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/team-aaa
  Scenario: Get all Application keys returns "OK" response
    Given there is a valid "application_key" in the system
    And new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys owned by current user returns "Bad Request" response
    Given new "ListCurrentUserApplicationKeys" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys owned by current user returns "Not Found" response
    Given new "ListCurrentUserApplicationKeys" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys owned by current user returns "OK" response
    Given new "ListCurrentUserApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys returns "Bad Request" response
    Given new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys returns "Not Found" response
    Given new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get all application keys returns "OK" response
    Given new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get an application key returns "Bad Request" response
    Given new "GetApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get an application key returns "Not Found" response
    Given new "GetApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/team-aaa
  Scenario: Get an application key returns "OK" response
    Given there is a valid "application_key" in the system
    And new "GetApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/team-aaa
  Scenario: Get one Application key owned by current user returns "OK" response
    Given there is a valid "application_key" in the system
    And new "GetCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "application_key.data.attributes.name"

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get one application key owned by current user returns "Not Found" response
    Given new "GetCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaa
  Scenario: Get one application key owned by current user returns "OK" response
    Given new "GetCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
