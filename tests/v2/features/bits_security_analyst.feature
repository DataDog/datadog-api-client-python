@endpoint(bits-security-analyst) @endpoint(bits-security-analyst-v2)
Feature: Bits Security Analyst
  Use the Bits Security Analyst endpoints to find the investigations of your
  Cloud SIEM signals, read an investigation's verdict and findings, and
  count investigations.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "BitsSecurityAnalyst" API

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Add an allowed outreach domain returns "Bad Request" response
    Given operation "AddSecurityAgentOutreachPolicyDomain" enabled
    And new "AddSecurityAgentOutreachPolicyDomain" request
    And body with value {"data": {"attributes": {"domain": "not a domain"}, "type": "outreach_policy_domain_add"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Add an allowed outreach domain returns "Conflict" response
    Given operation "AddSecurityAgentOutreachPolicyDomain" enabled
    And new "AddSecurityAgentOutreachPolicyDomain" request
    And body with value {"data": {"attributes": {"domain": "acme.com"}, "type": "outreach_policy_domain_add"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Add an allowed outreach domain returns "Not Found" response
    Given operation "AddSecurityAgentOutreachPolicyDomain" enabled
    And new "AddSecurityAgentOutreachPolicyDomain" request
    And body with value {"data": {"attributes": {"domain": "acme.com"}, "type": "outreach_policy_domain_add"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Add an allowed outreach domain returns "OK" response
    Given operation "AddSecurityAgentOutreachPolicyDomain" enabled
    And new "AddSecurityAgentOutreachPolicyDomain" request
    And body with value {"data": {"attributes": {"domain": "acme.com"}, "type": "outreach_policy_domain_add"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "outreach_policy"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Count Bits Security Analyst investigations returns "Bad Request" response
    Given operation "CountSecurityAgentInvestigations" enabled
    And new "CountSecurityAgentInvestigations" request
    And request contains "field" parameter with value "verdict"
    And request contains "filter[from]" parameter with value "not-a-time"
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors" has length 1
    And the response "errors[0].source.parameter" is equal to "filter[from]"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Count Bits Security Analyst investigations returns "OK" response
    Given operation "CountSecurityAgentInvestigations" enabled
    And new "CountSecurityAgentInvestigations" request
    And request contains "field" parameter with value "verdict"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "verdict"
    And the response "data.type" is equal to "investigation_counts"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Get a Bits Security Analyst investigation returns "Bad Request" response
    Given operation "GetSecurityAgentInvestigation" enabled
    And new "GetSecurityAgentInvestigation" request
    And request contains "investigation_id" parameter with value "not-a-uuid"
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors[0].source.parameter" is equal to "investigation_id"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Get a Bits Security Analyst investigation returns "Not Found" response
    Given operation "GetSecurityAgentInvestigation" enabled
    And new "GetSecurityAgentInvestigation" request
    And request contains "investigation_id" parameter with value "00000000-0000-4000-8000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Get a Bits Security Analyst investigation returns "OK" response
    Given operation "GetSecurityAgentInvestigation" enabled
    And new "GetSecurityAgentInvestigation" request
    And request contains "investigation_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Get the user outreach policy returns "Not Found" response
    Given operation "GetSecurityAgentOutreachPolicy" enabled
    And new "GetSecurityAgentOutreachPolicy" request
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Get the user outreach policy returns "OK" response
    Given operation "GetSecurityAgentOutreachPolicy" enabled
    And new "GetSecurityAgentOutreachPolicy" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "outreach_policy"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: List Bits Security Analyst investigations returns "Bad Request" response
    Given operation "ListSecurityAgentInvestigations" enabled
    And new "ListSecurityAgentInvestigations" request
    And request contains "filter[signal_id]" parameter with value "first-signal,second-signal"
    When the request is sent
    Then the response status is 400 Bad Request
    And the response "errors[0].source.parameter" is equal to "filter[signal_id]"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: List Bits Security Analyst investigations returns "OK" response
    Given operation "ListSecurityAgentInvestigations" enabled
    And new "ListSecurityAgentInvestigations" request
    And request contains "page[size]" parameter with value 1
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Remove an allowed outreach domain returns "Bad Request" response
    Given operation "RemoveSecurityAgentOutreachPolicyDomain" enabled
    And new "RemoveSecurityAgentOutreachPolicyDomain" request
    And request contains "domain" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Remove an allowed outreach domain returns "Conflict" response
    Given operation "RemoveSecurityAgentOutreachPolicyDomain" enabled
    And new "RemoveSecurityAgentOutreachPolicyDomain" request
    And request contains "domain" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Remove an allowed outreach domain returns "Not Found" response
    Given operation "RemoveSecurityAgentOutreachPolicyDomain" enabled
    And new "RemoveSecurityAgentOutreachPolicyDomain" request
    And request contains "domain" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Remove an allowed outreach domain returns "OK" response
    Given operation "RemoveSecurityAgentOutreachPolicyDomain" enabled
    And new "RemoveSecurityAgentOutreachPolicyDomain" request
    And request contains "domain" parameter with value "acme.com"
    When the request is sent
    Then the response status is 200 OK

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Update outreach policy rules returns "Bad Request" response
    Given operation "UpdateSecurityAgentOutreachPolicyRules" enabled
    And new "UpdateSecurityAgentOutreachPolicyRules" request
    And body with value {"data": {"attributes": {"rules": []}, "type": "outreach_policy_rules_update"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Update outreach policy rules returns "Conflict" response
    Given operation "UpdateSecurityAgentOutreachPolicyRules" enabled
    And new "UpdateSecurityAgentOutreachPolicyRules" request
    And body with value {"data": {"attributes": {"rules": [{"is_enabled": true, "rule_id": "abc-def-ghi"}]}, "type": "outreach_policy_rules_update"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Update outreach policy rules returns "Not Found" response
    Given operation "UpdateSecurityAgentOutreachPolicyRules" enabled
    And new "UpdateSecurityAgentOutreachPolicyRules" request
    And body with value {"data": {"attributes": {"rules": [{"is_enabled": true, "rule_id": "abc-def-ghi"}]}, "type": "outreach_policy_rules_update"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Update outreach policy rules returns "OK" response
    Given operation "UpdateSecurityAgentOutreachPolicyRules" enabled
    And new "UpdateSecurityAgentOutreachPolicyRules" request
    And body with value {"data": {"attributes": {"rules": [{"is_enabled": true, "rule_id": "abc-def-ghi"}]}, "type": "outreach_policy_rules_update"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "outreach_policy"

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Update the outreach mode returns "Bad Request" response
    Given operation "UpdateSecurityAgentOutreachMode" enabled
    And new "UpdateSecurityAgentOutreachMode" request
    And body with value {"data": {"attributes": {"mode": "always"}, "type": "outreach_policy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:ddoghq/k9-bits-ai
  Scenario: Update the outreach mode returns "Not Found" response
    Given operation "UpdateSecurityAgentOutreachMode" enabled
    And new "UpdateSecurityAgentOutreachMode" request
    And body with value {"data": {"attributes": {"mode": "automated"}, "type": "outreach_policy"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:ddoghq/k9-bits-ai
  Scenario: Update the outreach mode returns "OK" response
    Given operation "UpdateSecurityAgentOutreachMode" enabled
    And new "UpdateSecurityAgentOutreachMode" request
    And body with value {"data": {"attributes": {"mode": "automated"}, "type": "outreach_policy"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.mode" is equal to "automated"
