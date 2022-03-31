# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class MonthlyUsageAttributionSupportedMetrics(ModelSimple):

    allowed_values = {
        "value": {
            "API_USAGE": "api_usage",
            "API_PERCENTAGE": "api_percentage",
            "APM_HOST_USAGE": "apm_host_usage",
            "APM_HOST_PERCENTAGE": "apm_host_percentage",
            "BROWSER_USAGE": "browser_usage",
            "BROWSER_PERCENTAGE": "browser_percentage",
            "CONTAINER_USAGE": "container_usage",
            "CONTAINER_PERCENTAGE": "container_percentage",
            "CUSTOM_TIMESERIES_USAGE": "custom_timeseries_usage",
            "CUSTOM_TIMESERIES_PERCENTAGE": "custom_timeseries_percentage",
            "ESTIMATED_INDEXED_LOGS_USAGE": "estimated_indexed_logs_usage",
            "ESTIMATED_INDEXED_LOGS_PERCENTAGE": "estimated_indexed_logs_percentage",
            "FARGATE_USAGE": "fargate_usage",
            "FARGATE_PERCENTAGE": "fargate_percentage",
            "FUNCTIONS_USAGE": "functions_usage",
            "FUNCTIONS_PERCENTAGE": "functions_percentage",
            "INDEXED_LOGS_USAGE": "indexed_logs_usage",
            "INDEXED_LOGS_PERCENTAGE": "indexed_logs_percentage",
            "INFRA_HOST_USAGE": "infra_host_usage",
            "INFRA_HOST_PERCENTAGE": "infra_host_percentage",
            "INVOCATIONS_USAGE": "invocations_usage",
            "INVOCATIONS_PERCENTAGE": "invocations_percentage",
            "NPM_HOST_USAGE": "npm_host_usage",
            "NPM_HOST_PERCENTAGE": "npm_host_percentage",
            "PROFILED_CONTAINER_USAGE": "profiled_container_usage",
            "PROFILED_CONTAINER_PERCENTAGE": "profiled_container_percentage",
            "PROFILED_HOST_USAGE": "profiled_host_usage",
            "PROFILED_HOST_PERCENTAGE": "profiled_host_percentage",
            "SNMP_USAGE": "snmp_usage",
            "SNMP_PERCENTAGE": "snmp_percentage",
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
        Supported metrics for monthly usage attribution requests.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["api_usage", "api_percentage", "apm_host_usage", "apm_host_percentage", "browser_usage", "browser_percentage", "container_usage", "container_percentage", "custom_timeseries_usage", "custom_timeseries_percentage", "estimated_indexed_logs_usage", "estimated_indexed_logs_percentage", "fargate_usage", "fargate_percentage", "functions_usage", "functions_percentage", "indexed_logs_usage", "indexed_logs_percentage", "infra_host_usage", "infra_host_percentage", "invocations_usage", "invocations_percentage", "npm_host_usage", "npm_host_percentage", "profiled_container_usage", "profiled_container_percentage", "profiled_host_usage", "profiled_host_percentage", "snmp_usage", "snmp_percentage", "*"].
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
