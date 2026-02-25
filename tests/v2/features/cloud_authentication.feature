@endpoint(cloud-authentication) @endpoint(cloud-authentication-v2)
Feature: Cloud Authentication
  Configure AWS cloud authentication mappings for persona and intake
  authentication through the Datadog API.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudAuthentication" API

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create an AWS cloud authentication persona mapping returns "Bad Request" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create an AWS cloud authentication persona mapping returns "Conflict" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Create an AWS cloud authentication persona mapping returns "Created" response
    Given operation "CreateAWSCloudAuthPersonaMapping" enabled
    And new "CreateAWSCloudAuthPersonaMapping" request
    And body with value {"data": {"attributes": {"account_identifier": "test@test.com", "arn_pattern": "arn:aws:iam::123456789012:user/testuser"}, "type": "aws_cloud_auth_config"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete an AWS cloud authentication persona mapping returns "No Content" response
    Given operation "DeleteAWSCloudAuthPersonaMapping" enabled
    And new "DeleteAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Delete an AWS cloud authentication persona mapping returns "Not Found" response
    Given operation "DeleteAWSCloudAuthPersonaMapping" enabled
    And new "DeleteAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get an AWS cloud authentication persona mapping returns "Not Found" response
    Given operation "GetAWSCloudAuthPersonaMapping" enabled
    And new "GetAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: Get an AWS cloud authentication persona mapping returns "OK" response
    Given operation "GetAWSCloudAuthPersonaMapping" enabled
    And new "GetAWSCloudAuthPersonaMapping" request
    And request contains "persona_mapping_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List AWS cloud authentication persona mappings returns "Bad Request" response
    Given operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/team-aaaauthn
  Scenario: List AWS cloud authentication persona mappings returns "OK" response
    Given operation "ListAWSCloudAuthPersonaMappings" enabled
    And new "ListAWSCloudAuthPersonaMappings" request
    When the request is sent
    Then the response status is 200 OK
