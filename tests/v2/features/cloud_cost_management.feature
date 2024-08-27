@endpoint(cloud-cost-management) @endpoint(cloud-cost-management-v2)
Feature: Cloud Cost Management
  The Cloud Cost Management API allows you to set up, edit, and delete Cloud
  Cost Management accounts for AWS and Azure. You can query your cost data
  by using the [Metrics
  endpoint](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-
  data-across-multiple-products) and the `cloud_cost` data source. For more
  information, see the [Cloud Cost Management
  documentation](https://docs.datadoghq.com/cloud_cost_management/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudCostManagement" API

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Cloud Cost Enabled returns "OK" response
    Given new "GetCloudCostActivity" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management AWS CUR config returns "Bad Request" response
    Given new "CreateCostAWSCURConfig" request
    And body with value {"data": {"attributes": {"account_id": "123456789123", "bucket_name": "dd-cost-bucket", "bucket_region": "us-east-1", "report_name": "dd-report-name", "report_prefix": "dd-report-prefix"}, "type": "aws_cur_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management AWS CUR config returns "OK" response
    Given new "CreateCostAWSCURConfig" request
    And body with value {"data": {"attributes": {"account_id": "123456789123", "bucket_name": "dd-cost-bucket", "bucket_region": "us-east-1", "report_name": "dd-report-name", "report_prefix": "dd-report-prefix"}, "type": "aws_cur_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.account_id" is equal to "123456789123"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management Azure configs returns "Bad Request" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management Azure configs returns "OK" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "is_enabled": true, "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.configs[0].account_id" is equal to "1234abcd-1234-abcd-1234-1234abcd1234"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management AWS CUR config returns "Bad Request" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management AWS CUR config returns "No Content" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management AWS CUR config returns "Not Found" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management Azure config returns "Bad Request" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management Azure config returns "No Content" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management Azure config returns "Not Found" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete Custom Costs File returns "No Content" response
    Given new "DeleteCustomCostsFile" request
    And request contains "file_id" parameter with value "9d055d22-a838-4e9f-bc34-a4f9ab66280c"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Custom Costs file returns "No Content" response
    Given new "DeleteCustomCostsFile" request
    And request contains "file_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Get Custom Costs File returns "OK" response
    Given new "GetCustomCostsFile" request
    And request contains "file_id" parameter with value "9d055d22-a838-4e9f-bc34-a4f9ab66280c"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.name" is equal to "data.json"
    And the response "data.attributes.content[0].ChargeDescription" is equal to "my_description"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Get Custom Costs file returns "OK" response
    Given new "GetCustomCostsFile" request
    And request contains "file_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: List Cloud Cost Management AWS CUR configs returns "OK" response
    Given new "ListCostAWSCURConfigs" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.bucket_name" is equal to "test_bucket_name"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: List Cloud Cost Management Azure configs returns "OK" response
    Given new "ListCostAzureUCConfigs" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.configs[0].export_name" is equal to "test_export_name"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: List Custom Costs Files returns "OK" response
    Given new "ListCustomCostsFiles" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "data.json"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: List Custom Costs files returns "OK" response
    Given new "ListCustomCostsFiles" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: List related AWS accounts returns "Bad Request" response
    Given new "ListAWSRelatedAccounts" request
    And request contains "filter[management_account_id]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: List related AWS accounts returns "OK" response
    Given new "ListAWSRelatedAccounts" request
    And request contains "filter[management_account_id]" parameter with value "123456789123"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "test_name"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management AWS CUR config returns "OK" response
    Given new "UpdateCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "aws_cur_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.account_id" is equal to "000000000000"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management Azure config returns "Bad Request" response
    Given new "UpdateCostAzureUCConfigs" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "azure_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management Azure config returns "OK" response
    Given new "UpdateCostAzureUCConfigs" request
    And request contains "cloud_account_id" parameter with value "100"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "azure_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "azure_uc_configs"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Upload Custom Costs File returns "Accepted" response
    Given new "UploadCustomCostsFile" request
    And body with value [{ "ProviderName": "my_provider", "ChargePeriodStart": "2023-05-06", "ChargePeriodEnd": "2023-06-06","ChargeDescription": "my_description","BilledCost": 250,"BillingCurrency": "USD","Tags": {"key": "value"}}]
    When the request is sent
    Then the response status is 202 Accepted
    And the response "data.attributes.name" is equal to "data.json"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Upload Custom Costs file returns "Accepted" response
    Given new "UploadCustomCostsFile" request
    And body with value [{"BilledCost": 100.5, "BillingCurrency": "USD", "ChargeDescription": "Monthly usage charge for my service", "ChargePeriodEnd": "2023-02-28", "ChargePeriodStart": "2023-02-01"}]
    When the request is sent
    Then the response status is 202 Accepted
