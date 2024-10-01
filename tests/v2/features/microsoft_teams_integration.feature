@endpoint(microsoft-teams-integration) @endpoint(microsoft-teams-integration-v2)
Feature: Microsoft Teams Integration
  Configure your [Datadog Microsoft Teams
  integration](https://docs.datadoghq.com/integrations/microsoft_teams/)
  directly through the Datadog API. Note: These endpoints do not support
  legacy connector handles.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "MicrosoftTeamsIntegration" API

  @team:DataDog/chat-integrations
  Scenario: Create api handle returns "CREATED" response
    Given new "CreateApiHandle" request
    And body with value {"data": {"attributes": {"channel_id": "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2", "name": "{{unique}}", "team_id": "e5f50a58-c929-4fb3-8866-e2cd836de3c2", "tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97"}, "type": "handle"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{unique}}"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create handle returns "Bad Request" response
    Given new "CreateApiHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create handle returns "CREATED" response
    Given new "CreateApiHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create handle returns "Conflict" response
    Given new "CreateApiHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create handle returns "Failed Precondition" response
    Given new "CreateApiHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create handle returns "Not Found" response
    Given new "CreateApiHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/chat-integrations
  Scenario: Delete api handle returns "OK" response
    Given there is a valid "api_handle" in the system
    And new "DeleteApiHandle" request
    And request contains "handle_id" parameter from "api_handle.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete handle returns "Bad Request" response
    Given new "DeleteApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete handle returns "Failed Precondition" response
    Given new "DeleteApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete handle returns "OK" response
    Given new "DeleteApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/chat-integrations
  Scenario: Get all api handles returns "OK" response
    Given there is a valid "api_handle" in the system
    And new "ListApiHandles" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "ms-teams-handle-info"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all handles returns "Bad Request" response
    Given new "ListApiHandles" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all handles returns "Failed Precondition" response
    Given new "ListApiHandles" request
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all handles returns "Not Found" response
    Given new "ListApiHandles" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all handles returns "OK" response
    Given new "ListApiHandles" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/chat-integrations
  Scenario: Get api handle information by name returns "OK" response
    Given there is a valid "api_handle" in the system
    And new "GetApiHandleByName" request
    And request contains "handle_name" parameter from "api_handle.data.attributes.name"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.channel_id" has the same value as "api_handle.data.attributes.channel_id"
    And the response "data.attributes.team_id" has the same value as "api_handle.data.attributes.team_id"
    And the response "data.attributes.tenant_id" has the same value as "api_handle.data.attributes.tenant_id"

  @team:DataDog/chat-integrations
  Scenario: Get api handle information returns "OK" response
    Given there is a valid "api_handle" in the system
    And new "GetApiHandle" request
    And request contains "handle_id" parameter from "api_handle.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "api_handle.data.attributes.name"
    And the response "data.attributes.channel_id" has the same value as "api_handle.data.attributes.channel_id"
    And the response "data.attributes.team_id" has the same value as "api_handle.data.attributes.team_id"
    And the response "data.attributes.tenant_id" has the same value as "api_handle.data.attributes.tenant_id"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get channel information by name returns "Bad Request" response
    Given new "GetChannelByName" request
    And request contains "tenant_name" parameter from "REPLACE.ME"
    And request contains "team_name" parameter from "REPLACE.ME"
    And request contains "channel_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get channel information by name returns "Not Found" response
    Given new "GetChannelByName" request
    And request contains "tenant_name" parameter from "REPLACE.ME"
    And request contains "team_name" parameter from "REPLACE.ME"
    And request contains "channel_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get channel information by name returns "OK" response
    Given new "GetChannelByName" request
    And request contains "tenant_name" parameter from "REPLACE.ME"
    And request contains "team_name" parameter from "REPLACE.ME"
    And request contains "channel_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information by name returns "Bad Request" response
    Given new "GetApiHandleByName" request
    And request contains "handle_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information by name returns "Failed Precondition" response
    Given new "GetApiHandleByName" request
    And request contains "handle_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information by name returns "Not Found" response
    Given new "GetApiHandleByName" request
    And request contains "handle_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information by name returns "OK" response
    Given new "GetApiHandleByName" request
    And request contains "handle_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information returns "Bad Request" response
    Given new "GetApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information returns "Failed Precondition" response
    Given new "GetApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information returns "Not Found" response
    Given new "GetApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get handle information returns "OK" response
    Given new "GetApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/chat-integrations
  Scenario: Update api handle returns "OK" response
    Given there is a valid "api_handle" in the system
    And new "UpdateApiHandle" request
    And request contains "handle_id" parameter from "api_handle.data.id"
    And body with value {"data": {"attributes": {"name": "{{api_handle.data.attributes.name}}--updated"}, "type": "handle"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{api_handle.data.attributes.name}}--updated"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update handle returns "Bad Request" response
    Given new "UpdateApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update handle returns "Conflict" response
    Given new "UpdateApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update handle returns "Failed Precondition" response
    Given new "UpdateApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update handle returns "Not Found" response
    Given new "UpdateApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update handle returns "OK" response
    Given new "UpdateApiHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "handle"}}
    When the request is sent
    Then the response status is 200 OK
