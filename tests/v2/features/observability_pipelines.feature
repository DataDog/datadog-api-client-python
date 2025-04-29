@endpoint(observability-pipelines) @endpoint(observability-pipelines-v2)
Feature: Observability Pipelines
  Observability Pipelines allows you to collect and process logs within your
  own infrastructure, and then route them to downstream integrations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ObservabilityPipelines" API

  @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "Bad Request" response
    Given operation "CreatePipeline" enabled
    And new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "unknown-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "Conflict" response
    Given operation "CreatePipeline" enabled
    And new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "OK" response
    Given operation "CreatePipeline" enabled
    And new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data" has field "id"
    And the response "data.type" is equal to "pipelines"
    And the response "data.attributes.name" is equal to "Main Observability Pipeline"
    And the response "data.attributes.config.sources" has length 1
    And the response "data.attributes.config.processors" has length 1
    And the response "data.attributes.config.destinations" has length 1

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "Conflict" response
    Given operation "DeletePipeline" enabled
    And new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "Not Found" response
    Given operation "DeletePipeline" enabled
    And new "DeletePipeline" request
    And request contains "pipeline_id" parameter with value "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "OK" response
    Given operation "DeletePipeline" enabled
    And there is a valid "pipeline" in the system
    And new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/observability-pipelines
  Scenario: Get a specific pipeline returns "OK" response
    Given operation "GetPipeline" enabled
    And there is a valid "pipeline" in the system
    And new "GetPipeline" request
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has field "id"
    And the response "data.type" is equal to "pipelines"
    And the response "data.attributes.name" is equal to "Main Observability Pipeline"
    And the response "data.attributes.config.sources" has length 1
    And the response "data.attributes.config.processors" has length 1
    And the response "data.attributes.config.destinations" has length 1

  @team:DataDog/observability-pipelines
  Scenario: List pipelines returns "Bad Request" response
    Given operation "ListPipelines" enabled
    And new "ListPipelines" request
    And request contains "page[size]" parameter with value 0
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/observability-pipelines
  Scenario: List pipelines returns "OK" response
    Given operation "ListPipelines" enabled
    And there is a valid "pipeline" in the system
    And new "ListPipelines" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0]" has field "id"
    And the response "data[0].type" is equal to "pipelines"
    And the response "data[0].attributes.name" is equal to "Main Observability Pipeline"
    And the response "data[0].attributes.config.sources" has length 1
    And the response "data[0].attributes.config.processors" has length 1
    And the response "data[0].attributes.config.destinations" has length 1

  @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Bad Request" response
    Given operation "UpdatePipeline" enabled
    And new "UpdatePipeline" request
    And there is a valid "pipeline" in the system
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "unknown-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Conflict" response
    Given operation "UpdatePipeline" enabled
    And new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Not Found" response
    Given operation "UpdatePipeline" enabled
    And new "UpdatePipeline" request
    And request contains "pipeline_id" parameter with value "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "OK" response
    Given operation "UpdatePipeline" enabled
    And there is a valid "pipeline" in the system
    And new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "updated-datadog-logs-destination-id", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Updated Pipeline Name"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has field "id"
    And the response "data.type" is equal to "pipelines"
    And the response "data.attributes.name" is equal to "Updated Pipeline Name"
    And the response "data.attributes.config.sources" has length 1
    And the response "data.attributes.config.processors" has length 1
    And the response "data.attributes.config.destinations" has length 1
    And the response "data.attributes.config.destinations[0].id" is equal to "updated-datadog-logs-destination-id"

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline returns "Bad Request" response
    Given operation "ValidatePipeline" enabled
    And new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors[0].title" is equal to "Field 'include' is required"
    And the response "errors[0].meta.field" is equal to "include"
    And the response "errors[0].meta.id" is equal to "filter-processor"
    And the response "errors[0].meta.message" is equal to "Field 'include' is required"

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline returns "OK" response
    Given operation "ValidatePipeline" enabled
    And new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["filter-processor"], "type": "datadog_logs"}], "processors": [{"id": "filter-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "type": "filter"}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "errors" has length 0
