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
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "unknown-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "Conflict" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "pipeline_type": "logs", "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}, {"enabled": true, "field": "message", "id": "json-processor", "include": "*", "type": "parse_json"}]}], "processors": [], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/observability-pipelines
  Scenario: Create a new pipeline returns "OK" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data" has field "id"
    And the response "data.type" is equal to "pipelines"
    And the response "data.attributes.name" is equal to "Main Observability Pipeline"
    And the response "data.attributes.config.sources" has length 1
    And the response "data.attributes.config.processor_groups" has length 1
    And the response "data.attributes.config.destinations" has length 1

  @team:DataDog/observability-pipelines
  Scenario: Create a pipeline with dedupe processor with cache returns "OK" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "dedupe-processor", "include": "service:my-service", "type": "dedupe", "fields": ["message"], "mode": "match", "cache": {"num_events": 5000}}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Pipeline with Dedupe Cache"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.config.processor_groups[0].processors[0].type" is equal to "dedupe"
    And the response "data.attributes.config.processor_groups[0].processors[0].cache.num_events" is equal to 5000

  @team:DataDog/observability-pipelines
  Scenario: Create a pipeline with dedupe processor without cache returns "OK" response
    Given new "CreatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "dedupe-processor", "include": "service:my-service", "type": "dedupe", "fields": ["message"], "mode": "match"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Pipeline with Dedupe No Cache"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 201 OK
    And the response "data.attributes.config.processor_groups[0].processors[0].type" is equal to "dedupe"
    And the response "data.attributes.config.processor_groups[0].processors[0].fields[0]" is equal to "message"

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "Conflict" response
    Given new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "Not Found" response
    Given new "DeletePipeline" request
    And request contains "pipeline_id" parameter with value "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/observability-pipelines
  Scenario: Delete a pipeline returns "OK" response
    Given there is a valid "pipeline" in the system
    And new "DeletePipeline" request
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/observability-pipelines
  Scenario: Get a specific pipeline returns "OK" response
    Given there is a valid "pipeline" in the system
    And new "GetPipeline" request
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has field "id"
    And the response "data.type" is equal to "pipelines"
    And the response "data.attributes.name" is equal to "Main Observability Pipeline"
    And the response "data.attributes.config.sources" has length 1
    And the response "data.attributes.config.processor_groups" has length 1
    And the response "data.attributes.config.destinations" has length 1

  @team:DataDog/observability-pipelines
  Scenario: List pipelines returns "Bad Request" response
    Given new "ListPipelines" request
    And request contains "page[size]" parameter with value 0
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/observability-pipelines
  Scenario: List pipelines returns "OK" response
    Given there is a valid "pipeline" in the system
    And new "ListPipelines" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0]" has field "id"
    And the response "data[0].type" is equal to "pipelines"
    And the response "data[0].attributes" has field "name"
    And the response "data[0].attributes.config.sources[0]" has field "id"
    And the response "data[0].attributes.config.destinations[0]" has field "id"

  @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Bad Request" response
    Given new "UpdatePipeline" request
    And there is a valid "pipeline" in the system
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "unknown-processor", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Conflict" response
    Given new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "pipeline_type": "logs", "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}, {"enabled": true, "field": "message", "id": "json-processor", "include": "*", "type": "parse_json"}]}], "processors": [], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "Not Found" response
    Given new "UpdatePipeline" request
    And request contains "pipeline_id" parameter with value "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/observability-pipelines
  Scenario: Update a pipeline returns "OK" response
    Given there is a valid "pipeline" in the system
    And new "UpdatePipeline" request
    And request contains "pipeline_id" parameter from "pipeline.data.id"
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "updated-datadog-logs-destination-id", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Updated Pipeline Name"}, "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "type": "pipelines"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has field "id"
    And the response "data.type" is equal to "pipelines"
    And the response "data.attributes.name" is equal to "Updated Pipeline Name"
    And the response "data.attributes.config.sources" has length 1
    And the response "data.attributes.config.processor_groups" has length 1
    And the response "data.attributes.config.destinations" has length 1
    And the response "data.attributes.config.destinations[0].id" is equal to "updated-datadog-logs-destination-id"

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline returns "Bad Request" response
    Given new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors[0].title" is equal to "Field 'include' is required"
    And the response "errors[0].meta.field" is equal to "include"
    And the response "errors[0].meta.id" is equal to "filter-processor"
    And the response "errors[0].meta.message" is equal to "Field 'include' is required"

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline returns "OK" response
    Given new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "filter-processor", "include": "status:error", "type": "filter"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "Main Observability Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "errors" has length 0

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline with OCSF mapper custom mapping returns "OK" response
    Given new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "ocsf-mapper-processor", "include": "service:my-service", "mappings": [{"include": "source:custom", "mapping": {"mapping": [{"default": "", "dest": "time", "source": "timestamp"}, {"default": "", "dest": "severity", "source": "level"}, {"default": "", "dest": "device.type", "lookup": {"table": [{"contains": "Desktop", "value": "desktop"}]}, "source": "host.type"}], "metadata": {"class": "Device Inventory Info", "profiles": ["container"], "version": "1.3.0"}, "version": 1}}], "type": "ocsf_mapper"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "OCSF Custom Mapper Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "errors" has length 0

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline with OCSF mapper invalid custom mapping returns "Bad Request" response
    Given new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "ocsf-mapper-processor", "include": "service:my-service", "mappings": [{"include": "source:custom", "mapping": {"mapping": [{"dest": "time", "source": "timestamp"}], "metadata": {"class": "Invalid Class", "profiles": ["container"], "version": "1.3.0"}, "version": 0}}], "type": "ocsf_mapper"}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "OCSF Invalid Mapper Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/observability-pipelines
  Scenario: Validate an observability pipeline with OCSF mapper library mapping returns "OK" response
    Given new "ValidatePipeline" request
    And body with value {"data": {"attributes": {"config": {"destinations": [{"id": "datadog-logs-destination", "inputs": ["my-processor-group"], "type": "datadog_logs"}], "processor_groups": [{"enabled": true, "id": "my-processor-group", "include": "service:my-service", "inputs": ["datadog-agent-source"], "processors": [{"enabled": true, "id": "ocsf-mapper-processor", "include": "service:my-service", "type": "ocsf_mapper", "mappings": [{"include": "source:cloudtrail", "mapping": "CloudTrail Account Change"}]}]}], "sources": [{"id": "datadog-agent-source", "type": "datadog_agent"}]}, "name": "OCSF Mapper Pipeline"}, "type": "pipelines"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "errors" has length 0
