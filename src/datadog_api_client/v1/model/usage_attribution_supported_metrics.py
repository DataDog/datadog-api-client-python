# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class UsageAttributionSupportedMetrics(ModelSimple):

    allowed_values = {
        "value": {
            "CUSTOM_TIMESERIES_USAGE": "custom_timeseries_usage",
            "CONTAINER_USAGE": "container_usage",
            "SNMP_PERCENTAGE": "snmp_percentage",
            "APM_HOST_USAGE": "apm_host_usage",
            "BROWSER_USAGE": "browser_usage",
            "NPM_HOST_PERCENTAGE": "npm_host_percentage",
            "INFRA_HOST_USAGE": "infra_host_usage",
            "CUSTOM_TIMESERIES_PERCENTAGE": "custom_timeseries_percentage",
            "CONTAINER_PERCENTAGE": "container_percentage",
            "API_USAGE": "api_usage",
            "APM_HOST_PERCENTAGE": "apm_host_percentage",
            "INFRA_HOST_PERCENTAGE": "infra_host_percentage",
            "SNMP_USAGE": "snmp_usage",
            "BROWSER_PERCENTAGE": "browser_percentage",
            "API_PERCENTAGE": "api_percentage",
            "NPM_HOST_USAGE": "npm_host_usage",
            "LAMBDA_FUNCTIONS_USAGE": "lambda_functions_usage",
            "LAMBDA_FUNCTIONS_PERCENTAGE": "lambda_functions_percentage",
            "LAMBDA_INVOCATIONS_USAGE": "lambda_invocations_usage",
            "LAMBDA_INVOCATIONS_PERCENTAGE": "lambda_invocations_percentage",
            "FARGATE_USAGE": "fargate_usage",
            "FARGATE_PERCENTAGE": "fargate_percentage",
            "PROFILED_HOST_USAGE": "profiled_host_usage",
            "PROFILED_HOST_PERCENTAGE": "profiled_host_percentage",
            "PROFILED_CONTAINER_USAGE": "profiled_container_usage",
            "PROFILED_CONTAINER_PERCENTAGE": "profiled_container_percentage",
            "DBM_HOSTS_USAGE": "dbm_hosts_usage",
            "DBM_HOSTS_PERCENTAGE": "dbm_hosts_percentage",
            "DBM_QUERIES_USAGE": "dbm_queries_usage",
            "DBM_QUERIES_PERCENTAGE": "dbm_queries_percentage",
            "ESTIMATED_INDEXED_LOGS_USAGE": "estimated_indexed_logs_usage",
            "ESTIMATED_INDEXED_LOGS_PERCENTAGE": "estimated_indexed_logs_percentage",
            "APPSEC_USAGE": "appsec_usage",
            "APPSEC_PERCENTAGE": "appsec_percentage",
            "ESTIMATED_INDEXED_SPANS_USAGE": "estimated_indexed_spans_usage",
            "ESTIMATED_INDEXED_SPANS_PERCENTAGE": "estimated_indexed_spans_percentage",
            "ESTIMATED_INGESTED_SPANS_USAGE": "estimated_ingested_spans_usage",
            "ESTIMATED_INGESTED_SPANS_PERCENTAGE": "estimated_ingested_spans_percentage",
            "ALL": "*",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Supported fields for usage attribution requests (valid requests contain one or more metrics, or `*` for all).

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["custom_timeseries_usage", "container_usage", "snmp_percentage", "apm_host_usage", "browser_usage", "npm_host_percentage", "infra_host_usage", "custom_timeseries_percentage", "container_percentage", "api_usage", "apm_host_percentage", "infra_host_percentage", "snmp_usage", "browser_percentage", "api_percentage", "npm_host_usage", "lambda_functions_usage", "lambda_functions_percentage", "lambda_invocations_usage", "lambda_invocations_percentage", "fargate_usage", "fargate_percentage", "profiled_host_usage", "profiled_host_percentage", "profiled_container_usage", "profiled_container_percentage", "dbm_hosts_usage", "dbm_hosts_percentage", "dbm_queries_usage", "dbm_queries_percentage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "appsec_usage", "appsec_percentage", "estimated_indexed_spans_usage", "estimated_indexed_spans_percentage", "estimated_ingested_spans_usage", "estimated_ingested_spans_percentage", "*"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
