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
  Scenario: Create AWS on demand task returns "AWS on demand task created successfully." response
    Given new "CreateAwsOnDemandTask" request
    And body with value {"data": {"attributes": {"arn": "arn:aws:lambda:us-west-2:123456789012:function:my-function"}, "type": "aws_resource"}}
    When the request is sent
    Then the response status is 201 AWS on demand task created successfully
    And the response "data.attributes.arn" is equal to "arn:aws:lambda:us-west-2:123456789012:function:my-function"
    And the response "data.attributes.status" is equal to "QUEUED"

  @team:DataDog/k9-agentless
  Scenario: Create AWS on demand task returns "Bad Request" response
    Given new "CreateAwsOnDemandTask" request
    And body with value {"data": {"attributes": {"arn": "invalid-arn"}, "type": "aws_resource"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/k9-agentless
  Scenario: Create AWS scan options returns "Agentless scan options enabled successfully." response
    Given new "CreateAwsScanOptions" request
    And body with value {"data": {"id": "000000000003", "type": "aws_scan_options", "attributes": {"lambda": true, "sensitive_data": false, "vuln_containers_os": true, "vuln_host_os": true}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/k9-agentless
  Scenario: Create AWS scan options returns "Bad Request" response
    Given new "CreateAwsScanOptions" request
    And body with value {"data": {"id": "123", "type": "aws_scan_options", "attributes": {"lambda": true, "sensitive_data": false, "vuln_containers_os": true, "vuln_host_os": true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Create AWS scan options returns "Conflict" response
    Given new "CreateAwsScanOptions" request
    And body with value {"data":{"type":"aws_scan_options","id":"000000000002","attributes":{"vuln_host_os":true,"vuln_containers_os":true,"sensitive_data":false,"lambda":false}}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip-validation @team:DataDog/k9-agentless
  Scenario: Create Azure scan options returns "Created" response
    Given new "CreateAzureScanOptions" request
    And body with value {"data": {"attributes": {"vuln_containers_os": true, "vuln_host_os": true}, "id": "12345678-90ab-cdef-1234-567890abcdef", "type": "azure_scan_options"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/k9-agentless
  Scenario: Create GCP scan options returns "Agentless scan options enabled successfully." response
    Given new "CreateGcpScanOptions" request
    And body with value {"data": {"id": "new-project", "type": "gcp_scan_options", "attributes": {"vuln_host_os": true, "vuln_containers_os": true}}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/k9-agentless
  Scenario: Create GCP scan options returns "Bad Request" response
    Given new "CreateGcpScanOptions" request
    And body with value {"data": {"id": "no", "type": "gcp_scan_options", "attributes": {"vuln_host_os": true, "vuln_containers_os": true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Create GCP scan options returns "Conflict" response
    Given new "CreateGcpScanOptions" request
    And body with value {"data": {"id": "api-spec-test", "type": "gcp_scan_options", "attributes": {"vuln_host_os": true, "vuln_containers_os": true}}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/k9-agentless
  Scenario: Delete AWS scan options returns "Bad Request" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter with value "incorrectId"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-agentless
  Scenario: Delete AWS scan options returns "No Content" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-agentless
  Scenario: Delete AWS scan options returns "Not Found" response
    Given new "DeleteAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000005"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-agentless
  Scenario: Delete Azure scan options returns "No Content" response
    Given new "DeleteAzureScanOptions" request
    And request contains "subscription_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-agentless
  Scenario: Delete GCP scan options returns "Bad Request" response
    Given new "DeleteGcpScanOptions" request
    And request contains "project_id" parameter with value "no"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-agentless
  Scenario: Delete GCP scan options returns "No Content" response
    Given new "DeleteGcpScanOptions" request
    And request contains "project_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-agentless
  Scenario: Delete GCP scan options returns "Not Found" response
    Given new "DeleteGcpScanOptions" request
    And request contains "project_id" parameter with value "nonexistent-project-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Get AWS on demand task returns "Bad Request" response
    Given new "GetAwsOnDemandTask" request
    And request contains "task_id" parameter with value "invalid-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Get AWS on demand task returns "Not Found" response
    Given new "GetAwsOnDemandTask" request
    And request contains "task_id" parameter with value "00000000-0000-0000-824a-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Get AWS on demand task returns "OK." response
    Given new "GetAwsOnDemandTask" request
    And request contains "task_id" parameter with value "63d6b4f5-e5d0-4d90-824a-9580f05f026a"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.arn" is equal to "arn:aws:lambda:eu-west-3:376334461865:function:This-Is-An-Api-Spec-Test"

  @team:DataDog/k9-agentless
  Scenario: Get AWS scan options returns "Bad Request" response
    Given new "GetAwsScanOptions" request
    And request contains "account_id" parameter with value "not-an-account-id"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Get AWS scan options returns "Not Found" response
    Given new "GetAwsScanOptions" request
    And request contains "account_id" parameter with value "404404404404"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Get AWS scan options returns "OK" response
    Given there is a valid "aws_scan_options" in the system
    And new "GetAwsScanOptions" request
    And request contains "account_id" parameter with value "{{ aws_scan_options.id }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{ aws_scan_options.id }}"
    And the response "data.type" is equal to "{{ aws_scan_options.type }}"

  @skip @team:DataDog/k9-agentless
  Scenario: Get Azure scan options returns "Bad Request" response
    Given new "GetAzureScanOptions" request
    And request contains "subscription_id" parameter with value "invalid uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Get Azure scan options returns "Not Found" response
    Given new "GetAzureScanOptions" request
    And request contains "subscription_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-agentless
  Scenario: Get Azure scan options returns "OK" response
    Given new "GetAzureScanOptions" request
    And request contains "subscription_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-agentless
  Scenario: Get GCP scan options returns "Bad Request" response
    Given new "GetGcpScanOptions" request
    And request contains "project_id" parameter with value "no"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Get GCP scan options returns "Not Found" response
    Given new "GetGcpScanOptions" request
    And request contains "project_id" parameter with value "nonexistent-project-id"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Get GCP scan options returns "OK" response
    Given there is a valid "gcp_scan_options" in the system
    And new "GetGcpScanOptions" request
    And request contains "project_id" parameter with value "api-spec-test"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "api-spec-test"
    And the response "data.type" is equal to "{{ gcp_scan_options.type }}"

  @team:DataDog/k9-agentless
  Scenario: List AWS on demand tasks returns "OK" response
    Given new "ListAwsOnDemandTasks" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "aws_resource"

  @team:DataDog/k9-agentless
  Scenario: List AWS scan options returns "OK" response
    Given new "ListAwsScanOptions" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-agentless
  Scenario: List Azure scan options returns "OK" response
    Given new "ListAzureScanOptions" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-agentless
  Scenario: List GCP scan options returns "OK" response
    Given new "ListGcpScanOptions" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/k9-agentless
  Scenario: Update AWS scan options returns "Bad Request" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000003"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Update AWS scan options returns "Bad Request" response 2
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000003"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000005","attributes":{"vuln_host_os":true,"vuln_containers_os":true}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Update AWS scan options returns "No Content" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000002"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000002","attributes":{"vuln_host_os":true,"vuln_containers_os":true,"lambda":false}}}
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-agentless
  Scenario: Update AWS scan options returns "Not Found" response
    Given new "UpdateAwsScanOptions" request
    And request contains "account_id" parameter with value "000000000005"
    And body with value {"data":{"type":"aws_scan_options","id":"000000000005","attributes":{"vuln_host_os":true,"vuln_containers_os":true}}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-agentless
  Scenario: Update Azure scan options returns "OK" response
    Given new "UpdateAzureScanOptions" request
    And request contains "subscription_id" parameter from "REPLACE.ME"
    And body with value {"data": {"id": "12345678-90ab-cdef-1234-567890abcdef", "type": "azure_scan_options"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-agentless
  Scenario: Update GCP scan options returns "Bad Request" response
    Given new "UpdateGcpScanOptions" request
    And request contains "project_id" parameter with value "no"
    And body with value {"data": {"id": "different-project-id", "type": "gcp_scan_options"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-agentless
  Scenario: Update GCP scan options returns "Not Found" response
    Given new "UpdateGcpScanOptions" request
    And request contains "project_id" parameter with value "nonexistent-project-id"
    And body with value {"data": {"id": "nonexistent-project-id", "type": "gcp_scan_options", "attributes": {"vuln_host_os": true, "vuln_containers_os": true}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-agentless
  Scenario: Update GCP scan options returns "OK" response
    Given new "UpdateGcpScanOptions" request
    And request contains "project_id" parameter with value "api-spec-test"
    And body with value {"data": {"id": "api-spec-test", "type": "gcp_scan_options", "attributes": {"vuln_containers_os": false}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "api-spec-test"
    And the response "data.attributes.vuln_host_os" is equal to true
    And the response "data.attributes.vuln_containers_os" is equal to false
