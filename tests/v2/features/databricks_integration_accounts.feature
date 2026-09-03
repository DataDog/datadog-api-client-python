@endpoint(databricks-integration-accounts) @endpoint(databricks-integration-accounts-v2)
Feature: Databricks Integration Accounts
  Manage your Datadog Databricks integration accounts directly through the
  Datadog API. Create, update, and delete accounts, configure authentication
  and settings, and enable or disable dataflows such as Data Jobs
  Monitoring, serverless jobs, cluster logs, GPU metrics, cloud cost
  metrics, data observability, and model serving metrics. See the
  [Databricks integration
  page](https://docs.datadoghq.com/integrations/databricks/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "DatabricksIntegrationAccounts" API

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Databricks integration account returns "Bad Request" response
    Given operation "CreateDatabricksIntegrationAccount" enabled
    And new "CreateDatabricksIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Databricks integration account returns "Created" response
    Given operation "CreateDatabricksIntegrationAccount" enabled
    And new "CreateDatabricksIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Databricks integration account returns "Not Found" response
    Given operation "CreateDatabricksIntegrationAccount" enabled
    And new "CreateDatabricksIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Create a Databricks integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "CreateDatabricksIntegrationAccount" enabled
    And new "CreateDatabricksIntegrationAccount" request
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Databricks integration account returns "Bad Request" response
    Given operation "DeleteDatabricksIntegrationAccount" enabled
    And new "DeleteDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Databricks integration account returns "Not Found" response
    Given operation "DeleteDatabricksIntegrationAccount" enabled
    And new "DeleteDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Delete a Databricks integration account returns "OK" response
    Given operation "DeleteDatabricksIntegrationAccount" enabled
    And new "DeleteDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Databricks integration account returns "Bad Request" response
    Given operation "GetDatabricksIntegrationAccount" enabled
    And new "GetDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Databricks integration account returns "Not Found" response
    Given operation "GetDatabricksIntegrationAccount" enabled
    And new "GetDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Get a Databricks integration account returns "OK" response
    Given operation "GetDatabricksIntegrationAccount" enabled
    And new "GetDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Databricks integration accounts returns "Bad Request" response
    Given operation "ListDatabricksIntegrationAccounts" enabled
    And new "ListDatabricksIntegrationAccounts" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Databricks integration accounts returns "Not Found" response
    Given operation "ListDatabricksIntegrationAccounts" enabled
    And new "ListDatabricksIntegrationAccounts" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: List Databricks integration accounts returns "OK" response
    Given operation "ListDatabricksIntegrationAccounts" enabled
    And new "ListDatabricksIntegrationAccounts" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Databricks integration account returns "Bad Request" response
    Given operation "UpdateDatabricksIntegrationAccount" enabled
    And new "UpdateDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "id": "a9a69c2e-4f8d-4e42-9c1a-2a7a2d3b7c6f", "type": "integration-account"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Databricks integration account returns "Not Found" response
    Given operation "UpdateDatabricksIntegrationAccount" enabled
    And new "UpdateDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "id": "a9a69c2e-4f8d-4e42-9c1a-2a7a2d3b7c6f", "type": "integration-account"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Databricks integration account returns "OK" response
    Given operation "UpdateDatabricksIntegrationAccount" enabled
    And new "UpdateDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "id": "a9a69c2e-4f8d-4e42-9c1a-2a7a2d3b7c6f", "type": "integration-account"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/saas-integrations
  Scenario: Update a Databricks integration account returns "The server cannot process the request because it contains invalid data." response
    Given operation "UpdateDatabricksIntegrationAccount" enabled
    And new "UpdateDatabricksIntegrationAccount" request
    And request contains "account_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"authentication": {"auth_type": "databricks-oauth", "azure_tenant_id": "4d3bac44-0230-4732-9e70-cc00736f0a97", "client_id": "5c10654a-b3a3-4840-b37f-f477590c70a0", "client_secret": "your-client-secret"}, "dataflows": {"databricks-cloud-cost-metrics": {"enabled": true, "settings": {"ccm_collect_all_workspaces": true}}, "databricks-data-job-monitoring": {"enabled": true, "settings": {"dd_api_key_id": "fe383f4e-09fc-46bf-8e10-4efdd453a646", "dd_api_key_secret": "your-datadog-api-key", "djm_global_init_script_enabled": true, "script_gpum_enabled": true, "script_logs_enabled": true}}, "databricks-data-observability": {"enabled": true, "settings": {"do_crawlers_cron": "0 * * * *", "sync_system_catalog": true}}, "databricks-model-serving-metrics": {"enabled": true}, "databricks-serverless-jobs": {"enabled": true}}, "name": "My Databricks Workspace", "settings": {"system_tables_sql_warehouse_id": "aba7c023d4172910", "workspace_url": "https://dbc-1234abcd.cloud.databricks.com"}}, "id": "a9a69c2e-4f8d-4e42-9c1a-2a7a2d3b7c6f", "type": "integration-account"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.
