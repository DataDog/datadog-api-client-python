@endpoint(workflow-automation) @endpoint(workflow-automation-v2)
Feature: Workflow Automation
  Datadog Workflow Automation allows you to automate your end-to-end
  processes by connecting Datadog with the rest of your tech stack. Build
  workflows to auto-remediate your alerts, streamline your incident and
  security processes, and reduce manual toil. Workflow Automation supports
  over 1,000+ OOTB actions, including AWS, JIRA, ServiceNow, GitHub, and
  OpenAI. Learn more in our Workflow Automation docs
  [here](https://docs.datadoghq.com/service_management/workflows/).

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

  @team:DataDog/workflow-automation-dev
  Scenario: Create a Workflow returns "Bad request" response
    Given new "CreateWorkflow" request
    And body with value {"data": {"attributes": {"name": "Too many characters in description", "description": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "spec": {}}, "type": "workflows"}}
    When the request is sent
    Then the response status is 400 Bad request

  @team:DataDog/workflow-automation-dev
  Scenario: Create a Workflow returns "Successfully created a workflow." response
    Given new "CreateWorkflow" request
    And body with value {"data": {"attributes": {"description": "A sample workflow.", "name": "Example Workflow", "published": true, "spec": {"connectionEnvs": [{"connections": [{"connectionId": "11111111-1111-1111-1111-111111111111", "label": "INTEGRATION_DATADOG"}], "env": "default"}], "inputSchema": {"parameters": [{"defaultValue": "default", "name": "input", "type": "STRING"}]}, "outputSchema": {"parameters": [{"name": "output", "type": "ARRAY_OBJECT", "value": "outputValue"}]}, "steps": [{"actionId": "com.datadoghq.dd.monitor.listMonitors", "connectionLabel": "INTEGRATION_DATADOG", "name": "Step1", "outboundEdges": [{"branchName": "main", "nextStepName": "Step2"}], "parameters": [{"name": "tags", "value": "service:monitoring"}]}, {"actionId": "com.datadoghq.core.noop", "name": "Step2"}], "triggers": [{"monitorTrigger": {"rateLimit": {"count": 1, "interval": "3600s"}}, "startStepNames": ["Step1"]}, {"startStepNames": ["Step1"], "githubWebhookTrigger": {}}]}, "tags": ["team:infra", "service:monitoring", "foo:bar"]}, "type": "workflows"}}
    When the request is sent
    Then the response status is 201 Successfully created a workflow.

  @team:DataDog/workflow-automation-dev
  Scenario: Delete an existing Workflow returns "Not found" response
    Given new "DeleteWorkflow" request
    And request contains "workflow_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/workflow-automation-dev
  Scenario: Delete an existing Workflow returns "Successfully deleted a workflow." response
    Given there is a valid "workflow" in the system
    And new "DeleteWorkflow" request
    And request contains "workflow_id" parameter from "workflow.data.id"
    When the request is sent
    Then the response status is 204 Successfully deleted a workflow.

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

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing Workflow returns "Bad request" response
    Given new "GetWorkflow" request
    And request contains "workflow_id" parameter with value "bad-format"
    When the request is sent
    Then the response status is 400 Bad request

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing Workflow returns "Not found" response
    Given new "GetWorkflow" request
    And request contains "workflow_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/workflow-automation-dev
  Scenario: Get an existing Workflow returns "Successfully got a workflow." response
    Given there is a valid "workflow" in the system
    And new "GetWorkflow" request
    And request contains "workflow_id" parameter from "workflow.data.id"
    When the request is sent
    Then the response status is 200 Successfully got a workflow.

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

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Workflow returns "Bad request" response
    Given there is a valid "workflow" in the system
    And new "UpdateWorkflow" request
    And request contains "workflow_id" parameter from "workflow.data.id"
    And body with value {"data": {"attributes": {"name": "Too many characters in description", "description": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "spec": {}}, "id": "22222222-2222-2222-2222-222222222222", "type": "workflows"}}
    When the request is sent
    Then the response status is 400 Bad request

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Workflow returns "Not found" response
    Given new "UpdateWorkflow" request
    And request contains "workflow_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    And body with value {"data": {"attributes": {"description": "A sample workflow.", "name": "Example Workflow", "published": true, "spec": {"connectionEnvs": [{"connections": [{"connectionId": "11111111-1111-1111-1111-111111111111", "label": "INTEGRATION_DATADOG"}], "env": "default"}], "inputSchema": {"parameters": [{"defaultValue": "default", "name": "input", "type": "STRING"}]}, "outputSchema": {"parameters": [{"name": "output", "type": "ARRAY_OBJECT", "value": "outputValue"}]}, "steps": [{"actionId": "com.datadoghq.dd.monitor.listMonitors", "connectionLabel": "INTEGRATION_DATADOG", "name": "Step1", "outboundEdges": [{"branchName": "main", "nextStepName": "Step2"}], "parameters": [{"name": "tags", "value": "service:monitoring"}]}, {"actionId": "com.datadoghq.core.noop", "name": "Step2"}], "triggers": [{"monitorTrigger": {"rateLimit": {"count": 1, "interval": "3600s"}}, "startStepNames": ["Step1"]}, {"startStepNames": ["Step1"], "githubWebhookTrigger": {}}]}, "tags": ["team:infra", "service:monitoring", "foo:bar"]}, "id": "22222222-2222-2222-2222-222222222222", "type": "workflows"}}
    When the request is sent
    Then the response status is 404 Not found

  @team:DataDog/workflow-automation-dev
  Scenario: Update an existing Workflow returns "Successfully updated a workflow." response
    Given there is a valid "workflow" in the system
    And new "UpdateWorkflow" request
    And request contains "workflow_id" parameter from "workflow.data.id"
    And body with value {"data": {"attributes": {"description": "A sample workflow.", "name": "Example Workflow", "published": true, "spec": {"connectionEnvs": [{"connections": [{"connectionId": "11111111-1111-1111-1111-111111111111", "label": "INTEGRATION_DATADOG"}], "env": "default"}], "inputSchema": {"parameters": [{"defaultValue": "default", "name": "input", "type": "STRING"}]}, "outputSchema": {"parameters": [{"name": "output", "type": "ARRAY_OBJECT", "value": "outputValue"}]}, "steps": [{"actionId": "com.datadoghq.dd.monitor.listMonitors", "connectionLabel": "INTEGRATION_DATADOG", "name": "Step1", "outboundEdges": [{"branchName": "main", "nextStepName": "Step2"}], "parameters": [{"name": "tags", "value": "service:monitoring"}]}, {"actionId": "com.datadoghq.core.noop", "name": "Step2"}], "triggers": [{"monitorTrigger": {"rateLimit": {"count": 1, "interval": "3600s"}}, "startStepNames": ["Step1"]}, {"startStepNames": ["Step1"], "githubWebhookTrigger": {}}]}, "tags": ["team:infra", "service:monitoring", "foo:bar"]}, "id": "22222222-2222-2222-2222-222222222222", "type": "workflows"}}
    When the request is sent
    Then the response status is 200 Successfully updated a workflow.
