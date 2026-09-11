"""
Update a Snowflake integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.snowflake_integration_api import SnowflakeIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.snowflake_account_usage_metrics_integration_dataflow_request import (
    SnowflakeAccountUsageMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_account_usage_metrics_integration_dataflow_settings_request import (
    SnowflakeAccountUsageMetricsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_request import (
    SnowflakeCloudCostMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_settings_request import (
    SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_request import (
    SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_settings_request import (
    SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_request import (
    SnowflakeEventTableLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_settings_request import (
    SnowflakeEventTableLogsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_integration_account_authentication_request import (
    SnowflakeIntegrationAccountAuthenticationRequest,
)
from datadog_api_client.v2.model.snowflake_integration_account_private_key_auth_type import (
    SnowflakeIntegrationAccountPrivateKeyAuthType,
)
from datadog_api_client.v2.model.snowflake_integration_account_settings_update import (
    SnowflakeIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.snowflake_integration_account_update_attributes import (
    SnowflakeIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.snowflake_integration_account_update_data import SnowflakeIntegrationAccountUpdateData
from datadog_api_client.v2.model.snowflake_integration_account_update_request import (
    SnowflakeIntegrationAccountUpdateRequest,
)
from datadog_api_client.v2.model.snowflake_integration_dataflows_request import SnowflakeIntegrationDataflowsRequest
from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_request import (
    SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_settings_request import (
    SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_query_history_logs_integration_dataflow_request import (
    SnowflakeQueryHistoryLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_query_history_logs_integration_dataflow_settings_request import (
    SnowflakeQueryHistoryLogsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_request import (
    SnowflakeSecurityLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_settings_request import (
    SnowflakeSecurityLogsIntegrationDataflowSettingsRequest,
)
from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_request import (
    SnowflakeTaskHistoryLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_settings_request import (
    SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest,
)

body = SnowflakeIntegrationAccountUpdateRequest(
    data=SnowflakeIntegrationAccountUpdateData(
        attributes=SnowflakeIntegrationAccountUpdateAttributes(
            authentication=SnowflakeIntegrationAccountAuthenticationRequest(
                auth_type=SnowflakeIntegrationAccountPrivateKeyAuthType.SNOWFLAKE_PRIVATE_KEY,
                private_key="-----BEGIN PRIVATE KEY-----\nMIIE...\n-----END PRIVATE KEY-----",
                private_key_name="my-rsa-key",
                private_key_passphrase="your-private-key-passphrase",
            ),
            dataflows=SnowflakeIntegrationDataflowsRequest(
                snowflake_account_usage_metrics=SnowflakeAccountUsageMetricsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeAccountUsageMetricsIntegrationDataflowSettingsRequest(
                        account_usage_metrics_aggregate_last_24h=False,
                    ),
                ),
                snowflake_cloud_cost_metrics=SnowflakeCloudCostMetricsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeCloudCostMetricsIntegrationDataflowSettingsRequest(
                        query_tags="env,team,cost_center",
                    ),
                ),
                snowflake_data_observability_quality_monitoring=SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowSettingsRequest(
                        do_table_crawler_cron="0 */6 * * *",
                        sync_snowflake_system_database=True,
                    ),
                ),
                snowflake_event_table_logs=SnowflakeEventTableLogsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeEventTableLogsIntegrationDataflowSettingsRequest(
                        event_table_events_enabled=True,
                        event_table_logs_enabled=True,
                        event_table_logs_interval_min=15,
                        event_table_span_events_enabled=False,
                        event_table_spans_enabled=False,
                    ),
                ),
                snowflake_organization_usage_metrics=SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeOrganizationUsageMetricsIntegrationDataflowSettingsRequest(
                        organization_usage_metrics_aggregate_last_24h=False,
                    ),
                ),
                snowflake_query_history_logs=SnowflakeQueryHistoryLogsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeQueryHistoryLogsIntegrationDataflowSettingsRequest(
                        join_query_history_with_access_history_enabled=True,
                        query_history_logs_interval_min=15,
                    ),
                ),
                snowflake_security_logs=SnowflakeSecurityLogsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeSecurityLogsIntegrationDataflowSettingsRequest(
                        security_logs_interval_min=60,
                    ),
                ),
                snowflake_task_history_logs=SnowflakeTaskHistoryLogsIntegrationDataflowRequest(
                    enabled=True,
                    settings=SnowflakeTaskHistoryLogsIntegrationDataflowSettingsRequest(
                        task_history_logs_interval_min=30,
                    ),
                ),
            ),
            name="prod-snowflake",
            settings=SnowflakeIntegrationAccountSettingsUpdate(
                snowflake_account_identifier="myorg-myaccount",
                username="datadog_user",
            ),
        ),
        id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_snowflake_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = SnowflakeIntegrationApi(api_client)
    response = api_instance.update_snowflake_integration_account(account_id="account_id", body=body)

    print(response)
