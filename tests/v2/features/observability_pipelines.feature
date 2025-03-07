@endpoint(observability-pipelines) @endpoint(observability-pipelines-v2)
Feature: Observability Pipelines
  Observability Pipelines are awesome!

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ObservabilityPipelines" API

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "Bad Request" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": ""}, "id": "e8890e15-053e-4d34-9404-1b41b9e403e2", "type": "pipeline"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "Pipeline created" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": ""}, "id": "e8890e15-053e-4d34-9404-1b41b9e403e2", "type": "pipeline"}}
    When the request is sent
    Then the response status is 201 Pipeline created

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Delete a specific pipeline returns "Not Found" response
    Given new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Delete a specific pipeline returns "Pipeline deleted" response
    Given new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Pipeline deleted

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Get a specific pipeline returns "Details of a pipeline" response
    Given new "GetPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 Details of a pipeline

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Get a specific pipeline returns "Not Found" response
    Given new "GetPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Get all pipelines returns "A list of pipelines" response
    Given new "ListPipelines" request
    When the request is sent
    Then the response status is 200 A list of pipelines

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Update a specific pipeline returns "Bad Request" response
    Given new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": ""}, "id": "e8890e15-053e-4d34-9404-1b41b9e403e2", "type": "pipeline"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Update a specific pipeline returns "Not Found" response
    Given new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": ""}, "id": "e8890e15-053e-4d34-9404-1b41b9e403e2", "type": "pipeline"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Update a specific pipeline returns "Pipeline updated" response
    Given new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": ""}, "id": "e8890e15-053e-4d34-9404-1b41b9e403e2", "type": "pipeline"}}
    When the request is sent
    Then the response status is 200 Pipeline updated
