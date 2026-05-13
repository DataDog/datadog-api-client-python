@endpoint(dependency-management) @endpoint(dependency-management-v2)
Feature: Dependency Management
  Manage AI-powered dependency upgrade workflows for your organization's
  repositories.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DependencyManagement" API

  @generated @skip @team:DataDog/dependency-management
  Scenario: Cancel a workflow execution returns "Conflict" response
    Given operation "CancelWorkflowExecution" enabled
    And new "CancelWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/dependency-management
  Scenario: Cancel a workflow execution returns "No Content" response
    Given operation "CancelWorkflowExecution" enabled
    And new "CancelWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dependency-management
  Scenario: Cancel a workflow execution returns "Not Found" response
    Given operation "CancelWorkflowExecution" enabled
    And new "CancelWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Cancel workflow executions returns "Not Found" response
    Given operation "CancelWorkflowExecutions" enabled
    And new "CancelWorkflowExecutions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Cancel workflow executions returns "OK" response
    Given operation "CancelWorkflowExecutions" enabled
    And new "CancelWorkflowExecutions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dependency-management
  Scenario: Create an AI workflow returns "Bad Request" response
    Given operation "CreateAIWorkflow" enabled
    And new "CreateAIWorkflow" request
    And body with value {"entities": [[{"entity_kind": "service", "entity_name": "my-service", "entity_namespace": "default", "entity_team": "platform"}]], "filtering_logic": {"teams": ["platform"]}, "grouping_logic": "by-service", "idp_campaign_id": "campaign-abc123", "max_number_of_entities_per_session": 5, "prompt": "Upgrade the lodash dependency to version 4.17.21", "repository": "DataDog/datadog-agent", "user": "john.doe@example.com", "workflow_name": "Upgrade lodash to 4.17.21"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dependency-management
  Scenario: Create an AI workflow returns "Created" response
    Given operation "CreateAIWorkflow" enabled
    And new "CreateAIWorkflow" request
    And body with value {"entities": [[{"entity_kind": "service", "entity_name": "my-service", "entity_namespace": "default", "entity_team": "platform"}]], "filtering_logic": {"teams": ["platform"]}, "grouping_logic": "by-service", "idp_campaign_id": "campaign-abc123", "max_number_of_entities_per_session": 5, "prompt": "Upgrade the lodash dependency to version 4.17.21", "repository": "DataDog/datadog-agent", "user": "john.doe@example.com", "workflow_name": "Upgrade lodash to 4.17.21"}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/dependency-management
  Scenario: Create workflow executions returns "Bad Request" response
    Given operation "CreateWorkflowExecution" enabled
    And new "CreateWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dependency-management
  Scenario: Create workflow executions returns "Created" response
    Given operation "CreateWorkflowExecution" enabled
    And new "CreateWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/dependency-management
  Scenario: Create workflow executions returns "Not Found" response
    Given operation "CreateWorkflowExecution" enabled
    And new "CreateWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Delete an AI workflow returns "No Content" response
    Given operation "DeleteAIWorkflow" enabled
    And new "DeleteAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dependency-management
  Scenario: Delete an AI workflow returns "Not Found" response
    Given operation "DeleteAIWorkflow" enabled
    And new "DeleteAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Delete workflow executions returns "No Content" response
    Given operation "DeleteWorkflowExecutions" enabled
    And new "DeleteWorkflowExecutions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/dependency-management
  Scenario: Delete workflow executions returns "Not Found" response
    Given operation "DeleteWorkflowExecutions" enabled
    And new "DeleteWorkflowExecutions" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Get an AI workflow returns "Not Found" response
    Given operation "GetAIWorkflow" enabled
    And new "GetAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Get an AI workflow returns "OK" response
    Given operation "GetAIWorkflow" enabled
    And new "GetAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dependency-management
  Scenario: List AI workflow instances returns "Not Found" response
    Given operation "ListAIWorkflowInstances" enabled
    And new "ListAIWorkflowInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: List AI workflow instances returns "OK" response
    Given operation "ListAIWorkflowInstances" enabled
    And new "ListAIWorkflowInstances" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dependency-management
  Scenario: List AI workflows returns "Bad Request" response
    Given operation "ListAIWorkflows" enabled
    And new "ListAIWorkflows" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dependency-management
  Scenario: List AI workflows returns "OK" response
    Given operation "ListAIWorkflows" enabled
    And new "ListAIWorkflows" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dependency-management
  Scenario: List PR outputs returns "Not Found" response
    Given operation "ListPROutputs" enabled
    And new "ListPROutputs" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: List PR outputs returns "OK" response
    Given operation "ListPROutputs" enabled
    And new "ListPROutputs" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dependency-management
  Scenario: List execution steps returns "Not Found" response
    Given operation "ListExecutionSteps" enabled
    And new "ListExecutionSteps" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: List execution steps returns "OK" response
    Given operation "ListExecutionSteps" enabled
    And new "ListExecutionSteps" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/dependency-management
  Scenario: Rerun a workflow execution returns "Conflict" response
    Given operation "RerunWorkflowExecution" enabled
    And new "RerunWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/dependency-management
  Scenario: Rerun a workflow execution returns "Created" response
    Given operation "RerunWorkflowExecution" enabled
    And new "RerunWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/dependency-management
  Scenario: Rerun a workflow execution returns "Not Found" response
    Given operation "RerunWorkflowExecution" enabled
    And new "RerunWorkflowExecution" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Update an AI workflow returns "Bad Request" response
    Given operation "UpdateAIWorkflow" enabled
    And new "UpdateAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"completed_at": "2024-06-01T12:00:00Z", "entities": [[{"entity_kind": "service", "entity_name": "my-service", "entity_namespace": "default", "entity_team": "platform"}]], "filtering_logic": {"teams": ["platform"]}, "grouping_logic": "by-team", "max_number_of_entities_per_session": 10, "prompt": "Updated prompt for the dependency upgrade", "repository": "DataDog/datadog-agent", "workflow_name": "Updated workflow name"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/dependency-management
  Scenario: Update an AI workflow returns "Not Found" response
    Given operation "UpdateAIWorkflow" enabled
    And new "UpdateAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"completed_at": "2024-06-01T12:00:00Z", "entities": [[{"entity_kind": "service", "entity_name": "my-service", "entity_namespace": "default", "entity_team": "platform"}]], "filtering_logic": {"teams": ["platform"]}, "grouping_logic": "by-team", "max_number_of_entities_per_session": 10, "prompt": "Updated prompt for the dependency upgrade", "repository": "DataDog/datadog-agent", "workflow_name": "Updated workflow name"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/dependency-management
  Scenario: Update an AI workflow returns "OK" response
    Given operation "UpdateAIWorkflow" enabled
    And new "UpdateAIWorkflow" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"completed_at": "2024-06-01T12:00:00Z", "entities": [[{"entity_kind": "service", "entity_name": "my-service", "entity_namespace": "default", "entity_team": "platform"}]], "filtering_logic": {"teams": ["platform"]}, "grouping_logic": "by-team", "max_number_of_entities_per_session": 10, "prompt": "Updated prompt for the dependency upgrade", "repository": "DataDog/datadog-agent", "workflow_name": "Updated workflow name"}
    When the request is sent
    Then the response status is 200 OK
