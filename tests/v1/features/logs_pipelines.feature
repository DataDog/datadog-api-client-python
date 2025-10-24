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
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar", "support_rules": "rule_name_1 foo\nrule_name_2 bar"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Create a pipeline returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar", "support_rules": "rule_name_1 foo\nrule_name_2 bar"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
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
  Scenario: Create a pipeline with Decoder Processor returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testDecoderProcessor", "processors": [{"type": "decoder-processor", "is_enabled": true, "name": "test_decoder", "source": "encoded.field", "target": "decoded.field", "binary_to_text_encoding": "base16", "input_representation": "utf_8"}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Schema Processor and preserve_source false returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testSchemaProcessor", "processors": [{"type": "schema-processor", "is_enabled": true, "name": "Apply OCSF schema for 3001", "schema": {"schema_type": "ocsf", "version": "1.5.0", "class_uid": 3001, "class_name": "Account Change", "profiles": ["cloud", "datetime"]}, "mappers": [{"type": "schema-category-mapper", "name": "activity_id and activity_name", "categories": [{"filter": {"query": "@eventName:(*Create*)"}, "name": "Create", "id": 1}, {"filter": {"query": "@eventName:(ChangePassword OR PasswordUpdated)"}, "name": "Password Change", "id": 3}, {"filter": {"query": "@eventName:(*Attach*)"}, "name": "Attach Policy", "id": 7}, {"filter": {"query": "@eventName:(*Detach* OR *Remove*)"}, "name": "Detach Policy", "id": 8}, {"filter": {"query": "@eventName:(*Delete*)"}, "name": "Delete", "id": 6}, {"filter": {"query": "@eventName:*"}, "name": "Other", "id": 99}], "targets": {"name": "ocsf.activity_name", "id": "ocsf.activity_id"}, "fallback": {"values": {"ocsf.activity_id": "99", "ocsf.activity_name": "Other"}, "sources": {"ocsf.activity_name": ["eventName"]}}}, {"type": "schema-category-mapper", "name": "status", "categories": [{"filter": {"query": "-@errorCode:*"}, "id": 1, "name": "Success"}, {"filter": {"query": "@errorCode:*"}, "id": 2, "name": "Failure"}], "targets": {"id": "ocsf.status_id", "name": "ocsf.status"}}, {"type": "schema-category-mapper", "name": "Set default severity", "categories": [{"filter": {"query": "@eventName:*"}, "name": "Informational", "id": 1}], "targets": {"name": "ocsf.severity", "id": "ocsf.severity_id"}}, {"type": "schema-remapper", "name": "Map userIdentity to ocsf.user.uid", "sources": ["userIdentity.principalId", "responseElements.role.roleId", "responseElements.user.userId"], "target": "ocsf.user.uid", "preserve_source": false}, {"type": "schema-remapper", "name": "Map userName to ocsf.user.name", "sources": ["requestParameters.userName", "responseElements.role.roleName", "requestParameters.roleName", "responseElements.user.userName"], "target": "ocsf.user.name", "preserve_source": false}, {"type": "schema-remapper", "name": "Map api to ocsf.api", "sources": ["api"], "target": "ocsf.api", "preserve_source": false}, {"type": "schema-remapper", "name": "Map user to ocsf.user", "sources": ["user"], "target": "ocsf.user", "preserve_source": false}, {"type": "schema-remapper", "name": "Map actor to ocsf.actor", "sources": ["actor"], "target": "ocsf.actor", "preserve_source": false}, {"type": "schema-remapper", "name": "Map cloud to ocsf.cloud", "sources": ["cloud"], "target": "ocsf.cloud", "preserve_source": false}, {"type": "schema-remapper", "name": "Map http_request to ocsf.http_request", "sources": ["http_request"], "target": "ocsf.http_request", "preserve_source": false}, {"type": "schema-remapper", "name": "Map metadata to ocsf.metadata", "sources": ["metadata"], "target": "ocsf.metadata", "preserve_source": false}, {"type": "schema-remapper", "name": "Map time to ocsf.time", "sources": ["time"], "target": "ocsf.time", "preserve_source": false}, {"type": "schema-remapper", "name": "Map src_endpoint to ocsf.src_endpoint", "sources": ["src_endpoint"], "target": "ocsf.src_endpoint", "preserve_source": false}, {"type": "schema-remapper", "name": "Map severity to ocsf.severity", "sources": ["severity"], "target": "ocsf.severity", "preserve_source": false}, {"type": "schema-remapper", "name": "Map severity_id to ocsf.severity_id", "sources": ["severity_id"], "target": "ocsf.severity_id", "preserve_source": false}]}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Schema Processor and preserve_source true returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testSchemaProcessor", "processors": [{"type": "schema-processor", "is_enabled": true, "name": "Apply OCSF schema for 3001", "schema": {"schema_type": "ocsf", "version": "1.5.0", "class_uid": 3001, "class_name": "Account Change", "profiles": ["cloud", "datetime"]}, "mappers": [{"type": "schema-category-mapper", "name": "activity_id and activity_name", "categories": [{"filter": {"query": "@eventName:(*Create*)"}, "name": "Create", "id": 1}, {"filter": {"query": "@eventName:(ChangePassword OR PasswordUpdated)"}, "name": "Password Change", "id": 3}, {"filter": {"query": "@eventName:(*Attach*)"}, "name": "Attach Policy", "id": 7}, {"filter": {"query": "@eventName:(*Detach* OR *Remove*)"}, "name": "Detach Policy", "id": 8}, {"filter": {"query": "@eventName:(*Delete*)"}, "name": "Delete", "id": 6}, {"filter": {"query": "@eventName:*"}, "name": "Other", "id": 99}], "targets": {"name": "ocsf.activity_name", "id": "ocsf.activity_id"}, "fallback": {"values": {"ocsf.activity_id": "99", "ocsf.activity_name": "Other"}, "sources": {"ocsf.activity_name": ["eventName"]}}}, {"type": "schema-category-mapper", "name": "status", "categories": [{"filter": {"query": "-@errorCode:*"}, "id": 1, "name": "Success"}, {"filter": {"query": "@errorCode:*"}, "id": 2, "name": "Failure"}], "targets": {"id": "ocsf.status_id", "name": "ocsf.status"}}, {"type": "schema-category-mapper", "name": "Set default severity", "categories": [{"filter": {"query": "@eventName:*"}, "name": "Informational", "id": 1}], "targets": {"name": "ocsf.severity", "id": "ocsf.severity_id"}}, {"type": "schema-remapper", "name": "Map userIdentity to ocsf.user.uid", "sources": ["userIdentity.principalId", "responseElements.role.roleId", "responseElements.user.userId"], "target": "ocsf.user.uid", "preserve_source": true}, {"type": "schema-remapper", "name": "Map userName to ocsf.user.name", "sources": ["requestParameters.userName", "responseElements.role.roleName", "requestParameters.roleName", "responseElements.user.userName"], "target": "ocsf.user.name", "preserve_source": true}, {"type": "schema-remapper", "name": "Map api to ocsf.api", "sources": ["api"], "target": "ocsf.api", "preserve_source": true}, {"type": "schema-remapper", "name": "Map user to ocsf.user", "sources": ["user"], "target": "ocsf.user", "preserve_source": true}, {"type": "schema-remapper", "name": "Map actor to ocsf.actor", "sources": ["actor"], "target": "ocsf.actor", "preserve_source": true}, {"type": "schema-remapper", "name": "Map cloud to ocsf.cloud", "sources": ["cloud"], "target": "ocsf.cloud", "preserve_source": true}, {"type": "schema-remapper", "name": "Map http_request to ocsf.http_request", "sources": ["http_request"], "target": "ocsf.http_request", "preserve_source": true}, {"type": "schema-remapper", "name": "Map metadata to ocsf.metadata", "sources": ["metadata"], "target": "ocsf.metadata", "preserve_source": true}, {"type": "schema-remapper", "name": "Map time to ocsf.time", "sources": ["time"], "target": "ocsf.time", "preserve_source": true}, {"type": "schema-remapper", "name": "Map src_endpoint to ocsf.src_endpoint", "sources": ["src_endpoint"], "target": "ocsf.src_endpoint", "preserve_source": true}, {"type": "schema-remapper", "name": "Map severity to ocsf.severity", "sources": ["severity"], "target": "ocsf.severity", "preserve_source": true}, {"type": "schema-remapper", "name": "Map severity_id to ocsf.severity_id", "sources": ["severity_id"], "target": "ocsf.severity_id", "preserve_source": true}]}], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with Span Id Remapper returns "OK" response
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testPipeline", "processors": [{"type": "span-id-remapper", "is_enabled" : true, "name" : "test_filter", "sources" : [ "dd.span_id"] }], "tags": []}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/event-platform-experience
  Scenario: Create a pipeline with schema processor
    Given new "CreateLogsPipeline" request
    And body with value {"filter": {"query": "source:python"}, "name": "testSchemaProcessor", "processors": [{"type": "schema-processor", "is_enabled": true, "name": "Apply OCSF schema for 3001", "schema": {"schema_type": "ocsf", "version": "1.5.0", "class_uid": 3001, "class_name": "Account Change", "profiles": ["cloud", "datetime"]}, "mappers": [{"type": "schema-category-mapper", "name": "activity_id and activity_name", "categories": [{"filter": {"query": "@eventName:(*Create*)"}, "name": "Create", "id": 1}, {"filter": {"query": "@eventName:(ChangePassword OR PasswordUpdated)"}, "name": "Password Change", "id": 3}, {"filter": {"query": "@eventName:(*Attach*)"}, "name": "Attach Policy", "id": 7}, {"filter": {"query": "@eventName:(*Detach* OR *Remove*)"}, "name": "Detach Policy", "id": 8}, {"filter": {"query": "@eventName:(*Delete*)"}, "name": "Delete", "id": 6}, {"filter": {"query": "@eventName:*"}, "name": "Other", "id": 99}], "targets": {"name": "ocsf.activity_name", "id": "ocsf.activity_id"}, "fallback": {"values": {"ocsf.activity_id": "99", "ocsf.activity_name": "Other"}, "sources": {"ocsf.activity_name": ["eventName"]}}}, {"type": "schema-category-mapper", "name": "status", "categories": [{"filter": {"query": "-@errorCode:*"}, "id": 1, "name": "Success"}, {"filter": {"query": "@errorCode:*"}, "id": 2, "name": "Failure"}], "targets": {"id": "ocsf.status_id", "name": "ocsf.status"}}, {"type": "schema-category-mapper", "name": "Set default severity", "categories": [{"filter": {"query": "@eventName:*"}, "name": "Informational", "id": 1}], "targets": {"name": "ocsf.severity", "id": "ocsf.severity_id"}}, {"type": "schema-remapper", "name": "Map userIdentity to ocsf.user.uid", "sources": ["userIdentity.principalId", "responseElements.role.roleId", "responseElements.user.userId"], "target": "ocsf.user.uid"}, {"type": "schema-remapper", "name": "Map userName to ocsf.user.name", "sources": ["requestParameters.userName", "responseElements.role.roleName", "requestParameters.roleName", "responseElements.user.userName"], "target": "ocsf.user.name"}, {"type": "schema-remapper", "name": "Map api to ocsf.api", "sources": ["api"], "target": "ocsf.api"}, {"type": "schema-remapper", "name": "Map user to ocsf.user", "sources": ["user"], "target": "ocsf.user"}, {"type": "schema-remapper", "name": "Map actor to ocsf.actor", "sources": ["actor"], "target": "ocsf.actor"}, {"type": "schema-remapper", "name": "Map cloud to ocsf.cloud", "sources": ["cloud"], "target": "ocsf.cloud"}, {"type": "schema-remapper", "name": "Map http_request to ocsf.http_request", "sources": ["http_request"], "target": "ocsf.http_request"}, {"type": "schema-remapper", "name": "Map metadata to ocsf.metadata", "sources": ["metadata"], "target": "ocsf.metadata"}, {"type": "schema-remapper", "name": "Map time to ocsf.time", "sources": ["time"], "target": "ocsf.time"}, {"type": "schema-remapper", "name": "Map src_endpoint to ocsf.src_endpoint", "sources": ["src_endpoint"], "target": "ocsf.src_endpoint"}, {"type": "schema-remapper", "name": "Map severity to ocsf.severity", "sources": ["severity"], "target": "ocsf.severity"}, {"type": "schema-remapper", "name": "Map severity_id to ocsf.severity_id", "sources": ["severity_id"], "target": "ocsf.severity_id"}]}], "tags": []}
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
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar", "support_rules": "rule_name_1 foo\nrule_name_2 bar"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/event-platform-experience
  Scenario: Update a pipeline returns "OK" response
    Given new "UpdateLogsPipeline" request
    And request contains "pipeline_id" parameter from "REPLACE.ME"
    And body with value {"filter": {"query": "source:python"}, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar", "support_rules": "rule_name_1 foo\nrule_name_2 bar"}, "is_enabled": false, "samples": [], "source": "message", "type": "grok-parser"}], "tags": []}
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
