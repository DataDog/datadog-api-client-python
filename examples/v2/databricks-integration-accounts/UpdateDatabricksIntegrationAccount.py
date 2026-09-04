"""
Update a Databricks integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.databricks_integration_accounts_api import DatabricksIntegrationAccountsApi
from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_request import (
    DatabricksCloudCostMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_settings_request import (
    DatabricksCloudCostMetricsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.databricks_data_job_monitoring_integration_dataflow_request import (
    DatabricksDataJobMonitoringIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_data_job_monitoring_integration_dataflow_settings_request import (
    DatabricksDataJobMonitoringIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.databricks_data_observability_integration_dataflow_request import (
    DatabricksDataObservabilityIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_data_observability_integration_dataflow_settings_request import (
    DatabricksDataObservabilityIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_type import (
    DatabricksIntegrationAccountOAuthAuthType,
)
from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_update import (
    DatabricksIntegrationAccountOAuthAuthUpdate,
)
from datadog_api_client.v2.model.databricks_integration_account_settings_update import (
    DatabricksIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.databricks_integration_account_update_attributes import (
    DatabricksIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.databricks_integration_account_update_data import (
    DatabricksIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.databricks_integration_account_update_request import (
    DatabricksIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.databricks_integration_dataflows_request import DatabricksIntegrationDataflowsRequest
from datadog_api_client.v2.model.databricks_model_serving_metrics_integration_dataflow_request import (
    DatabricksModelServingMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_serverless_jobs_integration_dataflow_request import (
    DatabricksServerlessJobsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = DatabricksIntegrationAccountUpdateRequest(
    data=DatabricksIntegrationAccountUpdateData(
        attributes=DatabricksIntegrationAccountUpdateAttributes(
            authentication=DatabricksIntegrationAccountOAuthAuthUpdate(
                auth_type=DatabricksIntegrationAccountOAuthAuthType.DATABRICKS_OAUTH,
                azure_tenant_id="4d3bac44-0230-4732-9e70-cc00736f0a97",
                client_id="5c10654a-b3a3-4840-b37f-f477590c70a0",
                client_secret="your-client-secret",
            ),
            dataflows=DatabricksIntegrationDataflowsRequest(
                databricks_cloud_cost_metrics=DatabricksCloudCostMetricsIntegrationDataflowRequest(
                    enabled=True,
                    settings=DatabricksCloudCostMetricsIntegrationDataflowSettingsRequest(
                        ccm_collect_all_workspaces=True,
                    ),
                ),
                databricks_data_job_monitoring=DatabricksDataJobMonitoringIntegrationDataflowRequest(
                    enabled=True,
                    settings=DatabricksDataJobMonitoringIntegrationDataflowSettingsRequest(
                        dd_api_key_id="fe383f4e-09fc-46bf-8e10-4efdd453a646",
                        dd_api_key_secret="your-datadog-api-key",
                        djm_global_init_script_enabled=True,
                        script_gpum_enabled=True,
                        script_logs_enabled=True,
                    ),
                ),
                databricks_data_observability=DatabricksDataObservabilityIntegrationDataflowRequest(
                    enabled=True,
                    settings=DatabricksDataObservabilityIntegrationDataflowSettingsRequest(
                        do_crawlers_cron="0 * * * *",
                        sync_system_catalog=True,
                    ),
                ),
                databricks_model_serving_metrics=DatabricksModelServingMetricsIntegrationDataflowRequest(
                    enabled=True,
                ),
                databricks_serverless_jobs=DatabricksServerlessJobsIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="My Databricks Workspace",
            settings=DatabricksIntegrationAccountSettingsUpdate(
                system_tables_sql_warehouse_id="aba7c023d4172910",
                workspace_url="https://dbc-1234abcd.cloud.databricks.com",
            ),
        ),
        id="a9a69c2e-4f8d-4e42-9c1a-2a7a2d3b7c6f",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_databricks_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatabricksIntegrationAccountsApi(api_client)
    response = api_instance.update_databricks_integration_account(account_id="account_id", body=body)

    print(response)
