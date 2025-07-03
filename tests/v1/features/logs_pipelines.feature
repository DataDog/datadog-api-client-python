@endpoint(logs-pipelines) @endpoint(logs-pipelines-v1)
Feature: Logs Pipelines
  Pipelines and processors operate on incoming logs, parsing and
  transforming them into structured attributes for easier querying.  - See
  the [pipelines configuration
  page](https://app.datadoghq.com/logs/pipelines)   for a list of the
  pipelines and processors currently configured in web UI.  - Additional
  API-related information about processors can be found in the   [processors
  documentation](https://docs.datadoghq.com/logs/log_configuration/processor
  s/?tab=api#lookup-processor).  - For more information about Pipelines, see
  the   [pipeline documentation](https://docs.datadoghq.com/logs/log_configu
  ration/pipelines).  **Notes:**  **Grok parsing rules may effect JSON
  output and require returned data to be configured before using in a
  request.** For example, if you are using the data returned from a request
  for another request body, and have a parsing rule that uses a regex
  pattern like `\s` for spaces, you will need to configure all escaped
  spaces as `%{space}` to use in the body data.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsPipelines" API

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Create a pipeline returns "Bad Request" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Create a pipeline returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Array Processor Append Operation returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipelineArrayAppend", "processors": [{"type": "array-processor", "is_enabled": true, "name": "append_ip_to_array", "operation": {"type": "append", "source": "network.client.ip", "target": "sourceIps"}}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Array Processor Append Operation with preserve_source false returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipelineArrayAppendNoPreserve", "processors": [{"type": "array-processor", "is_enabled": true, "name": "append_ip_and_remove_source", "operation": {"type": "append", "source": "network.client.ip", "target": "sourceIps", "preserve_source": false}}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Array Processor Append Operation with preserve_source true returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipelineArrayAppendPreserve", "processors": [{"type": "array-processor", "is_enabled": true, "name": "append_ip_and_keep_source", "operation": {"type": "append", "source": "network.client.ip", "target": "sourceIps", "preserve_source": true}}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Array Processor Length Operation returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipelineArrayLength", "processors": [{"type": "array-processor", "is_enabled": true, "name": "count_tags", "operation": {"type": "length", "source": "tags", "target": "tagCount"}}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Array Processor Select Operation returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipelineArraySelect", "processors": [{"type": "array-processor", "is_enabled": true, "name": "extract_referrer", "operation": {"type": "select", "source": "httpRequest.headers", "target": "referrer", "filter": "name:Referrer", "value_to_extract": "value"}}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Span Id Remapper returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipeline", "processors": [{"type": "span-id-remapper", "is_enabled" : true, "name" : "test_filter", "sources" : [ "dd.span_id"] }], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Delete a pipeline returns "Bad Request" response
    Given new "DeleteLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Delete a pipeline returns "OK" response
    Given new "DeleteLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Get a pipeline returns "Bad Request" response
    Given new "GetLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Get a pipeline returns "OK" response
    Given new "GetLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Get all pipelines returns "OK" response
    Given new "ListLogsPipelines" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Get pipeline order returns "OK" response
    Given new "GetLogsPipelineOrder" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Update a pipeline returns "Bad Request" response
    Given new "UpdateLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Update a pipeline returns "OK" response
    Given new "UpdateLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Update pipeline order returns "Bad Request" response
    Given new "UpdateLogsPipelineOrder" request
    And body with value {"pipeline_ids": ["tags", "org_ids", "products"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Update pipeline order returns "OK" response
    Given new "UpdateLogsPipelineOrder" request
    And body with value {"pipeline_ids": ["tags", "org_ids", "products"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Update pipeline order returns "Unprocessable Entity" response
    Given new "UpdateLogsPipelineOrder" request
    And body with value {"pipeline_ids": ["tags", "org_ids", "products"]}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
