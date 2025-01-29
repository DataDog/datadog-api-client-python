@endpoint(agentless-scanning) @endpoint(agentless-scanning-v2)
Feature: Agentless Scanning
  Datadog Agentless Scanning provides visibility into risks and
  vulnerabilities within your hosts, running containers, and serverless
  functions—all without requiring teams to install Agents on every host or
  where Agents cannot be installed. Go to
  https://www.datadoghq.com/blog/agentless-scanning/ to learn more

  @team:DataDog/k9-cloud-security-platform @team:DataDog/web-frameworks
  Scenario: Get AWS Scan Options returns "OK" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AgentlessScanning" API
    And new "ListAwsScanOptions" request
    When the request is sent
    Then the response status is 200 OK
