@endpoint(google-chat-integration) @endpoint(google-chat-integration-v2)
Feature: Google Chat Integration
  Configure your [Datadog Google Chat
  integration](https://docs.datadoghq.com/integrations/google-hangouts-
  chat/) directly through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "GoogleChatIntegration" API

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create organization handle returns "Bad Request" response
    Given new "CreateOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "space_resource_name": "spaces/AAAAAAAAA"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/chat-integrations
  Scenario: Create organization handle returns "CREATED" response
    Given new "CreateOrganizationHandle" request
    And request contains "organization_binding_id" parameter with value "e54cb570-c674-529c-769d-84b312288ed7"
    And body with value {"data": {"attributes": {"name": "{{unique}}", "space_resource_name": "spaces/AAQA-zFIks8"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{unique}}"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create organization handle returns "Conflict" response
    Given new "CreateOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "space_resource_name": "spaces/AAAAAAAAA"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create organization handle returns "Not Found" response
    Given new "CreateOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "space_resource_name": "spaces/AAAAAAAAA"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete organization handle returns "Bad Request" response
    Given new "DeleteOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/chat-integrations
  Scenario: Delete organization handle returns "OK" response
    Given new "DeleteOrganizationHandle" request
    And there is a valid "organization_handle" in the system
    And request contains "organization_binding_id" parameter with value "e54cb570-c674-529c-769d-84b312288ed7"
    And request contains "handle_id" parameter from "organization_handle.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all organization handles returns "Bad Request" response
    Given new "ListOrganizationHandles" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all organization handles returns "Not Found" response
    Given new "ListOrganizationHandles" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/chat-integrations
  Scenario: Get all organization handles returns "OK" response
    Given new "ListOrganizationHandles" request
    And there is a valid "organization_handle" in the system
    And request contains "organization_binding_id" parameter with value "e54cb570-c674-529c-769d-84b312288ed7"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "google-chat-organization-handle"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get organization handle returns "Bad Request" response
    Given new "GetOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get organization handle returns "Not Found" response
    Given new "GetOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/chat-integrations
  Scenario: Get organization handle returns "OK" response
    Given new "GetOrganizationHandle" request
    And there is a valid "organization_handle" in the system
    And request contains "organization_binding_id" parameter with value "e54cb570-c674-529c-769d-84b312288ed7"
    And request contains "handle_id" parameter from "organization_handle.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "organization_handle.data.attributes.name"
    And the response "data.attributes.space_display_name" has the same value as "organization_handle.data.attributes.space_display_name"
    And the response "data.attributes.space_resource_name" has the same value as "organization_handle.data.attributes.space_resource_name"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get space information by display name returns "Bad Request" response
    Given new "GetSpaceByDisplayName" request
    And request contains "domain_name" parameter from "REPLACE.ME"
    And request contains "space_display_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get space information by display name returns "Not Found" response
    Given new "GetSpaceByDisplayName" request
    And request contains "domain_name" parameter from "REPLACE.ME"
    And request contains "space_display_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/chat-integrations
  Scenario: Get space information by display name returns "OK" response
    Given new "GetSpaceByDisplayName" request
    And request contains "domain_name" parameter with value "datadog.ninja"
    And request contains "space_display_name" parameter with value "api-test-space"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.resource_name" is equal to "spaces/AAQA-zFIks8"
    And the response "data.attributes.organization_binding_id" is equal to "e54cb570-c674-529c-769d-84b312288ed7"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update organization handle returns "Bad Request" response
    Given new "UpdateOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "space_resource_name": "spaces/AAAAAAAAA"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update organization handle returns "Conflict" response
    Given new "UpdateOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "space_resource_name": "spaces/AAAAAAAAA"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update organization handle returns "Not Found" response
    Given new "UpdateOrganizationHandle" request
    And request contains "organization_binding_id" parameter from "REPLACE.ME"
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "space_resource_name": "spaces/AAAAAAAAA"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/chat-integrations
  Scenario: Update organization handle returns "OK" response
    Given new "UpdateOrganizationHandle" request
    And there is a valid "organization_handle" in the system
    And request contains "organization_binding_id" parameter with value "e54cb570-c674-529c-769d-84b312288ed7"
    And request contains "handle_id" parameter from "organization_handle.data.id"
    And body with value {"data": {"attributes": {"name": "{{organization_handle.data.attributes.name}}--updated"}}, "type": "google-chat-organization-handle"}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{organization_handle.data.attributes.name}}--updated"
