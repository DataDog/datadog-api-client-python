@endpoint(key-management)
Feature: Key Management
  Manage your Datadog API and application keys. You need an API key and an
  application key for a user with the required permissions to interact with
  these endpoints. The full list of API and application keys can be seen on
  your [Datadog API page](https://app.datadoghq.com/account/settings#api).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "KeyManagement" API

  @integration-only
  Scenario: Get all API keys returns "OK" response
    Given there is a valid "api_key" in the system
    And new "ListAPIKeys" request
    And request contains "filter" parameter from "api_key.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK

  @integration-only
  Scenario: Create an API key returns "Created" response
    Given new "CreateAPIKey" request
    And body {"data": {"type": "api_keys", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 Created

  @integration-only
  Scenario: Delete an API key returns "No Content" response
    Given there is a valid "api_key" in the system
    And new "DeleteAPIKey" request
    And request contains "api_key_id" parameter from "api_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @integration-only
  Scenario: Get API key returns "OK" response
    Given there is a valid "api_key" in the system
    And new "GetAPIKey" request
    And request contains "api_key_id" parameter from "api_key.data.id"
    When the request is sent
    Then the response status is 200 OK

  @integration-only
  Scenario: Edit an API key returns "OK" response
    Given there is a valid "api_key" in the system
    And new "UpdateAPIKey" request
    And request contains "api_key_id" parameter from "api_key.data.id"
    And body {"data": {"type": "api_keys", "id": "{{ api_key.data.id }}", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 200 OK

  @skip
  Scenario: Get all Application keys returns "OK" response
    Given new "ListApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @skip
  Scenario: Delete an Application key returns "No Content" response
    Given there is a valid "application_key" in the system
    And new "DeleteApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip
  Scenario: Get all Application keys owned by current user returns "OK" response
    Given new "ListCurrentUserApplicationKeys" request
    When the request is sent
    Then the response status is 200 OK

  @skip
  Scenario: Create an Application key for current user returns "Created" response
    Given new "CreateCurrentUserApplicationKey" request
    And body {"data": {"type": "application_keys", "attributes": {"name": "{{ unique }}"}}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @skip
  Scenario: Delete an Application key owned by current user returns "No Content" response
    Given there is a valid "application_key" in the system
    And new "DeleteCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip
  Scenario: Get one Application key owned by current user returns "OK" response
    Given there is a valid "application_key" in the system
    And new "GetCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "application_key.data.attributes.name"

  @skip
  Scenario: Edit an application key owned by current user returns "OK" response
    Given there is a valid "application_key" in the system
    And new "UpdateCurrentUserApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    And body {"data": {"id": "{{ application_key.data.id }}", "type": "application_keys", "attributes": {"name" : "{{ application_key.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ application_key.data.attributes.name }}-updated"

  @skip
  Scenario: Edit an application key returns "OK" response
    Given there is a valid "application_key" in the system
    And new "UpdateApplicationKey" request
    And request contains "app_key_id" parameter from "application_key.data.id"
    And body {"data": {"id": "{{ application_key.data.id }}", "type": "application_keys", "attributes": {"name" : "{{ application_key.data.attributes.name }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{ application_key.data.attributes.name }}-updated"
