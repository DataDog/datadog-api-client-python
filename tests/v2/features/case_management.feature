@endpoint(case-management) @endpoint(case-management-v2)
Feature: Case Management
  View and manage cases and projects within Case Management. See the [Case
  Management
  page](https://docs.datadoghq.com/service_management/case_management/) for
  more information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CaseManagement" API

  @generated @skip @team:DataDog/case-management
  Scenario: Add insights to a case returns "Bad Request" response
    Given new "AddCaseInsights" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"insights": [{"ref": "/monitors/12345?q=total", "resource_id": "12345", "type": "SECURITY_SIGNAL"}]}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Add insights to a case returns "Not Found" response
    Given new "AddCaseInsights" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"insights": [{"ref": "/monitors/12345?q=total", "resource_id": "12345", "type": "SECURITY_SIGNAL"}]}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Add insights to a case returns "OK" response
    Given new "AddCaseInsights" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"insights": [{"ref": "/monitors/12345?q=total", "resource_id": "12345", "type": "SECURITY_SIGNAL"}]}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Aggregate cases returns "Bad Request" response
    Given new "AggregateCases" request
    And body with value {"data": {"attributes": {"group_by": {"groups": ["status"], "limit": 14}, "query_filter": "service:case-api"}, "type": "aggregate"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Aggregate cases returns "Not Found" response
    Given new "AggregateCases" request
    And body with value {"data": {"attributes": {"group_by": {"groups": ["status"], "limit": 14}, "query_filter": "service:case-api"}, "type": "aggregate"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Aggregate cases returns "OK" response
    Given new "AggregateCases" request
    And body with value {"data": {"attributes": {"group_by": {"groups": ["status"], "limit": 14}, "query_filter": "service:case-api"}, "type": "aggregate"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Archive case returns "Bad Request" response
    Given new "ArchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Archive case returns "Not Found" response
    Given new "ArchiveCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Archive case returns "OK" response
    Given new "ArchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Assign case returns "Bad Request" response
    Given new "AssignCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"assignee_id": "invalid-uuid"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Assign case returns "Not Found" response
    Given new "AssignCase" request
    And there is a valid "user" in the system
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"assignee_id": "{{user.data.id}}"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Assign case returns "OK" response
    Given new "AssignCase" request
    And there is a valid "case" in the system
    And there is a valid "user" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"assignee_id": "{{user.data.id}}"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Bulk update cases returns "Bad Request" response
    Given new "BulkUpdateCases" request
    And body with value {"data": {"attributes": {"case_ids": ["case-id-1", "case-id-2"], "payload": {"priority": "P1"}, "type": "priority"}, "type": "bulk"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Bulk update cases returns "Not Found" response
    Given new "BulkUpdateCases" request
    And body with value {"data": {"attributes": {"case_ids": ["case-id-1", "case-id-2"], "payload": {"priority": "P1"}, "type": "priority"}, "type": "bulk"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Bulk update cases returns "OK" response
    Given new "BulkUpdateCases" request
    And body with value {"data": {"attributes": {"case_ids": ["case-id-1", "case-id-2"], "payload": {"priority": "P1"}, "type": "priority"}, "type": "bulk"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Comment case returns "Bad Request" response
    Given new "CommentCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"comment": ""}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Comment case returns "Not Found" response
    Given new "CommentCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"comment": "Hello world !"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Comment case returns "OK" response
    Given new "CommentCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"comment": "Hello World !"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Count cases returns "Bad Request" response
    Given new "CountCases" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Count cases returns "Not Found" response
    Given new "CountCases" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Count cases returns "OK" response
    Given new "CountCases" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Create Jira issue for case returns "Accepted" response
    Given new "CreateCaseJiraIssue" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": {}, "issue_type_id": "10001", "jira_account_id": "1234", "project_id": "5678"}, "type": "issues"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/case-management
  Scenario: Create Jira issue for case returns "Bad Request" response
    Given new "CreateCaseJiraIssue" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": {}, "issue_type_id": "10001", "jira_account_id": "1234", "project_id": "5678"}, "type": "issues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create Jira issue for case returns "Not Found" response
    Given new "CreateCaseJiraIssue" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": {}, "issue_type_id": "10001", "jira_account_id": "1234", "project_id": "5678"}, "type": "issues"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create ServiceNow ticket for case returns "Accepted" response
    Given new "CreateCaseServiceNowTicket" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignment_group": "IT Support", "instance_name": "my-instance"}, "type": "tickets"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/case-management
  Scenario: Create ServiceNow ticket for case returns "Bad Request" response
    Given new "CreateCaseServiceNowTicket" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignment_group": "IT Support", "instance_name": "my-instance"}, "type": "tickets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create ServiceNow ticket for case returns "Not Found" response
    Given new "CreateCaseServiceNowTicket" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignment_group": "IT Support", "instance_name": "my-instance"}, "type": "tickets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case link returns "Bad Request" response
    Given new "CreateCaseLink" request
    And body with value {"data": {"attributes": {"child_entity_id": "4417921d-0866-4a38-822c-6f2a0f65f77d", "child_entity_type": "CASE", "parent_entity_id": "bf0cbac6-4c16-4cfb-b6bf-ca5e0ec37a4f", "parent_entity_type": "CASE", "relationship": "BLOCKS"}, "type": "link"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case link returns "Created" response
    Given new "CreateCaseLink" request
    And body with value {"data": {"attributes": {"child_entity_id": "4417921d-0866-4a38-822c-6f2a0f65f77d", "child_entity_type": "CASE", "parent_entity_id": "bf0cbac6-4c16-4cfb-b6bf-ca5e0ec37a4f", "parent_entity_type": "CASE", "relationship": "BLOCKS"}, "type": "link"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case link returns "Not Found" response
    Given new "CreateCaseLink" request
    And body with value {"data": {"attributes": {"child_entity_id": "4417921d-0866-4a38-822c-6f2a0f65f77d", "child_entity_type": "CASE", "parent_entity_id": "bf0cbac6-4c16-4cfb-b6bf-ca5e0ec37a4f", "parent_entity_type": "CASE", "relationship": "BLOCKS"}, "type": "link"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Create a case returns "Bad Request" response
    Given new "CreateCase" request
    And body with value {"data": {"attributes": {"priority": "NOT_DEFINED", "title": "Security breach investigation", "type_id": "00000000-0000-0000-0000-000000000001"}, "relationships": {"assignee": {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "userx"}}, "project": {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "project"}}}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Create a case returns "CREATED" response
    Given new "CreateCase" request
    And there is a valid "user" in the system
    And body with value {"data": {"attributes": {"priority": "NOT_DEFINED", "title": "Security breach investigation in {{ unique_hash }}", "type_id": "00000000-0000-0000-0000-000000000001"}, "relationships": {"assignee": {"data": {"id": "{{user.data.id}}", "type": "user"} }, "project": {"data": {"id": "d4bbe1af-f36e-42f1-87c1-493ca35c320e", "type": "project"}}}, "type": "case"}}
    When the request is sent
    Then the response status is 201 CREATED
    And the response "data" has field "id"
    And the response "data.attributes.title" is equal to "Security breach investigation in {{ unique_hash }}"
    And the response "data.attributes.type" is equal to "STANDARD"
    And the response "data.attributes.priority" is equal to "NOT_DEFINED"

  @team:DataDog/case-management
  Scenario: Create a case returns "Not Found" response
    Given new "CreateCase" request
    And body with value {"data": {"attributes": {"priority": "NOT_DEFINED", "title": "Security breach investigation", "type_id": "00000000-0000-0000-0000-000000000001"}, "relationships": {"assignee": {"data": {"id": "721074c8-63df-4d8f-a43d-ab41dd24ec35", "type": "user"}}, "project": {"data": {"id": "721074c8-63df-4d8f-a43d-ab41dd24ec35", "type": "project"}}}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case view returns "Bad Request" response
    Given new "CreateCaseView" request
    And body with value {"data": {"attributes": {"name": "Open bugs", "project_id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "query": "status:open type:bug"}, "type": "view"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case view returns "Created" response
    Given new "CreateCaseView" request
    And body with value {"data": {"attributes": {"name": "Open bugs", "project_id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "query": "status:open type:bug"}, "type": "view"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Create a case view returns "Not Found" response
    Given new "CreateCaseView" request
    And body with value {"data": {"attributes": {"name": "Open bugs", "project_id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "query": "status:open type:bug"}, "type": "view"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create a maintenance window returns "Bad Request" response
    Given new "CreateMaintenanceWindow" request
    And body with value {"data": {"attributes": {"end_at": "2026-06-01T06:00:00Z", "name": "Weekly maintenance", "query": "project:SEC", "start_at": "2026-06-01T00:00:00Z"}, "type": "maintenance_window"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a maintenance window returns "Created" response
    Given new "CreateMaintenanceWindow" request
    And body with value {"data": {"attributes": {"end_at": "2026-06-01T06:00:00Z", "name": "Weekly maintenance", "query": "project:SEC", "start_at": "2026-06-01T00:00:00Z"}, "type": "maintenance_window"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Create a maintenance window returns "Not Found" response
    Given new "CreateMaintenanceWindow" request
    And body with value {"data": {"attributes": {"end_at": "2026-06-01T06:00:00Z", "name": "Weekly maintenance", "query": "project:SEC", "start_at": "2026-06-01T00:00:00Z"}, "type": "maintenance_window"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create a notification rule returns "Bad Request" response
    Given new "CreateProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"is_enabled": true, "recipients": [{"data": {}, "type": "EMAIL"}], "triggers": [{"data": {}, "type": "CASE_CREATED"}]}, "type": "notification_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a notification rule returns "CREATED" response
    Given new "CreateProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"is_enabled": true, "recipients": [{"data": {}, "type": "EMAIL"}], "triggers": [{"data": {}, "type": "CASE_CREATED"}]}, "type": "notification_rule"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/case-management
  Scenario: Create a notification rule returns "Not Found" response
    Given new "CreateProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"is_enabled": true, "recipients": [{"data": {}, "type": "EMAIL"}], "triggers": [{"data": {}, "type": "CASE_CREATED"}]}, "type": "notification_rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create a project returns "Bad Request" response
    Given new "CreateProject" request
    And body with value {"data": {"attributes": {"enabled_custom_case_types": [], "key": "SEC", "name": "Security Investigation"}, "type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create a project returns "CREATED" response
    Given new "CreateProject" request
    And body with value {"data": {"attributes": {"enabled_custom_case_types": [], "key": "SEC", "name": "Security Investigation"}, "type": "project"}}
    When the request is sent
    Then the response status is 201 CREATED

  @generated @skip @team:DataDog/case-management
  Scenario: Create a project returns "Not Found" response
    Given new "CreateProject" request
    And body with value {"data": {"attributes": {"enabled_custom_case_types": [], "key": "SEC", "name": "Security Investigation"}, "type": "project"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create an automation rule returns "Bad Request" response
    Given new "CreateCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"data": {"handle": "workflow-handle-123"}, "type": "execute_workflow"}, "name": "Auto-assign workflow", "state": "ENABLED", "trigger": {"data": {}, "type": "case_created"}}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create an automation rule returns "Created" response
    Given new "CreateCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"data": {"handle": "workflow-handle-123"}, "type": "execute_workflow"}, "name": "Auto-assign workflow", "state": "ENABLED", "trigger": {"data": {}, "type": "case_created"}}, "type": "rule"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Create an automation rule returns "Not Found" response
    Given new "CreateCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"data": {"handle": "workflow-handle-123"}, "type": "execute_workflow"}, "name": "Auto-assign workflow", "state": "ENABLED", "trigger": {"data": {}, "type": "case_created"}}, "type": "rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Create investigation notebook for case returns "Bad Request" response
    Given new "CreateCaseNotebook" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "notebook"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Create investigation notebook for case returns "No Content" response
    Given new "CreateCaseNotebook" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "notebook"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Create investigation notebook for case returns "Not Found" response
    Given new "CreateCaseNotebook" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"type": "notebook"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case link returns "Bad Request" response
    Given new "DeleteCaseLink" request
    And request contains "link_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case link returns "No Content" response
    Given new "DeleteCaseLink" request
    And request contains "link_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case link returns "Not Found" response
    Given new "DeleteCaseLink" request
    And request contains "link_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case view returns "Bad Request" response
    Given new "DeleteCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case view returns "No Content" response
    Given new "DeleteCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a case view returns "Not Found" response
    Given new "DeleteCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a maintenance window returns "Bad Request" response
    Given new "DeleteMaintenanceWindow" request
    And request contains "maintenance_window_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a maintenance window returns "No Content" response
    Given new "DeleteMaintenanceWindow" request
    And request contains "maintenance_window_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a maintenance window returns "Not Found" response
    Given new "DeleteMaintenanceWindow" request
    And request contains "maintenance_window_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a notification rule returns "API error response" response
    Given new "DeleteProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "notification_rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response

  @generated @skip @team:DataDog/case-management
  Scenario: Delete a notification rule returns "No Content" response
    Given new "DeleteProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "notification_rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Delete an automation rule returns "No Content" response
    Given new "DeleteCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Delete an automation rule returns "Not Found" response
    Given new "DeleteCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/case-management
  Scenario: Delete case comment returns "Bad Request" response
    Given new "DeleteCaseComment" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And request contains "cell_id" parameter with value "not-an-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/case-management
  Scenario: Delete case comment returns "No Content" response
    Given new "DeleteCaseComment" request
    And there is a valid "case" in the system
    And there is a valid "comment" in the system
    And request contains "case_id" parameter from "case.id"
    And request contains "cell_id" parameter from "comment.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/case-management
  Scenario: Delete case comment returns "Not Found" response
    Given new "DeleteCaseComment" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And request contains "cell_id" parameter with value "23fca2aa-4967-4936-bdd7-9157d9e456d7"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Delete custom attribute from case returns "Not Found" response
    Given new "DeleteCaseCustomAttribute" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And request contains "custom_attribute_key" parameter with value "invalid_key"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/case-management
  Scenario: Delete custom attribute from case returns "OK" response
    Given new "DeleteCaseCustomAttribute" request
    And there is a valid "case_type" in the system
    And there is a valid "custom_attribute" in the system
    And there is a valid "case" with a custom "case_type" in the system
    And request contains "case_id" parameter from "case_with_type.id"
    And request contains "custom_attribute_key" parameter from "custom_attribute.attributes.key"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Disable an automation rule returns "Bad Request" response
    Given new "DisableCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Disable an automation rule returns "Not Found" response
    Given new "DisableCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Disable an automation rule returns "OK" response
    Given new "DisableCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Enable an automation rule returns "Bad Request" response
    Given new "EnableCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Enable an automation rule returns "Not Found" response
    Given new "EnableCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Enable an automation rule returns "OK" response
    Given new "EnableCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Favorite a project returns "Bad Request" response
    Given new "FavoriteCaseProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Favorite a project returns "No Content" response
    Given new "FavoriteCaseProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Favorite a project returns "Not Found" response
    Given new "FavoriteCaseProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get a case view returns "Bad Request" response
    Given new "GetCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get a case view returns "Not Found" response
    Given new "GetCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get a case view returns "OK" response
    Given new "GetCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get all projects returns "Bad Request" response
    Given new "GetProjects" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get all projects returns "Not Found" response
    Given new "GetProjects" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get all projects returns "OK" response
    Given new "GetProjects" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get an automation rule returns "Bad Request" response
    Given new "GetCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get an automation rule returns "Not Found" response
    Given new "GetCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get an automation rule returns "OK" response
    Given new "GetCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get case timeline returns "Bad Request" response
    Given new "ListCaseTimeline" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get case timeline returns "Not Found" response
    Given new "ListCaseTimeline" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get case timeline returns "OK" response
    Given new "ListCaseTimeline" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get notification rules returns "Bad Request" response
    Given new "GetProjectNotificationRules" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get notification rules returns "Not Found" response
    Given new "GetProjectNotificationRules" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get notification rules returns "OK" response
    Given new "GetProjectNotificationRules" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/case-management
  Scenario: Get the details of a case returns "Bad Request" response
    Given new "GetCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Get the details of a case returns "Not Found" response
    Given new "GetCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Get the details of a case returns "OK" response
    Given new "GetCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Get the details of a project returns "Bad Request" response
    Given new "GetProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Get the details of a project returns "Not Found" response
    Given new "GetProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Get the details of a project returns "OK" response
    Given new "GetProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Link existing Jira issue to case returns "Bad Request" response
    Given new "LinkJiraIssueToCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"jira_issue_url": "https://jira.example.com/browse/PROJ-123"}, "type": "issues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Link existing Jira issue to case returns "Conflict" response
    Given new "LinkJiraIssueToCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"jira_issue_url": "https://jira.example.com/browse/PROJ-123"}, "type": "issues"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/case-management
  Scenario: Link existing Jira issue to case returns "No Content" response
    Given new "LinkJiraIssueToCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"jira_issue_url": "https://jira.example.com/browse/PROJ-123"}, "type": "issues"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Link existing Jira issue to case returns "Not Found" response
    Given new "LinkJiraIssueToCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"jira_issue_url": "https://jira.example.com/browse/PROJ-123"}, "type": "issues"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Link incident to case returns "Bad Request" response
    Given new "LinkIncident" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incidents"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Link incident to case returns "Created" response
    Given new "LinkIncident" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incidents"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Link incident to case returns "Not Found" response
    Given new "LinkIncident" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "incidents"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List automation rules returns "Bad Request" response
    Given new "ListCaseAutomationRules" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: List automation rules returns "Not Found" response
    Given new "ListCaseAutomationRules" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List automation rules returns "OK" response
    Given new "ListCaseAutomationRules" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: List case links returns "Bad Request" response
    Given new "ListCaseLinks" request
    And request contains "entity_type" parameter from "REPLACE.ME"
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: List case links returns "Not Found" response
    Given new "ListCaseLinks" request
    And request contains "entity_type" parameter from "REPLACE.ME"
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List case links returns "OK" response
    Given new "ListCaseLinks" request
    And request contains "entity_type" parameter from "REPLACE.ME"
    And request contains "entity_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: List case views returns "Bad Request" response
    Given new "ListCaseViews" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: List case views returns "Not Found" response
    Given new "ListCaseViews" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List case views returns "OK" response
    Given new "ListCaseViews" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: List case watchers returns "Bad Request" response
    Given new "ListCaseWatchers" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: List case watchers returns "Not Found" response
    Given new "ListCaseWatchers" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List case watchers returns "OK" response
    Given new "ListCaseWatchers" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: List maintenance windows returns "Bad Request" response
    Given new "ListMaintenanceWindows" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: List maintenance windows returns "Not Found" response
    Given new "ListMaintenanceWindows" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List maintenance windows returns "OK" response
    Given new "ListMaintenanceWindows" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: List project favorites returns "Bad Request" response
    Given new "ListUserCaseProjectFavorites" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: List project favorites returns "Not Found" response
    Given new "ListUserCaseProjectFavorites" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: List project favorites returns "OK" response
    Given new "ListUserCaseProjectFavorites" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Remove Jira issue link from case returns "Bad Request" response
    Given new "UnlinkJiraIssue" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Remove Jira issue link from case returns "No Content" response
    Given new "UnlinkJiraIssue" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Remove Jira issue link from case returns "Not Found" response
    Given new "UnlinkJiraIssue" request
    And request contains "case_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Remove a project returns "API error response" response
    Given new "DeleteProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 API error response

  @generated @skip @team:DataDog/case-management
  Scenario: Remove a project returns "No Content" response
    Given new "DeleteProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Remove insights from a case returns "Bad Request" response
    Given new "RemoveCaseInsights" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"insights": [{"ref": "/monitors/12345?q=total", "resource_id": "12345", "type": "SECURITY_SIGNAL"}]}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Remove insights from a case returns "Not Found" response
    Given new "RemoveCaseInsights" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"insights": [{"ref": "/monitors/12345?q=total", "resource_id": "12345", "type": "SECURITY_SIGNAL"}]}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Remove insights from a case returns "OK" response
    Given new "RemoveCaseInsights" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"insights": [{"ref": "/monitors/12345?q=total", "resource_id": "12345", "type": "SECURITY_SIGNAL"}]}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Search cases returns "Bad Request" response
    Given new "SearchCases" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Search cases returns "Not Found" response
    Given new "SearchCases" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Search cases returns "OK" response
    Given new "SearchCases" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/case-management @with-pagination
  Scenario: Search cases returns "OK" response with pagination
    Given new "SearchCases" request
    And request contains "page[size]" parameter with value 2
    And request contains "filter" parameter with value "status:closed"
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/case-management
  Scenario: Unarchive case returns "Bad Request" response
    Given new "UnarchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Unarchive case returns "Not Found" response
    Given new "UnarchiveCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Unarchive case returns "OK" response
    Given new "UnarchiveCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Unassign case returns "Bad Request" response
    Given new "UnassignCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Unassign case returns "Not Found" response
    Given new "UnassignCase" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Unassign case returns "OK" response
    Given new "UnassignCase" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Unfavorite a project returns "Bad Request" response
    Given new "UnfavoriteCaseProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Unfavorite a project returns "No Content" response
    Given new "UnfavoriteCaseProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Unfavorite a project returns "Not Found" response
    Given new "UnfavoriteCaseProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Unwatch a case returns "Bad Request" response
    Given new "UnwatchCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Unwatch a case returns "No Content" response
    Given new "UnwatchCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Unwatch a case returns "Not Found" response
    Given new "UnwatchCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update a case view returns "Bad Request" response
    Given new "UpdateCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "view"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update a case view returns "Not Found" response
    Given new "UpdateCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "view"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update a case view returns "OK" response
    Given new "UpdateCaseView" request
    And request contains "view_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "view"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update a maintenance window returns "Bad Request" response
    Given new "UpdateMaintenanceWindow" request
    And request contains "maintenance_window_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "maintenance_window"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update a maintenance window returns "Not Found" response
    Given new "UpdateMaintenanceWindow" request
    And request contains "maintenance_window_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "maintenance_window"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update a maintenance window returns "OK" response
    Given new "UpdateMaintenanceWindow" request
    And request contains "maintenance_window_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {}, "type": "maintenance_window"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update a notification rule returns "Bad Request" response
    Given new "UpdateProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "notification_rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"recipients": [{"data": {}, "type": "EMAIL"}], "triggers": [{"data": {}, "type": "CASE_CREATED"}]}, "type": "notification_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update a notification rule returns "No Content" response
    Given new "UpdateProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "notification_rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"recipients": [{"data": {}, "type": "EMAIL"}], "triggers": [{"data": {}, "type": "CASE_CREATED"}]}, "type": "notification_rule"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/case-management
  Scenario: Update a notification rule returns "Not Found" response
    Given new "UpdateProjectNotificationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "notification_rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"recipients": [{"data": {}, "type": "EMAIL"}], "triggers": [{"data": {}, "type": "CASE_CREATED"}]}, "type": "notification_rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update a project returns "Bad Request" response
    Given new "UpdateProject" request
    And request contains "project_id" parameter with value "d4bbe1af-f36e-42f1-87c1-493ca35c320e"
    And body with value {"data": {"type": "invalid_type"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update a project returns "Not Found" response
    Given new "UpdateProject" request
    And request contains "project_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"type": "project", "attributes": {"name": "Updated Project Name"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update a project returns "OK" response
    Given new "UpdateProject" request
    And request contains "project_id" parameter with value "d4bbe1af-f36e-42f1-87c1-493ca35c320e"
    And body with value {"data": {"type": "project", "attributes": {"name": "Updated Project Name {{ unique }}"}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has field "id"
    And the response "data.attributes.name" is equal to "Updated Project Name {{ unique }}"

  @generated @skip @team:DataDog/case-management
  Scenario: Update an automation rule returns "Bad Request" response
    Given new "UpdateCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"data": {"handle": "workflow-handle-123"}, "type": "execute_workflow"}, "name": "Auto-assign workflow", "state": "ENABLED", "trigger": {"data": {}, "type": "case_created"}}, "type": "rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update an automation rule returns "Not Found" response
    Given new "UpdateCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"data": {"handle": "workflow-handle-123"}, "type": "execute_workflow"}, "name": "Auto-assign workflow", "state": "ENABLED", "trigger": {"data": {}, "type": "case_created"}}, "type": "rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update an automation rule returns "OK" response
    Given new "UpdateCaseAutomationRule" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"data": {"handle": "workflow-handle-123"}, "type": "execute_workflow"}, "name": "Auto-assign workflow", "state": "ENABLED", "trigger": {"data": {}, "type": "case_created"}}, "type": "rule"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/case-management
  Scenario: Update case attributes returns "Bad Request" response
    Given new "UpdateAttributes" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value { "data": { "type": "case", "attributes": { "attributes": { "service": "web-store"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case attributes returns "Not Found" response
    Given new "UpdateAttributes" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value { "data": { "type": "case", "attributes": { "attributes": {} } } }
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case attributes returns "OK" response
    Given new "UpdateAttributes" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"attributes": {"env": ["test"], "service": ["web-store", "web-api"], "team": ["engineer"]}}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update case comment returns "Bad Request" response
    Given new "UpdateCaseComment" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "cell_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"comment": "Updated comment text"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update case comment returns "Not Found" response
    Given new "UpdateCaseComment" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "cell_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"comment": "Updated comment text"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update case comment returns "OK" response
    Given new "UpdateCaseComment" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "cell_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"comment": "Updated comment text"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/case-management
  Scenario: Update case custom attribute returns "Bad Request" response
    Given new "UpdateCaseCustomAttribute" request
    And there is a valid "case_type" in the system
    And there is a valid "custom_attribute" in the system
    And there is a valid "case" with a custom "case_type" in the system
    And request contains "case_id" parameter from "case_with_type.id"
    And request contains "custom_attribute_key" parameter from "custom_attribute.attributes.key"
    And body with value {"data": {"attributes": {"type": "FLOAT", "is_multi": true, "value": [1.0, 2.4]}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case custom attribute returns "Not Found" response
    Given new "UpdateCaseCustomAttribute" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And request contains "custom_attribute_key" parameter with value "invalid_key"
    And body with value {"data": {"attributes": {"type": "TEXT", "is_multi": true, "value": ["Abba", "The Cure"]}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/case-management
  Scenario: Update case custom attribute returns "OK" response
    Given new "UpdateCaseCustomAttribute" request
    And there is a valid "case_type" in the system
    And there is a valid "custom_attribute" in the system
    And there is a valid "case" with a custom "case_type" in the system
    And request contains "case_id" parameter from "case_with_type.id"
    And request contains "custom_attribute_key" parameter from "custom_attribute.attributes.key"
    And body with value {"data": {"attributes": {"type": "TEXT", "is_multi": true, "value": ["Abba", "The Cure"]}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/case-management
  Scenario: Update case description returns "Bad Request" response
    Given new "UpdateCaseDescription" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"description": "Seeing some weird memory increase... We shouldn't ignore this"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case description returns "Not Found" response
    Given new "UpdateCaseDescription" request
    And request contains "case_id" parameter with value "0198c6b0-2a0a-7bea-87ff-3876f119aebb"
    And body with value {"data": {"attributes": {"description": "Seeing some weird memory increase... We shouldn't ignore this"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case description returns "OK" response
    Given new "UpdateCaseDescription" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"description": "Seeing some weird memory increase... Updating the description"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update case due date returns "Bad Request" response
    Given new "UpdateCaseDueDate" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"due_date": "2026-12-31"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update case due date returns "Not Found" response
    Given new "UpdateCaseDueDate" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"due_date": "2026-12-31"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update case due date returns "OK" response
    Given new "UpdateCaseDueDate" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"due_date": "2026-12-31"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Update case priority returns "Bad Request" response
    Given new "UpdatePriority" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"priority": "P1234"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case priority returns "Not Found" response
    Given new "UpdatePriority" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"priority": "P3"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case priority returns "OK" response
    Given new "UpdatePriority" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"priority": "P3"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.priority" is equal to "P3"

  @generated @skip @team:DataDog/case-management
  Scenario: Update case project returns "Bad Request" response
    Given new "MoveCaseToProject" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "project"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update case project returns "Not Found" response
    Given new "MoveCaseToProject" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "project"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update case project returns "OK" response
    Given new "MoveCaseToProject" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "e555e290-ed65-49bd-ae18-8acbfcf18db7", "type": "project"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Update case resolved reason returns "Bad Request" response
    Given new "UpdateCaseResolvedReason" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"security_resolved_reason": "FALSE_POSITIVE"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Update case resolved reason returns "Not Found" response
    Given new "UpdateCaseResolvedReason" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"security_resolved_reason": "FALSE_POSITIVE"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/case-management
  Scenario: Update case resolved reason returns "OK" response
    Given new "UpdateCaseResolvedReason" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"security_resolved_reason": "FALSE_POSITIVE"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/case-management
  Scenario: Update case status returns "Bad Request" response
    Given new "UpdateStatus" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"status": "OPENED"}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case status returns "Not Found" response
    Given new "UpdateStatus" request
    And request contains "case_id" parameter with value "67d80aa3-36ff-44b9-a694-c501a7591737"
    And body with value {"data": {"attributes": {"status": "OPEN"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case status returns "OK" response
    Given new "UpdateStatus" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"status": "IN_PROGRESS"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.status" is equal to "IN_PROGRESS"

  @team:DataDog/case-management
  Scenario: Update case title returns "Bad Request" response
    Given new "UpdateCaseTitle" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"title": ""}, "type": "case"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/case-management
  Scenario: Update case title returns "Not Found" response
    Given new "UpdateCaseTitle" request
    And request contains "case_id" parameter with value "0198c6b8-b08f-7c08-978a-d95217f2eeac"
    And body with value {"data": {"attributes": {"title": "Memory leak investigation on API"}, "type": "case"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/case-management
  Scenario: Update case title returns "OK" response
    Given new "UpdateCaseTitle" request
    And there is a valid "case" in the system
    And request contains "case_id" parameter from "case.id"
    And body with value {"data": {"attributes": {"title": "[UPDATED] Memory leak investigation on API"}, "type": "case"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/case-management
  Scenario: Watch a case returns "Bad Request" response
    Given new "WatchCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/case-management
  Scenario: Watch a case returns "Created" response
    Given new "WatchCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/case-management
  Scenario: Watch a case returns "Not Found" response
    Given new "WatchCase" request
    And request contains "case_id" parameter from "REPLACE.ME"
    And request contains "user_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found
