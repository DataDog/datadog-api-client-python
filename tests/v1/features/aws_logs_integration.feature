@endpoint(aws-logs-integration) @endpoint(aws-logs-integration-v1)
Feature: AWS Logs Integration
  Configure your Datadog-AWS-Logs integration directly through Datadog API.
  For more information, see the [AWS integration
  page](https://docs.datadoghq.com/api/?lang=bash#integration-aws-logs).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSLogsIntegration" API

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Add AWS Log Lambda ARN returns "Bad Request" response
    Given new "CreateAWSLambdaARN" request
    And body with value {"account_id": "1234567", "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Add AWS Log Lambda ARN returns "OK" response
    Given new "CreateAWSLambdaARN" request
    And body with value {"account_id": "1234567", "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Check permissions for log services returns "Bad Request" response
    Given new "CheckAWSLogsServicesAsync" request
    And body with value {"account_id": "1234567", "services": ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Check permissions for log services returns "OK" response
    Given new "CheckAWSLogsServicesAsync" request
    And body with value {"account_id": "1234567", "services": ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Check that an AWS Lambda Function exists returns "Bad Request" response
    Given new "CheckAWSLogsLambdaAsync" request
    And body with value {"account_id": "1234567", "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Check that an AWS Lambda Function exists returns "OK" response
    Given new "CheckAWSLogsLambdaAsync" request
    And body with value {"account_id": "1234567", "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Delete an AWS Logs integration returns "Bad Request" response
    Given new "DeleteAWSLambdaARN" request
    And body with value {"account_id": "1234567", "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Delete an AWS Logs integration returns "OK" response
    Given new "DeleteAWSLambdaARN" request
    And body with value {"account_id": "1234567", "lambda_arn": "arn:aws:lambda:us-east-1:1234567:function:LogsCollectionAPITest"}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Enable an AWS Logs integration returns "Bad Request" response
    Given new "EnableAWSLogServices" request
    And body with value {"account_id": "1234567", "services": ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Enable an AWS Logs integration returns "OK" response
    Given new "EnableAWSLogServices" request
    And body with value {"account_id": "1234567", "services": ["s3", "elb", "elbv2", "cloudfront", "redshift", "lambda"]}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: Get list of AWS log ready services returns "OK" response
    Given new "ListAWSLogsServices" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: List all AWS Logs integrations returns "Bad Request" response
    Given new "ListAWSLogsIntegrations" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-integrations
  Scenario: List all AWS Logs integrations returns "OK" response
    Given new "ListAWSLogsIntegrations" request
    When the request is sent
    Then the response status is 200 OK
