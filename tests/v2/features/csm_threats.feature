@endpoint(csm-threats) @endpoint(csm-threats-v2)
Feature: CSM Threats
  Cloud Security Management Threats (CSM Threats) monitors file, network,
  and process activity across your environment to detect real-time threats
  to your infrastructure. See [Cloud Security Management
  Threats](https://docs.datadoghq.com/security/threats/) for more
  information on setting up CSM Threats.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CSMThreats" API

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent rule returns "Bad Request" response
    Given new "CreateCSMThreatsAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == sh", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent rule returns "Conflict" response
    Given new "CreateCSMThreatsAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "name": "my_agent_rule"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent rule returns "OK" response
    Given new "CreateCSMThreatsAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "filters": ["os == \"linux\""], "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a Cloud Workload Security Agent rule returns "Bad Request" response
    Given new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "open.file.path = sh", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a Cloud Workload Security Agent rule returns "Conflict" response
    Given new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a Cloud Workload Security Agent rule returns "OK" response
    Given new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "Test Agent rule"

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a CSM Threats Agent rule returns "Not Found" response
    Given new "DeleteCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a CSM Threats Agent rule returns "OK" response
    Given there is a valid "agent_rule_rc" in the system
    And new "DeleteCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "DeleteCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "DeleteCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a CSM Threats Agent rule returns "Not Found" response
    Given new "GetCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a CSM Threats Agent rule returns "OK" response
    Given there is a valid "agent_rule_rc" in the system
    And new "GetCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "My Agent rule"

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "GetCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "GetCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "My Agent rule"

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get all CSM Threats Agent rules returns "OK" response
    Given new "ListCSMThreatsAgentRules" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get all Cloud Workload Security Agent rules returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "ListCloudWorkloadSecurityAgentRules" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "agent_rule"

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get the latest CSM Threats policy returns "OK" response
    Given new "DownloadCSMThreatsPolicy" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get the latest Cloud Workload Security policy returns "OK" response
    Given new "DownloadCloudWorkloadPolicyFile" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "Bad Request" response
    Given there is a valid "agent_rule_rc" in the system
    And new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "open.file.path = sh"}, "type": "agent_rule", "id":"{{ agent_rule.data.id }}"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "Concurrent Modification" response
    Given new "UpdateCSMThreatsAgentRule" request
    And there is a valid "agent_rule" in the system
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule", "id":"{{ agent_rule.data.id }}"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "Not Found" response
    Given new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule", "id":"abc-123-xyz"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "OK" response
    Given there is a valid "agent_rule_rc" in the system
    And new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule", "id":"{{ agent_rule.data.id }}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "Test Agent rule"

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "Bad Request" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "open.file.path = sh"}, "type": "agent_rule", "id":"{{ agent_rule.data.id }}"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "Concurrent Modification" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule", "id":"{{ agent_rule.data.id }}"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "abc-123-xyz"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule", "id":"abc-123-xyz"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Test Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "type": "agent_rule", "id":"{{ agent_rule.data.id }}"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "agent_rule"
    And the response "data.attributes.description" is equal to "Test Agent rule"
