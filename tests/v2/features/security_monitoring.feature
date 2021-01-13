@endpoint(security-monitoring)
Feature: Security Monitoring
  Detection rules for generating signals and listing of generated signals.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SecurityMonitoring" API

  @generated @skip
  Scenario: List rules returns "OK" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Delete an existing rule returns "OK" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip
  Scenario: Get a rule's details returns "OK" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Update an existing rule returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a quick list of security signals returns "OK" response
    Given operation "ListSecurityMonitoringSignals" enabled
    And new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: Get a list of security signals returns "OK" response
    Given operation "SearchSecurityMonitoringSignals" enabled
    And new "SearchSecurityMonitoringSignals" request
    And body {}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip
  Scenario: List rules returns "Bad Request" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Delete an existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get a rule's details returns "Not Found" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Update an existing rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Update an existing rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "<PATH>"
    And body {}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip
  Scenario: Get a quick list of security signals returns "Bad Request" response
    Given operation "ListSecurityMonitoringSignals" enabled
    And new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip
  Scenario: Get a list of security signals returns "Bad Request" response
    Given operation "SearchSecurityMonitoringSignals" enabled
    And new "SearchSecurityMonitoringSignals" request
    And body {}
    When the request is sent
    Then the response status is 400 Bad Request
