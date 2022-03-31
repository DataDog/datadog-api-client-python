# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody

    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody
    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody


class UsageBillableSummaryKeys(ModelNormal):
    @cached_property
    def openapi_types(_):
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

    def __init__(self, *args, **kwargs):
        """
        Response with aggregated usage types.

        :param apm_host_sum: Response with properties for each aggregated usage type.
        :type apm_host_sum: UsageBillableSummaryBody, optional

        :param apm_host_top99p: Response with properties for each aggregated usage type.
        :type apm_host_top99p: UsageBillableSummaryBody, optional

        :param apm_trace_search_sum: Response with properties for each aggregated usage type.
        :type apm_trace_search_sum: UsageBillableSummaryBody, optional

        :param fargate_container_average: Response with properties for each aggregated usage type.
        :type fargate_container_average: UsageBillableSummaryBody, optional

        :param infra_container_sum: Response with properties for each aggregated usage type.
        :type infra_container_sum: UsageBillableSummaryBody, optional

        :param infra_host_sum: Response with properties for each aggregated usage type.
        :type infra_host_sum: UsageBillableSummaryBody, optional

        :param infra_host_top99p: Response with properties for each aggregated usage type.
        :type infra_host_top99p: UsageBillableSummaryBody, optional

        :param iot_top99p: Response with properties for each aggregated usage type.
        :type iot_top99p: UsageBillableSummaryBody, optional

        :param lambda_function_average: Response with properties for each aggregated usage type.
        :type lambda_function_average: UsageBillableSummaryBody, optional

        :param logs_indexed_15day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_15day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_180day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_180day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_30day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_30day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_3day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_3day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_45day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_45day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_60day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_60day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_7day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_7day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_90day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_90day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_custom_retention_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_custom_retention_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_sum: UsageBillableSummaryBody, optional

        :param logs_ingested_sum: Response with properties for each aggregated usage type.
        :type logs_ingested_sum: UsageBillableSummaryBody, optional

        :param network_device_top99p: Response with properties for each aggregated usage type.
        :type network_device_top99p: UsageBillableSummaryBody, optional

        :param npm_flow_sum: Response with properties for each aggregated usage type.
        :type npm_flow_sum: UsageBillableSummaryBody, optional

        :param npm_host_sum: Response with properties for each aggregated usage type.
        :type npm_host_sum: UsageBillableSummaryBody, optional

        :param npm_host_top99p: Response with properties for each aggregated usage type.
        :type npm_host_top99p: UsageBillableSummaryBody, optional

        :param prof_container_sum: Response with properties for each aggregated usage type.
        :type prof_container_sum: UsageBillableSummaryBody, optional

        :param prof_host_top99p: Response with properties for each aggregated usage type.
        :type prof_host_top99p: UsageBillableSummaryBody, optional

        :param rum_sum: Response with properties for each aggregated usage type.
        :type rum_sum: UsageBillableSummaryBody, optional

        :param serverless_invocation_sum: Response with properties for each aggregated usage type.
        :type serverless_invocation_sum: UsageBillableSummaryBody, optional

        :param siem_sum: Response with properties for each aggregated usage type.
        :type siem_sum: UsageBillableSummaryBody, optional

        :param synthetics_api_tests_sum: Response with properties for each aggregated usage type.
        :type synthetics_api_tests_sum: UsageBillableSummaryBody, optional

        :param synthetics_browser_checks_sum: Response with properties for each aggregated usage type.
        :type synthetics_browser_checks_sum: UsageBillableSummaryBody, optional

        :param timeseries_average: Response with properties for each aggregated usage type.
        :type timeseries_average: UsageBillableSummaryBody, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageBillableSummaryKeys, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
