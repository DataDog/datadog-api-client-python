# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class UsageAttributionSort(ModelSimple):

    allowed_values = {
        "value": {
            "API_PERCENTAGE": "api_percentage",
            "SNMP_USAGE": "snmp_usage",
            "APM_HOST_USAGE": "apm_host_usage",
            "API_USAGE": "api_usage",
            "APPSEC_USAGE": "appsec_usage",
            "APPSEC_PERCENTAGE": "appsec_percentage",
            "CONTAINER_USAGE": "container_usage",
            "CUSTOM_TIMESERIES_PERCENTAGE": "custom_timeseries_percentage",
            "CONTAINER_PERCENTAGE": "container_percentage",
            "APM_HOST_PERCENTAGE": "apm_host_percentage",
            "NPM_HOST_PERCENTAGE": "npm_host_percentage",
            "BROWSER_PERCENTAGE": "browser_percentage",
            "BROWSER_USAGE": "browser_usage",
            "INFRA_HOST_PERCENTAGE": "infra_host_percentage",
            "SNMP_PERCENTAGE": "snmp_percentage",
            "NPM_HOST_USAGE": "npm_host_usage",
            "INFRA_HOST_USAGE": "infra_host_usage",
            "CUSTOM_TIMESERIES_USAGE": "custom_timeseries_usage",
            "LAMBDA_FUNCTIONS_USAGE": "lambda_functions_usage",
            "LAMBDA_FUNCTIONS_PERCENTAGE": "lambda_functions_percentage",
            "LAMBDA_INVOCATIONS_USAGE": "lambda_invocations_usage",
            "LAMBDA_INVOCATIONS_PERCENTAGE": "lambda_invocations_percentage",
            "ESTIMATED_INDEXED_LOGS_USAGE": "estimated_indexed_logs_usage",
            "ESTIMATED_INDEXED_LOGS_PERCENTAGE": "estimated_indexed_logs_percentage",
            "ESTIMATED_INDEXED_SPANS_USAGE": "estimated_indexed_spans_usage",
            "ESTIMATED_INDEXED_SPANS_PERCENTAGE": "estimated_indexed_spans_percentage",
            "ESTIMATED_INGESTED_SPANS_USAGE": "estimated_ingested_spans_usage",
            "ESTIMATED_INGESTED_SPANS_PERCENTAGE": "estimated_ingested_spans_percentage",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        The field to sort by.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: If omitted defaults to "custom_timeseries_usage". Must be one of ["api_percentage", "snmp_usage", "apm_host_usage", "api_usage", "appsec_usage", "appsec_percentage", "container_usage", "custom_timeseries_percentage", "container_percentage", "apm_host_percentage", "npm_host_percentage", "browser_percentage", "browser_usage", "infra_host_percentage", "snmp_percentage", "npm_host_usage", "infra_host_usage", "custom_timeseries_usage", "lambda_functions_usage", "lambda_functions_percentage", "lambda_invocations_usage", "lambda_invocations_percentage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "custom_timeseries_usage"

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
