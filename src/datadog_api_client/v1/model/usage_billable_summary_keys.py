# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody

    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody


class UsageBillableSummaryKeys(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "apm_host_sum": (UsageBillableSummaryBody,),
            "apm_host_top99p": (UsageBillableSummaryBody,),
            "apm_trace_search_sum": (UsageBillableSummaryBody,),
            "fargate_container_average": (UsageBillableSummaryBody,),
            "infra_container_sum": (UsageBillableSummaryBody,),
            "infra_host_sum": (UsageBillableSummaryBody,),
            "infra_host_top99p": (UsageBillableSummaryBody,),
            "iot_top99p": (UsageBillableSummaryBody,),
            "lambda_function_average": (UsageBillableSummaryBody,),
            "logs_indexed_15day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_180day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_30day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_3day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_45day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_60day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_7day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_90day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_custom_retention_sum": (UsageBillableSummaryBody,),
            "logs_indexed_sum": (UsageBillableSummaryBody,),
            "logs_ingested_sum": (UsageBillableSummaryBody,),
            "network_device_top99p": (UsageBillableSummaryBody,),
            "npm_flow_sum": (UsageBillableSummaryBody,),
            "npm_host_sum": (UsageBillableSummaryBody,),
            "npm_host_top99p": (UsageBillableSummaryBody,),
            "prof_container_sum": (UsageBillableSummaryBody,),
            "prof_host_top99p": (UsageBillableSummaryBody,),
            "rum_sum": (UsageBillableSummaryBody,),
            "serverless_invocation_sum": (UsageBillableSummaryBody,),
            "siem_sum": (UsageBillableSummaryBody,),
            "synthetics_api_tests_sum": (UsageBillableSummaryBody,),
            "synthetics_browser_checks_sum": (UsageBillableSummaryBody,),
            "timeseries_average": (UsageBillableSummaryBody,),
        }

    attribute_map = {
        "apm_host_sum": "apm_host_sum",
        "apm_host_top99p": "apm_host_top99p",
        "apm_trace_search_sum": "apm_trace_search_sum",
        "fargate_container_average": "fargate_container_average",
        "infra_container_sum": "infra_container_sum",
        "infra_host_sum": "infra_host_sum",
        "infra_host_top99p": "infra_host_top99p",
        "iot_top99p": "iot_top99p",
        "lambda_function_average": "lambda_function_average",
        "logs_indexed_15day_sum": "logs_indexed_15day_sum",
        "logs_indexed_180day_sum": "logs_indexed_180day_sum",
        "logs_indexed_30day_sum": "logs_indexed_30day_sum",
        "logs_indexed_3day_sum": "logs_indexed_3day_sum",
        "logs_indexed_45day_sum": "logs_indexed_45day_sum",
        "logs_indexed_60day_sum": "logs_indexed_60day_sum",
        "logs_indexed_7day_sum": "logs_indexed_7day_sum",
        "logs_indexed_90day_sum": "logs_indexed_90day_sum",
        "logs_indexed_custom_retention_sum": "logs_indexed_custom_retention_sum",
        "logs_indexed_sum": "logs_indexed_sum",
        "logs_ingested_sum": "logs_ingested_sum",
        "network_device_top99p": "network_device_top99p",
        "npm_flow_sum": "npm_flow_sum",
        "npm_host_sum": "npm_host_sum",
        "npm_host_top99p": "npm_host_top99p",
        "prof_container_sum": "prof_container_sum",
        "prof_host_top99p": "prof_host_top99p",
        "rum_sum": "rum_sum",
        "serverless_invocation_sum": "serverless_invocation_sum",
        "siem_sum": "siem_sum",
        "synthetics_api_tests_sum": "synthetics_api_tests_sum",
        "synthetics_browser_checks_sum": "synthetics_browser_checks_sum",
        "timeseries_average": "timeseries_average",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageBillableSummaryKeys - a model defined in OpenAPI

        Keyword Args:
            apm_host_sum (UsageBillableSummaryBody): [optional]
            apm_host_top99p (UsageBillableSummaryBody): [optional]
            apm_trace_search_sum (UsageBillableSummaryBody): [optional]
            fargate_container_average (UsageBillableSummaryBody): [optional]
            infra_container_sum (UsageBillableSummaryBody): [optional]
            infra_host_sum (UsageBillableSummaryBody): [optional]
            infra_host_top99p (UsageBillableSummaryBody): [optional]
            iot_top99p (UsageBillableSummaryBody): [optional]
            lambda_function_average (UsageBillableSummaryBody): [optional]
            logs_indexed_15day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_180day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_30day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_3day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_45day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_60day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_7day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_90day_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_custom_retention_sum (UsageBillableSummaryBody): [optional]
            logs_indexed_sum (UsageBillableSummaryBody): [optional]
            logs_ingested_sum (UsageBillableSummaryBody): [optional]
            network_device_top99p (UsageBillableSummaryBody): [optional]
            npm_flow_sum (UsageBillableSummaryBody): [optional]
            npm_host_sum (UsageBillableSummaryBody): [optional]
            npm_host_top99p (UsageBillableSummaryBody): [optional]
            prof_container_sum (UsageBillableSummaryBody): [optional]
            prof_host_top99p (UsageBillableSummaryBody): [optional]
            rum_sum (UsageBillableSummaryBody): [optional]
            serverless_invocation_sum (UsageBillableSummaryBody): [optional]
            siem_sum (UsageBillableSummaryBody): [optional]
            synthetics_api_tests_sum (UsageBillableSummaryBody): [optional]
            synthetics_browser_checks_sum (UsageBillableSummaryBody): [optional]
            timeseries_average (UsageBillableSummaryBody): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageBillableSummaryKeys, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
