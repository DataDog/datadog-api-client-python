@endpoint(on-prem-management-service) @endpoint(on-prem-management-service-v2)
Feature: On Prem Management Service
  Manage on-premises runners for workflow automation and app builder. Use
  these endpoints to enroll runners, check enrollment status, and register
  tokens for query execution.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OnPremManagementService" API

  @generated @skip @team:DataDog/action-platform
  Scenario: Create an enrollment returns "Bad Request" response
    Given operation "CreateOnPremManagementServiceEnrollment" enabled
    And new "CreateOnPremManagementServiceEnrollment" request
    And body with value {"data": {"attributes": {"actions_allowlist": ["com.datadoghq.jenkins.*"], "runner_host": "runner.example.com", "runner_modes": ["workflow_automation"], "runner_name": "my-runner"}, "type": "enrollment"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/action-platform
  Scenario: Create an enrollment returns "Created" response
    Given operation "CreateOnPremManagementServiceEnrollment" enabled
    And new "CreateOnPremManagementServiceEnrollment" request
    And body with value {"data": {"attributes": {"actions_allowlist": ["com.datadoghq.jenkins.*"], "runner_host": "runner.example.com", "runner_modes": ["workflow_automation"], "runner_name": "my-runner"}, "type": "enrollment"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/action-platform
  Scenario: Get enrollment status returns "Bad Request" response
    Given operation "GetOnPremManagementServiceEnrollment" enabled
    And new "GetOnPremManagementServiceEnrollment" request
    And request contains "token_hash" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/action-platform
  Scenario: Get enrollment status returns "Not Found" response
    Given operation "GetOnPremManagementServiceEnrollment" enabled
    And new "GetOnPremManagementServiceEnrollment" request
    And request contains "token_hash" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/action-platform
  Scenario: Get enrollment status returns "OK" response
    Given operation "GetOnPremManagementServiceEnrollment" enabled
    And new "GetOnPremManagementServiceEnrollment" request
    And request contains "token_hash" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/action-platform
  Scenario: Register a token returns "Bad Request" response
    Given operation "RegisterOnPremManagementServiceToken" enabled
    And new "RegisterOnPremManagementServiceToken" request
    And body with value {"data": {"attributes": {"app_id": "9a93d314-ca37-461d-b18e-0587f03c6e2a", "app_version": 5, "connection_id": "2f66ec56-d1f3-4a18-908d-5e8c12dfb3b0", "query_id": "8744d459-18aa-405b-821e-df9bb101c01e", "runner_id": "runner-GBUyh2Tm6oKS6ap4kt8Bbx"}, "type": "registerTokenRequest"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/action-platform
  Scenario: Register a token returns "Not Found" response
    Given operation "RegisterOnPremManagementServiceToken" enabled
    And new "RegisterOnPremManagementServiceToken" request
    And body with value {"data": {"attributes": {"app_id": "9a93d314-ca37-461d-b18e-0587f03c6e2a", "app_version": 5, "connection_id": "2f66ec56-d1f3-4a18-908d-5e8c12dfb3b0", "query_id": "8744d459-18aa-405b-821e-df9bb101c01e", "runner_id": "runner-GBUyh2Tm6oKS6ap4kt8Bbx"}, "type": "registerTokenRequest"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/action-platform
  Scenario: Register a token returns "OK" response
    Given operation "RegisterOnPremManagementServiceToken" enabled
    And new "RegisterOnPremManagementServiceToken" request
    And body with value {"data": {"attributes": {"app_id": "9a93d314-ca37-461d-b18e-0587f03c6e2a", "app_version": 5, "connection_id": "2f66ec56-d1f3-4a18-908d-5e8c12dfb3b0", "query_id": "8744d459-18aa-405b-821e-df9bb101c01e", "runner_id": "runner-GBUyh2Tm6oKS6ap4kt8Bbx"}, "type": "registerTokenRequest"}}
    When the request is sent
    Then the response status is 200 OK
