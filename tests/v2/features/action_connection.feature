@endpoint(action-connection) @endpoint(action-connection-v2)
Feature: Action Connection
  Action Connections extend your installed integrations and allow you to
  take action in your third-party systems (e.g. AWS, GitLab, and OpenAI)
  with Datadog’s [Workflow
  Automation](https://docs.datadoghq.com/service_management/workflows/) and
  [App Builder](https://docs.datadoghq.com/service_management/app_builder/)
  products.  Datadog’s Integrations automatically provide authentication for
  Slack, Microsoft Teams, PagerDuty, Opsgenie, Jira, GitHub, and Statuspage.
  You do not need additional connections in order to access these tools
  within Workflow Automation and App Builder.  We offer granular access
  control for editing and resolving connections.  **Note:** The Action
  Connection API currently supports AWS and HTTP integrations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ActionConnection" API

  @team:Datadog/action-platform
  Scenario: Create a new Action Connection returns "Bad Request" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"1"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/action-platform
  Scenario: Create a new Action Connection returns "Successfully created Action Connection" response
    Given new "CreateActionConnection" request
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection DELETE_ME","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 201 Successfully created Action Connection

  @generated @skip @team:Datadog/action-platform
  Scenario: Create a new Action Connection returns "Successfully created an Action Connection." response
    Given new "CreateActionConnection" request
    And body with value {"data": {"attributes": {"integration": {"credentials": {"account_id": "111222333444", "role": "my-role", "type": "AWSAssumeRole"}, "type": "AWS"}, "name": "My AWS Connection"}, "type": "action_connection"}}
    When the request is sent
    Then the response status is 201 Successfully created an Action Connection.

  @team:Datadog/action-platform
  Scenario: Delete an existing Action Connection returns "Not Found" response
    Given new "DeleteActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/action-platform
  Scenario: Delete an existing Action Connection returns "Successfully deleted Action Connection" response
    Given there is a valid "action_connection" in the system
    And new "DeleteActionConnection" request
    And request contains "connection_id" parameter from "action_connection.data.id"
    When the request is sent
    Then the response status is 204 The resource was deleted successfully.

  @generated @skip @team:Datadog/action-platform
  Scenario: Delete an existing Action Connection returns "The resource was deleted successfully." response
    Given new "DeleteActionConnection" request
    And request contains "connection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 The resource was deleted successfully.

  @team:Datadog/action-platform
  Scenario: Get an existing Action Connection returns "Bad Request" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "bad-format"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/action-platform
  Scenario: Get an existing Action Connection returns "Not Found" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/action-platform
  Scenario: Get an existing Action Connection returns "Successfully get Action Connection" response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    When the request is sent
    Then the response status is 200 Successfully get Action Connection

  @generated @skip @team:Datadog/action-platform
  Scenario: Get an existing Action Connection returns "Successfully got an Action Connection." response
    Given new "GetActionConnection" request
    And request contains "connection_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Successfully got an Action Connection.

  @team:Datadog/action-platform
  Scenario: Update an existing Action Connection returns "Bad Request" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"1"}}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/action-platform
  Scenario: Update an existing Action Connection returns "Not Found" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:Datadog/action-platform
  Scenario: Update an existing Action Connection returns "Successfully updated Action Connection" response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter with value "cb460d51-3c88-4e87-adac-d47131d0423d"
    And body with value {"data":{"type":"action_connection","attributes":{"name":"Cassette Connection","integration":{"type":"AWS","credentials":{"type":"AWSAssumeRole","role":"MyRoleUpdated","account_id":"123456789123"}}}}}
    When the request is sent
    Then the response status is 200 Successfully updated Action Connection

  @generated @skip @team:Datadog/action-platform
  Scenario: Update an existing Action Connection returns "Successfully updated an Action Connection." response
    Given new "UpdateActionConnection" request
    And request contains "connection_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"integration": {"credentials": {"account_id": "111222333444", "role": "my-role", "type": "AWSAssumeRole"}, "type": "AWS"}, "name": "My AWS Connection"}, "type": "action_connection"}}
    When the request is sent
    Then the response status is 200 Successfully updated an Action Connection.
