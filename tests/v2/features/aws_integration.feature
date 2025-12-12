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
  Scenario: Create an AWS account returns "AWS Account object" response
    Given new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"role_name": "DatadogIntegrationRole"}, "aws_account_id": "123456789012", "aws_partition": "aws", "ccm_config": {"data_export_configs": [{"bucket_name": "my-bucket", "bucket_region": "us-east-1", "report_name": "my-report", "report_prefix": "reports", "report_type": "CUR2.0"}]}, "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 200 AWS Account object

  @team:DataDog/aws-integrations
  Scenario: Create an AWS integration returns "AWS Account object" response
    Given new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"access_key_id": "AKIAIOSFODNN7EXAMPLE", "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}, "aws_account_id": "123456789012", "aws_partition": "aws", "ccm_config": {"data_export_configs": [{"bucket_name": "my-bucket", "bucket_region": "us-east-1", "report_name": "my-report", "report_prefix": "reports", "report_type": "CUR2.0"}]}, "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 200 AWS Account object

  @team:DataDog/aws-integrations
  Scenario: Create an AWS integration returns "Bad Request" response
    Given new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"role_name": "DatadogIntegrationRole"}, "aws_account_id": "123456789012", "aws_partition": "aws-invalid", "ccm_config": {"data_export_configs": [{"bucket_name": "my-bucket", "bucket_region": "us-east-1", "report_name": "my-report", "report_prefix": "reports", "report_type": "CUR2.0"}]}, "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: Create an AWS integration returns "Conflict" response
    Given there is a valid "aws_account_v2" in the system
    And new "CreateAWSAccount" request
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"role_name": "DatadogIntegrationRole"}, "aws_account_id": "123456789012", "aws_partition": "aws", "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Create an Amazon EventBridge source returns "Amazon EventBridge source created." response
    Given new "CreateAWSEventBridgeSource" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "create_event_bus": true, "event_generator_name": "app-alerts", "region": "us-east-1"}, "type": "event_bridge"}}
    When the request is sent
    Then the response status is 200 Amazon EventBridge source created.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Create an Amazon EventBridge source returns "Bad Request" response
    Given new "CreateAWSEventBridgeSource" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "create_event_bus": true, "event_generator_name": "app-alerts", "region": "us-east-1"}, "type": "event_bridge"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Create an Amazon EventBridge source returns "Conflict" response
    Given new "CreateAWSEventBridgeSource" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "create_event_bus": true, "event_generator_name": "app-alerts", "region": "us-east-1"}, "type": "event_bridge"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/aws-integrations
  Scenario: Delete an AWS integration returns "Bad Request" response
    Given new "DeleteAWSAccount" request
    And request contains "aws_account_config_id" parameter with value "not-a-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: Delete an AWS integration returns "No Content" response
    Given there is a valid "aws_account_v2" in the system
    And new "DeleteAWSAccount" request
    And request contains "aws_account_config_id" parameter from "aws_account_v2.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/aws-integrations
  Scenario: Delete an AWS integration returns "Not Found" response
    Given there is a valid "aws_account_v2" in the system
    And new "DeleteAWSAccount" request
    And request contains "aws_account_config_id" parameter with value "448169a8-251c-4344-abee-1c4edef39f7a"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response
    Given new "DeleteAWSEventBridgeSource" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "event_generator_name": "app-alerts-zyxw3210", "region": "us-east-1"}, "type": "event_bridge"}}
    When the request is sent
    Then the response status is 200 Amazon EventBridge source deleted.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Delete an Amazon EventBridge source returns "Bad Request" response
    Given new "DeleteAWSEventBridgeSource" request
    And body with value {"data": {"attributes": {"account_id": "123456789012", "event_generator_name": "app-alerts-zyxw3210", "region": "us-east-1"}, "type": "event_bridge"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: Generate a new external ID returns "AWS External ID object" response
    Given new "CreateNewAWSExternalID" request
    When the request is sent
    Then the response status is 200 AWS External ID object

  @team:DataDog/aws-integrations
  Scenario: Generate new external ID returns "AWS External ID object" response
    Given new "CreateNewAWSExternalID" request
    When the request is sent
    Then the response status is 200 AWS External ID object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Get AWS integration IAM permissions returns "AWS IAM Permissions object" response
    Given new "GetAWSIntegrationIAMPermissions" request
    When the request is sent
    Then the response status is 200 AWS IAM Permissions object

  @team:DataDog/aws-integrations
  Scenario: Get AWS integration standard IAM permissions returns "AWS IAM Permissions object" response
    Given new "GetAWSIntegrationIAMPermissionsStandard" request
    When the request is sent
    Then the response status is 200 AWS IAM Permissions object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Get AWS integration standard IAM permissions returns "AWS integration standard IAM permissions." response
    Given new "GetAWSIntegrationIAMPermissionsStandard" request
    When the request is sent
    Then the response status is 200 AWS integration standard IAM permissions.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Get all Amazon EventBridge sources returns "Amazon EventBridge sources list." response
    Given new "ListAWSEventBridgeSources" request
    When the request is sent
    Then the response status is 200 Amazon EventBridge sources list.

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Get all Amazon EventBridge sources returns "Bad Request" response
    Given new "ListAWSEventBridgeSources" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: Get an AWS integration by config ID returns "AWS Account object" response
    Given there is a valid "aws_account_v2" in the system
    And new "GetAWSAccount" request
    And request contains "aws_account_config_id" parameter from "aws_account_v2.data.id"
    When the request is sent
    Then the response status is 200 AWS Account object

  @team:DataDog/aws-integrations
  Scenario: Get an AWS integration by config ID returns "Bad Request" response
    Given new "GetAWSAccount" request
    And request contains "aws_account_config_id" parameter with value "not-a-uuid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: Get an AWS integration by config ID returns "Not Found" response
    Given new "GetAWSAccount" request
    And request contains "aws_account_config_id" parameter with value "448169a8-251c-4344-abee-1c4edef39f7a"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/aws-integrations
  Scenario: Get resource collection IAM permissions returns "AWS IAM Permissions object" response
    Given new "GetAWSIntegrationIAMPermissionsResourceCollection" request
    When the request is sent
    Then the response status is 200 AWS IAM Permissions object

  @generated @skip @team:DataDog/aws-integrations
  Scenario: Get resource collection IAM permissions returns "AWS integration resource collection IAM permissions." response
    Given new "GetAWSIntegrationIAMPermissionsResourceCollection" request
    When the request is sent
    Then the response status is 200 AWS integration resource collection IAM permissions.

  @team:DataDog/aws-integrations
  Scenario: List all AWS integrations returns "AWS Accounts List object" response
    Given new "ListAWSAccounts" request
    When the request is sent
    Then the response status is 200 AWS Accounts List object

  @team:DataDog/aws-integrations
  Scenario: List available namespaces returns "AWS Namespaces List object" response
    Given new "ListAWSNamespaces" request
    When the request is sent
    Then the response status is 200 AWS Namespaces List object

  @team:DataDog/aws-integrations
  Scenario: List namespaces returns "AWS Namespaces List object" response
    Given new "ListAWSNamespaces" request
    When the request is sent
    Then the response status is 200 AWS Namespaces List object

  @team:DataDog/aws-integrations
  Scenario: Update an AWS integration returns "AWS Account object" response
    Given there is a valid "aws_account_v2" in the system
    And new "UpdateAWSAccount" request
    And request contains "aws_account_config_id" parameter from "aws_account_v2.data.id"
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"role_name": "DatadogIntegrationRole"}, "aws_account_id": "123456789012", "aws_partition": "aws", "ccm_config": {"data_export_configs": [{"bucket_name": "updated-bucket", "bucket_region": "us-west-2", "report_name": "updated-report", "report_prefix": "cost-reports", "report_type": "CUR2.0"}]}, "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 200 AWS Account object

  @team:DataDog/aws-integrations
  Scenario: Update an AWS integration returns "Bad Request" response
    Given there is a valid "aws_account_v2" in the system
    And new "UpdateAWSAccount" request
    And request contains "aws_account_config_id" parameter from "aws_account_v2.data.id"
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"access_key_id": "AKIAIOSFODNN7EXAMPLE", "secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"}, "aws_account_id": "123456789012", "aws_partition": "aws", "ccm_config": {"data_export_configs": [{"bucket_name": "invalid-bucket", "bucket_region": "invalid-region", "report_name": "invalid-report", "report_prefix": "invalid", "report_type": "CUR2.0"}]}, "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/aws-integrations
  Scenario: Update an AWS integration returns "Not Found" response
    Given new "UpdateAWSAccount" request
    And request contains "aws_account_config_id" parameter with value "448169a8-251c-4344-abee-1c4edef39f7a"
    And body with value {"data": {"attributes": {"account_tags": ["key:value"], "auth_config": {"role_name": "DatadogIntegrationRole"}, "aws_account_id": "123456789012", "aws_partition": "aws", "ccm_config": {"data_export_configs": [{"bucket_name": "notfound-bucket", "bucket_region": "eu-west-1", "report_name": "notfound-report", "report_prefix": "notfound", "report_type": "CUR2.0"}]}, "logs_config": {"lambda_forwarder": {"lambdas": ["arn:aws:lambda:us-east-1:123456789012:function:DatadogLambdaLogForwarder"], "log_source_config": {"tag_filters": [{"source": "s3", "tags": ["test:test"]}]}, "sources": ["s3"]}}, "metrics_config": {"automute_enabled": true, "collect_cloudwatch_alarms": true, "collect_custom_metrics": true, "enabled": true, "tag_filters": [{"namespace": "AWS/EC2", "tags": ["key:value"]}]}, "resources_config": {"cloud_security_posture_management_collection": false, "extended_collection": false}, "traces_config": {}}, "type": "account"}}
    When the request is sent
    Then the response status is 404 Not Found
