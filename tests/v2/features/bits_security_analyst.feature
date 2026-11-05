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
