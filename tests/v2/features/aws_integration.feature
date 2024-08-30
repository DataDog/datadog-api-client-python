@endpoint(aws-integration) @endpoint(aws-integration-v2)
Feature: AWS Integration
  Configure your Datadog-AWS integration directly through the Datadog API.
  For more information, see the [AWS integration
  page](https://docs.datadoghq.com/integrations/amazon_web_services).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSIntegration" API

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Create account config returns "AWS Account object" response
    Given operation "CreateAWSAccount" enabled
    And new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"role_name": "test"}, "aws_account_id": "123456789012", "aws_partition": "aws", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 200 AWS Account object

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Create account config returns "Bad Request" response
    Given operation "CreateAWSAccount" enabled
    And new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"role_name": "test"}, "aws_account_id": "123456789012", "aws_partition": "aws-test", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Create account config returns "Conflict" response
    Given operation "CreateAWSAccount" enabled
    And new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"access_key_id": "AKIAIOSFODNN7EXAMPLE", "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}, "aws_account_id": "123456789012", "aws_partition": "aws", "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Delete account config returns "Bad Request" response
    Given operation "DeleteAWSAccount" enabled
    And new "DeleteAWSAccount" request
    And request contains "aws_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Delete account config returns "No Content" response
    Given operation "DeleteAWSAccount" enabled
    And there is a valid "aws_account_v2" in the system
    And new "DeleteAWSAccount" request
    And request contains "aws_account_id" parameter from "aws_account_v2.data.attributes.aws_account_id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Delete account config returns "Not Found" response
    Given operation "DeleteAWSAccount" enabled
    And new "DeleteAWSAccount" request
    And request contains "aws_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get account config returns "AWS Account object" response
    Given operation "GetAWSAccount" enabled
    And there is a valid "aws_account_v2" in the system
    And new "GetAWSAccount" request
    And request contains "aws_account_id" parameter from "aws_account_v2.data.attributes.aws_account_id"
    When the request is sent
    Then the response status is 200 AWS Account object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get account config returns "Bad Request" response
    Given operation "GetAWSAccount" enabled
    And new "GetAWSAccount" request
    And request contains "aws_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get account config returns "Not Found" response
    Given operation "GetAWSAccount" enabled
    And new "GetAWSAccount" request
    And request contains "aws_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get all account configs returns "AWS Accounts List object" response
    Given operation "ListAWSAccounts" enabled
    And there is a valid "aws_account_v2" in the system
    And new "ListAWSAccounts" request
    When the request is sent
    Then the response status is 200 AWS Accounts List object

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Patch account config returns "API error response." response
    Given operation "UpdateAWSAccount" enabled
    And there is a valid "aws_account_v2" in the system
    And new "UpdateAWSAccount" request
    And request contains "aws_account_id" parameter from "aws_account_v2.data.attributes.aws_account_id"
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"role_name": "test"}, "aws_account_id": "123456789012", "aws_partition": "aws-test", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 400 API error response.

  @team:DataDog/aws-integrations
  Scenario: AWS Integration - Patch account config returns "AWS Account object" response
    Given operation "UpdateAWSAccount" enabled
    And new "UpdateAWSAccount" request
    And there is a valid "aws_account_v2" in the system
    And request contains "aws_account_id" parameter from "aws_account_v2.data.attributes.aws_account_id"
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"role_name": "test"}, "aws_account_id": "123456789012", "aws_partition": "aws", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 200 AWS Account object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Patch account config returns "Bad Request" response
    Given operation "UpdateAWSAccount" enabled
    And new "UpdateAWSAccount" request
    And request contains "aws_account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"access_key_id": "AKIAIOSFODNN7EXAMPLE", "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}, "aws_account_id": "123456789012", "aws_partition": "aws", "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Patch account config returns "Not Found" response
    Given operation "UpdateAWSAccount" enabled
    And new "UpdateAWSAccount" request
    And request contains "aws_account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {"access_key_id": "AKIAIOSFODNN7EXAMPLE", "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}, "aws_account_id": "123456789012", "aws_partition": "aws", "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {}}, "id": "123456789012", "type": "account"}}
    When the request is sent
    Then the response status is 404 Not Found
