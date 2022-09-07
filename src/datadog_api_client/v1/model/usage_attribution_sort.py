# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class UsageAttributionSort(ModelSimple):
    """
    The field to sort by.

    :param value: If omitted defaults to "custom_timeseries_usage". Must be one of ["api_percentage", "snmp_usage", "apm_host_usage", "api_usage", "appsec_usage", "appsec_percentage", "container_usage", "custom_timeseries_percentage", "container_percentage", "apm_host_percentage", "npm_host_percentage", "browser_percentage", "browser_usage", "infra_host_percentage", "snmp_percentage", "npm_host_usage", "infra_host_usage", "custom_timeseries_usage", "lambda_functions_usage", "lambda_functions_percentage", "lambda_invocations_usage", "lambda_invocations_percentage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "estimated_ingested_logs_usage", "estimated_ingested_logs_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage"].
    :type value: str
    """

    allowed_values = {
        "api_percentage",
        "snmp_usage",
        "apm_host_usage",
        "api_usage",
        "appsec_usage",
        "appsec_percentage",
        "container_usage",
        "custom_timeseries_percentage",
        "container_percentage",
        "apm_host_percentage",
        "npm_host_percentage",
        "browser_percentage",
        "browser_usage",
        "infra_host_percentage",
        "snmp_percentage",
        "npm_host_usage",
        "infra_host_usage",
        "custom_timeseries_usage",
        "lambda_functions_usage",
        "lambda_functions_percentage",
        "lambda_invocations_usage",
        "lambda_invocations_percentage",
        "estimated_indexed_logs_usage",
        "estimated_indexed_logs_percentage",
        "estimated_ingested_logs_usage",
        "estimated_ingested_logs_percentage",
        "estimated_indexed_spans_usage",
        "estimated_indexed_spans_percentage",
        "estimated_ingested_spans_usage",
        "estimated_ingested_spans_percentage",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UsageAttributionSort.API_PERCENTAGE = UsageAttributionSort("api_percentage")
UsageAttributionSort.SNMP_USAGE = UsageAttributionSort("snmp_usage")
UsageAttributionSort.APM_HOST_USAGE = UsageAttributionSort("apm_host_usage")
UsageAttributionSort.API_USAGE = UsageAttributionSort("api_usage")
UsageAttributionSort.APPSEC_USAGE = UsageAttributionSort("appsec_usage")
UsageAttributionSort.APPSEC_PERCENTAGE = UsageAttributionSort("appsec_percentage")
UsageAttributionSort.CONTAINER_USAGE = UsageAttributionSort("container_usage")
UsageAttributionSort.CUSTOM_TIMESERIES_PERCENTAGE = UsageAttributionSort("custom_timeseries_percentage")
UsageAttributionSort.CONTAINER_PERCENTAGE = UsageAttributionSort("container_percentage")
UsageAttributionSort.APM_HOST_PERCENTAGE = UsageAttributionSort("apm_host_percentage")
UsageAttributionSort.NPM_HOST_PERCENTAGE = UsageAttributionSort("npm_host_percentage")
UsageAttributionSort.BROWSER_PERCENTAGE = UsageAttributionSort("browser_percentage")
UsageAttributionSort.BROWSER_USAGE = UsageAttributionSort("browser_usage")
UsageAttributionSort.INFRA_HOST_PERCENTAGE = UsageAttributionSort("infra_host_percentage")
UsageAttributionSort.SNMP_PERCENTAGE = UsageAttributionSort("snmp_percentage")
UsageAttributionSort.NPM_HOST_USAGE = UsageAttributionSort("npm_host_usage")
UsageAttributionSort.INFRA_HOST_USAGE = UsageAttributionSort("infra_host_usage")
UsageAttributionSort.CUSTOM_TIMESERIES_USAGE = UsageAttributionSort("custom_timeseries_usage")
UsageAttributionSort.LAMBDA_FUNCTIONS_USAGE = UsageAttributionSort("lambda_functions_usage")
UsageAttributionSort.LAMBDA_FUNCTIONS_PERCENTAGE = UsageAttributionSort("lambda_functions_percentage")
UsageAttributionSort.LAMBDA_INVOCATIONS_USAGE = UsageAttributionSort("lambda_invocations_usage")
UsageAttributionSort.LAMBDA_INVOCATIONS_PERCENTAGE = UsageAttributionSort("lambda_invocations_percentage")
UsageAttributionSort.ESTIMATED_INDEXED_LOGS_USAGE = UsageAttributionSort("estimated_indexed_logs_usage")
UsageAttributionSort.ESTIMATED_INDEXED_LOGS_PERCENTAGE = UsageAttributionSort("estimated_indexed_logs_percentage")
UsageAttributionSort.ESTIMATED_INGESTED_LOGS_USAGE = UsageAttributionSort("estimated_ingested_logs_usage")
UsageAttributionSort.ESTIMATED_INGESTED_LOGS_PERCENTAGE = UsageAttributionSort("estimated_ingested_logs_percentage")
UsageAttributionSort.ESTIMATED_INDEXED_SPANS_USAGE = UsageAttributionSort("estimated_indexed_spans_usage")
UsageAttributionSort.ESTIMATED_INDEXED_SPANS_PERCENTAGE = UsageAttributionSort("estimated_indexed_spans_percentage")
UsageAttributionSort.ESTIMATED_INGESTED_SPANS_USAGE = UsageAttributionSort("estimated_ingested_spans_usage")
UsageAttributionSort.ESTIMATED_INGESTED_SPANS_PERCENTAGE = UsageAttributionSort("estimated_ingested_spans_percentage")
