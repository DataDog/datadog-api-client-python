@endpoint(cloud-cost-management) @endpoint(cloud-cost-management-v2)
Feature: Cloud Cost Management
  The Cloud Cost Management API allows you to set up, edit, and delete Cloud
  Cost Management accounts for AWS, Azure, and Google Cloud. You can query
  your cost data by using the [Metrics
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

  @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management Azure configs returns "Bad Request" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "scope": "this_is_an_invalid_scope"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create Cloud Cost Management Azure configs returns "OK" response
    Given new "CreateCostAzureUCConfigs" request
    And body with value {"data": {"attributes": {"account_id": "1234abcd-1234-abcd-1234-1234abcd1234", "actual_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "amortized_bill_config": {"export_name": "dd-actual-export", "export_path": "dd-export-path", "storage_account": "dd-storage-account", "storage_container": "dd-storage-container"}, "client_id": "1234abcd-1234-abcd-1234-1234abcd1234", "scope": "subscriptions/1234abcd-1234-abcd-1234-1234abcd1234"}, "type": "azure_uc_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.configs[0].account_id" is equal to "1234abcd-1234-abcd-1234-1234abcd1234"

  @team:Datadog/cloud-cost-management
  Scenario: Create Google Cloud Usage Cost config returns "Bad Request" response
    Given new "CreateCostGCPUsageCostConfig" request
    And body with value {"data": {"attributes": {"billing_account_id": "123456_A123BC_12AB34", "bucket_name": "dd-cost-bucket", "export_dataset_name": "billing", "export_prefix": "datadog_cloud_cost_usage_export", "export_project_name": "dd-cloud-cost-report", "service_account": "InvalidServiceAccount"}, "type": "gcp_uc_config_post_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create Google Cloud Usage Cost config returns "OK" response
    Given new "CreateCostGCPUsageCostConfig" request
    And body with value {"data": {"attributes": {"billing_account_id": "123456_A123BC_12AB34", "bucket_name": "dd-cost-bucket", "export_dataset_name": "billing", "export_prefix": "datadog_cloud_cost_usage_export", "export_project_name": "dd-cloud-cost-report", "service_account": "dd-ccm-gcp-integration@my-environment.iam.gserviceaccount.com"}, "type": "gcp_uc_config_post_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.account_id" is equal to "123456_A123BC_12AB34"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create arbitrary cost rule returns "OK" response
    Given new "CreateArbitraryCostRule" request
    And body with value {"data": {"attributes": {"costs_to_allocate": [{"condition": "is", "tag": "account_id", "value": "123456789", "values":[]}, {"condition": "in", "tag": "environment", "value": "", "values": ["production", "staging"]}], "enabled": true, "order_id": 1, "provider": ["aws", "gcp"], "rule_name": "example-arbitrary-cost-rule", "strategy": {"allocated_by_tag_keys": ["team", "environment"], "based_on_costs": [{"condition": "is", "tag": "service", "value": "web-api", "values":[]}, {"condition": "not in", "tag": "team", "value": "", "values": ["legacy", "deprecated"]}], "granularity": "daily", "method": "proportional"}, "type": "shared"}, "type": "upsert_arbitrary_rule"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "arbitrary_rule"
    And the response "data.attributes.rule_name" is equal to "example-arbitrary-cost-rule"

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

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Create ruleset returns "OK" response
    Given new "CreateRuleset" request
    And body with value {"data": {"attributes": {"enabled": true, "rules": [{"enabled": true, "mapping": null, "name": "Add Cost Center Tag", "query": {"addition": {"key": "cost_center", "value": "engineering"}, "case_insensitivity": false, "if_not_exists": true, "query": "account_id:\"123456789\" AND service:\"web-api\""}, "reference_table": null}]}, "id": "New Ruleset", "type": "create_ruleset"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "ruleset"
    And the response "data.attributes.name" is equal to "New Ruleset"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management AWS CUR config returns "Bad Request" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management AWS CUR config returns "No Content" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value 100
    When the request is sent
    Then the response status is 204 No Content

  @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management AWS CUR config returns "Not Found" response
    Given new "DeleteCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value 123456
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
    And request contains "cloud_account_id" parameter with value 100
    When the request is sent
    Then the response status is 204 No Content

  @team:Datadog/cloud-cost-management
  Scenario: Delete Cloud Cost Management Azure config returns "Not Found" response
    Given new "DeleteCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter with value 123456
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
  Scenario: Delete Custom Costs file returns "Not Found" response
    Given new "DeleteCustomCostsFile" request
    And request contains "file_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Delete Google Cloud Usage Cost config returns "Bad Request" response
    Given new "DeleteCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete Google Cloud Usage Cost config returns "No Content" response
    Given new "DeleteCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value 100
    When the request is sent
    Then the response status is 204 No Content

  @team:Datadog/cloud-cost-management
  Scenario: Delete Google Cloud Usage Cost config returns "Not Found" response
    Given new "DeleteCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value 123456
    When the request is sent
    Then the response status is 404 Not Found

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
  Scenario: Delete arbitrary cost rule returns "No Content" response
    Given new "DeleteArbitraryCostRule" request
    And request contains "rule_id" parameter with value 123456
    When the request is sent
    Then the response status is 204 No Content

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Delete ruleset returns "No Content" response
    Given new "DeleteRuleset" request
    And request contains "ruleset_id" parameter with value "1c5dae14-237d-4b9a-a515-aa55b3939142"
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

  @team:Datadog/cloud-cost-management
  Scenario: Get Custom Costs file returns "Not Found" response
    Given new "GetCustomCostsFile" request
    And request contains "file_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Get Custom Costs file returns "OK" response
    Given new "GetCustomCostsFile" request
    And request contains "file_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Get Google Cloud Usage Cost config returns "OK" response
    Given new "GetCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value 123456
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "gcp_uc_config"
    And the response "data.attributes.account_id" is equal to "123456_ABCDEF_123ABC"

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
  Scenario: Get arbitrary cost rule returns "OK" response
    Given new "GetArbitraryCostRule" request
    And request contains "rule_id" parameter with value 123456
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Get cost AWS CUR config returns "OK" response
    Given new "GetCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value 123456
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "aws_cur_config"
    And the response "data.attributes.account_id" is equal to "123456123456"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Get cost Azure UC config returns "OK" response
    Given new "GetCostAzureUCConfig" request
    And request contains "cloud_account_id" parameter with value 123456
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "azure_uc_configs"
    And the response "data.attributes.configs[0].dataset_type" is equal to "amortized"
    And the response "data.attributes.configs[1].dataset_type" is equal to "actual"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Get ruleset returns "OK" response
    Given new "GetRuleset" request
    And request contains "ruleset_id" parameter with value "da0e30e2-615d-4dae-9a22-38cf86a87dde"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "ruleset"
    And the response "data.attributes.name" is equal to "New Ruleset"

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

  @team:Datadog/cloud-cost-management
  Scenario: List Custom Costs files returns "Bad Request" response
    Given new "ListCustomCostsFiles" request
    And request contains "filter[status]" parameter with value "invalid_file_status"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: List Custom Costs files returns "OK" response
    Given new "ListCustomCostsFiles" request
    When the request is sent
    Then the response status is 200 OK

  @team:Datadog/cloud-cost-management
  Scenario: List Google Cloud Usage Cost configs returns "OK" response
    Given new "ListCostGCPUsageCostConfigs" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: List arbitrary cost rules returns "OK" response
    Given new "ListArbitraryCostRules" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.rule_name" is equal to "example-arbitrary-cost-rule"

  @team:Datadog/cloud-cost-management
  Scenario: List budgets returns "OK" response
    Given new "ListBudgets" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: List rulesets returns "OK" response
    Given new "ListRulesets" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "New Ruleset"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Reorder arbitrary cost rules returns "Successfully reordered rules" response
    Given new "ReorderArbitraryCostRules" request
    And body with value {"data": [{"id": "456", "type": "arbitrary_rule"}, {"id": "123", "type": "arbitrary_rule"}, {"id": "789", "type": "arbitrary_rule"}]}
    When the request is sent
    Then the response status is 204 Successfully reordered rules

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Reorder rulesets returns "Successfully reordered rulesets" response
    Given new "ReorderRulesets" request
    And body with value {"data": [{"type": "ruleset"}]}
    When the request is sent
    Then the response status is 204 Successfully reordered rulesets

  @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management AWS CUR config returns "Not Found" response
    Given new "UpdateCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value 123456
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "aws_cur_config_patch_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management AWS CUR config returns "OK" response
    Given new "UpdateCostAWSCURConfig" request
    And request contains "cloud_account_id" parameter with value 100
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

  @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management Azure config returns "Not Found" response
    Given new "UpdateCostAzureUCConfigs" request
    And request contains "cloud_account_id" parameter with value 123456
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "azure_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update Cloud Cost Management Azure config returns "OK" response
    Given new "UpdateCostAzureUCConfigs" request
    And request contains "cloud_account_id" parameter with value 100
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "azure_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "azure_uc_configs"

  @generated @skip @team:Datadog/cloud-cost-management
  Scenario: Update Google Cloud Usage Cost config returns "Bad Request" response
    Given new "UpdateCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "gcp_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:Datadog/cloud-cost-management
  Scenario: Update Google Cloud Usage Cost config returns "Not Found" response
    Given new "UpdateCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value 123456
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "gcp_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update Google Cloud Usage Cost config returns "OK" response
    Given new "UpdateCostGCPUsageCostConfig" request
    And request contains "cloud_account_id" parameter with value 100
    And body with value {"data": {"attributes": {"is_enabled": true}, "type": "gcp_uc_config_patch_request"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.account_id" is equal to "123456_A123BC_12AB34"

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update arbitrary cost rule returns "OK" response
    Given new "UpdateArbitraryCostRule" request
    And request contains "rule_id" parameter with value 123456
    And body with value {"data": {"attributes": {"costs_to_allocate": [{"condition": "is", "tag": "account_id", "value": "123456789", "values":[]}, {"condition": "in", "tag": "environment", "value": "", "values": ["production", "staging"]}], "enabled": true, "order_id": 1, "provider": ["aws", "gcp"], "rule_name": "example-arbitrary-cost-rule", "strategy": {"allocated_by_tag_keys": ["team", "environment"], "based_on_costs": [{"condition": "is", "tag": "service", "value": "web-api", "values":[]}, {"condition": "not in", "tag": "team", "value": "", "values": ["legacy", "deprecated"]}], "granularity": "daily", "method": "proportional"}, "type": "shared"}, "type": "upsert_arbitrary_rule"}}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Update ruleset returns "OK" response
    Given new "UpdateRuleset" request
    And request contains "ruleset_id" parameter with value "1c5dae14-237d-4b9a-a515-aa55b3939142"
    And body with value {"data": {"attributes": {"enabled": true, "last_version": 3601919, "rules": [{"enabled": true, "mapping": {"destination_key": "team_owner", "if_not_exists": true, "source_keys": ["account_name", "account_id"]}, "name": "Account Name Mapping", "query": null, "reference_table": null}]}, "type": "update_ruleset"}}
    When the request is sent
    Then the response status is 200 OK

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

  @team:Datadog/cloud-cost-management
  Scenario: Upload Custom Costs file returns "Bad Request" response
    Given new "UploadCustomCostsFile" request
    And body with value [{"BilledCost": 100.5, "BillingCurrency": "USD", "ChargeDescription": "Monthly usage charge for my service", "ChargePeriodEnd": "2023-02-28", "ChargePeriodStart": "2023-02-01"}]
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:Datadog/cloud-cost-management
  Scenario: Validate query returns "OK" response
    Given new "ValidateQuery" request
    And body with value {"data": {"attributes": {"Query": "example:query AND test:true"}, "type": "validate_query"}}
    When the request is sent
    Then the response status is 200 OK
