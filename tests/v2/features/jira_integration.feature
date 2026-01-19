@endpoint(jira-integration) @endpoint(jira-integration-v2)
Feature: Jira Integration
  Manage your Jira Integration. Atlassian Jira is a project management and
  issue tracking tool for teams to coordinate work and handle tasks
  efficiently.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "JiraIntegration" API

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create Jira issue template returns "Bad Request" response
    Given operation "CreateJiraIssueTemplate" enabled
    And new "CreateJiraIssueTemplate" request
    And body with value {"data": {"attributes": {"fields": {"description": {"payload": "Test", "type": "json"}}, "issue_type_id": "12730", "jira-account": {"id": "80f16d40-1fba-486e-b1fc-983e6ca19bec"}, "name": "test-template", "project_id": "10772"}, "type": "jira-issue-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Create Jira issue template returns "Created" response
    Given operation "CreateJiraIssueTemplate" enabled
    And new "CreateJiraIssueTemplate" request
    And body with value {"data": {"attributes": {"fields": {"description": {"payload": "Test", "type": "json"}}, "issue_type_id": "12730", "jira-account": {"id": "80f16d40-1fba-486e-b1fc-983e6ca19bec"}, "name": "test-template", "project_id": "10772"}, "type": "jira-issue-template"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete Jira account returns "Bad Request" response
    Given operation "DeleteJiraAccount" enabled
    And new "DeleteJiraAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete Jira account returns "No Content" response
    Given operation "DeleteJiraAccount" enabled
    And new "DeleteJiraAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Delete Jira issue template returns "No Content" response
    Given operation "DeleteJiraIssueTemplate" enabled
    And new "DeleteJiraIssueTemplate" request
    And request contains "issue_template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get Jira issue template returns "Bad Request" response
    Given operation "GetJiraIssueTemplate" enabled
    And new "GetJiraIssueTemplate" request
    And request contains "issue_template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Get Jira issue template returns "OK" response
    Given operation "GetJiraIssueTemplate" enabled
    And new "GetJiraIssueTemplate" request
    And request contains "issue_template_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List Jira accounts returns "Not Found" response
    Given operation "ListJiraAccounts" enabled
    And new "ListJiraAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List Jira accounts returns "OK" response
    Given operation "ListJiraAccounts" enabled
    And new "ListJiraAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: List Jira issue templates returns "OK" response
    Given operation "ListJiraIssueTemplates" enabled
    And new "ListJiraIssueTemplates" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update Jira issue template returns "Bad Request" response
    Given operation "UpdateJiraIssueTemplate" enabled
    And new "UpdateJiraIssueTemplate" request
    And request contains "issue_template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": {"description": {"payload": "Updated Description", "type": "json"}}, "name": "test_template_updated"}, "type": "jira-issue-template"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/collaboration-integrations
  Scenario: Update Jira issue template returns "OK" response
    Given operation "UpdateJiraIssueTemplate" enabled
    And new "UpdateJiraIssueTemplate" request
    And request contains "issue_template_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"fields": {"description": {"payload": "Updated Description", "type": "json"}}, "name": "test_template_updated"}, "type": "jira-issue-template"}}
    When the request is sent
    Then the response status is 200 OK
