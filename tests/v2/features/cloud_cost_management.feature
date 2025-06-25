@endpoint(cloud-cost-management) @endpoint(cloud-cost-management-v2)
Feature: Cloud Cost Management
  The Cloud Cost Management API allows you to set up, edit, and delete Cloud
  Cost Management accounts for AWS, Azure, and GCP. You can query your cost
  data by using the [Metrics
  endpoint](https://docs.datadoghq.com/api/latest/metrics/#query-timeseries-
  data-across-multiple-products) and the `cloud_cost` data source. For more
  information, see the [Cloud Cost Management
  documentation](https://docs.datadoghq.com/cloud_cost_management/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudCostManagement" API

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management AWS CUR config returns "Bad Request" response
    Given new "CreateCostAWSCURConfig" request
    And body with value {"data": {"attributes": {"account_filters": {"excluded_accounts": ["123456789123", "123456789143"], "include_new_accounts": true, "included_accounts": ["123456789123", "123456789143"]}, "account_id": "123456789123", "bucket_name": "dd-cost-bucket", "bucket_region": "us-east-1", "report_name": "dd-report-name", "report_prefix": "dd-report-prefix"}, "type": "aws_cur_config_post_request"}}
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
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "scope": "/subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management Azure configs returns "OK" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "is_enabled": true, "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.configs[0].account_id" is equal to "1234abcd-1234-abcd-1234-1234abcd1234"

  @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management GCP Usage Cost config returns "Bad Request" response
    Given new "CreateCostGCPUsageCostConfig" request
    And body with value {"data": {"attributes": {"billing_account_id": "123456_A123BC_12AB34", "bucket_name": "dd-cost-bucket", "export_dataset_name": "billing", "export_prefix": "datadog_cloud_cost_usage_export", "export_project_name": "dd-cloud-cost-report", "service_account": "InvalidServiceAccount"}, "type": "gcp_uc_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management GCP Usage Cost config returns "OK" response
    Given new "CreateCostGCPUsageCostConfig" request
    And body with value {"data": {"attributes": {"billing_account_id": "123456_A123BC_12AB34", "bucket_name": "dd-cost-bucket", "export_dataset_name": "billing", "export_prefix": "datadog_cloud_cost_usage_export", "export_project_name": "dd-cloud-cost-report", "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com"}, "type": "gcp_uc_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.account_id" is equal to "123456_A123BC_12AB34"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Create or update a budget returns "Bad Request" response
    Given new "UpsertBudget" request
    And body with value {"data": {"attributes": {"created_at": 1738258683590, "created_by": "00000000-0a0a-0a0a-aaa0-00000000000a", "end_month": 202502, "entries": [{"amount": 500, "month": 202501, "tag_filters": [{"tag_key": "service", "tag_value": "ec2"}]}], "metrics_query": "aws.cost.amortized{service:ec2} by {service}", "name": "my budget", "org_id": 123, "start_month": 202501, "total_amount": 1000, "updated_at": 1738258683590, "updated_by": "00000000-0a0a-0a0a-aaa0-00000000000a"}, "id": "00000000-0a0a-0a0a-aaa0-00000000000a"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Create or update a budget returns "Not Found" response
    Given new "UpsertBudget" request
    And body with value {"data": {"attributes": {"created_at": 1738258683590, "created_by": "00000000-0a0a-0a0a-aaa0-00000000000a", "end_month": 202502, "entries": [{"amount": 500, "month": 202501, "tag_filters": [{"tag_key": "service", "tag_value": "ec2"}]}], "metrics_query": "aws.cost.amortized{service:ec2} by {service}", "name": "my budget", "org_id": 123, "start_month": 202501, "total_amount": 1000, "updated_at": 1738258683590, "updated_by": "00000000-0a0a-0a0a-aaa0-00000000000a"}, "id": "00000000-0a0a-0a0a-aaa0-00000000000a"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Create or update a budget returns "OK" response
    Given new "UpsertBudget" request
    And body with value {"data": {"attributes": {"created_at": 1738258683590, "created_by": "00000000-0a0a-0a0a-aaa0-00000000000a", "end_month": 202502, "entries": [{"amount": 500, "month": 202501, "tag_filters": [{"tag_key": "service", "tag_value": "ec2"}]}], "metrics_query": "aws.cost.amortized{service:ec2} by {service}", "name": "my budget", "org_id": 123, "start_month": 202501, "total_amount": 1000, "updated_at": 1738258683590, "updated_by": "00000000-0a0a-0a0a-aaa0-00000000000a"}, "id": "00000000-0a0a-0a0a-aaa0-00000000000a"}}
    When the request is sent
    Then the response status is 200 OK

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

  @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management GCP Usage Cost config returns "Bad Request" response
    Given new "DeleteCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value "Invalid"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management GCP Usage Cost config returns "No Content" response
    Given new "DeleteCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    When the request is sent
    Then the response status is 204 No Content

  @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management GCP Usage Cost config returns "Not Found" response
    Given new "DeleteCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value "123456"
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

  @team:Datadog/cloud-cost-management
  Scenario: Delete a budget returns "Bad Request" response
    Given new "DeleteBudget" request
    And request contains "budget_id" parameter with value "1"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete a budget returns "No Content" response
    Given new "DeleteBudget" request
    And request contains "budget_id" parameter from "REPLACE.ME"
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

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Get a budget returns "Bad Request" response
    Given new "GetBudget" request
    And request contains "budget_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/cloud-cost-management
  Scenario: Get a budget returns "Not Found" response
    Given new "GetBudget" request
    And request contains "budget_id" parameter with value "9d055d22-0a0a-0a0a-aaa0-00000000000a"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Get a budget returns "OK" response
    Given new "GetBudget" request
    And request contains "budget_id" parameter from "REPLACE.ME"
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

  @team:Datadog/cloud-cost-management
  Scenario: List Cloud Cost Management GCP Usage Cost configs returns "OK" response
    Given new "ListCostGCPUsageCostConfigs" request
    When the request is sent
    Then the response status is 200 OK

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

  @team:Datadog/cloud-cost-management
  Scenario: List budgets returns "OK" response
    Given new "ListBudgets" request
    When the request is sent
    Then the response status is 200 OK

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

  @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management GCP Usage Cost config returns "Bad Request" response
    Given new "UpdateCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value "InvalidValue"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "gcp_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management GCP Usage Cost config returns "Not Found" response
    Given new "UpdateCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value "12345678"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "gcp_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management GCP Usage Cost config returns "OK" response
    Given new "UpdateCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value "100"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "gcp_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.account_id" is equal to "123456_A123BC_12AB34"

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
