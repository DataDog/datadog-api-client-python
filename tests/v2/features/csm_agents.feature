@endpoint(csm-agents) @endpoint(csm-agents-v2)
Feature: CSM Agents
  Datadog Cloud Security Management (CSM) delivers real-time threat
  detection and continuous configuration audits across your entire cloud
  infrastructure, all in a unified view for seamless collaboration and
  faster remediation. Go to
  https://docs.datadoghq.com/security/cloud_security_management to learn
  more

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CSMAgents" API

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get all CSM Agents returns "OK" response
    Given new "ListAllCSMAgents" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get all CSM Serverless Agents returns "OK" response
    Given new "ListAllCSMServerlessAgents" request
    When the request is sent
    Then the response status is 200 OK
