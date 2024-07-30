@endpoint(workflow-automation) @endpoint(workflow-automation-v2)
Feature: Workflow Automation
  Automate your teams operational processes with Datadog Workflow
  Automation.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "WorkflowAutomation" API

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Cancel a workflow instance returns "Bad Request" response
    Given new "CancelWorkflowInstance" request
    And request contains "workflow_id" parameter with value "malformed"
    And request contains "instance_id" parameter with value "malformed"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Cancel a workflow instance returns "Not Found" response
    Given new "CancelWorkflowInstance" request
    And request contains "workflow_id" parameter with value "0233a3b7-b7ba-425e-a8cc-375ca2020b5b"
    And request contains "instance_id" parameter with value "e0c64dc8-f946-4ae8-8d79-54569031ce67"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Cancel a workflow instance returns "OK" response
    Given new "CancelWorkflowInstance" request
    And request contains "workflow_id" parameter with value "ccf73164-1998-4785-a7a3-8d06c7e5f558"
    And request contains "instance_id" parameter with value "305a472b-71ab-4ce8-8f8d-75db635627b5"
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Execute a workflow returns "Bad Request" response
    Given new "CreateWorkflowInstance" request
    And request contains "workflow_id" parameter with value "malformed"
    And body with value { "meta": { "payload": { "input": "value" } } }
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Execute a workflow returns "Created" response
    Given new "CreateWorkflowInstance" request
    And request contains "workflow_id" parameter with value "ccf73164-1998-4785-a7a3-8d06c7e5f558"
    And body with value { "meta": { "payload": { "input": "value" } } }
    When the request is sent
    Then the response status is 200 Created

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Get a workflow instance returns "Bad Request" response
    Given new "GetWorkflowInstance" request
    And request contains "workflow_id" parameter with value "malformed"
    And request contains "instance_id" parameter with value "malformed"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Get a workflow instance returns "Not Found" response
    Given new "GetWorkflowInstance" request
    And request contains "workflow_id" parameter with value "0233a3b7-b7ba-425e-a8cc-375ca2020b5b"
    And request contains "instance_id" parameter with value "e0c64dc8-f946-4ae8-8d79-54569031ce67"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: Get a workflow instance returns "OK" response
    Given new "GetWorkflowInstance" request
    And request contains "workflow_id" parameter with value "ccf73164-1998-4785-a7a3-8d06c7e5f558"
    And request contains "instance_id" parameter with value "305a472b-71ab-4ce8-8f8d-75db635627b5"
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: List workflow instances returns "Bad Request" response
    Given new "ListWorkflowInstances" request
    And request contains "workflow_id" parameter with value "malformed"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/workflow-automation-dev
  Scenario: List workflow instances returns "OK" response
    Given new "ListWorkflowInstances" request
    And request contains "workflow_id" parameter with value "ccf73164-1998-4785-a7a3-8d06c7e5f558"
    When the request is sent
    Then the response status is 200 OK
