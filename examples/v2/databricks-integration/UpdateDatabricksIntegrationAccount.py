"""
Update a Databricks integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.databricks_integration_api import DatabricksIntegrationApi
from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_request import (
    DatabricksCloudCostMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_cloud_cost_metrics_integration_dataflow_settings_request import (
    DatabricksCloudCostMetricsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.databricks_data_observability_jobs_monitoring_integration_dataflow_request import (
    DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_data_observability_jobs_monitoring_integration_dataflow_settings_request import (
    DatabricksDataObservabilityJobsMonitoringIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.databricks_data_observability_quality_monitoring_integration_dataflow_request import (
    DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.databricks_data_observability_quality_monitoring_integration_dataflow_settings_request import (
    DatabricksDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_request import (
    DatabricksIntegrationAccountOAuthAuthRequest,
)
from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_type import (
    DatabricksIntegrationAccountOAuthAuthType,
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
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = DatabricksIntegrationAccountUpdateRequest(
    data=DatabricksIntegrationAccountUpdateData(
        attributes=DatabricksIntegrationAccountUpdateAttributes(
            authentication=DatabricksIntegrationAccountOAuthAuthRequest(
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
                databricks_data_observability_jobs_monitoring=DatabricksDataObservabilityJobsMonitoringIntegrationDataflowRequest(
                    enabled=True,
                    settings=DatabricksDataObservabilityJobsMonitoringIntegrationDataflowSettingsRequest(
                        dd_api_key_id="fe383f4e-09fc-46bf-8e10-4efdd453a646",
                        dd_api_key_secret="your-datadog-api-key",
                        djm_global_init_script_enabled=True,
                        script_gpum_enabled=True,
                        script_logs_enabled=True,
                        serverless_jobs_enabled=True,
                    ),
                ),
                databricks_data_observability_quality_monitoring=DatabricksDataObservabilityQualityMonitoringIntegrationDataflowRequest(
                    enabled=True,
                    settings=DatabricksDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest(
                        do_crawlers_cron="0 * * * *",
                        sync_system_catalog=True,
                    ),
                ),
                databricks_model_serving_metrics=DatabricksModelServingMetricsIntegrationDataflowRequest(
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
    api_instance = DatabricksIntegrationApi(api_client)
    response = api_instance.update_databricks_integration_account(account_id="account_id", body=body)

    print(response)
