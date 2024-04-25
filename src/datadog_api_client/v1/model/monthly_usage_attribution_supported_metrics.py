# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonthlyUsageAttributionSupportedMetrics(ModelSimple):
    """
    Supported metrics for monthly usage attribution requests.

    :param value: Must be one of ["api_usage", "api_percentage", "apm_fargate_usage", "apm_fargate_percentage", "appsec_fargate_usage", "appsec_fargate_percentage", "apm_host_usage", "apm_host_percentage", "apm_usm_usage", "apm_usm_percentage", "appsec_usage", "appsec_percentage", "asm_serverless_traced_invocations_usage", "asm_serverless_traced_invocations_percentage", "browser_usage", "browser_percentage", "ci_visibility_itr_usage", "ci_visibility_itr_percentage", "cloud_siem_usage", "cloud_siem_percentage", "container_excl_agent_usage", "container_excl_agent_percentage", "container_usage", "container_percentage", "cspm_containers_percentage", "cspm_containers_usage", "cspm_hosts_percentage", "cspm_hosts_usage", "custom_timeseries_usage", "custom_timeseries_percentage", "custom_ingested_timeseries_usage", "custom_ingested_timeseries_percentage", "cws_containers_percentage", "cws_containers_usage", "cws_hosts_percentage", "cws_hosts_usage", "dbm_hosts_percentage", "dbm_hosts_usage", "dbm_queries_percentage", "dbm_queries_usage", "error_tracking_usage", "error_tracking_percentage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "estimated_ingested_logs_usage", "estimated_ingested_logs_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage", "fargate_usage", "fargate_percentage", "functions_usage", "functions_percentage", "incident_management_monthly_active_users_usage", "incident_management_monthly_active_users_percentage", "infra_host_usage", "infra_host_percentage", "invocations_usage", "invocations_percentage", "lambda_traced_invocations_usage", "lambda_traced_invocations_percentage", "mobile_app_testing_percentage", "mobile_app_testing_usage", "ndm_netflow_usage", "ndm_netflow_percentage", "npm_host_usage", "npm_host_percentage", "obs_pipeline_bytes_usage", "obs_pipeline_bytes_percentage", "obs_pipelines_vcpu_usage", "obs_pipelines_vcpu_percentage", "online_archive_usage", "online_archive_percentage", "profiled_container_usage", "profiled_container_percentage", "profiled_fargate_usage", "profiled_fargate_percentage", "profiled_host_usage", "profiled_host_percentage", "serverless_apps_usage", "serverless_apps_percentage", "snmp_usage", "snmp_percentage", "estimated_rum_sessions_usage", "estimated_rum_sessions_percentage", "universal_service_monitoring_usage", "universal_service_monitoring_percentage", "vuln_management_hosts_usage", "vuln_management_hosts_percentage", "sds_scanned_bytes_usage", "sds_scanned_bytes_percentage", "ci_test_indexed_spans_usage", "ci_test_indexed_spans_percentage", "ingested_logs_bytes_usage", "ingested_logs_bytes_percentage", "ci_pipeline_indexed_spans_usage", "ci_pipeline_indexed_spans_percentage", "indexed_spans_usage", "indexed_spans_percentage", "custom_event_usage", "custom_event_percentage", "logs_indexed_custom_retention_usage", "logs_indexed_custom_retention_percentage", "logs_indexed_360day_usage", "logs_indexed_360day_percentage", "logs_indexed_180day_usage", "logs_indexed_180day_percentage", "logs_indexed_90day_usage", "logs_indexed_90day_percentage", "logs_indexed_60day_usage", "logs_indexed_60day_percentage", "logs_indexed_45day_usage", "logs_indexed_45day_percentage", "logs_indexed_30day_usage", "logs_indexed_30day_percentage", "logs_indexed_15day_usage", "logs_indexed_15day_percentage", "logs_indexed_7day_usage", "logs_indexed_7day_percentage", "logs_indexed_3day_usage", "logs_indexed_3day_percentage", "logs_indexed_1day_usage", "logs_indexed_1day_percentage", "rum_replay_sessions_usage", "rum_replay_sessions_percentage", "rum_browser_mobile_sessions_usage", "rum_browser_mobile_sessions_percentage", "ingested_spans_bytes_usage", "ingested_spans_bytes_percentage", "siem_ingested_bytes_usage", "siem_ingested_bytes_percentage", "workflow_executions_usage", "workflow_executions_percentage", "*"].
    :type value: str
    """

    allowed_values = {
        "api_usage",
        "api_percentage",
        "apm_fargate_usage",
        "apm_fargate_percentage",
        "appsec_fargate_usage",
        "appsec_fargate_percentage",
        "apm_host_usage",
        "apm_host_percentage",
        "apm_usm_usage",
        "apm_usm_percentage",
        "appsec_usage",
        "appsec_percentage",
        "asm_serverless_traced_invocations_usage",
        "asm_serverless_traced_invocations_percentage",
        "browser_usage",
        "browser_percentage",
        "ci_visibility_itr_usage",
        "ci_visibility_itr_percentage",
        "cloud_siem_usage",
        "cloud_siem_percentage",
        "container_excl_agent_usage",
        "container_excl_agent_percentage",
        "container_usage",
        "container_percentage",
        "cspm_containers_percentage",
        "cspm_containers_usage",
        "cspm_hosts_percentage",
        "cspm_hosts_usage",
        "custom_timeseries_usage",
        "custom_timeseries_percentage",
        "custom_ingested_timeseries_usage",
        "custom_ingested_timeseries_percentage",
        "cws_containers_percentage",
        "cws_containers_usage",
        "cws_hosts_percentage",
        "cws_hosts_usage",
        "dbm_hosts_percentage",
        "dbm_hosts_usage",
        "dbm_queries_percentage",
        "dbm_queries_usage",
        "error_tracking_usage",
        "error_tracking_percentage",
        "estimated_indexed_logs_usage",
        "estimated_indexed_logs_percentage",
        "estimated_ingested_logs_usage",
        "estimated_ingested_logs_percentage",
        "estimated_indexed_spans_usage",
        "estimated_indexed_spans_percentage",
        "estimated_ingested_spans_usage",
        "estimated_ingested_spans_percentage",
        "fargate_usage",
        "fargate_percentage",
        "functions_usage",
        "functions_percentage",
        "incident_management_monthly_active_users_usage",
        "incident_management_monthly_active_users_percentage",
        "infra_host_usage",
        "infra_host_percentage",
        "invocations_usage",
        "invocations_percentage",
        "lambda_traced_invocations_usage",
        "lambda_traced_invocations_percentage",
        "mobile_app_testing_percentage",
        "mobile_app_testing_usage",
        "ndm_netflow_usage",
        "ndm_netflow_percentage",
        "npm_host_usage",
        "npm_host_percentage",
        "obs_pipeline_bytes_usage",
        "obs_pipeline_bytes_percentage",
        "obs_pipelines_vcpu_usage",
        "obs_pipelines_vcpu_percentage",
        "online_archive_usage",
        "online_archive_percentage",
        "profiled_container_usage",
        "profiled_container_percentage",
        "profiled_fargate_usage",
        "profiled_fargate_percentage",
        "profiled_host_usage",
        "profiled_host_percentage",
        "serverless_apps_usage",
        "serverless_apps_percentage",
        "snmp_usage",
        "snmp_percentage",
        "estimated_rum_sessions_usage",
        "estimated_rum_sessions_percentage",
        "universal_service_monitoring_usage",
        "universal_service_monitoring_percentage",
        "vuln_management_hosts_usage",
        "vuln_management_hosts_percentage",
        "sds_scanned_bytes_usage",
        "sds_scanned_bytes_percentage",
        "ci_test_indexed_spans_usage",
        "ci_test_indexed_spans_percentage",
        "ingested_logs_bytes_usage",
        "ingested_logs_bytes_percentage",
        "ci_pipeline_indexed_spans_usage",
        "ci_pipeline_indexed_spans_percentage",
        "indexed_spans_usage",
        "indexed_spans_percentage",
        "custom_event_usage",
        "custom_event_percentage",
        "logs_indexed_custom_retention_usage",
        "logs_indexed_custom_retention_percentage",
        "logs_indexed_360day_usage",
        "logs_indexed_360day_percentage",
        "logs_indexed_180day_usage",
        "logs_indexed_180day_percentage",
        "logs_indexed_90day_usage",
        "logs_indexed_90day_percentage",
        "logs_indexed_60day_usage",
        "logs_indexed_60day_percentage",
        "logs_indexed_45day_usage",
        "logs_indexed_45day_percentage",
        "logs_indexed_30day_usage",
        "logs_indexed_30day_percentage",
        "logs_indexed_15day_usage",
        "logs_indexed_15day_percentage",
        "logs_indexed_7day_usage",
        "logs_indexed_7day_percentage",
        "logs_indexed_3day_usage",
        "logs_indexed_3day_percentage",
        "logs_indexed_1day_usage",
        "logs_indexed_1day_percentage",
        "rum_replay_sessions_usage",
        "rum_replay_sessions_percentage",
        "rum_browser_mobile_sessions_usage",
        "rum_browser_mobile_sessions_percentage",
        "ingested_spans_bytes_usage",
        "ingested_spans_bytes_percentage",
        "siem_ingested_bytes_usage",
        "siem_ingested_bytes_percentage",
        "workflow_executions_usage",
        "workflow_executions_percentage",
        "*",
    }
    API_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    API_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APM_FARGATE_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APM_FARGATE_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APPSEC_FARGATE_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APPSEC_FARGATE_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APM_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APM_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APM_USM_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APM_USM_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APPSEC_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APPSEC_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ASM_SERVERLESS_TRACED_INVOCATIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ASM_SERVERLESS_TRACED_INVOCATIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    BROWSER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    BROWSER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_VISIBILITY_ITR_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_VISIBILITY_ITR_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CLOUD_SIEM_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CLOUD_SIEM_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONTAINER_EXCL_AGENT_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONTAINER_EXCL_AGENT_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONTAINER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONTAINER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_CONTAINERS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_CONTAINERS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_HOSTS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_HOSTS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_TIMESERIES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_TIMESERIES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_INGESTED_TIMESERIES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_INGESTED_TIMESERIES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CWS_CONTAINERS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CWS_CONTAINERS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CWS_HOSTS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CWS_HOSTS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    DBM_HOSTS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    DBM_HOSTS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    DBM_QUERIES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    DBM_QUERIES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ERROR_TRACKING_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ERROR_TRACKING_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INDEXED_LOGS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INDEXED_LOGS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INGESTED_LOGS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INGESTED_LOGS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INDEXED_SPANS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INDEXED_SPANS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INGESTED_SPANS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_INGESTED_SPANS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    FARGATE_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    FARGATE_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    FUNCTIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    FUNCTIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INCIDENT_MANAGEMENT_MONTHLY_ACTIVE_USERS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INCIDENT_MANAGEMENT_MONTHLY_ACTIVE_USERS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INFRA_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INFRA_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INVOCATIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INVOCATIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LAMBDA_TRACED_INVOCATIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LAMBDA_TRACED_INVOCATIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    MOBILE_APP_TESTING_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    MOBILE_APP_TESTING_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NDM_NETFLOW_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NDM_NETFLOW_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NPM_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NPM_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    OBS_PIPELINE_BYTES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    OBS_PIPELINE_BYTES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    OBS_PIPELINES_VCPU_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    OBS_PIPELINES_VCPU_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ONLINE_ARCHIVE_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ONLINE_ARCHIVE_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_CONTAINER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_CONTAINER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_FARGATE_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_FARGATE_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SERVERLESS_APPS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SERVERLESS_APPS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SNMP_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SNMP_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_RUM_SESSIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_RUM_SESSIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    UNIVERSAL_SERVICE_MONITORING_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    UNIVERSAL_SERVICE_MONITORING_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    VULN_MANAGEMENT_HOSTS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    VULN_MANAGEMENT_HOSTS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SDS_SCANNED_BYTES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SDS_SCANNED_BYTES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_TEST_INDEXED_SPANS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_TEST_INDEXED_SPANS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INGESTED_LOGS_BYTES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INGESTED_LOGS_BYTES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_PIPELINE_INDEXED_SPANS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_PIPELINE_INDEXED_SPANS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INDEXED_SPANS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INDEXED_SPANS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_EVENT_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_EVENT_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_CUSTOM_RETENTION_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_CUSTOM_RETENTION_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_360DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_360DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_180DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_180DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_90DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_90DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_60DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_60DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_45DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_45DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_30DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_30DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_15DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_15DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_7DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_7DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_3DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_3DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_1DAY_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    LOGS_INDEXED_1DAY_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    RUM_REPLAY_SESSIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    RUM_REPLAY_SESSIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    RUM_BROWSER_MOBILE_SESSIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    RUM_BROWSER_MOBILE_SESSIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INGESTED_SPANS_BYTES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INGESTED_SPANS_BYTES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SIEM_INGESTED_BYTES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SIEM_INGESTED_BYTES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    WORKFLOW_EXECUTIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    WORKFLOW_EXECUTIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ALL: ClassVar["MonthlyUsageAttributionSupportedMetrics"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonthlyUsageAttributionSupportedMetrics.API_USAGE = MonthlyUsageAttributionSupportedMetrics("api_usage")
MonthlyUsageAttributionSupportedMetrics.API_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics("api_percentage")
MonthlyUsageAttributionSupportedMetrics.APM_FARGATE_USAGE = MonthlyUsageAttributionSupportedMetrics("apm_fargate_usage")
MonthlyUsageAttributionSupportedMetrics.APM_FARGATE_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "apm_fargate_percentage"
)
MonthlyUsageAttributionSupportedMetrics.APPSEC_FARGATE_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "appsec_fargate_usage"
)
MonthlyUsageAttributionSupportedMetrics.APPSEC_FARGATE_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "appsec_fargate_percentage"
)
MonthlyUsageAttributionSupportedMetrics.APM_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics("apm_host_usage")
MonthlyUsageAttributionSupportedMetrics.APM_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "apm_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.APM_USM_USAGE = MonthlyUsageAttributionSupportedMetrics("apm_usm_usage")
MonthlyUsageAttributionSupportedMetrics.APM_USM_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "apm_usm_percentage"
)
MonthlyUsageAttributionSupportedMetrics.APPSEC_USAGE = MonthlyUsageAttributionSupportedMetrics("appsec_usage")
MonthlyUsageAttributionSupportedMetrics.APPSEC_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics("appsec_percentage")
MonthlyUsageAttributionSupportedMetrics.ASM_SERVERLESS_TRACED_INVOCATIONS_USAGE = (
    MonthlyUsageAttributionSupportedMetrics("asm_serverless_traced_invocations_usage")
)
MonthlyUsageAttributionSupportedMetrics.ASM_SERVERLESS_TRACED_INVOCATIONS_PERCENTAGE = (
    MonthlyUsageAttributionSupportedMetrics("asm_serverless_traced_invocations_percentage")
)
MonthlyUsageAttributionSupportedMetrics.BROWSER_USAGE = MonthlyUsageAttributionSupportedMetrics("browser_usage")
MonthlyUsageAttributionSupportedMetrics.BROWSER_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "browser_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CI_VISIBILITY_ITR_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "ci_visibility_itr_usage"
)
MonthlyUsageAttributionSupportedMetrics.CI_VISIBILITY_ITR_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "ci_visibility_itr_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CLOUD_SIEM_USAGE = MonthlyUsageAttributionSupportedMetrics("cloud_siem_usage")
MonthlyUsageAttributionSupportedMetrics.CLOUD_SIEM_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "cloud_siem_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CONTAINER_EXCL_AGENT_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "container_excl_agent_usage"
)
MonthlyUsageAttributionSupportedMetrics.CONTAINER_EXCL_AGENT_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "container_excl_agent_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CONTAINER_USAGE = MonthlyUsageAttributionSupportedMetrics("container_usage")
MonthlyUsageAttributionSupportedMetrics.CONTAINER_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "container_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CSPM_CONTAINERS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "cspm_containers_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CSPM_CONTAINERS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "cspm_containers_usage"
)
MonthlyUsageAttributionSupportedMetrics.CSPM_HOSTS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "cspm_hosts_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CSPM_HOSTS_USAGE = MonthlyUsageAttributionSupportedMetrics("cspm_hosts_usage")
MonthlyUsageAttributionSupportedMetrics.CUSTOM_TIMESERIES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "custom_timeseries_usage"
)
MonthlyUsageAttributionSupportedMetrics.CUSTOM_TIMESERIES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "custom_timeseries_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CUSTOM_INGESTED_TIMESERIES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "custom_ingested_timeseries_usage"
)
MonthlyUsageAttributionSupportedMetrics.CUSTOM_INGESTED_TIMESERIES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "custom_ingested_timeseries_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CWS_CONTAINERS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "cws_containers_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CWS_CONTAINERS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "cws_containers_usage"
)
MonthlyUsageAttributionSupportedMetrics.CWS_HOSTS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "cws_hosts_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CWS_HOSTS_USAGE = MonthlyUsageAttributionSupportedMetrics("cws_hosts_usage")
MonthlyUsageAttributionSupportedMetrics.DBM_HOSTS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "dbm_hosts_percentage"
)
MonthlyUsageAttributionSupportedMetrics.DBM_HOSTS_USAGE = MonthlyUsageAttributionSupportedMetrics("dbm_hosts_usage")
MonthlyUsageAttributionSupportedMetrics.DBM_QUERIES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "dbm_queries_percentage"
)
MonthlyUsageAttributionSupportedMetrics.DBM_QUERIES_USAGE = MonthlyUsageAttributionSupportedMetrics("dbm_queries_usage")
MonthlyUsageAttributionSupportedMetrics.ERROR_TRACKING_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "error_tracking_usage"
)
MonthlyUsageAttributionSupportedMetrics.ERROR_TRACKING_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "error_tracking_percentage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INDEXED_LOGS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_indexed_logs_usage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INDEXED_LOGS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_indexed_logs_percentage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INGESTED_LOGS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_ingested_logs_usage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INGESTED_LOGS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_ingested_logs_percentage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INDEXED_SPANS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_indexed_spans_usage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INDEXED_SPANS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_indexed_spans_percentage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INGESTED_SPANS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_ingested_spans_usage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_INGESTED_SPANS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_ingested_spans_percentage"
)
MonthlyUsageAttributionSupportedMetrics.FARGATE_USAGE = MonthlyUsageAttributionSupportedMetrics("fargate_usage")
MonthlyUsageAttributionSupportedMetrics.FARGATE_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "fargate_percentage"
)
MonthlyUsageAttributionSupportedMetrics.FUNCTIONS_USAGE = MonthlyUsageAttributionSupportedMetrics("functions_usage")
MonthlyUsageAttributionSupportedMetrics.FUNCTIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "functions_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INCIDENT_MANAGEMENT_MONTHLY_ACTIVE_USERS_USAGE = (
    MonthlyUsageAttributionSupportedMetrics("incident_management_monthly_active_users_usage")
)
MonthlyUsageAttributionSupportedMetrics.INCIDENT_MANAGEMENT_MONTHLY_ACTIVE_USERS_PERCENTAGE = (
    MonthlyUsageAttributionSupportedMetrics("incident_management_monthly_active_users_percentage")
)
MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics("infra_host_usage")
MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "infra_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INVOCATIONS_USAGE = MonthlyUsageAttributionSupportedMetrics("invocations_usage")
MonthlyUsageAttributionSupportedMetrics.INVOCATIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "invocations_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LAMBDA_TRACED_INVOCATIONS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "lambda_traced_invocations_usage"
)
MonthlyUsageAttributionSupportedMetrics.LAMBDA_TRACED_INVOCATIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "lambda_traced_invocations_percentage"
)
MonthlyUsageAttributionSupportedMetrics.MOBILE_APP_TESTING_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "mobile_app_testing_percentage"
)
MonthlyUsageAttributionSupportedMetrics.MOBILE_APP_TESTING_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "mobile_app_testing_usage"
)
MonthlyUsageAttributionSupportedMetrics.NDM_NETFLOW_USAGE = MonthlyUsageAttributionSupportedMetrics("ndm_netflow_usage")
MonthlyUsageAttributionSupportedMetrics.NDM_NETFLOW_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "ndm_netflow_percentage"
)
MonthlyUsageAttributionSupportedMetrics.NPM_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics("npm_host_usage")
MonthlyUsageAttributionSupportedMetrics.NPM_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "npm_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.OBS_PIPELINE_BYTES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "obs_pipeline_bytes_usage"
)
MonthlyUsageAttributionSupportedMetrics.OBS_PIPELINE_BYTES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "obs_pipeline_bytes_percentage"
)
MonthlyUsageAttributionSupportedMetrics.OBS_PIPELINES_VCPU_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "obs_pipelines_vcpu_usage"
)
MonthlyUsageAttributionSupportedMetrics.OBS_PIPELINES_VCPU_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "obs_pipelines_vcpu_percentage"
)
MonthlyUsageAttributionSupportedMetrics.ONLINE_ARCHIVE_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "online_archive_usage"
)
MonthlyUsageAttributionSupportedMetrics.ONLINE_ARCHIVE_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "online_archive_percentage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_CONTAINER_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_container_usage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_CONTAINER_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_container_percentage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_FARGATE_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_fargate_usage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_FARGATE_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_fargate_percentage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_host_usage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.SERVERLESS_APPS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "serverless_apps_usage"
)
MonthlyUsageAttributionSupportedMetrics.SERVERLESS_APPS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "serverless_apps_percentage"
)
MonthlyUsageAttributionSupportedMetrics.SNMP_USAGE = MonthlyUsageAttributionSupportedMetrics("snmp_usage")
MonthlyUsageAttributionSupportedMetrics.SNMP_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics("snmp_percentage")
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_RUM_SESSIONS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_rum_sessions_usage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_RUM_SESSIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_rum_sessions_percentage"
)
MonthlyUsageAttributionSupportedMetrics.UNIVERSAL_SERVICE_MONITORING_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "universal_service_monitoring_usage"
)
MonthlyUsageAttributionSupportedMetrics.UNIVERSAL_SERVICE_MONITORING_PERCENTAGE = (
    MonthlyUsageAttributionSupportedMetrics("universal_service_monitoring_percentage")
)
MonthlyUsageAttributionSupportedMetrics.VULN_MANAGEMENT_HOSTS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "vuln_management_hosts_usage"
)
MonthlyUsageAttributionSupportedMetrics.VULN_MANAGEMENT_HOSTS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "vuln_management_hosts_percentage"
)
MonthlyUsageAttributionSupportedMetrics.SDS_SCANNED_BYTES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "sds_scanned_bytes_usage"
)
MonthlyUsageAttributionSupportedMetrics.SDS_SCANNED_BYTES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "sds_scanned_bytes_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CI_TEST_INDEXED_SPANS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "ci_test_indexed_spans_usage"
)
MonthlyUsageAttributionSupportedMetrics.CI_TEST_INDEXED_SPANS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "ci_test_indexed_spans_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INGESTED_LOGS_BYTES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "ingested_logs_bytes_usage"
)
MonthlyUsageAttributionSupportedMetrics.INGESTED_LOGS_BYTES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "ingested_logs_bytes_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CI_PIPELINE_INDEXED_SPANS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "ci_pipeline_indexed_spans_usage"
)
MonthlyUsageAttributionSupportedMetrics.CI_PIPELINE_INDEXED_SPANS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "ci_pipeline_indexed_spans_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INDEXED_SPANS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "indexed_spans_usage"
)
MonthlyUsageAttributionSupportedMetrics.INDEXED_SPANS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "indexed_spans_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CUSTOM_EVENT_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "custom_event_usage"
)
MonthlyUsageAttributionSupportedMetrics.CUSTOM_EVENT_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "custom_event_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_CUSTOM_RETENTION_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_custom_retention_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_CUSTOM_RETENTION_PERCENTAGE = (
    MonthlyUsageAttributionSupportedMetrics("logs_indexed_custom_retention_percentage")
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_360DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_360day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_360DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_360day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_180DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_180day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_180DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_180day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_90DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_90day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_90DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_90day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_60DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_60day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_60DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_60day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_45DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_45day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_45DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_45day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_30DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_30day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_30DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_30day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_15DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_15day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_15DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_15day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_7DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_7day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_7DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_7day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_3DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_3day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_3DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_3day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_1DAY_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_1day_usage"
)
MonthlyUsageAttributionSupportedMetrics.LOGS_INDEXED_1DAY_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "logs_indexed_1day_percentage"
)
MonthlyUsageAttributionSupportedMetrics.RUM_REPLAY_SESSIONS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "rum_replay_sessions_usage"
)
MonthlyUsageAttributionSupportedMetrics.RUM_REPLAY_SESSIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "rum_replay_sessions_percentage"
)
MonthlyUsageAttributionSupportedMetrics.RUM_BROWSER_MOBILE_SESSIONS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "rum_browser_mobile_sessions_usage"
)
MonthlyUsageAttributionSupportedMetrics.RUM_BROWSER_MOBILE_SESSIONS_PERCENTAGE = (
    MonthlyUsageAttributionSupportedMetrics("rum_browser_mobile_sessions_percentage")
)
MonthlyUsageAttributionSupportedMetrics.INGESTED_SPANS_BYTES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "ingested_spans_bytes_usage"
)
MonthlyUsageAttributionSupportedMetrics.INGESTED_SPANS_BYTES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "ingested_spans_bytes_percentage"
)
MonthlyUsageAttributionSupportedMetrics.SIEM_INGESTED_BYTES_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "siem_ingested_bytes_usage"
)
MonthlyUsageAttributionSupportedMetrics.SIEM_INGESTED_BYTES_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "siem_ingested_bytes_percentage"
)
MonthlyUsageAttributionSupportedMetrics.WORKFLOW_EXECUTIONS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "workflow_executions_usage"
)
MonthlyUsageAttributionSupportedMetrics.WORKFLOW_EXECUTIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "workflow_executions_percentage"
)
MonthlyUsageAttributionSupportedMetrics.ALL = MonthlyUsageAttributionSupportedMetrics("*")
