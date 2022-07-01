# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageBillableSummaryKeys(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody

        return {
            "apm_fargate_average": (UsageBillableSummaryBody,),
            "apm_fargate_sum": (UsageBillableSummaryBody,),
            "apm_host_sum": (UsageBillableSummaryBody,),
            "apm_host_top99p": (UsageBillableSummaryBody,),
            "apm_profiler_host_sum": (UsageBillableSummaryBody,),
            "apm_profiler_host_top99p": (UsageBillableSummaryBody,),
            "apm_trace_search_sum": (UsageBillableSummaryBody,),
            "application_security_host_sum": (UsageBillableSummaryBody,),
            "ci_pipeline_indexed_spans_sum": (UsageBillableSummaryBody,),
            "ci_pipeline_maximum": (UsageBillableSummaryBody,),
            "ci_pipeline_sum": (UsageBillableSummaryBody,),
            "ci_test_indexed_spans_sum": (UsageBillableSummaryBody,),
            "ci_testing_maximum": (UsageBillableSummaryBody,),
            "ci_testing_sum": (UsageBillableSummaryBody,),
            "cspm_container_sum": (UsageBillableSummaryBody,),
            "cspm_host_sum": (UsageBillableSummaryBody,),
            "cspm_host_top99p": (UsageBillableSummaryBody,),
            "custom_event_sum": (UsageBillableSummaryBody,),
            "cws_container_sum": (UsageBillableSummaryBody,),
            "cws_host_sum": (UsageBillableSummaryBody,),
            "cws_host_top99p": (UsageBillableSummaryBody,),
            "dbm_host_sum": (UsageBillableSummaryBody,),
            "dbm_host_top99p": (UsageBillableSummaryBody,),
            "dbm_normalized_queries_average": (UsageBillableSummaryBody,),
            "dbm_normalized_queries_sum": (UsageBillableSummaryBody,),
            "fargate_container_apm_and_profiler_average": (UsageBillableSummaryBody,),
            "fargate_container_apm_and_profiler_sum": (UsageBillableSummaryBody,),
            "fargate_container_average": (UsageBillableSummaryBody,),
            "fargate_container_profiler_average": (UsageBillableSummaryBody,),
            "fargate_container_profiler_sum": (UsageBillableSummaryBody,),
            "fargate_container_sum": (UsageBillableSummaryBody,),
            "incident_management_maximum": (UsageBillableSummaryBody,),
            "incident_management_sum": (UsageBillableSummaryBody,),
            "infra_and_apm_host_sum": (UsageBillableSummaryBody,),
            "infra_and_apm_host_top99p": (UsageBillableSummaryBody,),
            "infra_container_sum": (UsageBillableSummaryBody,),
            "infra_host_sum": (UsageBillableSummaryBody,),
            "infra_host_top99p": (UsageBillableSummaryBody,),
            "ingested_spans_sum": (UsageBillableSummaryBody,),
            "ingested_timeseries_average": (UsageBillableSummaryBody,),
            "ingested_timeseries_sum": (UsageBillableSummaryBody,),
            "iot_sum": (UsageBillableSummaryBody,),
            "iot_top99p": (UsageBillableSummaryBody,),
            "lambda_function_average": (UsageBillableSummaryBody,),
            "lambda_function_sum": (UsageBillableSummaryBody,),
            "logs_indexed_15day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_180day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_30day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_360day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_3day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_45day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_60day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_7day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_90day_sum": (UsageBillableSummaryBody,),
            "logs_indexed_custom_retention_sum": (UsageBillableSummaryBody,),
            "logs_indexed_sum": (UsageBillableSummaryBody,),
            "logs_ingested_sum": (UsageBillableSummaryBody,),
            "network_device_sum": (UsageBillableSummaryBody,),
            "network_device_top99p": (UsageBillableSummaryBody,),
            "npm_flow_sum": (UsageBillableSummaryBody,),
            "npm_host_sum": (UsageBillableSummaryBody,),
            "npm_host_top99p": (UsageBillableSummaryBody,),
            "observability_pipeline_sum": (UsageBillableSummaryBody,),
            "online_archive_sum": (UsageBillableSummaryBody,),
            "prof_container_sum": (UsageBillableSummaryBody,),
            "prof_host_sum": (UsageBillableSummaryBody,),
            "prof_host_top99p": (UsageBillableSummaryBody,),
            "rum_lite_sum": (UsageBillableSummaryBody,),
            "rum_replay_sum": (UsageBillableSummaryBody,),
            "rum_sum": (UsageBillableSummaryBody,),
            "rum_units_sum": (UsageBillableSummaryBody,),
            "sensitive_data_scanner_sum": (UsageBillableSummaryBody,),
            "serverless_invocation_sum": (UsageBillableSummaryBody,),
            "siem_sum": (UsageBillableSummaryBody,),
            "standard_timeseries_average": (UsageBillableSummaryBody,),
            "synthetics_api_tests_sum": (UsageBillableSummaryBody,),
            "synthetics_browser_checks_sum": (UsageBillableSummaryBody,),
            "timeseries_average": (UsageBillableSummaryBody,),
            "timeseries_sum": (UsageBillableSummaryBody,),
        }

    attribute_map = {
        "apm_fargate_average": "apm_fargate_average",
        "apm_fargate_sum": "apm_fargate_sum",
        "apm_host_sum": "apm_host_sum",
        "apm_host_top99p": "apm_host_top99p",
        "apm_profiler_host_sum": "apm_profiler_host_sum",
        "apm_profiler_host_top99p": "apm_profiler_host_top99p",
        "apm_trace_search_sum": "apm_trace_search_sum",
        "application_security_host_sum": "application_security_host_sum",
        "ci_pipeline_indexed_spans_sum": "ci_pipeline_indexed_spans_sum",
        "ci_pipeline_maximum": "ci_pipeline_maximum",
        "ci_pipeline_sum": "ci_pipeline_sum",
        "ci_test_indexed_spans_sum": "ci_test_indexed_spans_sum",
        "ci_testing_maximum": "ci_testing_maximum",
        "ci_testing_sum": "ci_testing_sum",
        "cspm_container_sum": "cspm_container_sum",
        "cspm_host_sum": "cspm_host_sum",
        "cspm_host_top99p": "cspm_host_top99p",
        "custom_event_sum": "custom_event_sum",
        "cws_container_sum": "cws_container_sum",
        "cws_host_sum": "cws_host_sum",
        "cws_host_top99p": "cws_host_top99p",
        "dbm_host_sum": "dbm_host_sum",
        "dbm_host_top99p": "dbm_host_top99p",
        "dbm_normalized_queries_average": "dbm_normalized_queries_average",
        "dbm_normalized_queries_sum": "dbm_normalized_queries_sum",
        "fargate_container_apm_and_profiler_average": "fargate_container_apm_and_profiler_average",
        "fargate_container_apm_and_profiler_sum": "fargate_container_apm_and_profiler_sum",
        "fargate_container_average": "fargate_container_average",
        "fargate_container_profiler_average": "fargate_container_profiler_average",
        "fargate_container_profiler_sum": "fargate_container_profiler_sum",
        "fargate_container_sum": "fargate_container_sum",
        "incident_management_maximum": "incident_management_maximum",
        "incident_management_sum": "incident_management_sum",
        "infra_and_apm_host_sum": "infra_and_apm_host_sum",
        "infra_and_apm_host_top99p": "infra_and_apm_host_top99p",
        "infra_container_sum": "infra_container_sum",
        "infra_host_sum": "infra_host_sum",
        "infra_host_top99p": "infra_host_top99p",
        "ingested_spans_sum": "ingested_spans_sum",
        "ingested_timeseries_average": "ingested_timeseries_average",
        "ingested_timeseries_sum": "ingested_timeseries_sum",
        "iot_sum": "iot_sum",
        "iot_top99p": "iot_top99p",
        "lambda_function_average": "lambda_function_average",
        "lambda_function_sum": "lambda_function_sum",
        "logs_indexed_15day_sum": "logs_indexed_15day_sum",
        "logs_indexed_180day_sum": "logs_indexed_180day_sum",
        "logs_indexed_30day_sum": "logs_indexed_30day_sum",
        "logs_indexed_360day_sum": "logs_indexed_360day_sum",
        "logs_indexed_3day_sum": "logs_indexed_3day_sum",
        "logs_indexed_45day_sum": "logs_indexed_45day_sum",
        "logs_indexed_60day_sum": "logs_indexed_60day_sum",
        "logs_indexed_7day_sum": "logs_indexed_7day_sum",
        "logs_indexed_90day_sum": "logs_indexed_90day_sum",
        "logs_indexed_custom_retention_sum": "logs_indexed_custom_retention_sum",
        "logs_indexed_sum": "logs_indexed_sum",
        "logs_ingested_sum": "logs_ingested_sum",
        "network_device_sum": "network_device_sum",
        "network_device_top99p": "network_device_top99p",
        "npm_flow_sum": "npm_flow_sum",
        "npm_host_sum": "npm_host_sum",
        "npm_host_top99p": "npm_host_top99p",
        "observability_pipeline_sum": "observability_pipeline_sum",
        "online_archive_sum": "online_archive_sum",
        "prof_container_sum": "prof_container_sum",
        "prof_host_sum": "prof_host_sum",
        "prof_host_top99p": "prof_host_top99p",
        "rum_lite_sum": "rum_lite_sum",
        "rum_replay_sum": "rum_replay_sum",
        "rum_sum": "rum_sum",
        "rum_units_sum": "rum_units_sum",
        "sensitive_data_scanner_sum": "sensitive_data_scanner_sum",
        "serverless_invocation_sum": "serverless_invocation_sum",
        "siem_sum": "siem_sum",
        "standard_timeseries_average": "standard_timeseries_average",
        "synthetics_api_tests_sum": "synthetics_api_tests_sum",
        "synthetics_browser_checks_sum": "synthetics_browser_checks_sum",
        "timeseries_average": "timeseries_average",
        "timeseries_sum": "timeseries_sum",
    }

    def __init__(self, *args, **kwargs):
        """
        Response with aggregated usage types.

        :param apm_fargate_average: Response with properties for each aggregated usage type.
        :type apm_fargate_average: UsageBillableSummaryBody, optional

        :param apm_fargate_sum: Response with properties for each aggregated usage type.
        :type apm_fargate_sum: UsageBillableSummaryBody, optional

        :param apm_host_sum: Response with properties for each aggregated usage type.
        :type apm_host_sum: UsageBillableSummaryBody, optional

        :param apm_host_top99p: Response with properties for each aggregated usage type.
        :type apm_host_top99p: UsageBillableSummaryBody, optional

        :param apm_profiler_host_sum: Response with properties for each aggregated usage type.
        :type apm_profiler_host_sum: UsageBillableSummaryBody, optional

        :param apm_profiler_host_top99p: Response with properties for each aggregated usage type.
        :type apm_profiler_host_top99p: UsageBillableSummaryBody, optional

        :param apm_trace_search_sum: Response with properties for each aggregated usage type.
        :type apm_trace_search_sum: UsageBillableSummaryBody, optional

        :param application_security_host_sum: Response with properties for each aggregated usage type.
        :type application_security_host_sum: UsageBillableSummaryBody, optional

        :param ci_pipeline_indexed_spans_sum: Response with properties for each aggregated usage type.
        :type ci_pipeline_indexed_spans_sum: UsageBillableSummaryBody, optional

        :param ci_pipeline_maximum: Response with properties for each aggregated usage type.
        :type ci_pipeline_maximum: UsageBillableSummaryBody, optional

        :param ci_pipeline_sum: Response with properties for each aggregated usage type.
        :type ci_pipeline_sum: UsageBillableSummaryBody, optional

        :param ci_test_indexed_spans_sum: Response with properties for each aggregated usage type.
        :type ci_test_indexed_spans_sum: UsageBillableSummaryBody, optional

        :param ci_testing_maximum: Response with properties for each aggregated usage type.
        :type ci_testing_maximum: UsageBillableSummaryBody, optional

        :param ci_testing_sum: Response with properties for each aggregated usage type.
        :type ci_testing_sum: UsageBillableSummaryBody, optional

        :param cspm_container_sum: Response with properties for each aggregated usage type.
        :type cspm_container_sum: UsageBillableSummaryBody, optional

        :param cspm_host_sum: Response with properties for each aggregated usage type.
        :type cspm_host_sum: UsageBillableSummaryBody, optional

        :param cspm_host_top99p: Response with properties for each aggregated usage type.
        :type cspm_host_top99p: UsageBillableSummaryBody, optional

        :param custom_event_sum: Response with properties for each aggregated usage type.
        :type custom_event_sum: UsageBillableSummaryBody, optional

        :param cws_container_sum: Response with properties for each aggregated usage type.
        :type cws_container_sum: UsageBillableSummaryBody, optional

        :param cws_host_sum: Response with properties for each aggregated usage type.
        :type cws_host_sum: UsageBillableSummaryBody, optional

        :param cws_host_top99p: Response with properties for each aggregated usage type.
        :type cws_host_top99p: UsageBillableSummaryBody, optional

        :param dbm_host_sum: Response with properties for each aggregated usage type.
        :type dbm_host_sum: UsageBillableSummaryBody, optional

        :param dbm_host_top99p: Response with properties for each aggregated usage type.
        :type dbm_host_top99p: UsageBillableSummaryBody, optional

        :param dbm_normalized_queries_average: Response with properties for each aggregated usage type.
        :type dbm_normalized_queries_average: UsageBillableSummaryBody, optional

        :param dbm_normalized_queries_sum: Response with properties for each aggregated usage type.
        :type dbm_normalized_queries_sum: UsageBillableSummaryBody, optional

        :param fargate_container_apm_and_profiler_average: Response with properties for each aggregated usage type.
        :type fargate_container_apm_and_profiler_average: UsageBillableSummaryBody, optional

        :param fargate_container_apm_and_profiler_sum: Response with properties for each aggregated usage type.
        :type fargate_container_apm_and_profiler_sum: UsageBillableSummaryBody, optional

        :param fargate_container_average: Response with properties for each aggregated usage type.
        :type fargate_container_average: UsageBillableSummaryBody, optional

        :param fargate_container_profiler_average: Response with properties for each aggregated usage type.
        :type fargate_container_profiler_average: UsageBillableSummaryBody, optional

        :param fargate_container_profiler_sum: Response with properties for each aggregated usage type.
        :type fargate_container_profiler_sum: UsageBillableSummaryBody, optional

        :param fargate_container_sum: Response with properties for each aggregated usage type.
        :type fargate_container_sum: UsageBillableSummaryBody, optional

        :param incident_management_maximum: Response with properties for each aggregated usage type.
        :type incident_management_maximum: UsageBillableSummaryBody, optional

        :param incident_management_sum: Response with properties for each aggregated usage type.
        :type incident_management_sum: UsageBillableSummaryBody, optional

        :param infra_and_apm_host_sum: Response with properties for each aggregated usage type.
        :type infra_and_apm_host_sum: UsageBillableSummaryBody, optional

        :param infra_and_apm_host_top99p: Response with properties for each aggregated usage type.
        :type infra_and_apm_host_top99p: UsageBillableSummaryBody, optional

        :param infra_container_sum: Response with properties for each aggregated usage type.
        :type infra_container_sum: UsageBillableSummaryBody, optional

        :param infra_host_sum: Response with properties for each aggregated usage type.
        :type infra_host_sum: UsageBillableSummaryBody, optional

        :param infra_host_top99p: Response with properties for each aggregated usage type.
        :type infra_host_top99p: UsageBillableSummaryBody, optional

        :param ingested_spans_sum: Response with properties for each aggregated usage type.
        :type ingested_spans_sum: UsageBillableSummaryBody, optional

        :param ingested_timeseries_average: Response with properties for each aggregated usage type.
        :type ingested_timeseries_average: UsageBillableSummaryBody, optional

        :param ingested_timeseries_sum: Response with properties for each aggregated usage type.
        :type ingested_timeseries_sum: UsageBillableSummaryBody, optional

        :param iot_sum: Response with properties for each aggregated usage type.
        :type iot_sum: UsageBillableSummaryBody, optional

        :param iot_top99p: Response with properties for each aggregated usage type.
        :type iot_top99p: UsageBillableSummaryBody, optional

        :param lambda_function_average: Response with properties for each aggregated usage type.
        :type lambda_function_average: UsageBillableSummaryBody, optional

        :param lambda_function_sum: Response with properties for each aggregated usage type.
        :type lambda_function_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_15day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_15day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_180day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_180day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_30day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_30day_sum: UsageBillableSummaryBody, optional

        :param logs_indexed_360day_sum: Response with properties for each aggregated usage type.
        :type logs_indexed_360day_sum: UsageBillableSummaryBody, optional

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

        :param network_device_sum: Response with properties for each aggregated usage type.
        :type network_device_sum: UsageBillableSummaryBody, optional

        :param network_device_top99p: Response with properties for each aggregated usage type.
        :type network_device_top99p: UsageBillableSummaryBody, optional

        :param npm_flow_sum: Response with properties for each aggregated usage type.
        :type npm_flow_sum: UsageBillableSummaryBody, optional

        :param npm_host_sum: Response with properties for each aggregated usage type.
        :type npm_host_sum: UsageBillableSummaryBody, optional

        :param npm_host_top99p: Response with properties for each aggregated usage type.
        :type npm_host_top99p: UsageBillableSummaryBody, optional

        :param observability_pipeline_sum: Response with properties for each aggregated usage type.
        :type observability_pipeline_sum: UsageBillableSummaryBody, optional

        :param online_archive_sum: Response with properties for each aggregated usage type.
        :type online_archive_sum: UsageBillableSummaryBody, optional

        :param prof_container_sum: Response with properties for each aggregated usage type.
        :type prof_container_sum: UsageBillableSummaryBody, optional

        :param prof_host_sum: Response with properties for each aggregated usage type.
        :type prof_host_sum: UsageBillableSummaryBody, optional

        :param prof_host_top99p: Response with properties for each aggregated usage type.
        :type prof_host_top99p: UsageBillableSummaryBody, optional

        :param rum_lite_sum: Response with properties for each aggregated usage type.
        :type rum_lite_sum: UsageBillableSummaryBody, optional

        :param rum_replay_sum: Response with properties for each aggregated usage type.
        :type rum_replay_sum: UsageBillableSummaryBody, optional

        :param rum_sum: Response with properties for each aggregated usage type.
        :type rum_sum: UsageBillableSummaryBody, optional

        :param rum_units_sum: Response with properties for each aggregated usage type.
        :type rum_units_sum: UsageBillableSummaryBody, optional

        :param sensitive_data_scanner_sum: Response with properties for each aggregated usage type.
        :type sensitive_data_scanner_sum: UsageBillableSummaryBody, optional

        :param serverless_invocation_sum: Response with properties for each aggregated usage type.
        :type serverless_invocation_sum: UsageBillableSummaryBody, optional

        :param siem_sum: Response with properties for each aggregated usage type.
        :type siem_sum: UsageBillableSummaryBody, optional

        :param standard_timeseries_average: Response with properties for each aggregated usage type.
        :type standard_timeseries_average: UsageBillableSummaryBody, optional

        :param synthetics_api_tests_sum: Response with properties for each aggregated usage type.
        :type synthetics_api_tests_sum: UsageBillableSummaryBody, optional

        :param synthetics_browser_checks_sum: Response with properties for each aggregated usage type.
        :type synthetics_browser_checks_sum: UsageBillableSummaryBody, optional

        :param timeseries_average: Response with properties for each aggregated usage type.
        :type timeseries_average: UsageBillableSummaryBody, optional

        :param timeseries_sum: Response with properties for each aggregated usage type.
        :type timeseries_sum: UsageBillableSummaryBody, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageBillableSummaryKeys, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
