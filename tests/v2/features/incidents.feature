@endpoint(incidents) @endpoint(incidents-v2)
Feature: Incidents
  Manage incident response, as well as associated attachments, metadata, and
  todos. See the [Incident Management
  page](https://docs.datadoghq.com/service_management/incident_management/)
  for more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Incidents" API

  @team:DataDog/incident-app
  Scenario: Add commander to an incident returns "OK" response
    Given operation "UpdateIncident" enabled
    And there is a valid "user" in the system
    And there is a valid "incident" in the system
    And new "UpdateIncident" request
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"id": "{{incident.data.id}}", "type": "incidents", "relationships": {"commander_user": {"data": {"id": "{{user.data.id}}", "type": "users"}}}}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/incident-app
  Scenario: Create an incident impact returns "Bad Request" response
    Given operation "CreateIncidentImpact" enabled
    And new "CreateIncidentImpact" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"description": "Service was unavailable for external users", "end_at": "2025-08-29T13:17:00Z", "fields": {"customers_impacted": "all", "products_impacted": ["shopping", "marketing"]}, "start_at": "2025-08-28T13:17:00Z"}, "type": "incident_impacts"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/incident-app
  Scenario: Create an incident impact returns "CREATED" response
    Given there is a valid "incident" in the system
    And operation "CreateIncidentImpact" enabled
    And new "CreateIncidentImpact" request
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"type": "incident_impacts", "attributes": {"start_at": "2025-09-12T13:50:00.000Z", "end_at": "2025-09-12T14:50:00.000Z", "description": "Outage in the us-east-1 region"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.type" is equal to "incident_impacts"
    And the response "data.relationships.incident.data.id" has the same value as "incident.data.id"

  @skip @team:DataDog/incident-app
  Scenario: Create an incident impact returns "Not Found" response
    Given operation "CreateIncidentImpact" enabled
    And new "CreateIncidentImpact" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"description": "Service was unavailable for external users", "end_at": "2025-08-29T13:17:00Z", "fields": {"customers_impacted": "all", "products_impacted": ["shopping", "marketing"]}, "start_at": "2025-08-28T13:17:00Z"}, "type": "incident_impacts"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Create an incident integration metadata returns "Bad Request" response
    Given operation "CreateIncidentIntegration" enabled
    And new "CreateIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_id": "00000000-aaaa-0000-0000-000000000000", "integration_type": 1, "metadata": {"channels": []}}, "type": "incident_integrations"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/incident-app
  Scenario: Create an incident integration metadata returns "CREATED" response
    Given operation "CreateIncidentIntegration" enabled
    And new "CreateIncidentIntegration" request
    And there is a valid "incident" in the system
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"attributes": {"incident_id": "{{ incident.data.id }}", "integration_type": 1, "metadata": {"channels": [{"channel_id": "C0123456789", "channel_name": "#new-channel", "team_id": "T01234567", "redirect_url": "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"}]}}, "type": "incident_integrations"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.type" is equal to "incident_integrations"
    And the response "data.attributes.metadata.channels" has length 1
    And the response "data.attributes.metadata.channels[0].channel_name" is equal to "#new-channel"

  @generated @skip @team:DataDog/incident-app
  Scenario: Create an incident integration metadata returns "Not Found" response
    Given operation "CreateIncidentIntegration" enabled
    And new "CreateIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_id": "00000000-aaaa-0000-0000-000000000000", "integration_type": 1, "metadata": {"channels": []}}, "type": "incident_integrations"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident notification rule returns "Bad Request" response
    Given operation "CreateIncidentNotificationRule" enabled
    And new "CreateIncidentNotificationRule" request
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "enabled": true, "handles": ["@team-email@company.com", "@slack-channel"], "renotify_on": ["status", "severity"], "trigger": "incident_created_trigger", "visibility": "organization"}, "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}, "notification_template": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "notification_templates"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident notification rule returns "Created" response
    Given operation "CreateIncidentNotificationRule" enabled
    And new "CreateIncidentNotificationRule" request
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "enabled": true, "handles": ["@team-email@company.com", "@slack-channel"], "renotify_on": ["status", "severity"], "trigger": "incident_created_trigger", "visibility": "organization"}, "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}, "notification_template": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "notification_templates"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident notification rule returns "Not Found" response
    Given operation "CreateIncidentNotificationRule" enabled
    And new "CreateIncidentNotificationRule" request
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "enabled": true, "handles": ["@team-email@company.com", "@slack-channel"], "renotify_on": ["status", "severity"], "trigger": "incident_created_trigger", "visibility": "organization"}, "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}, "notification_template": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "notification_templates"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Create an incident returns "Bad Request" response
    Given operation "CreateIncident" enabled
    And new "CreateIncident" request
    And body with value {"data": {"attributes": {"customer_impact_scope": "Example customer impact scope", "customer_impacted": false, "fields": {"severity": {"type": "dropdown", "value": "SEV-5"}}, "incident_type_uuid": "00000000-0000-0000-0000-000000000000", "initial_cells": [{"cell_type": "markdown", "content": {"content": "An example timeline cell message."}, "important": false}], "is_test": false, "notification_handles": [{"display_name": "Jane Doe", "handle": "@user@email.com"}, {"display_name": "Slack Channel", "handle": "@slack-channel"}, {"display_name": "Incident Workflow", "handle": "@workflow-from-incident"}], "title": "A test incident title"}, "relationships": {"commander_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}}, "type": "incidents"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/incident-app
  Scenario: Create an incident returns "CREATED" response
    Given there is a valid "user" in the system
    And operation "CreateIncident" enabled
    And new "CreateIncident" request
    And body with value {"data": {"type": "incidents", "attributes": {"title": "{{unique}}", "customer_impacted": false, "fields": {"state": {"type": "dropdown", "value": "resolved"}}}, "relationships": {"commander_user": {"data": {"type": "{{ user.data.type }}", "id": "{{ user.data.id }}"}}}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.relationships.commander_user.data.id" has the same value as "user.data.id"
    And the response "data.attributes.title" has the same value as "unique"

  @generated @skip @team:DataDog/incident-app
  Scenario: Create an incident returns "Not Found" response
    Given operation "CreateIncident" enabled
    And new "CreateIncident" request
    And body with value {"data": {"attributes": {"customer_impact_scope": "Example customer impact scope", "customer_impacted": false, "fields": {"severity": {"type": "dropdown", "value": "SEV-5"}}, "incident_type_uuid": "00000000-0000-0000-0000-000000000000", "initial_cells": [{"cell_type": "markdown", "content": {"content": "An example timeline cell message."}, "important": false}], "is_test": false, "notification_handles": [{"display_name": "Jane Doe", "handle": "@user@email.com"}, {"display_name": "Slack Channel", "handle": "@slack-channel"}, {"display_name": "Incident Workflow", "handle": "@workflow-from-incident"}], "title": "A test incident title"}, "relationships": {"commander_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}}, "type": "incidents"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident todo returns "Bad Request" response
    Given operation "CreateIncidentTodo" enabled
    And new "CreateIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignees": ["@test.user@test.com"], "completed": "2023-03-06T22:00:00.000000+00:00", "content": "Restore lost data.", "due_date": "2023-07-10T05:00:00.000000+00:00", "incident_id": "00000000-aaaa-0000-0000-000000000000"}, "type": "incident_todos"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/incident-app
  Scenario: Create an incident todo returns "CREATED" response
    Given operation "CreateIncidentTodo" enabled
    And new "CreateIncidentTodo" request
    And there is a valid "incident" in the system
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"attributes": {"assignees": ["@test.user@test.com"], "content": "Restore lost data."}, "type": "incident_todos"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.attributes.assignees" has length 1

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident todo returns "Not Found" response
    Given operation "CreateIncidentTodo" enabled
    And new "CreateIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignees": ["@test.user@test.com"], "completed": "2023-03-06T22:00:00.000000+00:00", "content": "Restore lost data.", "due_date": "2023-07-10T05:00:00.000000+00:00", "incident_id": "00000000-aaaa-0000-0000-000000000000"}, "type": "incident_todos"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident type returns "Bad Request" response
    Given operation "CreateIncidentType" enabled
    And new "CreateIncidentType" request
    And body with value {"data": {"attributes": {"description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.", "is_default": false, "name": "Security Incident"}, "type": "incident_types"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:Datadog/incident-app
  Scenario: Create an incident type returns "CREATED" response
    Given operation "CreateIncidentType" enabled
    And new "CreateIncidentType" request
    And body with value {"data": {"attributes": {"description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.", "is_default": false, "name": "Security Incident"}, "type": "incident_types"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:Datadog/incident-app
  Scenario: Create an incident type returns "Not Found" response
    Given operation "CreateIncidentType" enabled
    And new "CreateIncidentType" request
    And body with value {"data": {"attributes": {"description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data.", "is_default": false, "name": "Security Incident"}, "type": "incident_types"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Create global incident handle returns "Bad Request" response
    Given operation "CreateGlobalIncidentHandle" enabled
    And new "CreateGlobalIncidentHandle" request
    And body with value {"data": {"attributes": {"fields": {"severity": ["SEV-1"]}, "name": "@incident-sev-1"}, "id": "b2494081-cdf0-4205-b366-4e1dd4fdf0bf", "relationships": {"commander_user": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}, "incident_type": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}}, "type": "incidents_handles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Create global incident handle returns "Created" response
    Given operation "CreateGlobalIncidentHandle" enabled
    And new "CreateGlobalIncidentHandle" request
    And body with value {"data": {"attributes": {"fields": {"severity": ["SEV-1"]}, "name": "@incident-sev-1"}, "id": "b2494081-cdf0-4205-b366-4e1dd4fdf0bf", "relationships": {"commander_user": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}, "incident_type": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}}, "type": "incidents_handles"}}
    When the request is sent
    Then the response status is 201 Created

  @skip @team:DataDog/incident-app
  Scenario: Create incident attachment returns "Bad Request" response
    Given operation "CreateIncidentAttachment" enabled
    And new "CreateIncidentAttachment" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"attachment": {"documentUrl": "https://app.datadoghq.com/notebook/123/Postmortem-IR-123", "title": "Postmortem-IR-123"}, "attachment_type": "postmortem"}, "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/incident-app
  Scenario: Create incident attachment returns "Created" response
    Given operation "CreateIncidentAttachment" enabled
    And there is a valid "incident" in the system
    And new "CreateIncidentAttachment" request
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"attributes": {"attachment": {"documentUrl": "https://app.datadoghq.com/notebook/{{ unique_alnum }}/{{ unique }}", "title": "{{ unique }}"}, "attachment_type": "postmortem"}, "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "incident_attachments"
    And the response "data.attributes.attachment.title" has the same value as "unique"

  @team:Datadog/incident-app
  Scenario: Create incident notification rule returns "Bad Request" response
    Given operation "CreateIncidentNotificationRule" enabled
    And new "CreateIncidentNotificationRule" request
    And body with value {"data": {"type": "invalid_type", "attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "handles": ["@test-email@company.com"], "visibility": "organization", "trigger": "incident_created_trigger", "enabled": true}, "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/incident-app
  Scenario: Create incident notification rule returns "Created" response
    Given there is a valid "incident_type" in the system
    And operation "CreateIncidentNotificationRule" enabled
    And new "CreateIncidentNotificationRule" request
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "handles": ["@test-email@company.com"], "visibility": "organization", "trigger": "incident_created_trigger", "enabled": true}, "relationships": {"incident_type": {"data": {"id": "{{ incident_type.data.id }}", "type": "incident_types"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "incident_notification_rules"
    And the response "data.attributes.visibility" is equal to "organization"
    And the response "data.attributes.enabled" is equal to true

  @team:Datadog/incident-app
  Scenario: Create incident notification template returns "Bad Request" response
    Given operation "CreateIncidentNotificationTemplate" enabled
    And new "CreateIncidentNotificationTemplate" request
    And body with value {"data": {"attributes": {"category": "alert", "content": "An incident has been declared. Please join the incident channel for updates.", "name": "Test Template", "subject": "Incident Alert"}, "type": "invalid_type"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/incident-app
  Scenario: Create incident notification template returns "Created" response
    Given there is a valid "incident_type" in the system
    And operation "CreateIncidentNotificationTemplate" enabled
    And new "CreateIncidentNotificationTemplate" request
    And body with value {"data": {"attributes": {"category": "alert", "content": "An incident has been declared.\n\nTitle: Sample Incident Title\nSeverity: SEV-2\nAffected Services: web-service, database-service\nStatus: active\n\nPlease join the incident channel for updates.", "name": "{{ unique }}", "subject": "SEV-2 Incident: Sample Incident Title"}, "relationships": {"incident_type": {"data": {"id": "{{ incident_type.data.id }}", "type": "incident_types"}}}, "type": "notification_templates"}}
    When the request is sent
    Then the response status is 201 Created
    And the response "data.type" is equal to "notification_templates"
    And the response "data.attributes.name" has the same value as "unique"
    And the response "data.attributes.category" is equal to "alert"
    And the response "data.relationships.incident_type.data.id" has the same value as "incident_type.data.id"

  @team:Datadog/incident-app
  Scenario: Create incident notification template returns "Not Found" response
    Given operation "CreateIncidentNotificationTemplate" enabled
    And new "CreateIncidentNotificationTemplate" request
    And body with value {"data": {"attributes": {"category": "alert", "content": "An incident has been declared. Please join the incident channel for updates.", "name": "Incident Alert Template", "subject": "Incident Alert"}, "relationships": {"incident_type": {"data": {"id": "00000000-1111-2222-3333-444444444444", "type": "incident_types"}}}, "type": "notification_templates"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Create postmortem attachment returns "Bad Request" response
    Given operation "CreateIncidentPostmortemAttachment" enabled
    And new "CreateIncidentPostmortemAttachment" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"content": "## Incident Summary\nThis incident was caused by..."}}, "id": "cell-1", "type": "markdown"}], "content": "# Incident Report - IR-123\n[...]", "postmortem_template_id": "93645509-874e-45c4-adfa-623bfeaead89-123", "title": "Postmortem-IR-123"}, "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Create postmortem attachment returns "Created" response
    Given operation "CreateIncidentPostmortemAttachment" enabled
    And new "CreateIncidentPostmortemAttachment" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"content": "## Incident Summary\nThis incident was caused by..."}}, "id": "cell-1", "type": "markdown"}], "content": "# Incident Report - IR-123\n[...]", "postmortem_template_id": "93645509-874e-45c4-adfa-623bfeaead89-123", "title": "Postmortem-IR-123"}, "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/incident-app
  Scenario: Create postmortem template returns "Bad Request" response
    Given operation "CreateIncidentPostmortemTemplate" enabled
    And new "CreateIncidentPostmortemTemplate" request
    And body with value {"data": {"attributes": {"name": "Standard Postmortem Template"}, "type": "postmortem_template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Create postmortem template returns "Created" response
    Given operation "CreateIncidentPostmortemTemplate" enabled
    And new "CreateIncidentPostmortemTemplate" request
    And body with value {"data": {"attributes": {"name": "Standard Postmortem Template"}, "type": "postmortem_template"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete a notification template returns "Bad Request" response
    Given operation "DeleteIncidentNotificationTemplate" enabled
    And new "DeleteIncidentNotificationTemplate" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete a notification template returns "No Content" response
    Given operation "DeleteIncidentNotificationTemplate" enabled
    And new "DeleteIncidentNotificationTemplate" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete a notification template returns "Not Found" response
    Given operation "DeleteIncidentNotificationTemplate" enabled
    And new "DeleteIncidentNotificationTemplate" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete an existing incident returns "Bad Request" response
    Given operation "DeleteIncident" enabled
    And new "DeleteIncident" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete an existing incident returns "Not Found" response
    Given operation "DeleteIncident" enabled
    And new "DeleteIncident" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Delete an existing incident returns "OK" response
    Given operation "DeleteIncident" enabled
    And there is a valid "incident" in the system
    And new "DeleteIncident" request
    And request contains "incident_id" parameter from "incident.data.id"
    When the request is sent
    Then the response status is 204 OK

  @skip @team:DataDog/incident-app
  Scenario: Delete an incident impact returns "No Content" response
    Given there is a valid "incident" in the system
    And the "incident" has an "incident_impact"
    And operation "DeleteIncidentImpact" enabled
    And new "DeleteIncidentImpact" request
    And request contains "incident_id" parameter from "incident_impact.data.relationships.incident.data.id"
    And request contains "impact_id" parameter from "incident_impact.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @skip @team:DataDog/incident-app
  Scenario: Delete an incident impact returns "Not Found" response
    Given operation "DeleteIncidentImpact" enabled
    And new "DeleteIncidentImpact" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And request contains "impact_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete an incident integration metadata returns "Bad Request" response
    Given operation "DeleteIncidentIntegration" enabled
    And new "DeleteIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "integration_metadata_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete an incident integration metadata returns "Not Found" response
    Given operation "DeleteIncidentIntegration" enabled
    And new "DeleteIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "integration_metadata_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Delete an incident integration metadata returns "OK" response
    Given operation "DeleteIncidentIntegration" enabled
    And new "DeleteIncidentIntegration" request
    And there is a valid "incident" in the system
    And request contains "incident_id" parameter from "incident.data.id"
    And the "incident" has an "incident_integration_metadata"
    And request contains "integration_metadata_id" parameter from "incident_integration_metadata.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident notification rule returns "Bad Request" response
    Given operation "DeleteIncidentNotificationRule" enabled
    And new "DeleteIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident notification rule returns "No Content" response
    Given operation "DeleteIncidentNotificationRule" enabled
    And new "DeleteIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident notification rule returns "Not Found" response
    Given operation "DeleteIncidentNotificationRule" enabled
    And new "DeleteIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident todo returns "Bad Request" response
    Given operation "DeleteIncidentTodo" enabled
    And new "DeleteIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "todo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident todo returns "Not Found" response
    Given operation "DeleteIncidentTodo" enabled
    And new "DeleteIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "todo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/incident-app
  Scenario: Delete an incident todo returns "OK" response
    Given operation "DeleteIncidentTodo" enabled
    And new "DeleteIncidentTodo" request
    And there is a valid "incident" in the system
    And the "incident" has an "incident_todo"
    And request contains "incident_id" parameter from "incident.data.id"
    And request contains "todo_id" parameter from "incident_todo.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident type returns "Bad Request" response
    Given operation "DeleteIncidentType" enabled
    And new "DeleteIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Delete an incident type returns "Not Found" response
    Given operation "DeleteIncidentType" enabled
    And new "DeleteIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:Datadog/incident-app
  Scenario: Delete an incident type returns "OK" response
    Given operation "DeleteIncidentType" enabled
    And new "DeleteIncidentType" request
    And there is a valid "incident_type" in the system
    And request contains "incident_type_id" parameter from "incident_type.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete global incident handle returns "Bad Request" response
    Given operation "DeleteGlobalIncidentHandle" enabled
    And new "DeleteGlobalIncidentHandle" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete global incident handle returns "No Content" response
    Given operation "DeleteGlobalIncidentHandle" enabled
    And new "DeleteGlobalIncidentHandle" request
    When the request is sent
    Then the response status is 204 No Content

  @skip @team:DataDog/incident-app
  Scenario: Delete incident attachment returns "Bad Request" response
    Given operation "DeleteIncidentAttachment" enabled
    And new "DeleteIncidentAttachment" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And request contains "attachment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/incident-app
  Scenario: Delete incident attachment returns "No Content" response
    Given operation "DeleteIncidentAttachment" enabled
    And there is a valid "incident" in the system
    And there is a valid "incident_attachment" in the system
    And new "DeleteIncidentAttachment" request
    And request contains "incident_id" parameter from "incident.data.id"
    And request contains "attachment_id" parameter from "incident_attachment.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/incident-app
  Scenario: Delete incident attachment returns "Not Found" response
    Given operation "DeleteIncidentAttachment" enabled
    And new "DeleteIncidentAttachment" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And request contains "attachment_id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Delete incident notification rule returns "No Content" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_rule" in the system
    And operation "DeleteIncidentNotificationRule" enabled
    And new "DeleteIncidentNotificationRule" request
    And request contains "id" parameter from "notification_rule.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:Datadog/incident-app
  Scenario: Delete incident notification rule returns "Not Found" response
    Given operation "DeleteIncidentNotificationRule" enabled
    And new "DeleteIncidentNotificationRule" request
    And request contains "id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Delete incident notification template returns "No Content" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_template" in the system
    And operation "DeleteIncidentNotificationTemplate" enabled
    And new "DeleteIncidentNotificationTemplate" request
    And request contains "id" parameter from "notification_template.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete postmortem template returns "Bad Request" response
    Given operation "DeleteIncidentPostmortemTemplate" enabled
    And new "DeleteIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete postmortem template returns "No Content" response
    Given operation "DeleteIncidentPostmortemTemplate" enabled
    And new "DeleteIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/incident-app
  Scenario: Delete postmortem template returns "Not Found" response
    Given operation "DeleteIncidentPostmortemTemplate" enabled
    And new "DeleteIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Get a list of an incident's integration metadata returns "Bad Request" response
    Given operation "ListIncidentIntegrations" enabled
    And new "ListIncidentIntegrations" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Get a list of an incident's integration metadata returns "Not Found" response
    Given operation "ListIncidentIntegrations" enabled
    And new "ListIncidentIntegrations" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Get a list of an incident's integration metadata returns "OK" response
    Given operation "ListIncidentIntegrations" enabled
    And new "ListIncidentIntegrations" request
    And there is a valid "incident" in the system
    And request contains "incident_id" parameter from "incident.data.id"
    And the "incident" has an "incident_integration_metadata"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.metadata.channels[0].channel_name" is equal to "#example-channel-name"

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of an incident's todos returns "Bad Request" response
    Given operation "ListIncidentTodos" enabled
    And new "ListIncidentTodos" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of an incident's todos returns "Not Found" response
    Given operation "ListIncidentTodos" enabled
    And new "ListIncidentTodos" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/incident-app
  Scenario: Get a list of an incident's todos returns "OK" response
    Given operation "ListIncidentTodos" enabled
    And new "ListIncidentTodos" request
    And there is a valid "incident" in the system
    And the "incident" has an "incident_todo"
    And request contains "incident_id" parameter from "incident.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].attributes.assignees" has length 2
    And the response "data[0].attributes.content" is equal to "Follow up with customer about the impact they saw."

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of incident types returns "Bad Request" response
    Given operation "ListIncidentTypes" enabled
    And new "ListIncidentTypes" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get a list of incident types returns "OK" response
    Given operation "ListIncidentTypes" enabled
    And new "ListIncidentTypes" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Get a list of incidents returns "Bad Request" response
    Given operation "ListIncidents" enabled
    And new "ListIncidents" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Get a list of incidents returns "Not Found" response
    Given operation "ListIncidents" enabled
    And new "ListIncidents" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Get a list of incidents returns "OK" response
    Given operation "ListIncidents" enabled
    And there is a valid "incident" in the system
    And new "ListIncidents" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "incidents"

  @replay-only @skip-validation @team:DataDog/incident-app @with-pagination
  Scenario: Get a list of incidents returns "OK" response with pagination
    Given operation "ListIncidents" enabled
    And new "ListIncidents" request
    And request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:Datadog/incident-app
  Scenario: Get an incident notification rule returns "Bad Request" response
    Given operation "GetIncidentNotificationRule" enabled
    And new "GetIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get an incident notification rule returns "Not Found" response
    Given operation "GetIncidentNotificationRule" enabled
    And new "GetIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Get an incident notification rule returns "OK" response
    Given operation "GetIncidentNotificationRule" enabled
    And new "GetIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Get global incident settings returns "Bad Request" response
    Given operation "GetGlobalIncidentSettings" enabled
    And new "GetGlobalIncidentSettings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Get global incident settings returns "OK" response
    Given operation "GetGlobalIncidentSettings" enabled
    And new "GetGlobalIncidentSettings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Get incident integration metadata details returns "Bad Request" response
    Given operation "GetIncidentIntegration" enabled
    And new "GetIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "integration_metadata_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Get incident integration metadata details returns "Not Found" response
    Given operation "GetIncidentIntegration" enabled
    And new "GetIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "integration_metadata_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Get incident integration metadata details returns "OK" response
    Given operation "GetIncidentIntegration" enabled
    And new "GetIncidentIntegration" request
    And there is a valid "incident" in the system
    And request contains "incident_id" parameter from "incident.data.id"
    And the "incident" has an "incident_integration_metadata"
    And request contains "integration_metadata_id" parameter from "incident_integration_metadata.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:Datadog/incident-app
  Scenario: Get incident notification rule returns "Not Found" response
    Given operation "GetIncidentNotificationRule" enabled
    And new "GetIncidentNotificationRule" request
    And request contains "id" parameter with value "00000000-0000-0000-0000-000000000001"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Get incident notification rule returns "OK" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_rule" in the system
    And operation "GetIncidentNotificationRule" enabled
    And new "GetIncidentNotificationRule" request
    And request contains "id" parameter from "notification_rule.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "incident_notification_rules"
    And the response "data.id" has the same value as "notification_rule.data.id"

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident notification template returns "Bad Request" response
    Given operation "GetIncidentNotificationTemplate" enabled
    And new "GetIncidentNotificationTemplate" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident notification template returns "Not Found" response
    Given operation "GetIncidentNotificationTemplate" enabled
    And new "GetIncidentNotificationTemplate" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Get incident notification template returns "OK" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_template" in the system
    And operation "GetIncidentNotificationTemplate" enabled
    And new "GetIncidentNotificationTemplate" request
    And request contains "id" parameter from "notification_template.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "notification_templates"
    And the response "data.id" has the same value as "notification_template.data.id"
    And the response "data" has field "attributes"
    And the response "data" has field "relationships"

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident todo details returns "Bad Request" response
    Given operation "GetIncidentTodo" enabled
    And new "GetIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "todo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident todo details returns "Not Found" response
    Given operation "GetIncidentTodo" enabled
    And new "GetIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "todo_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/incident-app
  Scenario: Get incident todo details returns "OK" response
    Given operation "GetIncidentTodo" enabled
    And new "GetIncidentTodo" request
    And there is a valid "incident" in the system
    And the "incident" has an "incident_todo"
    And request contains "incident_id" parameter from "incident.data.id"
    And request contains "todo_id" parameter from "incident_todo.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.assignees" has length 2
    And the response "data.attributes.content" is equal to "Follow up with customer about the impact they saw."

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident type details returns "Bad Request" response
    Given operation "GetIncidentType" enabled
    And new "GetIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident type details returns "Not Found" response
    Given operation "GetIncidentType" enabled
    And new "GetIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Get incident type details returns "OK" response
    Given operation "GetIncidentType" enabled
    And new "GetIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Get postmortem template returns "Bad Request" response
    Given operation "GetIncidentPostmortemTemplate" enabled
    And new "GetIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Get postmortem template returns "Not Found" response
    Given operation "GetIncidentPostmortemTemplate" enabled
    And new "GetIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Get postmortem template returns "OK" response
    Given operation "GetIncidentPostmortemTemplate" enabled
    And new "GetIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Get the details of an incident returns "Bad Request" response
    Given operation "GetIncident" enabled
    And new "GetIncident" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Get the details of an incident returns "Not Found" response
    Given operation "GetIncident" enabled
    And new "GetIncident" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Get the details of an incident returns "OK" response
    Given operation "GetIncident" enabled
    And there is a valid "incident" in the system
    And new "GetIncident" request
    And request contains "incident_id" parameter from "incident.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.title" has the same value as "incident.data.attributes.title"

  @generated @skip @team:DataDog/incident-app
  Scenario: Import an incident returns "Bad Request" response
    Given operation "ImportIncident" enabled
    And new "ImportIncident" request
    And body with value {"data": {"attributes": {"declared": "2025-01-01T00:00:00Z", "detected": "2025-01-01T00:00:00Z", "fields": {"severity": {"value": "SEV-5"}, "state": {"value": "active"}}, "incident_type_uuid": "00000000-0000-0000-0000-000000000000", "resolved": "2025-01-01T01:00:00Z", "title": "Imported incident from external system", "visibility": "organization"}, "relationships": {"commander_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}, "declared_by_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}}, "type": "incidents"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/incident-app
  Scenario: Import an incident returns "CREATED" response
    Given operation "ImportIncident" enabled
    And new "ImportIncident" request
    And body with value {"data": {"type": "incidents", "attributes": {"title": "{{unique}}", "visibility": "organization"}}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data.type" is equal to "incidents"
    And the response "data.attributes.title" has the same value as "unique"

  @generated @skip @team:DataDog/incident-app
  Scenario: Import an incident returns "Not Found" response
    Given operation "ImportIncident" enabled
    And new "ImportIncident" request
    And body with value {"data": {"attributes": {"declared": "2025-01-01T00:00:00Z", "detected": "2025-01-01T00:00:00Z", "fields": {"severity": {"value": "SEV-5"}, "state": {"value": "active"}}, "incident_type_uuid": "00000000-0000-0000-0000-000000000000", "resolved": "2025-01-01T01:00:00Z", "title": "Imported incident from external system", "visibility": "organization"}, "relationships": {"commander_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}, "declared_by_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}}, "type": "incidents"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: List an incident's impacts returns "Bad Request" response
    Given new "ListIncidentImpacts" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: List an incident's impacts returns "Not Found" response
    Given new "ListIncidentImpacts" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/incident-app
  Scenario: List an incident's impacts returns "OK" response
    Given there is a valid "incident" in the system
    And operation "ListIncidentImpacts" enabled
    And new "ListIncidentImpacts" request
    And request contains "incident_id" parameter from "incident.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: List global incident handles returns "Bad Request" response
    Given operation "ListGlobalIncidentHandles" enabled
    And new "ListGlobalIncidentHandles" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: List global incident handles returns "OK" response
    Given operation "ListGlobalIncidentHandles" enabled
    And new "ListGlobalIncidentHandles" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/incident-app
  Scenario: List incident attachments returns "Bad Request" response
    Given operation "ListIncidentAttachments" enabled
    And new "ListIncidentAttachments" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/incident-app
  Scenario: List incident attachments returns "OK" response
    Given operation "ListIncidentAttachments" enabled
    And there is a valid "incident" in the system
    And there is a valid "incident_attachment" in the system
    And new "ListIncidentAttachments" request
    And request contains "incident_id" parameter from "incident.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1

  @generated @skip @team:Datadog/incident-app
  Scenario: List incident notification rules returns "Bad Request" response
    Given operation "ListIncidentNotificationRules" enabled
    And new "ListIncidentNotificationRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: List incident notification rules returns "Not Found" response
    Given operation "ListIncidentNotificationRules" enabled
    And new "ListIncidentNotificationRules" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: List incident notification rules returns "OK" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_rule" in the system
    And operation "ListIncidentNotificationRules" enabled
    And new "ListIncidentNotificationRules" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "data[0].type" is equal to "incident_notification_rules"

  @generated @skip @team:Datadog/incident-app
  Scenario: List incident notification templates returns "Bad Request" response
    Given operation "ListIncidentNotificationTemplates" enabled
    And new "ListIncidentNotificationTemplates" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: List incident notification templates returns "Not Found" response
    Given operation "ListIncidentNotificationTemplates" enabled
    And new "ListIncidentNotificationTemplates" request
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: List incident notification templates returns "OK" response
    Given operation "ListIncidentNotificationTemplates" enabled
    And new "ListIncidentNotificationTemplates" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 0

  @generated @skip @team:DataDog/incident-app
  Scenario: List postmortem templates returns "Bad Request" response
    Given operation "ListIncidentPostmortemTemplates" enabled
    And new "ListIncidentPostmortemTemplates" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: List postmortem templates returns "OK" response
    Given operation "ListIncidentPostmortemTemplates" enabled
    And new "ListIncidentPostmortemTemplates" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/incident-app
  Scenario: Remove commander from an incident returns "OK" response
    Given operation "UpdateIncident" enabled
    And there is a valid "incident" in the system
    And new "UpdateIncident" request
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"id": "{{incident.data.id}}", "type": "incidents", "relationships": {"commander_user": {"data": null}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.relationships.commander_user.data" is equal to null

  @generated @skip @team:DataDog/incident-app
  Scenario: Search for incidents returns "Bad Request" response
    Given operation "SearchIncidents" enabled
    And new "SearchIncidents" request
    And request contains "query" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Search for incidents returns "Not Found" response
    Given operation "SearchIncidents" enabled
    And new "SearchIncidents" request
    And request contains "query" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/incident-app
  Scenario: Search for incidents returns "OK" response
    Given operation "SearchIncidents" enabled
    And there is a valid "incident" in the system
    And new "SearchIncidents" request
    And request contains "query" parameter with value "state:(active OR stable OR resolved)"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "incidents_search_results"
    And the response "data.attributes.incidents[0].data.type" is equal to "incidents"

  @replay-only @skip-validation @team:DataDog/incident-app @with-pagination
  Scenario: Search for incidents returns "OK" response with pagination
    Given operation "SearchIncidents" enabled
    And new "SearchIncidents" request
    And request contains "query" parameter with value "state:(active OR stable OR resolved)"
    And request contains "page[size]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/incident-app
  Scenario: Update an existing incident integration metadata returns "Bad Request" response
    Given operation "UpdateIncidentIntegration" enabled
    And new "UpdateIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "integration_metadata_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_id": "00000000-aaaa-0000-0000-000000000000", "integration_type": 1, "metadata": {"channels": []}}, "type": "incident_integrations"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Update an existing incident integration metadata returns "Not Found" response
    Given operation "UpdateIncidentIntegration" enabled
    And new "UpdateIncidentIntegration" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "integration_metadata_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_id": "00000000-aaaa-0000-0000-000000000000", "integration_type": 1, "metadata": {"channels": []}}, "type": "incident_integrations"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Update an existing incident integration metadata returns "OK" response
    Given operation "UpdateIncidentIntegration" enabled
    And new "UpdateIncidentIntegration" request
    And there is a valid "incident" in the system
    And request contains "incident_id" parameter from "incident.data.id"
    And the "incident" has an "incident_integration_metadata"
    And request contains "integration_metadata_id" parameter from "incident_integration_metadata.data.id"
    And body with value {"data": {"attributes": {"incident_id": "{{ incident.data.id }}", "integration_type": 1, "metadata": {"channels": [{"channel_id": "C0123456789", "channel_name": "#updated-channel-name", "team_id": "T01234567", "redirect_url": "https://slack.com/app_redirect?channel=C0123456789&team=T01234567"}]}}, "type": "incident_integrations"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.metadata.channels[0].channel_name" is equal to "#updated-channel-name"

  @generated @skip @team:DataDog/incident-app
  Scenario: Update an existing incident returns "Bad Request" response
    Given operation "UpdateIncident" enabled
    And new "UpdateIncident" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"customer_impact_end": null, "customer_impact_scope": "Example customer impact scope", "customer_impact_start": null, "customer_impacted": false, "detected": null, "fields": {"severity": {"type": "dropdown", "value": "SEV-5"}}, "notification_handles": [{"display_name": "Jane Doe", "handle": "@user@email.com"}, {"display_name": "Slack Channel", "handle": "@slack-channel"}, {"display_name": "Incident Workflow", "handle": "@workflow-from-incident"}], "title": "A test incident title"}, "id": "00000000-0000-0000-4567-000000000000", "relationships": {"commander_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}, "integrations": {"data": [{"id": "00000000-abcd-0005-0000-000000000000", "type": "incident_integrations"}, {"id": "00000000-abcd-0006-0000-000000000000", "type": "incident_integrations"}]}, "postmortem": {"data": {"id": "00000000-0000-abcd-3000-000000000000", "type": "incident_postmortems"}}}, "type": "incidents"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Update an existing incident returns "Not Found" response
    Given operation "UpdateIncident" enabled
    And new "UpdateIncident" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"customer_impact_end": null, "customer_impact_scope": "Example customer impact scope", "customer_impact_start": null, "customer_impacted": false, "detected": null, "fields": {"severity": {"type": "dropdown", "value": "SEV-5"}}, "notification_handles": [{"display_name": "Jane Doe", "handle": "@user@email.com"}, {"display_name": "Slack Channel", "handle": "@slack-channel"}, {"display_name": "Incident Workflow", "handle": "@workflow-from-incident"}], "title": "A test incident title"}, "id": "00000000-0000-0000-4567-000000000000", "relationships": {"commander_user": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "users"}}, "integrations": {"data": [{"id": "00000000-abcd-0005-0000-000000000000", "type": "incident_integrations"}, {"id": "00000000-abcd-0006-0000-000000000000", "type": "incident_integrations"}]}, "postmortem": {"data": {"id": "00000000-0000-abcd-3000-000000000000", "type": "incident_postmortems"}}}, "type": "incidents"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Update an existing incident returns "OK" response
    Given operation "UpdateIncident" enabled
    And there is a valid "incident" in the system
    And new "UpdateIncident" request
    And request contains "incident_id" parameter from "incident.data.id"
    And body with value {"data": {"id": "{{incident.data.id}}", "type": "incidents", "attributes": {"fields": {"state": {"type": "dropdown", "value":"resolved"}}, "title": "{{ incident.data.attributes.title }}-updated"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.title" is equal to "{{ incident.data.attributes.title }}-updated"

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident notification rule returns "Bad Request" response
    Given operation "UpdateIncidentNotificationRule" enabled
    And new "UpdateIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "enabled": true, "handles": ["@team-email@company.com", "@slack-channel"], "renotify_on": ["status", "severity"], "trigger": "incident_created_trigger", "visibility": "organization"}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}, "notification_template": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "notification_templates"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident notification rule returns "Not Found" response
    Given operation "UpdateIncidentNotificationRule" enabled
    And new "UpdateIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "enabled": true, "handles": ["@team-email@company.com", "@slack-channel"], "renotify_on": ["status", "severity"], "trigger": "incident_created_trigger", "visibility": "organization"}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}, "notification_template": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "notification_templates"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident notification rule returns "OK" response
    Given operation "UpdateIncidentNotificationRule" enabled
    And new "UpdateIncidentNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "enabled": true, "handles": ["@team-email@company.com", "@slack-channel"], "renotify_on": ["status", "severity"], "trigger": "incident_created_trigger", "visibility": "organization"}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}, "notification_template": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "notification_templates"}}}, "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident todo returns "Bad Request" response
    Given operation "UpdateIncidentTodo" enabled
    And new "UpdateIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "todo_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignees": ["@test.user@test.com"], "completed": "2023-03-06T22:00:00.000000+00:00", "content": "Restore lost data.", "due_date": "2023-07-10T05:00:00.000000+00:00", "incident_id": "00000000-aaaa-0000-0000-000000000000"}, "type": "incident_todos"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident todo returns "Not Found" response
    Given operation "UpdateIncidentTodo" enabled
    And new "UpdateIncidentTodo" request
    And request contains "incident_id" parameter from "REPLACE.ME"
    And request contains "todo_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignees": ["@test.user@test.com"], "completed": "2023-03-06T22:00:00.000000+00:00", "content": "Restore lost data.", "due_date": "2023-07-10T05:00:00.000000+00:00", "incident_id": "00000000-aaaa-0000-0000-000000000000"}, "type": "incident_todos"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Update an incident todo returns "OK" response
    Given operation "UpdateIncidentTodo" enabled
    And new "UpdateIncidentTodo" request
    And there is a valid "incident" in the system
    And the "incident" has an "incident_todo"
    And request contains "incident_id" parameter from "incident.data.id"
    And request contains "todo_id" parameter from "incident_todo.data.id"
    And body with value {"data": {"attributes": {"assignees": ["@test.user@test.com"], "content": "Restore lost data.", "completed": "2023-03-06T22:00:00.000000+00:00", "due_date": "2023-07-10T05:00:00.000000+00:00"}, "type": "incident_todos"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.assignees" has length 1
    And the response "data.attributes.content" is equal to "Restore lost data."

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident type returns "Bad Request" response
    Given operation "UpdateIncidentType" enabled
    And new "UpdateIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data. Note: This will notify the security team.", "is_default": false, "name": "Security Incident"}, "id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/incident-app
  Scenario: Update an incident type returns "Not Found" response
    Given operation "UpdateIncidentType" enabled
    And new "UpdateIncidentType" request
    And request contains "incident_type_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Any incidents that harm (or have the potential to) the confidentiality, integrity, or availability of our data. Note: This will notify the security team.", "is_default": false, "name": "Security Incident"}, "id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:Datadog/incident-app
  Scenario: Update an incident type returns "OK" response
    Given operation "UpdateIncidentType" enabled
    And new "UpdateIncidentType" request
    And there is a valid "incident_type" in the system
    And request contains "incident_type_id" parameter from "incident_type.data.id"
    And body with value {"data": {"id": "{{incident_type.data.id}}", "attributes": {"name": "{{incident_type.data.attributes.name}}-updated"}, "type": "incident_types"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Update global incident handle returns "Bad Request" response
    Given operation "UpdateGlobalIncidentHandle" enabled
    And new "UpdateGlobalIncidentHandle" request
    And body with value {"data": {"attributes": {"fields": {"severity": ["SEV-1"]}, "name": "@incident-sev-1"}, "id": "b2494081-cdf0-4205-b366-4e1dd4fdf0bf", "relationships": {"commander_user": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}, "incident_type": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}}, "type": "incidents_handles"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Update global incident handle returns "OK" response
    Given operation "UpdateGlobalIncidentHandle" enabled
    And new "UpdateGlobalIncidentHandle" request
    And body with value {"data": {"attributes": {"fields": {"severity": ["SEV-1"]}, "name": "@incident-sev-1"}, "id": "b2494081-cdf0-4205-b366-4e1dd4fdf0bf", "relationships": {"commander_user": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}, "incident_type": {"data": {"id": "f7b538b1-ed7c-4e84-82de-fdf84a539d40", "type": "incident_types"}}}, "type": "incidents_handles"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/incident-app
  Scenario: Update global incident settings returns "Bad Request" response
    Given operation "UpdateGlobalIncidentSettings" enabled
    And new "UpdateGlobalIncidentSettings" request
    And body with value {"data": {"attributes": {"analytics_dashboard_id": "abc-123-def"}, "type": "incidents_global_settings"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Update global incident settings returns "OK" response
    Given operation "UpdateGlobalIncidentSettings" enabled
    And new "UpdateGlobalIncidentSettings" request
    And body with value {"data": {"attributes": {"analytics_dashboard_id": "abc-123-def"}, "type": "incidents_global_settings"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/incident-app
  Scenario: Update incident attachment returns "Bad Request" response
    Given operation "UpdateIncidentAttachment" enabled
    And new "UpdateIncidentAttachment" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-00000000000"
    And request contains "attachment_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"attributes": {"attachment": {"documentUrl": "https://app.datadoghq.com/notebook/124/Postmortem-IR-124", "title": "Postmortem-IR-124"}}, "id": "00000000-abcd-0002-0000-000000000000", "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/incident-app
  Scenario: Update incident attachment returns "Not Found" response
    Given operation "UpdateIncidentAttachment" enabled
    And new "UpdateIncidentAttachment" request
    And request contains "incident_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And request contains "attachment_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"attachment": {"documentUrl": "https://app.datadoghq.com/notebook/124/Postmortem-IR-124", "title": "Postmortem-IR-124"}}, "id": "00000000-abcd-0002-0000-000000000000", "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/incident-app
  Scenario: Update incident attachment returns "OK" response
    Given operation "UpdateIncidentAttachment" enabled
    And there is a valid "incident" in the system
    And there is a valid "incident_attachment" in the system
    And new "UpdateIncidentAttachment" request
    And request contains "incident_id" parameter from "incident.data.id"
    And request contains "attachment_id" parameter from "incident_attachment.data.id"
    And body with value {"data": {"attributes": {"attachment": {"documentUrl": "https://app.datadoghq.com/notebook/124/{{ unique }}", "title": "{{ unique }}"}}, "id": "{{ incident_attachment.data.id }}", "type": "incident_attachments"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "incident_attachments"
    And the response "data.attributes.attachment.title" has the same value as "unique"

  @team:Datadog/incident-app
  Scenario: Update incident notification rule returns "Bad Request" response
    Given operation "UpdateIncidentNotificationRule" enabled
    And new "UpdateIncidentNotificationRule" request
    And request contains "id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"type": "invalid_type", "attributes": {"conditions": [{"field": "severity", "values": ["SEV-1", "SEV-2"]}], "handles": ["@test-email@company.com"], "visibility": "organization", "trigger": "incident_created_trigger", "enabled": true}, "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incident_types"}}}, "id": "00000000-0000-0000-0000-000000000001"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/incident-app
  Scenario: Update incident notification rule returns "Not Found" response
    Given operation "UpdateIncidentNotificationRule" enabled
    And new "UpdateIncidentNotificationRule" request
    And request contains "id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"attributes": {"enabled": false, "conditions": [{"field": "severity", "values": ["SEV-1"]}], "handles": ["@test-email@company.com"], "trigger": "incident_created_trigger"}, "relationships": {"incident_type": {"data": {"id": "00000000-0000-0000-0000-000000000001", "type": "incident_types"}}}, "id": "00000000-0000-0000-0000-000000000001", "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Update incident notification rule returns "OK" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_rule" in the system
    And operation "UpdateIncidentNotificationRule" enabled
    And new "UpdateIncidentNotificationRule" request
    And request contains "id" parameter from "notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": false, "conditions": [{"field": "severity", "values": ["SEV-1"]}], "handles": ["@updated-team-email@company.com"], "visibility": "private", "trigger": "incident_modified_trigger"}, "relationships": {"incident_type": {"data": {"id": "{{ incident_type.data.id }}", "type": "incident_types"}}}, "id": "{{ notification_rule.data.id }}", "type": "incident_notification_rules"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "incident_notification_rules"
    And the response "data.id" has the same value as "notification_rule.data.id"
    And the response "data.attributes.visibility" is equal to "private"
    And the response "data.attributes.enabled" is equal to false

  @team:Datadog/incident-app
  Scenario: Update incident notification template returns "Bad Request" response
    Given operation "UpdateIncidentNotificationTemplate" enabled
    And new "UpdateIncidentNotificationTemplate" request
    And request contains "id" parameter with value "00000000-1111-2222-3333-444444444444"
    And body with value {"data": {"attributes": {"category": "update", "content": "Incident Status Update: For more details, visit the incident page.", "name": "Update Template", "subject": "Incident Update"}, "id": "00000000-0000-0000-0000-000000000001", "type": "invalid_type"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/incident-app
  Scenario: Update incident notification template returns "Not Found" response
    Given operation "UpdateIncidentNotificationTemplate" enabled
    And new "UpdateIncidentNotificationTemplate" request
    And request contains "id" parameter with value "00000000-1111-2222-3333-444444444444"
    And body with value {"data": {"attributes": {"category": "update", "content": "Incident Status Update: For more details, visit the incident page.", "name": "Updated Template Name", "subject": "Incident Update"}, "id": "00000000-1111-2222-3333-444444444444", "type": "notification_templates"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/incident-app
  Scenario: Update incident notification template returns "OK" response
    Given there is a valid "incident_type" in the system
    And there is a valid "notification_template" in the system
    And operation "UpdateIncidentNotificationTemplate" enabled
    And new "UpdateIncidentNotificationTemplate" request
    And request contains "id" parameter from "notification_template.data.id"
    And body with value {"data": {"attributes": {"category": "update", "content": "Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.", "name": "{{ unique }}", "subject": "Incident Update: Sample Incident Title - resolved"}, "id": "{{ notification_template.data.id }}", "type": "notification_templates"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "notification_templates"
    And the response "data.id" has the same value as "notification_template.data.id"
    And the response "data.attributes.name" has the same value as "unique"
    And the response "data.attributes.category" is equal to "update"

  @generated @skip @team:DataDog/incident-app
  Scenario: Update postmortem template returns "Bad Request" response
    Given operation "UpdateIncidentPostmortemTemplate" enabled
    And new "UpdateIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Standard Postmortem Template"}, "type": "postmortem_template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/incident-app
  Scenario: Update postmortem template returns "Not Found" response
    Given operation "UpdateIncidentPostmortemTemplate" enabled
    And new "UpdateIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Standard Postmortem Template"}, "type": "postmortem_template"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/incident-app
  Scenario: Update postmortem template returns "OK" response
    Given operation "UpdateIncidentPostmortemTemplate" enabled
    And new "UpdateIncidentPostmortemTemplate" request
    And request contains "template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"name": "Standard Postmortem Template"}, "type": "postmortem_template"}}
    When the request is sent
    Then the response status is 200 OK
