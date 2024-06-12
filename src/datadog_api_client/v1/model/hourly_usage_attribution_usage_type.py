# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HourlyUsageAttributionUsageType(ModelSimple):
    """
    Supported products for hourly usage attribution requests.

    :param value: Must be one of ["api_usage", "apm_fargate_usage", "apm_host_usage", "apm_usm_usage", "appsec_fargate_usage", "appsec_usage", "asm_serverless_traced_invocations_usage", "asm_serverless_traced_invocations_percentage", "browser_usage", "ci_pipeline_indexed_spans_usage", "ci_test_indexed_spans_usage", "ci_visibility_itr_usage", "cloud_siem_usage", "container_excl_agent_usage", "container_usage", "cspm_containers_usage", "cspm_hosts_usage", "custom_event_usage", "custom_ingested_timeseries_usage", "custom_timeseries_usage", "cws_containers_usage", "cws_hosts_usage", "dbm_hosts_usage", "dbm_queries_usage", "error_tracking_usage", "error_tracking_percentage", "estimated_indexed_logs_usage", "estimated_indexed_spans_usage", "estimated_ingested_logs_usage", "estimated_ingested_spans_usage", "estimated_rum_sessions_usage", "fargate_usage", "functions_usage", "incident_management_monthly_active_users_usage", "indexed_spans_usage", "infra_host_usage", "ingested_logs_bytes_usage", "ingested_spans_bytes_usage", "invocations_usage", "lambda_traced_invocations_usage", "logs_indexed_15day_usage", "logs_indexed_180day_usage", "logs_indexed_1day_usage", "logs_indexed_30day_usage", "logs_indexed_360day_usage", "logs_indexed_3day_usage", "logs_indexed_45day_usage", "logs_indexed_60day_usage", "logs_indexed_7day_usage", "logs_indexed_90day_usage", "logs_indexed_custom_retention_usage", "mobile_app_testing_usage", "ndm_netflow_usage", "npm_host_usage", "obs_pipeline_bytes_usage", "obs_pipelines_vcpu_usage", "online_archive_usage", "profiled_container_usage", "profiled_fargate_usage", "profiled_host_usage", "rum_browser_mobile_sessions_usage", "rum_replay_sessions_usage", "sds_scanned_bytes_usage", "serverless_apps_usage", "siem_ingested_bytes_usage", "snmp_usage", "universal_service_monitoring_usage", "vuln_management_hosts_usage", "workflow_executions_usage"].
    :type value: str
    """

    allowed_values = {
        "api_usage",
        "apm_fargate_usage",
        "apm_host_usage",
        "apm_usm_usage",
        "appsec_fargate_usage",
        "appsec_usage",
        "asm_serverless_traced_invocations_usage",
        "asm_serverless_traced_invocations_percentage",
        "browser_usage",
        "ci_pipeline_indexed_spans_usage",
        "ci_test_indexed_spans_usage",
        "ci_visibility_itr_usage",
        "cloud_siem_usage",
        "container_excl_agent_usage",
        "container_usage",
        "cspm_containers_usage",
        "cspm_hosts_usage",
        "custom_event_usage",
        "custom_ingested_timeseries_usage",
        "custom_timeseries_usage",
        "cws_containers_usage",
        "cws_hosts_usage",
        "dbm_hosts_usage",
        "dbm_queries_usage",
        "error_tracking_usage",
        "error_tracking_percentage",
        "estimated_indexed_logs_usage",
        "estimated_indexed_spans_usage",
        "estimated_ingested_logs_usage",
        "estimated_ingested_spans_usage",
        "estimated_rum_sessions_usage",
        "fargate_usage",
        "functions_usage",
        "incident_management_monthly_active_users_usage",
        "indexed_spans_usage",
        "infra_host_usage",
        "ingested_logs_bytes_usage",
        "ingested_spans_bytes_usage",
        "invocations_usage",
        "lambda_traced_invocations_usage",
        "logs_indexed_15day_usage",
        "logs_indexed_180day_usage",
        "logs_indexed_1day_usage",
        "logs_indexed_30day_usage",
        "logs_indexed_360day_usage",
        "logs_indexed_3day_usage",
        "logs_indexed_45day_usage",
        "logs_indexed_60day_usage",
        "logs_indexed_7day_usage",
        "logs_indexed_90day_usage",
        "logs_indexed_custom_retention_usage",
        "mobile_app_testing_usage",
        "ndm_netflow_usage",
        "npm_host_usage",
        "obs_pipeline_bytes_usage",
        "obs_pipelines_vcpu_usage",
        "online_archive_usage",
        "profiled_container_usage",
        "profiled_fargate_usage",
        "profiled_host_usage",
        "rum_browser_mobile_sessions_usage",
        "rum_replay_sessions_usage",
        "sds_scanned_bytes_usage",
        "serverless_apps_usage",
        "siem_ingested_bytes_usage",
        "snmp_usage",
        "universal_service_monitoring_usage",
        "vuln_management_hosts_usage",
        "workflow_executions_usage",
    }
    API_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APM_FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APM_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APM_USM_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APPSEC_FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APPSEC_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ASM_SERVERLESS_TRACED_INVOCATIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ASM_SERVERLESS_TRACED_INVOCATIONS_PERCENTAGE: ClassVar["HourlyUsageAttributionUsageType"]
    BROWSER_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CI_PIPELINE_INDEXED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CI_TEST_INDEXED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CI_VISIBILITY_ITR_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CLOUD_SIEM_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CONTAINER_EXCL_AGENT_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CONTAINER_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CSPM_CONTAINERS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CSPM_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CUSTOM_EVENT_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CUSTOM_INGESTED_TIMESERIES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CUSTOM_TIMESERIES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CWS_CONTAINERS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CWS_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    DBM_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    DBM_QUERIES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ERROR_TRACKING_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ERROR_TRACKING_PERCENTAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INDEXED_LOGS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INDEXED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INGESTED_LOGS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INGESTED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_RUM_SESSIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    FUNCTIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INCIDENT_MANAGEMENT_MONTHLY_ACTIVE_USERS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INDEXED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INFRA_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INGESTED_LOGS_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INGESTED_SPANS_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INVOCATIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LAMBDA_TRACED_INVOCATIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_15DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_180DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_1DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_30DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_360DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_3DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_45DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_60DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_7DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_90DAY_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    LOGS_INDEXED_CUSTOM_RETENTION_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    MOBILE_APP_TESTING_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    NDM_NETFLOW_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    NPM_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    OBS_PIPELINE_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    OBS_PIPELINE_VCPU_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ONLINE_ARCHIVE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    PROFILED_CONTAINER_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    PROFILED_FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    PROFILED_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    RUM_BROWSER_MOBILE_SESSIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    RUM_REPLAY_SESSIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SDS_SCANNED_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SERVERLESS_APPS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SIEM_INGESTED_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SNMP_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    UNIVERSAL_SERVICE_MONITORING_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    VULN_MANAGEMENT_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    WORKFLOW_EXECUTIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HourlyUsageAttributionUsageType.API_USAGE = HourlyUsageAttributionUsageType("api_usage")
