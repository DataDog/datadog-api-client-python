# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class UsageAttributionSupportedMetrics(ModelSimple):
    """
    Supported fields for usage attribution requests (valid requests contain one or more metrics, or `*` for all).

    :param value: Must be one of ["custom_timeseries_usage", "container_usage", "snmp_percentage", "apm_host_usage", "browser_usage", "npm_host_percentage", "infra_host_usage", "custom_timeseries_percentage", "container_percentage", "api_usage", "apm_host_percentage", "infra_host_percentage", "snmp_usage", "browser_percentage", "api_percentage", "npm_host_usage", "lambda_functions_usage", "lambda_functions_percentage", "lambda_invocations_usage", "lambda_invocations_percentage", "fargate_usage", "fargate_percentage", "profiled_host_usage", "profiled_host_percentage", "profiled_container_usage", "profiled_container_percentage", "dbm_hosts_usage", "dbm_hosts_percentage", "dbm_queries_usage", "dbm_queries_percentage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "estimated_ingested_logs_usage", "estimated_ingested_logs_percentage", "appsec_usage", "appsec_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage", "*"].
    :type value: str
    """

    allowed_values = {
        "custom_timeseries_usage",
        "container_usage",
        "snmp_percentage",
        "apm_host_usage",
        "browser_usage",
        "npm_host_percentage",
        "infra_host_usage",
        "custom_timeseries_percentage",
        "container_percentage",
        "api_usage",
        "apm_host_percentage",
        "infra_host_percentage",
        "snmp_usage",
        "browser_percentage",
        "api_percentage",
        "npm_host_usage",
        "lambda_functions_usage",
        "lambda_functions_percentage",
        "lambda_invocations_usage",
        "lambda_invocations_percentage",
        "fargate_usage",
        "fargate_percentage",
        "profiled_host_usage",
        "profiled_host_percentage",
        "profiled_container_usage",
        "profiled_container_percentage",
        "dbm_hosts_usage",
        "dbm_hosts_percentage",
        "dbm_queries_usage",
        "dbm_queries_percentage",
        "estimated_indexed_logs_usage",
        "estimated_indexed_logs_percentage",
        "estimated_ingested_logs_usage",
        "estimated_ingested_logs_percentage",
        "appsec_usage",
        "appsec_percentage",
        "estimated_indexed_spans_usage",
        "estimated_indexed_spans_percentage",
        "estimated_ingested_spans_usage",
        "estimated_ingested_spans_percentage",
        "*",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UsageAttributionSupportedMetrics.CUSTOM_TIMESERIES_USAGE = UsageAttributionSupportedMetrics("custom_timeseries_usage")
UsageAttributionSupportedMetrics.CONTAINER_USAGE = UsageAttributionSupportedMetrics("container_usage")
UsageAttributionSupportedMetrics.SNMP_PERCENTAGE = UsageAttributionSupportedMetrics("snmp_percentage")
UsageAttributionSupportedMetrics.APM_HOST_USAGE = UsageAttributionSupportedMetrics("apm_host_usage")
UsageAttributionSupportedMetrics.BROWSER_USAGE = UsageAttributionSupportedMetrics("browser_usage")
UsageAttributionSupportedMetrics.NPM_HOST_PERCENTAGE = UsageAttributionSupportedMetrics("npm_host_percentage")
UsageAttributionSupportedMetrics.INFRA_HOST_USAGE = UsageAttributionSupportedMetrics("infra_host_usage")
UsageAttributionSupportedMetrics.CUSTOM_TIMESERIES_PERCENTAGE = UsageAttributionSupportedMetrics(
    "custom_timeseries_percentage"
)
UsageAttributionSupportedMetrics.CONTAINER_PERCENTAGE = UsageAttributionSupportedMetrics("container_percentage")
UsageAttributionSupportedMetrics.API_USAGE = UsageAttributionSupportedMetrics("api_usage")
UsageAttributionSupportedMetrics.APM_HOST_PERCENTAGE = UsageAttributionSupportedMetrics("apm_host_percentage")
UsageAttributionSupportedMetrics.INFRA_HOST_PERCENTAGE = UsageAttributionSupportedMetrics("infra_host_percentage")
UsageAttributionSupportedMetrics.SNMP_USAGE = UsageAttributionSupportedMetrics("snmp_usage")
UsageAttributionSupportedMetrics.BROWSER_PERCENTAGE = UsageAttributionSupportedMetrics("browser_percentage")
UsageAttributionSupportedMetrics.API_PERCENTAGE = UsageAttributionSupportedMetrics("api_percentage")
UsageAttributionSupportedMetrics.NPM_HOST_USAGE = UsageAttributionSupportedMetrics("npm_host_usage")
UsageAttributionSupportedMetrics.LAMBDA_FUNCTIONS_USAGE = UsageAttributionSupportedMetrics("lambda_functions_usage")
UsageAttributionSupportedMetrics.LAMBDA_FUNCTIONS_PERCENTAGE = UsageAttributionSupportedMetrics(
    "lambda_functions_percentage"
)
UsageAttributionSupportedMetrics.LAMBDA_INVOCATIONS_USAGE = UsageAttributionSupportedMetrics("lambda_invocations_usage")
UsageAttributionSupportedMetrics.LAMBDA_INVOCATIONS_PERCENTAGE = UsageAttributionSupportedMetrics(
    "lambda_invocations_percentage"
)
UsageAttributionSupportedMetrics.FARGATE_USAGE = UsageAttributionSupportedMetrics("fargate_usage")
UsageAttributionSupportedMetrics.FARGATE_PERCENTAGE = UsageAttributionSupportedMetrics("fargate_percentage")
UsageAttributionSupportedMetrics.PROFILED_HOST_USAGE = UsageAttributionSupportedMetrics("profiled_host_usage")
UsageAttributionSupportedMetrics.PROFILED_HOST_PERCENTAGE = UsageAttributionSupportedMetrics("profiled_host_percentage")
UsageAttributionSupportedMetrics.PROFILED_CONTAINER_USAGE = UsageAttributionSupportedMetrics("profiled_container_usage")
UsageAttributionSupportedMetrics.PROFILED_CONTAINER_PERCENTAGE = UsageAttributionSupportedMetrics(
    "profiled_container_percentage"
)
UsageAttributionSupportedMetrics.DBM_HOSTS_USAGE = UsageAttributionSupportedMetrics("dbm_hosts_usage")
UsageAttributionSupportedMetrics.DBM_HOSTS_PERCENTAGE = UsageAttributionSupportedMetrics("dbm_hosts_percentage")
UsageAttributionSupportedMetrics.DBM_QUERIES_USAGE = UsageAttributionSupportedMetrics("dbm_queries_usage")
UsageAttributionSupportedMetrics.DBM_QUERIES_PERCENTAGE = UsageAttributionSupportedMetrics("dbm_queries_percentage")
UsageAttributionSupportedMetrics.ESTIMATED_INDEXED_LOGS_USAGE = UsageAttributionSupportedMetrics(
    "estimated_indexed_logs_usage"
)
UsageAttributionSupportedMetrics.ESTIMATED_INDEXED_LOGS_PERCENTAGE = UsageAttributionSupportedMetrics(
    "estimated_indexed_logs_percentage"
)
UsageAttributionSupportedMetrics.ESTIMATED_INGESTED_LOGS_USAGE = UsageAttributionSupportedMetrics(
    "estimated_ingested_logs_usage"
)
UsageAttributionSupportedMetrics.ESTIMATED_INGESTED_LOGS_PERCENTAGE = UsageAttributionSupportedMetrics(
    "estimated_ingested_logs_percentage"
)
UsageAttributionSupportedMetrics.APPSEC_USAGE = UsageAttributionSupportedMetrics("appsec_usage")
UsageAttributionSupportedMetrics.APPSEC_PERCENTAGE = UsageAttributionSupportedMetrics("appsec_percentage")
UsageAttributionSupportedMetrics.ESTIMATED_INDEXED_SPANS_USAGE = UsageAttributionSupportedMetrics(
    "estimated_indexed_spans_usage"
)
UsageAttributionSupportedMetrics.ESTIMATED_INDEXED_SPANS_PERCENTAGE = UsageAttributionSupportedMetrics(
    "estimated_indexed_spans_percentage"
)
UsageAttributionSupportedMetrics.ESTIMATED_INGESTED_SPANS_USAGE = UsageAttributionSupportedMetrics(
    "estimated_ingested_spans_usage"
)
UsageAttributionSupportedMetrics.ESTIMATED_INGESTED_SPANS_PERCENTAGE = UsageAttributionSupportedMetrics(
    "estimated_ingested_spans_percentage"
)
UsageAttributionSupportedMetrics.ALL = UsageAttributionSupportedMetrics("*")
