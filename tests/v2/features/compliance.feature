@endpoint(compliance) @endpoint(compliance-v2)
Feature: Compliance
  Datadog Cloud Security Misconfigurations provides aggregated views of
  compliance rules and findings across your cloud resources, helping you
  assess posture against industry frameworks (such as HIPAA, SOC 2, ISO
  27001) and custom frameworks. Learn more at https://docs.datadoghq.com/sec
  urity/cloud_security_management/misconfigurations/#maintain-compliance-
  with-industry-frameworks-and-benchmarks.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Compliance" API
    And operation "GetRuleBasedView" enabled
    And new "GetRuleBasedView" request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get the rule-based view of compliance findings returns "Bad Request" response
    Given request contains "to" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-misconfigs
  Scenario: Get the rule-based view of compliance findings returns "OK" response
    Given request contains "to" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
