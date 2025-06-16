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

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create Workflows webhook handle returns "Bad Request" response
    Given new "CreateWorkflowsWebhookHandle" request
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create Workflows webhook handle returns "CREATED" response
    Given new "CreateWorkflowsWebhookHandle" request
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create Workflows webhook handle returns "Conflict" response
    Given new "CreateWorkflowsWebhookHandle" request
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create Workflows webhook handle returns "Failed Precondition" response
    Given new "CreateWorkflowsWebhookHandle" request
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create Workflows webhook handle returns "Not Found" response
    Given new "CreateWorkflowsWebhookHandle" request
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 404 Not Found

  @integration-only @team:DataDog/chat-integrations
  Scenario: Create api handle returns "CREATED" response
    Given new "CreateTenantBasedHandle" request
    And body with value {"data": {"attributes": {"channel_id": "19:iD_D2xy_sAa-JV851JJYwIa6mlW9F9Nxm3SLyZq68qY1@thread.tacv2", "name": "{{unique}}", "team_id": "e5f50a58-c929-4fb3-8866-e2cd836de3c2", "tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{unique}}"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create tenant-based handle returns "Bad Request" response
    Given new "CreateTenantBasedHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create tenant-based handle returns "CREATED" response
    Given new "CreateTenantBasedHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create tenant-based handle returns "Conflict" response
    Given new "CreateTenantBasedHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create tenant-based handle returns "Failed Precondition" response
    Given new "CreateTenantBasedHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Create tenant-based handle returns "Not Found" response
    Given new "CreateTenantBasedHandle" request
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/chat-integrations
  Scenario: Create workflow webhook handle returns "CREATED" response
    Given new "CreateWorkflowsWebhookHandle" request
    And body with value {"data": {"attributes": {"name": "{{unique}}", "url": "https://example.logic.azure.com/workflows/123"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.name" is equal to "{{unique}}"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete Workflows webhook handle returns "Bad Request" response
    Given new "DeleteWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete Workflows webhook handle returns "Failed Precondition" response
    Given new "DeleteWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete Workflows webhook handle returns "OK" response
    Given new "DeleteWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @integration-only @team:DataDog/chat-integrations
  Scenario: Delete api handle returns "OK" response
    Given there is a valid "tenant_based_handle" in the system
    And new "DeleteTenantBasedHandle" request
    And request contains "handle_id" parameter from "tenant_based_handle.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete tenant-based handle returns "Bad Request" response
    Given new "DeleteTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete tenant-based handle returns "Failed Precondition" response
    Given new "DeleteTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Delete tenant-based handle returns "OK" response
    Given new "DeleteTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/chat-integrations
  Scenario: Delete workflow webhook handle returns "OK" response
    Given there is a valid "workflows_webhook_handle" in the system
    And new "DeleteWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "workflows_webhook_handle.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get Workflows webhook handle information returns "Bad Request" response
    Given new "GetWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get Workflows webhook handle information returns "Failed Precondition" response
    Given new "GetWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get Workflows webhook handle information returns "Not Found" response
    Given new "GetWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get Workflows webhook handle information returns "OK" response
    Given new "GetWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all Workflows webhook handles returns "Bad Request" response
    Given new "ListWorkflowsWebhookHandles" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all Workflows webhook handles returns "Failed Precondition" response
    Given new "ListWorkflowsWebhookHandles" request
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all Workflows webhook handles returns "Not Found" response
    Given new "ListWorkflowsWebhookHandles" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all Workflows webhook handles returns "OK" response
    Given new "ListWorkflowsWebhookHandles" request
    When the request is sent
    Then the response status is 200 OK

  @integration-only @team:DataDog/chat-integrations
  Scenario: Get all api handles returns "OK" response
    Given there is a valid "tenant_based_handle" in the system
    And new "ListTenantBasedHandles" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "ms-teams-tenant-based-handle-info"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all tenant-based handles returns "Bad Request" response
    Given new "ListTenantBasedHandles" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all tenant-based handles returns "Failed Precondition" response
    Given new "ListTenantBasedHandles" request
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all tenant-based handles returns "Not Found" response
    Given new "ListTenantBasedHandles" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get all tenant-based handles returns "OK" response
    Given new "ListTenantBasedHandles" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/chat-integrations
  Scenario: Get all workflow webhook handles returns "OK" response
    Given there is a valid "workflows_webhook_handle" in the system
    And new "ListWorkflowsWebhookHandles" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "workflows-webhook-handle"

  @integration-only @team:DataDog/chat-integrations
  Scenario: Get api handle information returns "OK" response
    Given there is a valid "tenant_based_handle" in the system
    And new "GetTenantBasedHandle" request
    And request contains "handle_id" parameter from "tenant_based_handle.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" has the same value as "tenant_based_handle.data.attributes.name"
    And the response "data.attributes.channel_id" has the same value as "tenant_based_handle.data.attributes.channel_id"
    And the response "data.attributes.team_id" has the same value as "tenant_based_handle.data.attributes.team_id"
    And the response "data.attributes.tenant_id" has the same value as "tenant_based_handle.data.attributes.tenant_id"

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
  Scenario: Get tenant-based handle information returns "Bad Request" response
    Given new "GetTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get tenant-based handle information returns "Failed Precondition" response
    Given new "GetTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get tenant-based handle information returns "Not Found" response
    Given new "GetTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Get tenant-based handle information returns "OK" response
    Given new "GetTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/chat-integrations
  Scenario: Get workflow webhook handle information returns "OK" response
    Given there is a valid "workflows_webhook_handle" in the system
    And new "GetWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "workflows_webhook_handle.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update Workflows webhook handle returns "Bad Request" response
    Given new "UpdateWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update Workflows webhook handle returns "Conflict" response
    Given new "UpdateWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update Workflows webhook handle returns "Failed Precondition" response
    Given new "UpdateWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update Workflows webhook handle returns "Not Found" response
    Given new "UpdateWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update Workflows webhook handle returns "OK" response
    Given new "UpdateWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "fake-handle-name", "url": "https://fake.url.com"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 200 OK

  @integration-only @team:DataDog/chat-integrations
  Scenario: Update api handle returns "OK" response
    Given there is a valid "tenant_based_handle" in the system
    And new "UpdateTenantBasedHandle" request
    And request contains "handle_id" parameter from "tenant_based_handle.data.id"
    And body with value {"data": {"attributes": {"name": "{{tenant_based_handle.data.attributes.name}}--updated"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{tenant_based_handle.data.attributes.name}}--updated"

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update tenant-based handle returns "Bad Request" response
    Given new "UpdateTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update tenant-based handle returns "Conflict" response
    Given new "UpdateTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update tenant-based handle returns "Failed Precondition" response
    Given new "UpdateTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 412 Failed Precondition

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update tenant-based handle returns "Not Found" response
    Given new "UpdateTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/chat-integrations
  Scenario: Update tenant-based handle returns "OK" response
    Given new "UpdateTenantBasedHandle" request
    And request contains "handle_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"channel_id": "fake-channel-id", "name": "fake-handle-name", "team_id": "00000000-0000-0000-0000-000000000000", "tenant_id": "00000000-0000-0000-0000-000000000001"}, "type": "tenant-based-handle"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/chat-integrations
  Scenario: Update workflow webhook handle returns "OK" response
    Given there is a valid "workflows_webhook_handle" in the system
    And new "UpdateWorkflowsWebhookHandle" request
    And request contains "handle_id" parameter from "workflows_webhook_handle.data.id"
    And body with value {"data": {"attributes": {"name": "{{workflows_webhook_handle.data.attributes.name}}--updated"}, "type": "workflows-webhook-handle"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "{{workflows_webhook_handle.data.attributes.name}}--updated"
