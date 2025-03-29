@endpoint(observability-pipelines) @endpoint(observability-pipelines-v2)
Feature: Observability Pipelines
  Observability Pipelines are awesome!

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ObservabilityPipelines" API

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "Pipeline created" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": "Main Observability Pipeline"}, "id": "pipeline-1", "type": "pipeline"}}
    When the request is sent
    Then the response status is 201 Pipeline created

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "Not Found" response
    Given new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "Pipeline deleted" response
    Given new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 Pipeline deleted

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Get a specific pipeline returns "A specific pipeline" response
    Given new "GetPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 A specific pipeline

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Updated pipeline" response
    Given new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"destinations": [], "processors": [], "sources": []}, "name": "Main Observability Pipeline"}, "id": "pipeline-1", "type": "pipeline"}}
    When the request is sent
    Then the response status is 200 Updated pipeline
