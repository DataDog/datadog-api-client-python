@endpoint(csm-coverage-analysis) @endpoint(csm-coverage-analysis-v2)
Feature: CSM Coverage Analysis
  Datadog Cloud Security Management (CSM) delivers real-time threat
  detection and continuous configuration audits across your entire cloud
  infrastructure, all in a unified view for seamless collaboration and
  faster remediation. Go to
  https://docs.datadoghq.com/security/cloud_security_management to learn
  more.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CSMCoverageAnalysis" API

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get the CSM Cloud Accounts Coverage Analysis returns "OK" response
    Given new "GetCSMCloudAccountsCoverageAnalysis" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get the CSM Hosts and Containers Coverage Analysis returns "OK" response
    Given new "GetCSMHostsAndContainersCoverageAnalysis" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get the CSM Serverless Coverage Analysis returns "OK" response
    Given new "GetCSMServerlessCoverageAnalysis" request
    When the request is sent
    Then the response status is 200 OK
