@endpoint(agentless-scanning) @endpoint(agentless-scanning-v2)
Feature: Agentless Scanning
  Datadog Agentless Scanning provides visibility into risks and
  vulnerabilities within your hosts, running containers, and serverless
  functions—all without requiring teams to install Agents on every host or
  where Agents cannot be installed. Go to
  https://www.datadoghq.com/blog/agentless-scanning/ to learn more.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AgentlessScanning" API

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete AWS Scan Options returns "Bad Request" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter with value "incorrectId"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Delete AWS Scan Options returns "No Content" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-cloud-security-platform
  Scenario: Delete AWS Scan Options returns "Not Found" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000005"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-cloud-security-platform
  Scenario: Get AWS Scan Options returns "OK" response
    Given new "ListAwsScanOptions" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Patch AWS Scan Options returns "Bad Request" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000003"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Patch AWS Scan Options returns "Bad Request" response 2
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000003"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000005","attributes":{"vuln_host_os":true,"vuln_containers_os":true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Patch AWS Scan Options returns "No Content" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000002"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000002","attributes":{"vuln_host_os":true,"vuln_containers_os":true,"lambda":false}}}
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-cloud-security-platform
  Scenario: Patch AWS Scan Options returns "Not Found" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000005"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000005","attributes":{"vuln_host_os":true,"vuln_containers_os":true}}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/k9-cloud-security-platform
  Scenario: Post AWS Scan Options returns "Agentless scan options enabled successfully." response
    Given new "CreateAwsScanOptions" request
    And body with value {"data": {"id": "000000000003", "type": "aws_scan_options", "attributes": {"lambda": true, "sensitive_data": false, "vuln_containers_os": true, "vuln_host_os": true}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/k9-cloud-security-platform
  Scenario: Post AWS Scan Options returns "Bad Request" response
    Given new "CreateAwsScanOptions" request
    And body with value {"data": {"id": "123", "type": "aws_scan_options", "attributes": {"lambda": true, "sensitive_data": false, "vuln_containers_os": true, "vuln_host_os": true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-cloud-security-platform
  Scenario: Post AWS Scan Options returns "Conflict" response
    Given new "CreateAwsScanOptions" request
    And body with value {"data":{"type":"aws_scan_options","id":"000000000002","attributes":{"vuln_host_os":true,"vuln_containers_os":true,"lambda":false}}}
    When the request is sent
    Then the response status is 409 Conflict