HourlyUsageAttributionUsageType.APM_FARGATE_USAGE = HourlyUsageAttributionUsageType("apm_fargate_usage")
HourlyUsageAttributionUsageType.APM_HOST_USAGE = HourlyUsageAttributionUsageType("apm_host_usage")
HourlyUsageAttributionUsageType.APM_USM_USAGE = HourlyUsageAttributionUsageType("apm_usm_usage")
HourlyUsageAttributionUsageType.APPSEC_FARGATE_USAGE = HourlyUsageAttributionUsageType("appsec_fargate_usage")
HourlyUsageAttributionUsageType.APPSEC_USAGE = HourlyUsageAttributionUsageType("appsec_usage")
HourlyUsageAttributionUsageType.ASM_SERVERLESS_TRACED_INVOCATIONS_USAGE = HourlyUsageAttributionUsageType(
    "asm_serverless_traced_invocations_usage"
)
HourlyUsageAttributionUsageType.ASM_SERVERLESS_TRACED_INVOCATIONS_PERCENTAGE = HourlyUsageAttributionUsageType(
    "asm_serverless_traced_invocations_percentage"
)
HourlyUsageAttributionUsageType.BROWSER_USAGE = HourlyUsageAttributionUsageType("browser_usage")
HourlyUsageAttributionUsageType.CI_PIPELINE_INDEXED_SPANS_USAGE = HourlyUsageAttributionUsageType(
    "ci_pipeline_indexed_spans_usage"
)
HourlyUsageAttributionUsageType.CI_TEST_INDEXED_SPANS_USAGE = HourlyUsageAttributionUsageType(
    "ci_test_indexed_spans_usage"
)
HourlyUsageAttributionUsageType.CI_VISIBILITY_ITR_USAGE = HourlyUsageAttributionUsageType("ci_visibility_itr_usage")
HourlyUsageAttributionUsageType.CLOUD_SIEM_USAGE = HourlyUsageAttributionUsageType("cloud_siem_usage")
HourlyUsageAttributionUsageType.CONTAINER_EXCL_AGENT_USAGE = HourlyUsageAttributionUsageType(
    "container_excl_agent_usage"
)
HourlyUsageAttributionUsageType.CONTAINER_USAGE = HourlyUsageAttributionUsageType("container_usage")
HourlyUsageAttributionUsageType.CSPM_CONTAINERS_USAGE = HourlyUsageAttributionUsageType("cspm_containers_usage")
HourlyUsageAttributionUsageType.CSPM_HOSTS_USAGE = HourlyUsageAttributionUsageType("cspm_hosts_usage")
HourlyUsageAttributionUsageType.CUSTOM_EVENT_USAGE = HourlyUsageAttributionUsageType("custom_event_usage")
HourlyUsageAttributionUsageType.CUSTOM_INGESTED_TIMESERIES_USAGE = HourlyUsageAttributionUsageType(
    "custom_ingested_timeseries_usage"
)
HourlyUsageAttributionUsageType.CUSTOM_TIMESERIES_USAGE = HourlyUsageAttributionUsageType("custom_timeseries_usage")
HourlyUsageAttributionUsageType.CWS_CONTAINERS_USAGE = HourlyUsageAttributionUsageType("cws_containers_usage")
HourlyUsageAttributionUsageType.CWS_HOSTS_USAGE = HourlyUsageAttributionUsageType("cws_hosts_usage")
HourlyUsageAttributionUsageType.DBM_HOSTS_USAGE = HourlyUsageAttributionUsageType("dbm_hosts_usage")
HourlyUsageAttributionUsageType.DBM_QUERIES_USAGE = HourlyUsageAttributionUsageType("dbm_queries_usage")
HourlyUsageAttributionUsageType.ERROR_TRACKING_USAGE = HourlyUsageAttributionUsageType("error_tracking_usage")
HourlyUsageAttributionUsageType.ERROR_TRACKING_PERCENTAGE = HourlyUsageAttributionUsageType("error_tracking_percentage")
HourlyUsageAttributionUsageType.ESTIMATED_INDEXED_LOGS_USAGE = HourlyUsageAttributionUsageType(
    "estimated_indexed_logs_usage"
)
HourlyUsageAttributionUsageType.ESTIMATED_INDEXED_SPANS_USAGE = HourlyUsageAttributionUsageType(
    "estimated_indexed_spans_usage"
)
HourlyUsageAttributionUsageType.ESTIMATED_INGESTED_LOGS_USAGE = HourlyUsageAttributionUsageType(
    "estimated_ingested_logs_usage"
)
HourlyUsageAttributionUsageType.ESTIMATED_INGESTED_SPANS_USAGE = HourlyUsageAttributionUsageType(
    "estimated_ingested_spans_usage"
)
HourlyUsageAttributionUsageType.ESTIMATED_RUM_SESSIONS_USAGE = HourlyUsageAttributionUsageType(
    "estimated_rum_sessions_usage"
)
HourlyUsageAttributionUsageType.FARGATE_USAGE = HourlyUsageAttributionUsageType("fargate_usage")
HourlyUsageAttributionUsageType.FUNCTIONS_USAGE = HourlyUsageAttributionUsageType("functions_usage")
HourlyUsageAttributionUsageType.INCIDENT_MANAGEMENT_MONTHLY_ACTIVE_USERS_USAGE = HourlyUsageAttributionUsageType(
    "incident_management_monthly_active_users_usage"
)
HourlyUsageAttributionUsageType.INDEXED_SPANS_USAGE = HourlyUsageAttributionUsageType("indexed_spans_usage")
HourlyUsageAttributionUsageType.INFRA_HOST_USAGE = HourlyUsageAttributionUsageType("infra_host_usage")
HourlyUsageAttributionUsageType.INGESTED_LOGS_BYTES_USAGE = HourlyUsageAttributionUsageType("ingested_logs_bytes_usage")
HourlyUsageAttributionUsageType.INGESTED_SPANS_BYTES_USAGE = HourlyUsageAttributionUsageType(
    "ingested_spans_bytes_usage"
)
HourlyUsageAttributionUsageType.INVOCATIONS_USAGE = HourlyUsageAttributionUsageType("invocations_usage")
HourlyUsageAttributionUsageType.LAMBDA_TRACED_INVOCATIONS_USAGE = HourlyUsageAttributionUsageType(
    "lambda_traced_invocations_usage"
)
HourlyUsageAttributionUsageType.LOGS_INDEXED_15DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_15day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_180DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_180day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_1DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_1day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_30DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_30day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_360DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_360day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_3DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_3day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_45DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_45day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_60DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_60day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_7DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_7day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_90DAY_USAGE = HourlyUsageAttributionUsageType("logs_indexed_90day_usage")
HourlyUsageAttributionUsageType.LOGS_INDEXED_CUSTOM_RETENTION_USAGE = HourlyUsageAttributionUsageType(
    "logs_indexed_custom_retention_usage"
)
HourlyUsageAttributionUsageType.MOBILE_APP_TESTING_USAGE = HourlyUsageAttributionUsageType("mobile_app_testing_usage")
HourlyUsageAttributionUsageType.NDM_NETFLOW_USAGE = HourlyUsageAttributionUsageType("ndm_netflow_usage")
HourlyUsageAttributionUsageType.NPM_HOST_USAGE = HourlyUsageAttributionUsageType("npm_host_usage")
HourlyUsageAttributionUsageType.OBS_PIPELINE_BYTES_USAGE = HourlyUsageAttributionUsageType("obs_pipeline_bytes_usage")
HourlyUsageAttributionUsageType.OBS_PIPELINE_VCPU_USAGE = HourlyUsageAttributionUsageType("obs_pipelines_vcpu_usage")
HourlyUsageAttributionUsageType.ONLINE_ARCHIVE_USAGE = HourlyUsageAttributionUsageType("online_archive_usage")
HourlyUsageAttributionUsageType.PROFILED_CONTAINER_USAGE = HourlyUsageAttributionUsageType("profiled_container_usage")
HourlyUsageAttributionUsageType.PROFILED_FARGATE_USAGE = HourlyUsageAttributionUsageType("profiled_fargate_usage")
HourlyUsageAttributionUsageType.PROFILED_HOST_USAGE = HourlyUsageAttributionUsageType("profiled_host_usage")
HourlyUsageAttributionUsageType.RUM_BROWSER_MOBILE_SESSIONS_USAGE = HourlyUsageAttributionUsageType(
    "rum_browser_mobile_sessions_usage"
)
HourlyUsageAttributionUsageType.RUM_REPLAY_SESSIONS_USAGE = HourlyUsageAttributionUsageType("rum_replay_sessions_usage")
HourlyUsageAttributionUsageType.SDS_SCANNED_BYTES_USAGE = HourlyUsageAttributionUsageType("sds_scanned_bytes_usage")
HourlyUsageAttributionUsageType.SERVERLESS_APPS_USAGE = HourlyUsageAttributionUsageType("serverless_apps_usage")
HourlyUsageAttributionUsageType.SIEM_INGESTED_BYTES_USAGE = HourlyUsageAttributionUsageType("siem_ingested_bytes_usage")
HourlyUsageAttributionUsageType.SNMP_USAGE = HourlyUsageAttributionUsageType("snmp_usage")
HourlyUsageAttributionUsageType.UNIVERSAL_SERVICE_MONITORING_USAGE = HourlyUsageAttributionUsageType(
    "universal_service_monitoring_usage"
)
HourlyUsageAttributionUsageType.VULN_MANAGEMENT_HOSTS_USAGE = HourlyUsageAttributionUsageType(
    "vuln_management_hosts_usage"
)
HourlyUsageAttributionUsageType.WORKFLOW_EXECUTIONS_USAGE = HourlyUsageAttributionUsageType("workflow_executions_usage")
