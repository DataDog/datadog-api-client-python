@endpoint(agentless-scanning) @endpoint(agentless-scanning-v2)
Feature: Agentless Scanning
  Datadog Agentless Scanning provides visibility into risks and
  vulnerabilities within your hosts, running containers, and serverless
  functions—all without requiring teams to install Agents on every host or
  where Agents cannot be installed. Agentless offers also Sensitive Data
  Scanning capabilities on your storage. Go to
  https://www.datadoghq.com/blog/agentless-scanning/ to learn more.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AgentlessScanning" API

  @team:DataDog/k9-agentless
  Scenario: Delete AWS Scan Options returns "Bad Request" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter with value "incorrectId"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-agentless
  Scenario: Delete AWS Scan Options returns "No Content" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-agentless
  Scenario: Delete AWS Scan Options returns "Not Found" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000005"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Get AWS On Demand task by id returns "Bad Request" response
    Given new "GetAwsOnDemandTask" request
    And request contains "task_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Get AWS On Demand task by id returns "Not Found" response
    Given new "GetAwsOnDemandTask" request
    And request contains "task_id" parameter with value "00000000-0000-0000-824a-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Get AWS On Demand task by id returns "OK." response
    Given new "GetAwsOnDemandTask" request
    And request contains "task_id" parameter with value "63d6b4f5-e5d0-4d90-824a-9580f05f026a"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.arn" is equal to "arn:aws:lambda:eu-west-3:376334461865:function:This-Is-An-Api-Spec-Test"

  @team:DataDog/k9-agentless
  Scenario: Get AWS On Demand tasks returns "OK" response
    Given new "ListAwsOnDemandTasks" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "aws_resource"

  @team:DataDog/k9-agentless
  Scenario: Get AWS Scan Options returns "OK" response
    Given new "ListAwsScanOptions" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/k9-agentless
  Scenario: Patch AWS Scan Options returns "Bad Request" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000003"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Patch AWS Scan Options returns "Bad Request" response 2
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000003"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000005","attributes":{"vuln_host_os":true,"vuln_containers_os":true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Patch AWS Scan Options returns "No Content" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000002"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000002","attributes":{"vuln_host_os":true,"vuln_containers_os":true,"lambda":false}}}
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-agentless
  Scenario: Patch AWS Scan Options returns "Not Found" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000005"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000005","attributes":{"vuln_host_os":true,"vuln_containers_os":true}}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/k9-agentless
  Scenario: Post AWS Scan Options returns "Agentless scan options enabled successfully." response
    Given new "CreateAwsScanOptions" request
    And body with value {"data": {"id": "000000000003", "type": "aws_scan_options", "attributes": {"lambda": true, "sensitive_data": false, "vuln_containers_os": true, "vuln_host_os": true}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/k9-agentless
  Scenario: Post AWS Scan Options returns "Bad Request" response
    Given new "CreateAwsScanOptions" request
    And body with value {"data": {"id": "123", "type": "aws_scan_options", "attributes": {"lambda": true, "sensitive_data": false, "vuln_containers_os": true, "vuln_host_os": true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Post AWS Scan Options returns "Conflict" response
    Given new "CreateAwsScanOptions" request
    And body with value {"data":{"type":"aws_scan_options","id":"000000000002","attributes":{"vuln_host_os":true,"vuln_containers_os":true,"sensitive_data":false,"lambda":false}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-agentless
  Scenario: Post an AWS on demand task returns "AWS on demand task created successfully." response
    Given new "CreateAwsOnDemandTask" request
    And body with value {"data": {"attributes": {"arn": "arn:aws:lambda:eu-west-3:376334461865:function:This-Is-An-Api-Spec-Test"}, "type": "aws_resource"}}
    When the request is sent
    Then the response status is 201 AWS on demand task created successfully
    And the response "data.attributes.arn" is equal to "arn:aws:lambda:eu-west-3:376334461865:function:This-Is-An-Api-Spec-Test"
    And the response "data.attributes.status" is equal to "QUEUED"

  @team:DataDog/k9-agentless
  Scenario: Post an AWS on demand task returns "Bad Request" response
    Given new "CreateAwsOnDemandTask" request
    And body with value {"data": {"attributes": {"arn": "invalid-arn"}, "type": "aws_resource"}}
    When the request is sent
    Then the response status is 400 Bad Request
