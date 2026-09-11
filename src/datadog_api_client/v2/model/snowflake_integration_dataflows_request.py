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
    from datadog_api_client.v2.model.snowflake_account_usage_metrics_integration_dataflow_request import (
        SnowflakeAccountUsageMetricsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_request import (
        SnowflakeCloudCostMetricsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_request import (
        SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_request import (
        SnowflakeEventTableLogsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_request import (
        SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_query_history_logs_integration_dataflow_request import (
        SnowflakeQueryHistoryLogsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_request import (
        SnowflakeSecurityLogsIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_request import (
        SnowflakeTaskHistoryLogsIntegrationDataflowRequest,
    )


class SnowflakeIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_account_usage_metrics_integration_dataflow_request import (
            SnowflakeAccountUsageMetricsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_cloud_cost_metrics_integration_dataflow_request import (
            SnowflakeCloudCostMetricsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_data_observability_quality_monitoring_integration_dataflow_request import (
            SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_event_table_logs_integration_dataflow_request import (
            SnowflakeEventTableLogsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_organization_usage_metrics_integration_dataflow_request import (
            SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_query_history_logs_integration_dataflow_request import (
            SnowflakeQueryHistoryLogsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_security_logs_integration_dataflow_request import (
            SnowflakeSecurityLogsIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.snowflake_task_history_logs_integration_dataflow_request import (
            SnowflakeTaskHistoryLogsIntegrationDataflowRequest,
        )

        return {
            "snowflake_account_usage_metrics": (SnowflakeAccountUsageMetricsIntegrationDataflowRequest,),
            "snowflake_cloud_cost_metrics": (SnowflakeCloudCostMetricsIntegrationDataflowRequest,),
            "snowflake_data_observability_quality_monitoring": (
                SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest,
            ),
            "snowflake_event_table_logs": (SnowflakeEventTableLogsIntegrationDataflowRequest,),
            "snowflake_organization_usage_metrics": (SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest,),
            "snowflake_query_history_logs": (SnowflakeQueryHistoryLogsIntegrationDataflowRequest,),
            "snowflake_security_logs": (SnowflakeSecurityLogsIntegrationDataflowRequest,),
            "snowflake_task_history_logs": (SnowflakeTaskHistoryLogsIntegrationDataflowRequest,),
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
            SnowflakeAccountUsageMetricsIntegrationDataflowRequest, UnsetType
        ] = unset,
        snowflake_cloud_cost_metrics: Union[SnowflakeCloudCostMetricsIntegrationDataflowRequest, UnsetType] = unset,
        snowflake_data_observability_quality_monitoring: Union[
            SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest, UnsetType
        ] = unset,
        snowflake_event_table_logs: Union[SnowflakeEventTableLogsIntegrationDataflowRequest, UnsetType] = unset,
        snowflake_organization_usage_metrics: Union[
            SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest, UnsetType
        ] = unset,
        snowflake_query_history_logs: Union[SnowflakeQueryHistoryLogsIntegrationDataflowRequest, UnsetType] = unset,
        snowflake_security_logs: Union[SnowflakeSecurityLogsIntegrationDataflowRequest, UnsetType] = unset,
        snowflake_task_history_logs: Union[SnowflakeTaskHistoryLogsIntegrationDataflowRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Snowflake, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it, and use ``settings`` to configure what it collects. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow reads from Snowflake as the user in ``settings.username`` , so that user's role must be granted access to the underlying views; a dataflow enabled without those grants is stored but collects no data.

        :param snowflake_account_usage_metrics: Account-level usage metrics read from the Snowflake ``ACCOUNT_USAGE`` schema, covering storage usage, credit consumption, and query activity.
        :type snowflake_account_usage_metrics: SnowflakeAccountUsageMetricsIntegrationDataflowRequest, optional

        :param snowflake_cloud_cost_metrics: Cost data aggregated from the Snowflake ``ORGANIZATION_USAGE`` schema. `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_ must be enabled for your organization while this dataflow is enabled. Any request that enables this dataflow without Cloud Cost Management is rejected with a ``422`` response. The Snowflake role also needs the ORGANIZATION_BILLING_VIEWER database role to read the underlying cost views.
        :type snowflake_cloud_cost_metrics: SnowflakeCloudCostMetricsIntegrationDataflowRequest, optional

        :param snowflake_data_observability_quality_monitoring: Data Observability, which collects lineage and data quality information from your Snowflake databases so you can explore how data flows and detect and resolve quality issues.
        :type snowflake_data_observability_quality_monitoring: SnowflakeDataObservabilityQualityMonitoringIntegrationDataflowRequest, optional

        :param snowflake_event_table_logs: Records from your Snowflake event tables, used to monitor application behavior and identify issues. ``enabled`` turns the dataflow on and off as a whole, and the per-record-type toggles in ``settings`` select which kinds of record it collects while it is on. The Snowflake role needs usage granted on the database, the schema, and the event table itself.
        :type snowflake_event_table_logs: SnowflakeEventTableLogsIntegrationDataflowRequest, optional

        :param snowflake_organization_usage_metrics: Organization-level usage metrics read from the Snowflake ``ORGANIZATION_USAGE`` schema, covering the credit consumption of every account in the organization and the history of data transferred out of Snowflake. Reading that schema requires the ORGADMIN role.
        :type snowflake_organization_usage_metrics: SnowflakeOrganizationUsageMetricsIntegrationDataflowRequest, optional

        :param snowflake_query_history_logs: Per-query logs that let you identify long-running, poorly performing, and expensive queries.
        :type snowflake_query_history_logs: SnowflakeQueryHistoryLogsIntegrationDataflowRequest, optional

        :param snowflake_security_logs: Security logs from the Snowflake ``ACCOUNT_USAGE`` schema, for analyzing the security of your Snowflake account and running threat detection with `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_.
        :type snowflake_security_logs: SnowflakeSecurityLogsIntegrationDataflowRequest, optional

        :param snowflake_task_history_logs: Execution logs for your scheduled Snowflake tasks, covering start and end time, status, and any error message.
        :type snowflake_task_history_logs: SnowflakeTaskHistoryLogsIntegrationDataflowRequest, optional
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
