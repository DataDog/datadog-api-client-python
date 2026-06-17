@endpoint(aws-wif) @endpoint(aws-wif-v2)
Feature: AWS WIF
  Manage AWS Workload Identity Federation (WIF) mappings. Persona mappings
  link IAM role ARN patterns to Datadog users for delegated-token
  authentication. Intake mappings link IAM role ARN patterns to managed-
  rotation API keys for agent telemetry ingestion.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSWIF" API

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Create an AWS WIF intake mapping returns "Bad Request" response
    Given new "CreateAwsWifIntakeMapping" request
    And body with value {"data": {"attributes": {"arn_pattern": "arn:aws:iam::123456789012:role/my-agent-role"}, "type": "aws_wif_intake_mapping"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Create an AWS WIF intake mapping returns "Conflict" response
    Given new "CreateAwsWifIntakeMapping" request
    And body with value {"data": {"attributes": {"arn_pattern": "arn:aws:iam::123456789012:role/my-agent-role"}, "type": "aws_wif_intake_mapping"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Create an AWS WIF intake mapping returns "Created" response
    Given new "CreateAwsWifIntakeMapping" request
    And body with value {"data": {"attributes": {"arn_pattern": "arn:aws:iam::123456789012:role/my-agent-role"}, "type": "aws_wif_intake_mapping"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Create an AWS WIF persona mapping returns "Bad Request" response
    Given new "CreateAwsWifPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "user@example.com", "arn_pattern": "arn:aws:iam::123456789012:role/my-workload-role"}, "type": "aws_wif_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Create an AWS WIF persona mapping returns "Conflict" response
    Given new "CreateAwsWifPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "user@example.com", "arn_pattern": "arn:aws:iam::123456789012:role/my-workload-role"}, "type": "aws_wif_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Create an AWS WIF persona mapping returns "Created" response
    Given new "CreateAwsWifPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "user@example.com", "arn_pattern": "arn:aws:iam::123456789012:role/my-workload-role"}, "type": "aws_wif_config"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an AWS WIF intake mapping returns "Bad Request" response
    Given new "DeleteAwsWifIntakeMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an AWS WIF intake mapping returns "No Content" response
    Given new "DeleteAwsWifIntakeMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an AWS WIF intake mapping returns "Not Found" response
    Given new "DeleteAwsWifIntakeMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an AWS WIF persona mapping returns "Bad Request" response
    Given new "DeleteAwsWifPersonaMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an AWS WIF persona mapping returns "No Content" response
    Given new "DeleteAwsWifPersonaMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Delete an AWS WIF persona mapping returns "Not Found" response
    Given new "DeleteAwsWifPersonaMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an AWS WIF intake mapping returns "Bad Request" response
    Given new "GetAwsWifIntakeMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an AWS WIF intake mapping returns "Not Found" response
    Given new "GetAwsWifIntakeMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an AWS WIF intake mapping returns "OK" response
    Given new "GetAwsWifIntakeMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an AWS WIF persona mapping returns "Bad Request" response
    Given new "GetAwsWifPersonaMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an AWS WIF persona mapping returns "Not Found" response
    Given new "GetAwsWifPersonaMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: Get an AWS WIF persona mapping returns "OK" response
    Given new "GetAwsWifPersonaMapping" request
    And request contains "config_uuid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List AWS WIF intake mappings returns "OK" response
    Given new "ListAwsWifIntakeMappings" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/delegated-auth-login
  Scenario: List AWS WIF persona mappings returns "OK" response
    Given new "ListAwsWifPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK
