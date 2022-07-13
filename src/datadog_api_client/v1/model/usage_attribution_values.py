# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageAttributionValues(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_percentage": (float,),
            "api_usage": (float,),
            "apm_host_percentage": (float,),
            "apm_host_usage": (float,),
            "appsec_percentage": (float,),
            "appsec_usage": (float,),
            "browser_percentage": (float,),
            "browser_usage": (float,),
            "container_percentage": (float,),
            "container_usage": (float,),
            "cspm_container_percentage": (float,),
            "cspm_container_usage": (float,),
            "cspm_host_percentage": (float,),
            "cspm_host_usage": (float,),
            "custom_timeseries_percentage": (float,),
            "custom_timeseries_usage": (float,),
            "cws_container_percentage": (float,),
            "cws_container_usage": (float,),
            "cws_host_percentage": (float,),
            "cws_host_usage": (float,),
            "dbm_hosts_percentage": (float,),
            "dbm_hosts_usage": (float,),
            "dbm_queries_percentage": (float,),
            "dbm_queries_usage": (float,),
            "estimated_indexed_logs_percentage": (float,),
            "estimated_indexed_logs_usage": (float,),
            "estimated_indexed_spans_percentage": (float,),
            "estimated_indexed_spans_usage": (float,),
            "estimated_ingested_spans_percentage": (float,),
            "estimated_ingested_spans_usage": (float,),
            "infra_host_percentage": (float,),
            "infra_host_usage": (float,),
            "lambda_functions_percentage": (float,),
            "lambda_functions_usage": (float,),
            "lambda_invocations_percentage": (float,),
            "lambda_invocations_usage": (float,),
            "npm_host_percentage": (float,),
            "npm_host_usage": (float,),
            "profiled_container_percentage": (float,),
            "profiled_container_usage": (float,),
            "profiled_hosts_percentage": (float,),
            "profiled_hosts_usage": (float,),
            "snmp_percentage": (float,),
            "snmp_usage": (float,),
        }

    attribute_map = {
        "api_percentage": "api_percentage",
        "api_usage": "api_usage",
        "apm_host_percentage": "apm_host_percentage",
        "apm_host_usage": "apm_host_usage",
        "appsec_percentage": "appsec_percentage",
        "appsec_usage": "appsec_usage",
        "browser_percentage": "browser_percentage",
        "browser_usage": "browser_usage",
        "container_percentage": "container_percentage",
        "container_usage": "container_usage",
        "cspm_container_percentage": "cspm_container_percentage",
        "cspm_container_usage": "cspm_container_usage",
        "cspm_host_percentage": "cspm_host_percentage",
        "cspm_host_usage": "cspm_host_usage",
        "custom_timeseries_percentage": "custom_timeseries_percentage",
        "custom_timeseries_usage": "custom_timeseries_usage",
        "cws_container_percentage": "cws_container_percentage",
        "cws_container_usage": "cws_container_usage",
        "cws_host_percentage": "cws_host_percentage",
        "cws_host_usage": "cws_host_usage",
        "dbm_hosts_percentage": "dbm_hosts_percentage",
        "dbm_hosts_usage": "dbm_hosts_usage",
        "dbm_queries_percentage": "dbm_queries_percentage",
        "dbm_queries_usage": "dbm_queries_usage",
        "estimated_indexed_logs_percentage": "estimated_indexed_logs_percentage",
        "estimated_indexed_logs_usage": "estimated_indexed_logs_usage",
        "estimated_indexed_spans_percentage": "estimated_indexed_spans_percentage",
        "estimated_indexed_spans_usage": "estimated_indexed_spans_usage",
        "estimated_ingested_spans_percentage": "estimated_ingested_spans_percentage",
        "estimated_ingested_spans_usage": "estimated_ingested_spans_usage",
        "infra_host_percentage": "infra_host_percentage",
        "infra_host_usage": "infra_host_usage",
        "lambda_functions_percentage": "lambda_functions_percentage",
        "lambda_functions_usage": "lambda_functions_usage",
        "lambda_invocations_percentage": "lambda_invocations_percentage",
        "lambda_invocations_usage": "lambda_invocations_usage",
        "npm_host_percentage": "npm_host_percentage",
        "npm_host_usage": "npm_host_usage",
        "profiled_container_percentage": "profiled_container_percentage",
        "profiled_container_usage": "profiled_container_usage",
        "profiled_hosts_percentage": "profiled_hosts_percentage",
        "profiled_hosts_usage": "profiled_hosts_usage",
        "snmp_percentage": "snmp_percentage",
        "snmp_usage": "snmp_usage",
    }

    def __init__(self, *args, **kwargs):
        """
        Fields in Usage Summary by tag(s).

        :param api_percentage: The percentage of synthetic API test usage by tag(s).
        :type api_percentage: float, optional

        :param api_usage: The synthetic API test usage by tag(s).
        :type api_usage: float, optional

        :param apm_host_percentage: The percentage of APM host usage by tag(s).
        :type apm_host_percentage: float, optional

        :param apm_host_usage: The APM host usage by tag(s).
        :type apm_host_usage: float, optional

        :param appsec_percentage: The percentage of Application Security Monitoring host usage by tag(s).
        :type appsec_percentage: float, optional

        :param appsec_usage: The Application Security Monitoring host usage by tag(s).
        :type appsec_usage: float, optional

        :param browser_percentage: The percentage of synthetic browser test usage by tag(s).
        :type browser_percentage: float, optional

        :param browser_usage: The synthetic browser test usage by tag(s).
        :type browser_usage: float, optional

        :param container_percentage: The percentage of container usage by tag(s).
        :type container_percentage: float, optional

        :param container_usage: The container usage by tag(s).
        :type container_usage: float, optional

        :param cspm_container_percentage: The percentage of Cloud Security Posture Management container usage by tag(s)
        :type cspm_container_percentage: float, optional

        :param cspm_container_usage: The Cloud Security Posture Management container usage by tag(s)
        :type cspm_container_usage: float, optional

        :param cspm_host_percentage: The percentage of Cloud Security Posture Management host usage by tag(s)
        :type cspm_host_percentage: float, optional

        :param cspm_host_usage: The Cloud Security Posture Management host usage by tag(s)
        :type cspm_host_usage: float, optional

        :param custom_timeseries_percentage: The percentage of custom metrics usage by tag(s).
        :type custom_timeseries_percentage: float, optional

        :param custom_timeseries_usage: The custom metrics usage by tag(s).
        :type custom_timeseries_usage: float, optional

        :param cws_container_percentage: The percentage of Cloud Workload Security container usage by tag(s)
        :type cws_container_percentage: float, optional

        :param cws_container_usage: The Cloud Workload Security container usage by tag(s)
        :type cws_container_usage: float, optional

        :param cws_host_percentage: The percentage of Cloud Workload Security host usage by tag(s)
        :type cws_host_percentage: float, optional

        :param cws_host_usage: The Cloud Workload Security host usage by tag(s)
        :type cws_host_usage: float, optional

        :param dbm_hosts_percentage: The percentage of Database Monitoring host usage by tag(s).
        :type dbm_hosts_percentage: float, optional

        :param dbm_hosts_usage: The Database Monitoring host usage by tag(s).
        :type dbm_hosts_usage: float, optional

        :param dbm_queries_percentage: The percentage of Database Monitoring normalized queries usage by tag(s).
        :type dbm_queries_percentage: float, optional

        :param dbm_queries_usage: The Database Monitoring normalized queries usage by tag(s).
        :type dbm_queries_usage: float, optional

        :param estimated_indexed_logs_percentage: The percentage of estimated live indexed logs usage by tag(s). Note this field is in private beta.
        :type estimated_indexed_logs_percentage: float, optional

        :param estimated_indexed_logs_usage: The estimated live indexed logs usage by tag(s). Note this field is in private beta.
        :type estimated_indexed_logs_usage: float, optional

        :param estimated_indexed_spans_percentage: The percentage of estimated indexed spans usage by tag(s). Note this field is in private beta.
        :type estimated_indexed_spans_percentage: float, optional

        :param estimated_indexed_spans_usage: The estimated indexed spans usage by tag(s). Note this field is in private beta.
        :type estimated_indexed_spans_usage: float, optional

        :param estimated_ingested_spans_percentage: The percentage of estimated ingested spans usage by tag(s). Note this field is in private beta.
        :type estimated_ingested_spans_percentage: float, optional

        :param estimated_ingested_spans_usage: The estimated ingested spans usage by tag(s). Note this field is in private beta.
        :type estimated_ingested_spans_usage: float, optional

        :param infra_host_percentage: The percentage of infrastructure host usage by tag(s).
        :type infra_host_percentage: float, optional

        :param infra_host_usage: The infrastructure host usage by tag(s).
        :type infra_host_usage: float, optional

        :param lambda_functions_percentage: The percentage of Lambda function usage by tag(s).
        :type lambda_functions_percentage: float, optional

        :param lambda_functions_usage: The Lambda function usage by tag(s).
        :type lambda_functions_usage: float, optional

        :param lambda_invocations_percentage: The percentage of Lambda invocation usage by tag(s).
        :type lambda_invocations_percentage: float, optional

        :param lambda_invocations_usage: The Lambda invocation usage by tag(s).
        :type lambda_invocations_usage: float, optional

        :param npm_host_percentage: The percentage of network host usage by tag(s).
        :type npm_host_percentage: float, optional

        :param npm_host_usage: The network host usage by tag(s).
        :type npm_host_usage: float, optional

        :param profiled_container_percentage: The percentage of profiled containers usage by tag(s).
        :type profiled_container_percentage: float, optional

        :param profiled_container_usage: The profiled container usage by tag(s).
        :type profiled_container_usage: float, optional

        :param profiled_hosts_percentage: The percentage of profiled hosts usage by tag(s).
        :type profiled_hosts_percentage: float, optional

        :param profiled_hosts_usage: The profiled host usage by tag(s).
        :type profiled_hosts_usage: float, optional

        :param snmp_percentage: The percentage of network device usage by tag(s).
        :type snmp_percentage: float, optional

        :param snmp_usage: The network device usage by tag(s).
        :type snmp_usage: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAttributionValues, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
