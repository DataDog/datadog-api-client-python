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

    :param value: Must be one of ["api_usage", "api_percentage", "apm_fargate_usage", "apm_fargate_percentage", "appsec_fargate_usage", "appsec_fargate_percentage", "apm_host_usage", "apm_host_percentage", "appsec_usage", "appsec_percentage", "browser_usage", "browser_percentage", "container_usage", "container_percentage", "cspm_containers_percentage", "cspm_containers_usage", "cspm_hosts_percentage", "cspm_hosts_usage", "custom_timeseries_usage", "custom_timeseries_percentage", "cws_containers_percentage", "cws_containers_usage", "cws_hosts_percentage", "cws_hosts_usage", "dbm_hosts_percentage", "dbm_hosts_usage", "dbm_queries_percentage", "dbm_queries_usage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "estimated_ingested_logs_usage", "estimated_ingested_logs_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage", "fargate_usage", "fargate_percentage", "functions_usage", "functions_percentage", "indexed_logs_usage", "indexed_logs_percentage", "infra_host_usage", "infra_host_percentage", "invocations_usage", "invocations_percentage", "npm_host_usage", "npm_host_percentage", "profiled_container_usage", "profiled_container_percentage", "profiled_host_usage", "profiled_host_percentage", "snmp_usage", "snmp_percentage", "estimated_rum_sessions_usage", "estimated_rum_sessions_percentage", "cont_usage", "cont_percentage", "*"].
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
        "appsec_usage",
        "appsec_percentage",
        "browser_usage",
        "browser_percentage",
        "container_usage",
        "container_percentage",
        "cspm_containers_percentage",
        "cspm_containers_usage",
        "cspm_hosts_percentage",
        "cspm_hosts_usage",
        "custom_timeseries_usage",
        "custom_timeseries_percentage",
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
        "indexed_logs_usage",
        "indexed_logs_percentage",
        "infra_host_usage",
        "infra_host_percentage",
        "invocations_usage",
        "invocations_percentage",
        "npm_host_usage",
        "npm_host_percentage",
        "profiled_container_usage",
        "profiled_container_percentage",
        "profiled_host_usage",
        "profiled_host_percentage",
        "snmp_usage",
        "snmp_percentage",
        "estimated_rum_sessions_usage",
        "estimated_rum_sessions_percentage",
        "cont_usage",
        "cont_percentage",
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
    APPSEC_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    APPSEC_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    BROWSER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    BROWSER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONTAINER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONTAINER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_CONTAINERS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_CONTAINERS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_HOSTS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CSPM_HOSTS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_TIMESERIES_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CUSTOM_TIMESERIES_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
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
    INDEXED_LOGS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INDEXED_LOGS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INFRA_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INFRA_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INVOCATIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    INVOCATIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NPM_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    NPM_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_CONTAINER_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_CONTAINER_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_HOST_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    PROFILED_HOST_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SNMP_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    SNMP_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_RUM_SESSIONS_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    ESTIMATED_RUM_SESSIONS_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONT_USAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
    CONT_PERCENTAGE: ClassVar["MonthlyUsageAttributionSupportedMetrics"]
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
MonthlyUsageAttributionSupportedMetrics.APPSEC_USAGE = MonthlyUsageAttributionSupportedMetrics("appsec_usage")
MonthlyUsageAttributionSupportedMetrics.APPSEC_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics("appsec_percentage")
MonthlyUsageAttributionSupportedMetrics.BROWSER_USAGE = MonthlyUsageAttributionSupportedMetrics("browser_usage")
MonthlyUsageAttributionSupportedMetrics.BROWSER_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "browser_percentage"
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
MonthlyUsageAttributionSupportedMetrics.INDEXED_LOGS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "indexed_logs_usage"
)
MonthlyUsageAttributionSupportedMetrics.INDEXED_LOGS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "indexed_logs_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics("infra_host_usage")
MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "infra_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.INVOCATIONS_USAGE = MonthlyUsageAttributionSupportedMetrics("invocations_usage")
MonthlyUsageAttributionSupportedMetrics.INVOCATIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "invocations_percentage"
)
MonthlyUsageAttributionSupportedMetrics.NPM_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics("npm_host_usage")
MonthlyUsageAttributionSupportedMetrics.NPM_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "npm_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_CONTAINER_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_container_usage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_CONTAINER_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_container_percentage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_HOST_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_host_usage"
)
MonthlyUsageAttributionSupportedMetrics.PROFILED_HOST_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "profiled_host_percentage"
)
MonthlyUsageAttributionSupportedMetrics.SNMP_USAGE = MonthlyUsageAttributionSupportedMetrics("snmp_usage")
MonthlyUsageAttributionSupportedMetrics.SNMP_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics("snmp_percentage")
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_RUM_SESSIONS_USAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_rum_sessions_usage"
)
MonthlyUsageAttributionSupportedMetrics.ESTIMATED_RUM_SESSIONS_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics(
    "estimated_rum_sessions_percentage"
)
MonthlyUsageAttributionSupportedMetrics.CONT_USAGE = MonthlyUsageAttributionSupportedMetrics("cont_usage")
MonthlyUsageAttributionSupportedMetrics.CONT_PERCENTAGE = MonthlyUsageAttributionSupportedMetrics("cont_percentage")
MonthlyUsageAttributionSupportedMetrics.ALL = MonthlyUsageAttributionSupportedMetrics("*")
