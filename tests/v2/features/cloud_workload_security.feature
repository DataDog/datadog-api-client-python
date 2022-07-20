@endpoint(cloud-workload-security) @endpoint(cloud-workload-security-v2)
Feature: Cloud Workload Security
  Workload activity security rules for generating events using the Datadog
  security Agent.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudWorkloadSecurity" API

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Create a Cloud Workload Security Agent rule returns "Bad Request" response
    Given new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "open.file.path = sh", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Create a Cloud Workload Security Agent rule returns "Conflict" response
    Given new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Create a Cloud Workload Security Agent rule returns "OK" response
    Given new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "Test Agent rule"

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "DeleteCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Delete a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "DeleteCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Get a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "GetCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Get a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "GetCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "My Agent rule"

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Get all Cloud Workload Security Agent rules returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "ListCloudWorkloadSecurityAgentRules" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "agent_rule"

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Get the latest Cloud Workload Security policy returns "OK" response
    Given new "DownloadCloudWorkloadPolicyFile" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Update a Cloud Workload Security Agent rule returns "Bad Request" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "open.file.path = sh"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Update a Cloud Workload Security Agent rule returns "Concurrent Modification" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Update a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cws-backend @team:DataDog/k9-cloud-security-platform
  Scenario: Update a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "Test Agent rule"
