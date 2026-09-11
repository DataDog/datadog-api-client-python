# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.snowflake_account_usage_metrics_integration_dataflow_response import (
        SnowflakeAccountUsageMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_response import (
        SnowflakeCloudCostMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_response import (
        SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_response import (
        SnowflakeEventTableLogsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_response import (
        SnowflakeOrganizationUsageMetricsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_query_history_logs_integration_dataflow_response import (
        SnowflakeQueryHistoryLogsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_response import (
        SnowflakeSecurityLogsIntegrationDataflowResponse,
    )
    from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_response import (
        SnowflakeTaskHistoryLogsIntegrationDataflowResponse,
    )


class SnowflakeIntegrationDataflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_account_usage_metrics_integration_dataflow_response import (
            SnowflakeAccountUsageMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_response import (
            SnowflakeCloudCostMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_response import (
            SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_response import (
            SnowflakeEventTableLogsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_response import (
            SnowflakeOrganizationUsageMetricsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_query_history_logs_integration_dataflow_response import (
            SnowflakeQueryHistoryLogsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_response import (
            SnowflakeSecurityLogsIntegrationDataflowResponse,
        )
        from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_response import (
            SnowflakeTaskHistoryLogsIntegrationDataflowResponse,
        )

        return {
            "snowflake_account_usage_metrics": (SnowflakeAccountUsageMetricsIntegrationDataflowResponse,),
            "snowflake_cloud_cost_metrics": (SnowflakeCloudCostMetricsIntegrationDataflowResponse,),
            "snowflake_data_observability_quality_monitoring": (
                SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowResponse,
            ),
            "snowflake_event_table_logs": (SnowflakeEventTableLogsIntegrationDataflowResponse,),
            "snowflake_organization_usage_metrics": (SnowflakeOrganizationUsageMetricsIntegrationDataflowResponse,),
            "snowflake_query_history_logs": (SnowflakeQueryHistoryLogsIntegrationDataflowResponse,),
            "snowflake_security_logs": (SnowflakeSecurityLogsIntegrationDataflowResponse,),
            "snowflake_task_history_logs": (SnowflakeTaskHistoryLogsIntegrationDataflowResponse,),
        }

    attribute_map = {
        "snowflake_account_usage_metrics": "snowflake-account-usage-metrics",
        "snowflake_cloud_cost_metrics": "snowflake-cloud-cost-metrics",
        "snowflake_data_observability_quality_monitoring": "snowflake-data-observability-quality-monitoring",
        "snowflake_event_table_logs": "snowflake-event-table-logs",
        "snowflake_organization_usage_metrics": "snowflake-organization-usage-metrics",
        "snowflake_query_history_logs": "snowflake-query-history-logs",
        "snowflake_security_logs": "snowflake-security-logs",
        "snowflake_task_history_logs": "snowflake-task-history-logs",
    }

    def __init__(
        self_,
        snowflake_account_usage_metrics: Union[
            SnowflakeAccountUsageMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        snowflake_cloud_cost_metrics: Union[SnowflakeCloudCostMetricsIntegrationDataflowResponse, UnsetType] = unset,
        snowflake_data_observability_quality_monitoring: Union[
            SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowResponse, UnsetType
        ] = unset,
        snowflake_event_table_logs: Union[SnowflakeEventTableLogsIntegrationDataflowResponse, UnsetType] = unset,
        snowflake_organization_usage_metrics: Union[
            SnowflakeOrganizationUsageMetricsIntegrationDataflowResponse, UnsetType
        ] = unset,
        snowflake_query_history_logs: Union[SnowflakeQueryHistoryLogsIntegrationDataflowResponse, UnsetType] = unset,
        snowflake_security_logs: Union[SnowflakeSecurityLogsIntegrationDataflowResponse, UnsetType] = unset,
        snowflake_task_history_logs: Union[SnowflakeTaskHistoryLogsIntegrationDataflowResponse, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Snowflake, keyed by dataflow id.

        :param snowflake_account_usage_metrics: Account-level usage metrics read from the Snowflake ``ACCOUNT_USAGE`` schema, covering storage usage, credit consumption, and query activity.
        :type snowflake_account_usage_metrics: SnowflakeAccountUsageMetricsIntegrationDataflowResponse, optional

        :param snowflake_cloud_cost_metrics: Cost data aggregated from the Snowflake ``ORGANIZATION_USAGE`` schema. Requires `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_ to be set up for your organization, and the ORGANIZATION_BILLING_VIEWER database role on the Snowflake role.
        :type snowflake_cloud_cost_metrics: SnowflakeCloudCostMetricsIntegrationDataflowResponse, optional

        :param snowflake_data_observability_quality_monitoring: Data Observability, which collects lineage and data quality information from your Snowflake databases so you can explore how data flows and detect and resolve quality issues.
        :type snowflake_data_observability_quality_monitoring: SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowResponse, optional

        :param snowflake_event_table_logs: Records from your Snowflake event tables, used to monitor application behavior and identify issues. ``enabled`` turns the dataflow on and off as a whole, and the per-record-type toggles in ``settings`` select which kinds of record it collects while it is on. The Snowflake role needs usage granted on the database, the schema, and the event table itself.
        :type snowflake_event_table_logs: SnowflakeEventTableLogsIntegrationDataflowResponse, optional

        :param snowflake_organization_usage_metrics: Organization-level usage metrics read from the Snowflake ``ORGANIZATION_USAGE`` schema, covering the credit consumption of every account in the organization and the history of data transferred out of Snowflake. Reading that schema requires the ORGADMIN role.
        :type snowflake_organization_usage_metrics: SnowflakeOrganizationUsageMetricsIntegrationDataflowResponse, optional

        :param snowflake_query_history_logs: Per-query logs that let you identify long-running, poorly performing, and expensive queries.
        :type snowflake_query_history_logs: SnowflakeQueryHistoryLogsIntegrationDataflowResponse, optional

        :param snowflake_security_logs: Security logs from the Snowflake ``ACCOUNT_USAGE`` schema, for analyzing the security of your Snowflake account and running threat detection with `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_.
        :type snowflake_security_logs: SnowflakeSecurityLogsIntegrationDataflowResponse, optional

        :param snowflake_task_history_logs: Execution logs for your scheduled Snowflake tasks, covering start and end time, status, and any error message.
        :type snowflake_task_history_logs: SnowflakeTaskHistoryLogsIntegrationDataflowResponse, optional
        """
        if snowflake_account_usage_metrics is not unset:
            kwargs["snowflake_account_usage_metrics"] = snowflake_account_usage_metrics
        if snowflake_cloud_cost_metrics is not unset:
            kwargs["snowflake_cloud_cost_metrics"] = snowflake_cloud_cost_metrics
        if snowflake_data_observability_quality_monitoring is not unset:
            kwargs["snowflake_data_observability_quality_monitoring"] = snowflake_data_observability_quality_monitoring
        if snowflake_event_table_logs is not unset:
            kwargs["snowflake_event_table_logs"] = snowflake_event_table_logs
        if snowflake_organization_usage_metrics is not unset:
            kwargs["snowflake_organization_usage_metrics"] = snowflake_organization_usage_metrics
        if snowflake_query_history_logs is not unset:
            kwargs["snowflake_query_history_logs"] = snowflake_query_history_logs
        if snowflake_security_logs is not unset:
            kwargs["snowflake_security_logs"] = snowflake_security_logs
        if snowflake_task_history_logs is not unset:
            kwargs["snowflake_task_history_logs"] = snowflake_task_history_logs
        super().__init__(kwargs)
