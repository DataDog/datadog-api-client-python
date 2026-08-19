@endpoint(execution-policy) @endpoint(execution-policy-v2)
Feature: Execution Policy
  Execution policies control which actions Datadog Action Platform is
  allowed to run against your infrastructure, and where. Each policy pairs
  an effect (allow or deny) with a pattern of actions, and can scope that
  decision to specific Kubernetes namespaces, scripts, or remote shell
  paths.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ExecutionPolicy" API

  @team:DataDog/action-platform
  Scenario: Create an execution policy returns "Bad Request" response
    Given operation "CreateExecutionPolicy" enabled
    And new "CreateExecutionPolicy" request
    And body with value {"data": {"type": "execution_policy", "attributes": {"name": "Cassette Execution Policy", "effect": "invalid_effect", "action_pattern": {"integration": "INTEGRATION_SCRIPT", "action_fqns": ["com.datadoghq.script.*"]}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/action-platform
  Scenario: Create an execution policy returns "Created" response
    Given operation "CreateExecutionPolicy" enabled
    And new "CreateExecutionPolicy" request
    And body with value {"data": {"type": "execution_policy", "attributes": {"name": "Cassette Execution Policy {{ unique_lower_alnum }}", "effect": "allow", "action_pattern": {"integration": "INTEGRATION_SCRIPT", "action_fqns": ["com.datadoghq.script.*"]}}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/action-platform
  Scenario: Create an execution policy with scope and targets returns "Created" response
    Given operation "CreateExecutionPolicy" enabled
    And new "CreateExecutionPolicy" request
    And body with value {"data": {"type": "execution_policy", "attributes": {"name": "Cassette Execution Policy {{ unique_lower_alnum }}", "effect": "allow", "action_pattern": {"integration": "INTEGRATION_SCRIPT", "action_fqns": ["com.datadoghq.script.*"]}, "scope": {"scripts": {"rules": [{"target_script_names": ["restart_service.sh"]}]}}, "targets": [{"name": "Production hosts", "agent_tags": ["env:prod"]}]}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/action-platform
  Scenario: Delete an execution policy returns "No Content" response
    Given there is a valid "execution_policy" in the system
    And operation "DeleteExecutionPolicy" enabled
    And new "DeleteExecutionPolicy" request
    And request contains "policy_id" parameter from "execution_policy.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/action-platform
  Scenario: Delete an execution policy returns "Not Found" response
    Given operation "DeleteExecutionPolicy" enabled
    And new "DeleteExecutionPolicy" request
    And request contains "policy_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/action-platform
  Scenario: Get an execution policy returns "Not Found" response
    Given operation "GetExecutionPolicy" enabled
    And new "GetExecutionPolicy" request
    And request contains "policy_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/action-platform
  Scenario: Get an execution policy returns "OK" response
    Given there is a valid "execution_policy" in the system
    And operation "GetExecutionPolicy" enabled
    And new "GetExecutionPolicy" request
    And request contains "policy_id" parameter from "execution_policy.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/action-platform
  Scenario: List execution policies returns "Bad Request" response
    Given operation "ListExecutionPolicies" enabled
    And new "ListExecutionPolicies" request
    And request contains "page[size]" parameter with value 0
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/action-platform
  Scenario: List execution policies returns "OK" response
    Given there is a valid "execution_policy" in the system
    And operation "ListExecutionPolicies" enabled
    And new "ListExecutionPolicies" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/action-platform
  Scenario: List execution policies with query parameters returns "OK" response
    Given there is a valid "execution_policy" in the system
    And operation "ListExecutionPolicies" enabled
    And new "ListExecutionPolicies" request
    And request contains "page[size]" parameter with value 10
    And request contains "page[number]" parameter with value 0
    And request contains "filter[name]" parameter from "execution_policy.data.attributes.name"
    And request contains "filter[ids]" parameter with value ["{{ execution_policy.data.id }}"]
    And request contains "filter[integration]" parameter with value ["INTEGRATION_SCRIPT"]
    And request contains "filter[effects]" parameter with value ["allow"]
    And request contains "filter[creator_ids]" parameter with value ["{{ execution_policy.data.attributes.created_by }}"]
    And request contains "sort" parameter with value ["-created_at"]
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/action-platform
  Scenario: Update an execution policy returns "Bad Request" response
    Given there is a valid "execution_policy" in the system
    And operation "UpdateExecutionPolicy" enabled
    And new "UpdateExecutionPolicy" request
    And request contains "policy_id" parameter from "execution_policy.data.id"
    And body with value {"data": {"id": "{{ execution_policy.data.id }}", "type": "execution_policy", "attributes": {"name": "Cassette Execution Policy Updated", "effect": "invalid_effect", "action_pattern": {"integration": "INTEGRATION_SCRIPT", "action_fqns": ["com.datadoghq.script.*"]}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/action-platform
  Scenario: Update an execution policy returns "Not Found" response
    Given operation "UpdateExecutionPolicy" enabled
    And new "UpdateExecutionPolicy" request
    And request contains "policy_id" parameter with value "aaa11111-aa11-aa11-aaaa-aaaaaa111111"
    And body with value {"data": {"id": "aaa11111-aa11-aa11-aaaa-aaaaaa111111", "type": "execution_policy", "attributes": {"name": "Cassette Execution Policy Updated", "effect": "allow", "action_pattern": {"integration": "INTEGRATION_SCRIPT", "action_fqns": ["com.datadoghq.script.*"]}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/action-platform
  Scenario: Update an execution policy returns "OK" response
    Given there is a valid "execution_policy" in the system
    And operation "UpdateExecutionPolicy" enabled
    And new "UpdateExecutionPolicy" request
    And request contains "policy_id" parameter from "execution_policy.data.id"
    And body with value {"data": {"id": "{{ execution_policy.data.id }}", "type": "execution_policy", "attributes": {"name": "Cassette Execution Policy Updated", "effect": "allow", "action_pattern": {"integration": "INTEGRATION_SCRIPT", "action_fqns": ["com.datadoghq.script.*"]}}}}
    When the request is sent
    Then the response status is 200 OK
