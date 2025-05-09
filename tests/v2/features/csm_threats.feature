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
  Scenario: Create a CSM Threats Agent policy returns "Bad Request" response
    Given new "CreateCSMThreatsAgentPolicy" request
    And body with value {"data": {"attributes": {"description": "My agent policy", "enabled": true, "hostTags": [], "hostTagsLists": [], "name": "test"}, "type": "policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent policy returns "Conflict" response
    Given new "CreateCSMThreatsAgentPolicy" request
    And body with value {"data": {"attributes": {"description": "My agent policy", "enabled": true, "hostTags": [], "name": "my_agent_policy"}, "type": "policy"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent policy returns "OK" response
    Given new "CreateCSMThreatsAgentPolicy" request
    And body with value {"data": {"attributes": {"description": "My agent policy", "enabled": true, "hostTagsLists": [["env:test"]], "name": "my_agent_policy"}, "type": "policy"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent rule returns "Bad Request" response
    Given there is a valid "policy_rc" in the system
    And new "CreateCSMThreatsAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name", "filters": [], "name": "my_agent_rule", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent rule returns "Conflict" response
    Given there is a valid "policy_rc" in the system
    And new "CreateCSMThreatsAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "filters": [], "name": "my_agent_rule", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a CSM Threats Agent rule returns "OK" response
    Given there is a valid "policy_rc" in the system
    And new "CreateCSMThreatsAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "filters": [], "name": "{{ unique_lower_alnum }}", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a Cloud Workload Security Agent rule returns "Bad Request" response
    Given there is a valid "policy_rc" in the system
    And new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name", "filters": [], "name": "my_agent_rule"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a Cloud Workload Security Agent rule returns "Conflict" response
    Given there is a valid "policy_rc" in the system
    And new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "filters": [], "name": "my_agent_rule"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Create a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "policy_rc" in the system
    And new "CreateCloudWorkloadSecurityAgentRule" request
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "filters": [], "name": "{{ unique_lower_alnum }}"}, "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a CSM Threats Agent policy returns "Not Found" response
    Given new "DeleteCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter with value "non-existent-policy-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a CSM Threats Agent policy returns "OK" response
    Given there is a valid "policy_rc" in the system
    And new "DeleteCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter from "policy.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a CSM Threats Agent rule returns "Not Found" response
    Given new "DeleteCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter with value "non-existent-rule-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a CSM Threats Agent rule returns "OK" response
    Given there is a valid "policy_rc" in the system
    And there is a valid "agent_rule_rc" in the system
    And new "DeleteCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And request contains "policy_id" parameter from "policy.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Delete a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "DeleteCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "non-existent-rule-id"
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
  Scenario: Get a CSM Threats Agent policy returns "Not Found" response
    Given new "GetCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter with value "non-existent-policy-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a CSM Threats Agent policy returns "OK" response
    Given there is a valid "policy_rc" in the system
    And new "GetCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter from "policy.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a CSM Threats Agent rule returns "Not Found" response
    Given new "GetCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter with value "non-existent-rule-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a CSM Threats Agent rule returns "OK" response
    Given there is a valid "policy_rc" in the system
    And there is a valid "agent_rule_rc" in the system
    And new "GetCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And request contains "policy_id" parameter from "policy.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "GetCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "non-existent-rule-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "GetCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get all CSM Threats Agent policies returns "OK" response
    Given new "ListCSMThreatsAgentPolicies" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get all CSM Threats Agent rules returns "OK" response
    Given new "ListCSMThreatsAgentRules" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Get all Cloud Workload Security Agent rules returns "OK" response
    Given new "ListCloudWorkloadSecurityAgentRules" request
    When the request is sent
    Then the response status is 200 OK

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
  Scenario: Update a CSM Threats Agent policy returns "Bad Request" response
    Given there is a valid "policy_rc" in the system
    And new "UpdateCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter from "policy.data.id"
    And body with value {"data": {"attributes": {"description": "My agent policy", "enabled": true, "hostTags": ["env:test"], "hostTagsLists": [["env:test"]], "name": ""}, "id": "{{ policy.data.id }}", "type": "policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent policy returns "Concurrent Modification" response
    Given there is a valid "policy_rc" in the system
    And new "UpdateCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter from "policy.data.id"
    And body with value {"data": {"attributes": {"description": "My agent policy", "enabled": true, "hostTags": [], "name": "my_agent_policy"}, "id": "{{ policy.data.id }}", "type": "policy"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent policy returns "Not Found" response
    Given new "UpdateCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter with value "non-existent-policy-id"
    And body with value {"data": {"attributes": {"description": "My agent policy", "enabled": true, "hostTags": [], "name": "my_agent_policy"}, "id": "non-existent-policy-id", "type": "policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent policy returns "OK" response
    Given there is a valid "policy_rc" in the system
    And new "UpdateCSMThreatsAgentPolicy" request
    And request contains "policy_id" parameter from "policy.data.id"
    And body with value {"data": {"attributes": {"description": "Updated agent policy", "enabled": true, "hostTagsLists": [["env:test"]], "name": "updated_agent_policy"}, "id": "{{ policy.data.id }}", "type": "policy"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "Bad Request" response
    Given there is a valid "policy_rc" in the system
    And there is a valid "agent_rule_rc" in the system
    And new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "id": "invalid-agent-rule-id", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "Concurrent Modification" response
    Given there is a valid "agent_rule_rc" in the system
    And there is a valid "policy_rc" in the system
    And new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "id": "{{ agent_rule.data.id }}", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "Not Found" response
    Given there is a valid "policy_rc" in the system
    And new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter with value "non-existent-rule-id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "id": "non-existent-rule-id", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a CSM Threats Agent rule returns "OK" response
    Given there is a valid "policy_rc" in the system
    And there is a valid "agent_rule_rc" in the system
    And new "UpdateCSMThreatsAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And request contains "policy_id" parameter from "policy.data.id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\"", "policy_id": "{{ policy.data.id }}", "product_tags": []}, "id": "{{ agent_rule.data.id }}", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "Bad Request" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name"}, "id": "{{ agent_rule.data.id }}", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "Concurrent Modification" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "id": "{{ agent_rule.data.id }}", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "Not Found" response
    Given new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter with value "non-existent-rule-id"
    And body with value {"data": {"attributes": {"description": "My Agent rule", "enabled": true, "expression": "exec.file.name == \"sh\""}, "id": "invalid-agent-rule-id", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform @team:DataDog/k9-cws-backend
  Scenario: Update a Cloud Workload Security Agent rule returns "OK" response
    Given there is a valid "agent_rule" in the system
    And new "UpdateCloudWorkloadSecurityAgentRule" request
    And request contains "agent_rule_id" parameter from "agent_rule.data.id"
    And body with value {"data": {"attributes": {"description": "Updated Agent rule", "expression": "exec.file.name == \"sh\""}, "id": "{{ agent_rule.data.id }}", "type": "agent_rule"}}
    When the request is sent
    Then the response status is 200 OK
