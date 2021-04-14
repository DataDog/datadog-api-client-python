@endpoint(logs-pipelines)
Feature: Logs Pipelines
  Pipelines and processors operate on incoming logs, parsing and
  transforming them into structured attributes for easier querying.  - See
  the [pipelines configuration
  page](https://app.datadoghq.com/logs/pipelines)   for a list of the
  pipelines and processors currently configured in our UI.  - Additional
  API-related information about processors can be found in the   [processors
  documentation](https://docs.datadoghq.com/logs/processing/processors/?tab=
  api#lookup-processor).  - For more information about Pipelines, see the
  [pipeline documentation](https://docs.datadoghq.com/logs/processing).
  **Notes:**  These endpoints are only available for admin users. Make sure
  to use an application key created by an admin.  **Grok parsing rules may
  effect JSON output and require returned data to be configured before using
  in a request.** For example, if you are using the data returned from a
  request for another request body, and have a parsing rule that uses a
  regex pattern like `\s` for spaces, you will need to configure all escaped
  spaces as `%{space}` to use in the body data.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "LogsPipelines" API

  @generated @skip
  Scenario: Create a pipeline returns "Bad Request" response
    Given new "CreateLogsPipeline" request
    And body {"filter": {"query": "source:python"}, "id": null, "is_enabled": null, "is_read_only": null, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "name": null, "samples": [], "source": "message", "type": "grok-parser"}], "type": "pipeline"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a pipeline returns "OK" response
    Given new "CreateLogsPipeline" request
    And body {"filter": {"query": "source:python"}, "id": null, "is_enabled": null, "is_read_only": null, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "name": null, "samples": [], "source": "message", "type": "grok-parser"}], "type": "pipeline"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete a pipeline returns "Bad Request" response
    Given new "DeleteLogsPipeline" request
    And request contains "pipeline_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete a pipeline returns "OK" response
    Given new "DeleteLogsPipeline" request
    And request contains "pipeline_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a pipeline returns "Bad Request" response
    Given new "GetLogsPipeline" request
    And request contains "pipeline_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a pipeline returns "OK" response
    Given new "GetLogsPipeline" request
    And request contains "pipeline_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get all pipelines returns "OK" response
    Given new "ListLogsPipelines" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get pipeline order returns "OK" response
    Given new "GetLogsPipelineOrder" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update a pipeline returns "Bad Request" response
    Given new "UpdateLogsPipeline" request
    And request contains "pipeline_id" parameter from "<PATH>"
    And body {"filter": {"query": "source:python"}, "id": null, "is_enabled": null, "is_read_only": null, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "name": null, "samples": [], "source": "message", "type": "grok-parser"}], "type": "pipeline"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update a pipeline returns "OK" response
    Given new "UpdateLogsPipeline" request
    And request contains "pipeline_id" parameter from "<PATH>"
    And body {"filter": {"query": "source:python"}, "id": null, "is_enabled": null, "is_read_only": null, "name": "", "processors": [{"grok": {"match_rules": "rule_name_1 foo\nrule_name_2 bar\n", "support_rules": "rule_name_1 foo\nrule_name_2 bar\n"}, "is_enabled": false, "name": null, "samples": [], "source": "message", "type": "grok-parser"}], "type": "pipeline"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update pipeline order returns "Bad Request" response
    Given new "UpdateLogsPipelineOrder" request
    And body {"pipeline_ids": ["tags", "org_ids", "products"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update pipeline order returns "OK" response
    Given new "UpdateLogsPipelineOrder" request
    And body {"pipeline_ids": ["tags", "org_ids", "products"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update pipeline order returns "Unprocessable Entity" response
    Given new "UpdateLogsPipelineOrder" request
    And body {"pipeline_ids": ["tags", "org_ids", "products"]}
    When the request is sent
    Then the response status is 422 Unprocessable Entity
