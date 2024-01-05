@endpoint(cloud-cost-management) @endpoint(cloud-cost-management-v2)
Feature: Cloud Cost Management
  The Cloud Cost Management API allows you to setup, edit and delete cloud
  cost management accounts for AWS & Azure.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudCostManagement" API

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Cloud Cost Enabled returns "OK" response
    Given new "GetCloudCostActivity" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Create Cloud Cost Management AWS CUR config returns "Bad Request" response
    Given new "CreateCostAWSCURConfig" request
    And body with value {"data": {"attributes": {"account_id": "123456789123", "bucket_name": "dd-cost-bucket", "bucket_region": "us-east-1", "report_name": "dd-report-name", "report_prefix": "dd-report-prefix"}, "type": "aws_cur_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Create Cloud Cost Management AWS CUR config returns "OK" response
    Given new "CreateCostAWSCURConfig" request
    And body with value {"data": {"attributes": {"account_id": "123456789123", "bucket_name": "dd-cost-bucket", "bucket_region": "us-east-1", "report_name": "dd-report-name", "report_prefix": "dd-report-prefix"}, "type": "aws_cur_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.account_id" is equal to "123456789123"

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Create Cloud Cost Management Azure configs returns "Bad Request" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Create Cloud Cost Management Azure configs returns "OK" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "is_enabled": true, "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.configs[0].account_id" is equal to "1234abcd-1234-abcd-1234-1234abcd1234"

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Delete Cloud Cost Management AWS CUR config returns "Bad Request" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Delete Cloud Cost Management AWS CUR config returns "No Content" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Delete Cloud Cost Management AWS CUR config returns "Not Found" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Delete Cloud Cost Management Azure config returns "Bad Request" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Delete Cloud Cost Management Azure config returns "No Content" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Delete Cloud Cost Management Azure config returns "Not Found" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: List Cloud Cost Management AWS CUR configs returns "OK" response
    Given new "ListCostAWSCURConfigs" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.bucket_name" is equal to "test_bucket_name"

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: List Cloud Cost Management Azure configs returns "OK" response
    Given new "ListCostAzureUCConfigs" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.configs[0].export_name" is equal to "test_export_name"

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: List related AWS accounts returns "Bad Request" response
    Given new "ListAWSRelatedAccounts" request
    And request contains "filter[management_account_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: List related AWS accounts returns "OK" response
    Given new "ListAWSRelatedAccounts" request
    And request contains "filter[management_account_id]" parameter with value "123456789123"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "test_name"

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Update Cloud Cost Management AWS CUR config returns "OK" response
    Given new "UpdateCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "aws_cur_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.account_id" is equal to "000000000000"

  @generated @skip @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Update Cloud Cost Management Azure config returns "Bad Request" response
    Given new "UpdateCostAzureUCConfigs" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "azure_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management @team:Datadog/integrations-tools-and-libraries
  Scenario: Update Cloud Cost Management Azure config returns "OK" response
    Given new "UpdateCostAzureUCConfigs" request
    And request contains "cloud_account_id" parameter with value "100"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "azure_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "azure_uc_configs"
