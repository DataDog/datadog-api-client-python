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

    :param value: Must be one of ["api_usage", "api_percentage", "apm_fargate_usage", "apm_fargate_percentage", "appsec_fargate_usage", "appsec_fargate_percentage", "apm_host_usage", "apm_host_percentage", "apm_usm_usage", "apm_usm_percentage", "appsec_usage", "appsec_percentage", "browser_usage", "browser_percentage", "ci_visibility_itr_usage", "ci_visibility_itr_percentage", "container_excl_agent_usage", "container_excl_agent_percentage", "container_usage", "container_percentage", "cspm_containers_percentage", "cspm_containers_usage", "cspm_hosts_percentage", "cspm_hosts_usage", "custom_timeseries_usage", "custom_timeseries_percentage", "custom_ingested_timeseries_usage", "custom_ingested_timeseries_percentage", "cws_containers_percentage", "cws_containers_usage", "cws_hosts_percentage", "cws_hosts_usage", "dbm_hosts_percentage", "dbm_hosts_usage", "dbm_queries_percentage", "dbm_queries_usage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "estimated_ingested_logs_usage", "estimated_ingested_logs_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage", "fargate_usage", "fargate_percentage", "functions_usage", "functions_percentage", "infra_host_usage", "infra_host_percentage", "invocations_usage", "invocations_percentage", "mobile_app_testing_percentage", "mobile_app_testing_usage", "ndm_netflow_usage", "ndm_netflow_percentage", "npm_host_usage", "npm_host_percentage", "obs_pipeline_bytes_usage", "obs_pipeline_bytes_percentage", "profiled_container_usage", "profiled_container_percentage", "profiled_fargate_usage", "profiled_fargate_percentage", "profiled_host_usage", "profiled_host_percentage", "serverless_apps_usage", "serverless_apps_percentage", "snmp_usage", "snmp_percentage", "estimated_rum_sessions_usage", "estimated_rum_sessions_percentage", "universal_service_monitoring_usage", "universal_service_monitoring_percentage", "vuln_management_hosts_usage", "vuln_management_hosts_percentage", "sds_scanned_bytes_usage", "sds_scanned_bytes_percentage", "*"].
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
        "browser_usage",
        "browser_percentage",
        "ci_visibility_itr_usage",
        "ci_visibility_itr_percentage",
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
        "infra_host_usage",
        "infra_host_percentage",
        "invocations_usage",
        "invocations_percentage",
        "mobile_app_testing_percentage",
        "mobile_app_testing_usage",
        "ndm_netflow_usage",
        "ndm_netflow_percentage",
        "npm_host_usage",
        "npm_host_percentage",
        "obs_pipeline_bytes_usage",
        "obs_pipeline_bytes_percentage",
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
    BROWSER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    BROWSER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_VISIBILITY_ITR_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CI_VISIBILITY_ITR_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
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
    INFRA_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INFRA_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INVOCATIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INVOCATIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    MOBILE_APP_TESTING_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    MOBILE_APP_TESTING_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NDM_NETFLOW_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NDM_NETFLOW_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NPM_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NPM_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    OBS_PIPELINE_BYTES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    OBS_PIPELINE_BYTES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
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
MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics("infra_host_usage")
MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "infra_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INVOCATIONS_USAGE = MonthlyUsageAttributionSupportedMetrics("invocations_usage")
MonthlyUsageAttributionSupportedMetrics.INVOCATIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "invocations_percentage"
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
MonthlyUsageAttributionSupportedMetrics.ALL = MonthlyUsageAttributionSupportedMetrics("*")
