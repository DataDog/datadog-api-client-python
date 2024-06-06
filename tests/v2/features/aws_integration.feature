@endpoint(aws-integration) @endpoint(aws-integration-v2)
Feature: AWS Integration
  Configure your Datadog-AWS integration directly through the Datadog API.
  For more information, see the [AWS integration
  page](https://docs.datadoghq.com/integrations/amazon_web_services).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSIntegration" API

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Create account returns "API error response." response
    Given operation "CreateAWSAccountv2" enabled
    And new "CreateAWSAccountv2" request
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {}, "aws_account_id": "123456789012", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"exclude_only": ["AWS/EC2"], "include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "type": "aws_account"}}
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Create account returns "AWS Account object" response
    Given operation "CreateAWSAccountv2" enabled
    And new "CreateAWSAccountv2" request
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {}, "aws_account_id": "123456789012", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"exclude_only": ["AWS/EC2"], "include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "type": "aws_account"}}
    When the request is sent
    Then the response status is 201 AWS Account object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Delete account returns "API error response." response
    Given operation "DeleteAWSAccountv2" enabled
    And new "DeleteAWSAccountv2" request
    And request contains "aws_account_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Delete account returns "No Content" response
    Given operation "DeleteAWSAccountv2" enabled
    And new "DeleteAWSAccountv2" request
    And request contains "aws_account_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get account returns "API error response." response
    Given operation "GetAWSAccountv2" enabled
    And new "GetAWSAccountv2" request
    And request contains "aws_account_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get account returns "AWS Account object" response
    Given operation "GetAWSAccountv2" enabled
    And new "GetAWSAccountv2" request
    And request contains "aws_account_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 AWS Account object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Get all accounts returns "AWS Account object" response
    Given operation "ListAWSAccountsv2" enabled
    And new "ListAWSAccountsv2" request
    When the request is sent
    Then the response status is 200 AWS Account object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Patch account returns "API error response." response
    Given operation "PatchAWSAccountv2" enabled
    And new "PatchAWSAccountv2" request
    And request contains "aws_account_config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {}, "aws_account_id": "123456789012", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"exclude_only": ["AWS/EC2"], "include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "type": "aws_account"}}
    When the request is sent
    Then the response status is 400 API error response.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: AWS Integration - Patch account returns "No Content" response
    Given operation "PatchAWSAccountv2" enabled
    And new "PatchAWSAccountv2" request
    And request contains "aws_account_config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"account_tags": [], "auth_config": {}, "aws_account_id": "123456789012", "aws_regions": {"include_only": ["us-east-1"]}, "logs_config": {"lambda_forwarder": {"lambdas": [], "sources": ["s3"]}}, "metrics_config": {"namespace_filters": {"exclude_only": ["AWS/EC2"], "include_only": ["AWS/EC2"]}, "tag_filters": [{"namespace": "AWS/EC2", "tags": []}]}, "resources_config": {}, "traces_config": {"xray_services": {"include_only": ["AWS/AppSync"]}}}, "type": "aws_account"}}
    When the request is sent
    Then the response status is 204 No Content
