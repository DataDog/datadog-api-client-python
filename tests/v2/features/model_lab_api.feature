@endpoint(model-lab-api) @endpoint(model-lab-api-v2)
Feature: Model Lab API
  Manage Model Lab projects, runs, artifacts, and facets for ML experiment
  tracking.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ModelLabAPI" API

  @generated @skip @team:DataDog/ml-observability
  Scenario: Delete a Model Lab run returns "Bad Request" response
    Given operation "DeleteModelLabRun" enabled
    And new "DeleteModelLabRun" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: Delete a Model Lab run returns "No Content" response
    Given operation "DeleteModelLabRun" enabled
    And new "DeleteModelLabRun" request
    And request contains "run_id" parameter with value 70158
    When the request is sent
    Then the response status is 204 No Content

  @replay-only @team:DataDog/ml-observability
  Scenario: Delete a Model Lab run returns "Not Found" response
    Given operation "DeleteModelLabRun" enabled
    And new "DeleteModelLabRun" request
    And request contains "run_id" parameter with value 999999
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: Download artifact content returns "OK" response
    Given operation "GetModelLabArtifactContent" enabled
    And new "GetModelLabArtifactContent" request
    And request contains "project_id" parameter with value "2387"
    And request contains "artifact_path" parameter with value "f635c73b70594ab6bb6e212cdf87d0d5/artifacts/lora_model/adapter_config.json"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get Model Lab artifact content returns "Bad Request" response
    Given operation "GetModelLabArtifactContent" enabled
    And new "GetModelLabArtifactContent" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "artifact_path" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get Model Lab artifact content returns "OK" response
    Given operation "GetModelLabArtifactContent" enabled
    And new "GetModelLabArtifactContent" request
    And request contains "project_id" parameter from "REPLACE.ME"
    And request contains "artifact_path" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get a Model Lab project returns "Bad Request" response
    Given operation "GetModelLabProject" enabled
    And new "GetModelLabProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: Get a Model Lab project returns "Not Found" response
    Given operation "GetModelLabProject" enabled
    And new "GetModelLabProject" request
    And request contains "project_id" parameter with value 999999
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: Get a Model Lab project returns "OK" response
    Given operation "GetModelLabProject" enabled
    And new "GetModelLabProject" request
    And request contains "project_id" parameter with value 2387
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Get a Model Lab run returns "Bad Request" response
    Given operation "GetModelLabRun" enabled
    And new "GetModelLabRun" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: Get a Model Lab run returns "Not Found" response
    Given operation "GetModelLabRun" enabled
    And new "GetModelLabRun" request
    And request contains "run_id" parameter with value 999999
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: Get a Model Lab run returns "OK" response
    Given operation "GetModelLabRun" enabled
    And new "GetModelLabRun" request
    And request contains "run_id" parameter with value 70158
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab project artifacts returns "Bad Request" response
    Given operation "ListModelLabProjectArtifacts" enabled
    And new "ListModelLabProjectArtifacts" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab project artifacts returns "OK" response
    Given operation "ListModelLabProjectArtifacts" enabled
    And new "ListModelLabProjectArtifacts" request
    And request contains "project_id" parameter with value 2387
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab project facet keys returns "OK" response
    Given operation "ListModelLabProjectFacetKeys" enabled
    And new "ListModelLabProjectFacetKeys" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab project facet values returns "Bad Request" response
    Given operation "ListModelLabProjectFacetValues" enabled
    And new "ListModelLabProjectFacetValues" request
    And request contains "facet_type" parameter from "REPLACE.ME"
    And request contains "facet_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab project facet values returns "OK" response
    Given operation "ListModelLabProjectFacetValues" enabled
    And new "ListModelLabProjectFacetValues" request
    And request contains "facet_type" parameter with value "tag"
    And request contains "facet_name" parameter with value "model"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab projects returns "Bad Request" response
    Given operation "ListModelLabProjects" enabled
    And new "ListModelLabProjects" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab projects returns "OK" response
    Given operation "ListModelLabProjects" enabled
    And new "ListModelLabProjects" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab run artifacts returns "Bad Request" response
    Given operation "ListModelLabRunArtifacts" enabled
    And new "ListModelLabRunArtifacts" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab run artifacts returns "Not Found" response
    Given operation "ListModelLabRunArtifacts" enabled
    And new "ListModelLabRunArtifacts" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab run artifacts returns "OK" response
    Given operation "ListModelLabRunArtifacts" enabled
    And new "ListModelLabRunArtifacts" request
    And request contains "run_id" parameter with value 70158
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab run facet keys returns "Bad Request" response
    Given operation "ListModelLabRunFacetKeys" enabled
    And new "ListModelLabRunFacetKeys" request
    And request contains "filter[project_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab run facet keys returns "Not Found" response
    Given operation "ListModelLabRunFacetKeys" enabled
    And new "ListModelLabRunFacetKeys" request
    And request contains "filter[project_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab run facet keys returns "OK" response
    Given operation "ListModelLabRunFacetKeys" enabled
    And new "ListModelLabRunFacetKeys" request
    And request contains "filter[project_id]" parameter with value 2387
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab run facet values returns "Bad Request" response
    Given operation "ListModelLabRunFacetValues" enabled
    And new "ListModelLabRunFacetValues" request
    And request contains "filter[project_id]" parameter from "REPLACE.ME"
    And request contains "facet_type" parameter from "REPLACE.ME"
    And request contains "facet_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab run facet values returns "Not Found" response
    Given operation "ListModelLabRunFacetValues" enabled
    And new "ListModelLabRunFacetValues" request
    And request contains "filter[project_id]" parameter from "REPLACE.ME"
    And request contains "facet_type" parameter from "REPLACE.ME"
    And request contains "facet_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab run facet values returns "OK" response
    Given operation "ListModelLabRunFacetValues" enabled
    And new "ListModelLabRunFacetValues" request
    And request contains "filter[project_id]" parameter with value 2387
    And request contains "facet_type" parameter with value "tag"
    And request contains "facet_name" parameter with value "model"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: List Model Lab runs returns "Bad Request" response
    Given operation "ListModelLabRuns" enabled
    And new "ListModelLabRuns" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: List Model Lab runs returns "OK" response
    Given operation "ListModelLabRuns" enabled
    And new "ListModelLabRuns" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/ml-observability
  Scenario: Pin a Model Lab run returns "Bad Request" response
    Given operation "PinModelLabRun" enabled
    And new "PinModelLabRun" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: Pin a Model Lab run returns "No Content" response
    Given operation "PinModelLabRun" enabled
    And new "PinModelLabRun" request
    And request contains "run_id" parameter with value 70158
    When the request is sent
    Then the response status is 204 No Content

  @replay-only @team:DataDog/ml-observability
  Scenario: Pin a Model Lab run returns "Not Found" response
    Given operation "PinModelLabRun" enabled
    And new "PinModelLabRun" request
    And request contains "run_id" parameter with value 999999
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Remove star from a Model Lab project returns "Bad Request" response
    Given operation "UnstarModelLabProject" enabled
    And new "UnstarModelLabProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/ml-observability
  Scenario: Remove star from a Model Lab project returns "No Content" response
    Given operation "UnstarModelLabProject" enabled
    And new "UnstarModelLabProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Remove star from a Model Lab project returns "Not Found" response
    Given operation "UnstarModelLabProject" enabled
    And new "UnstarModelLabProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Star a Model Lab project returns "Bad Request" response
    Given operation "StarModelLabProject" enabled
    And new "StarModelLabProject" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: Star a Model Lab project returns "No Content" response
    Given operation "StarModelLabProject" enabled
    And new "StarModelLabProject" request
    And request contains "project_id" parameter with value 2387
    When the request is sent
    Then the response status is 204 No Content

  @replay-only @team:DataDog/ml-observability
  Scenario: Star a Model Lab project returns "Not Found" response
    Given operation "StarModelLabProject" enabled
    And new "StarModelLabProject" request
    And request contains "project_id" parameter with value 999999
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/ml-observability
  Scenario: Unpin a Model Lab run returns "Bad Request" response
    Given operation "UnpinModelLabRun" enabled
    And new "UnpinModelLabRun" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/ml-observability
  Scenario: Unpin a Model Lab run returns "No Content" response
    Given operation "UnpinModelLabRun" enabled
    And new "UnpinModelLabRun" request
    And request contains "run_id" parameter with value 70158
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/ml-observability
  Scenario: Unpin a Model Lab run returns "Not Found" response
    Given operation "UnpinModelLabRun" enabled
    And new "UnpinModelLabRun" request
    And request contains "run_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/ml-observability
  Scenario: Unstar a Model Lab project returns "No Content" response
    Given operation "UnstarModelLabProject" enabled
    And new "UnstarModelLabProject" request
    And request contains "project_id" parameter with value 2387
    When the request is sent
    Then the response status is 204 No Content
