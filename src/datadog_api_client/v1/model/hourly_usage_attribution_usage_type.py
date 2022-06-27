# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class HourlyUsageAttributionUsageType(ModelSimple):

    allowed_values = {
        "value": {
            "API_USAGE": "api_usage",
            "APM_HOST_USAGE": "apm_host_usage",
            "APPSEC_USAGE": "appsec_usage",
            "BROWSER_USAGE": "browser_usage",
            "CONTAINER_USAGE": "container_usage",
            "CUSTOM_TIMESERIES_USAGE": "custom_timeseries_usage",
            "ESTIMATED_INDEXED_LOGS_USAGE": "estimated_indexed_logs_usage",
            "ESTIMATED_INDEXED_SPANS_USAGE": "estimated_indexed_spans_usage",
            "FARGATE_USAGE": "fargate_usage",
            "FUNCTIONS_USAGE": "functions_usage",
            "INDEXED_LOGS_USAGE": "indexed_logs_usage",
            "INFRA_HOST_USAGE": "infra_host_usage",
            "INVOCATIONS_USAGE": "invocations_usage",
            "NPM_HOST_USAGE": "npm_host_usage",
            "PROFILED_CONTAINER_USAGE": "profiled_container_usage",
            "PROFILED_HOST_USAGE": "profiled_host_usage",
            "SNMP_USAGE": "snmp_usage",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Supported products for hourly usage attribution requests.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["api_usage", "apm_host_usage", "appsec_usage", "browser_usage", "container_usage", "custom_timeseries_usage", "estimated_indexed_logs_usage", "estimated_indexed_spans_usage", "fargate_usage", "functions_usage", "indexed_logs_usage", "infra_host_usage", "invocations_usage", "npm_host_usage", "profiled_container_usage", "profiled_host_usage", "snmp_usage"].
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
