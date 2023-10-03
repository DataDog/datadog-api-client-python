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

    :param value: Must be one of ["api_usage", "apm_fargate_usage", "apm_host_usage", "apm_usm_usage", "appsec_fargate_usage", "appsec_usage", "browser_usage", "ci_visibility_itr_usage", "container_excl_agent_usage", "container_usage", "cspm_containers_usage", "cspm_hosts_usage", "custom_ingested_timeseries_usage", "custom_timeseries_usage", "cws_containers_usage", "cws_hosts_usage", "dbm_hosts_usage", "dbm_queries_usage", "estimated_indexed_logs_usage", "estimated_indexed_spans_usage", "estimated_ingested_logs_usage", "estimated_ingested_spans_usage", "estimated_rum_sessions_usage", "fargate_usage", "functions_usage", "infra_host_usage", "invocations_usage", "mobile_app_testing_usage", "ndm_netflow_usage", "npm_host_usage", "obs_pipeline_bytes_usage", "profiled_container_usage", "profiled_fargate_usage", "profiled_host_usage", "sds_scanned_bytes_usage", "serverless_apps_usage", "snmp_usage", "universal_service_monitoring_usage", "vuln_management_hosts_usage"].
    :type value: str
    """

    allowed_values = {
        "api_usage",
        "apm_fargate_usage",
        "apm_host_usage",
        "apm_usm_usage",
        "appsec_fargate_usage",
        "appsec_usage",
        "browser_usage",
        "ci_visibility_itr_usage",
        "container_excl_agent_usage",
        "container_usage",
        "cspm_containers_usage",
        "cspm_hosts_usage",
        "custom_ingested_timeseries_usage",
        "custom_timeseries_usage",
        "cws_containers_usage",
        "cws_hosts_usage",
        "dbm_hosts_usage",
        "dbm_queries_usage",
        "estimated_indexed_logs_usage",
        "estimated_indexed_spans_usage",
        "estimated_ingested_logs_usage",
        "estimated_ingested_spans_usage",
        "estimated_rum_sessions_usage",
        "fargate_usage",
        "functions_usage",
        "infra_host_usage",
        "invocations_usage",
        "mobile_app_testing_usage",
        "ndm_netflow_usage",
        "npm_host_usage",
        "obs_pipeline_bytes_usage",
        "profiled_container_usage",
        "profiled_fargate_usage",
        "profiled_host_usage",
        "sds_scanned_bytes_usage",
        "serverless_apps_usage",
        "snmp_usage",
        "universal_service_monitoring_usage",
        "vuln_management_hosts_usage",
    }
    API_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APM_FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APM_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APM_USM_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APPSEC_FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    APPSEC_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    BROWSER_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CI_VISIBILITY_ITR_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CONTAINER_EXCL_AGENT_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CONTAINER_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CSPM_CONTAINERS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CSPM_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CUSTOM_INGESTED_TIMESERIES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CUSTOM_TIMESERIES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CWS_CONTAINERS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    CWS_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    DBM_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    DBM_QUERIES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INDEXED_LOGS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INDEXED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INGESTED_LOGS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_INGESTED_SPANS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    ESTIMATED_RUM_SESSIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    FUNCTIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INFRA_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    INVOCATIONS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    MOBILE_APP_TESTING_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    NDM_NETFLOW_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    NPM_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    OBS_PIPELINE_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    PROFILED_CONTAINER_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    PROFILED_FARGATE_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    PROFILED_HOST_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SDS_SCANNED_BYTES_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SERVERLESS_APPS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    SNMP_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    UNIVERSAL_SERVICE_MONITORING_USAGE: ClassVar["HourlyUsageAttributionUsageType"]
    VULN_MANAGEMENT_HOSTS_USAGE: ClassVar["HourlyUsageAttributionUsageType"]

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
HourlyUsageAttributionUsageType.BROWSER_USAGE = HourlyUsageAttributionUsageType("browser_usage")
HourlyUsageAttributionUsageType.CI_VISIBILITY_ITR_USAGE = HourlyUsageAttributionUsageType("ci_visibility_itr_usage")
HourlyUsageAttributionUsageType.CONTAINER_EXCL_AGENT_USAGE = HourlyUsageAttributionUsageType(
    "container_excl_agent_usage"
)
HourlyUsageAttributionUsageType.CONTAINER_USAGE = HourlyUsageAttributionUsageType("container_usage")
HourlyUsageAttributionUsageType.CSPM_CONTAINERS_USAGE = HourlyUsageAttributionUsageType("cspm_containers_usage")
HourlyUsageAttributionUsageType.CSPM_HOSTS_USAGE = HourlyUsageAttributionUsageType("cspm_hosts_usage")
HourlyUsageAttributionUsageType.CUSTOM_INGESTED_TIMESERIES_USAGE = HourlyUsageAttributionUsageType(
    "custom_ingested_timeseries_usage"
)
HourlyUsageAttributionUsageType.CUSTOM_TIMESERIES_USAGE = HourlyUsageAttributionUsageType("custom_timeseries_usage")
HourlyUsageAttributionUsageType.CWS_CONTAINERS_USAGE = HourlyUsageAttributionUsageType("cws_containers_usage")
HourlyUsageAttributionUsageType.CWS_HOSTS_USAGE = HourlyUsageAttributionUsageType("cws_hosts_usage")
HourlyUsageAttributionUsageType.DBM_HOSTS_USAGE = HourlyUsageAttributionUsageType("dbm_hosts_usage")
HourlyUsageAttributionUsageType.DBM_QUERIES_USAGE = HourlyUsageAttributionUsageType("dbm_queries_usage")
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
HourlyUsageAttributionUsageType.INFRA_HOST_USAGE = HourlyUsageAttributionUsageType("infra_host_usage")
HourlyUsageAttributionUsageType.INVOCATIONS_USAGE = HourlyUsageAttributionUsageType("invocations_usage")
HourlyUsageAttributionUsageType.MOBILE_APP_TESTING_USAGE = HourlyUsageAttributionUsageType("mobile_app_testing_usage")
HourlyUsageAttributionUsageType.NDM_NETFLOW_USAGE = HourlyUsageAttributionUsageType("ndm_netflow_usage")
HourlyUsageAttributionUsageType.NPM_HOST_USAGE = HourlyUsageAttributionUsageType("npm_host_usage")
HourlyUsageAttributionUsageType.OBS_PIPELINE_BYTES_USAGE = HourlyUsageAttributionUsageType("obs_pipeline_bytes_usage")
HourlyUsageAttributionUsageType.PROFILED_CONTAINER_USAGE = HourlyUsageAttributionUsageType("profiled_container_usage")
HourlyUsageAttributionUsageType.PROFILED_FARGATE_USAGE = HourlyUsageAttributionUsageType("profiled_fargate_usage")
HourlyUsageAttributionUsageType.PROFILED_HOST_USAGE = HourlyUsageAttributionUsageType("profiled_host_usage")
HourlyUsageAttributionUsageType.SDS_SCANNED_BYTES_USAGE = HourlyUsageAttributionUsageType("sds_scanned_bytes_usage")
HourlyUsageAttributionUsageType.SERVERLESS_APPS_USAGE = HourlyUsageAttributionUsageType("serverless_apps_usage")
HourlyUsageAttributionUsageType.SNMP_USAGE = HourlyUsageAttributionUsageType("snmp_usage")
HourlyUsageAttributionUsageType.UNIVERSAL_SERVICE_MONITORING_USAGE = HourlyUsageAttributionUsageType(
    "universal_service_monitoring_usage"
)
HourlyUsageAttributionUsageType.VULN_MANAGEMENT_HOSTS_USAGE = HourlyUsageAttributionUsageType(
    "vuln_management_hosts_usage"
)
