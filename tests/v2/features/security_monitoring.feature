@v2 @security_monitoring @todo
Feature: Security Monitoring
  Detection Rules for generating signals

  Background:
    Given a valid "apiKeyAuth" key
    And a valid "appKeyAuth" key
    And an instance of "SecurityMonitoring" API

  Scenario: List rules leading to OK
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Create a detection rule leading to OK
    Given new "CreateSecurityMonitoringRule" request
    And body {}
    When the request is sent
    Then the status is 200 OK

  Scenario: Delete an existing rule leading to OK
    Given new "DeleteSecurityMonitoringRule" request
    When the request is sent
    Then the status is 204 OK

  Scenario: Get a rule's details leading to OK
    Given new "GetSecurityMonitoringRule" request
    When the request is sent
    Then the status is 200 OK

  Scenario: Update an existing rule leading to OK
    Given new "UpdateSecurityMonitoringRule" request
    And body {}
    When the request is sent
    Then the status is 200 OK
