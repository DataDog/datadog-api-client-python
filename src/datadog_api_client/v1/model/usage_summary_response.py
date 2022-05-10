# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_by_retention import LogsByRetention
    from datadog_api_client.v1.model.usage_summary_date import UsageSummaryDate

    globals()["LogsByRetention"] = LogsByRetention
    globals()["UsageSummaryDate"] = UsageSummaryDate


class UsageSummaryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "agent_host_top99p_sum": (int,),
            "apm_azure_app_service_host_top99p_sum": (int,),
            "apm_host_top99p_sum": (int,),
            "audit_logs_lines_indexed_agg_sum": (int,),
            "avg_profiled_fargate_tasks_sum": (int,),
            "aws_host_top99p_sum": (int,),
            "aws_lambda_func_count": (int,),
            "aws_lambda_invocations_sum": (int,),
            "azure_app_service_top99p_sum": (int,),
            "azure_host_top99p_sum": (int,),
            "billable_ingested_bytes_agg_sum": (int,),
            "browser_rum_lite_session_count_agg_sum": (int,),
            "browser_rum_replay_session_count_agg_sum": (int,),
            "browser_rum_units_agg_sum": (int,),
            "ci_pipeline_indexed_spans_agg_sum": (int,),
            "ci_test_indexed_spans_agg_sum": (int,),
            "ci_visibility_pipeline_committers_hwm_sum": (int,),
            "ci_visibility_test_committers_hwm_sum": (int,),
            "container_avg_sum": (int,),
            "container_hwm_sum": (int,),
            "cspm_aas_host_top99p_sum": (int,),
            "cspm_azure_host_top99p_sum": (int,),
            "cspm_container_avg_sum": (int,),
            "cspm_container_hwm_sum": (int,),
            "cspm_host_top99p_sum": (int,),
            "custom_ts_sum": (int,),
            "cws_containers_avg_sum": (int,),
            "cws_host_top99p_sum": (int,),
            "dbm_host_top99p_sum": (int,),
            "dbm_queries_avg_sum": (int,),
            "end_date": (datetime,),
            "fargate_tasks_count_avg_sum": (int,),
            "fargate_tasks_count_hwm_sum": (int,),
            "gcp_host_top99p_sum": (int,),
            "heroku_host_top99p_sum": (int,),
            "incident_management_monthly_active_users_hwm_sum": (int,),
            "indexed_events_count_agg_sum": (int,),
            "infra_host_top99p_sum": (int,),
            "ingested_events_bytes_agg_sum": (int,),
            "iot_device_agg_sum": (int,),
            "iot_device_top99p_sum": (int,),
            "last_updated": (datetime,),
            "live_indexed_events_agg_sum": (int,),
            "live_ingested_bytes_agg_sum": (int,),
            "logs_by_retention": (LogsByRetention,),
            "mobile_rum_lite_session_count_agg_sum": (int,),
            "mobile_rum_session_count_agg_sum": (int,),
            "mobile_rum_session_count_android_agg_sum": (int,),
            "mobile_rum_session_count_ios_agg_sum": (int,),
            "mobile_rum_session_count_reactnative_agg_sum": (int,),
            "mobile_rum_units_agg_sum": (int,),
            "netflow_indexed_events_count_agg_sum": (int,),
            "npm_host_top99p_sum": (int,),
            "observability_pipelines_bytes_processed_agg_sum": (int,),
            "online_archive_events_count_agg_sum": (int,),
            "opentelemetry_host_top99p_sum": (int,),
            "profiling_container_agent_count_avg": (int,),
            "profiling_host_count_top99p_sum": (int,),
            "rehydrated_indexed_events_agg_sum": (int,),
            "rehydrated_ingested_bytes_agg_sum": (int,),
            "rum_browser_and_mobile_session_count": (int,),
            "rum_session_count_agg_sum": (int,),
            "rum_total_session_count_agg_sum": (int,),
            "rum_units_agg_sum": (int,),
            "sds_logs_scanned_bytes_sum": (int,),
            "sds_total_scanned_bytes_sum": (int,),
            "start_date": (datetime,),
            "synthetics_browser_check_calls_count_agg_sum": (int,),
            "synthetics_check_calls_count_agg_sum": (int,),
            "trace_search_indexed_events_count_agg_sum": (int,),
            "twol_ingested_events_bytes_agg_sum": (int,),
            "usage": ([UsageSummaryDate],),
            "vsphere_host_top99p_sum": (int,),
        }

    attribute_map = {
        "agent_host_top99p_sum": "agent_host_top99p_sum",
        "apm_azure_app_service_host_top99p_sum": "apm_azure_app_service_host_top99p_sum",
        "apm_host_top99p_sum": "apm_host_top99p_sum",
        "audit_logs_lines_indexed_agg_sum": "audit_logs_lines_indexed_agg_sum",
        "avg_profiled_fargate_tasks_sum": "avg_profiled_fargate_tasks_sum",
        "aws_host_top99p_sum": "aws_host_top99p_sum",
        "aws_lambda_func_count": "aws_lambda_func_count",
        "aws_lambda_invocations_sum": "aws_lambda_invocations_sum",
        "azure_app_service_top99p_sum": "azure_app_service_top99p_sum",
        "azure_host_top99p_sum": "azure_host_top99p_sum",
        "billable_ingested_bytes_agg_sum": "billable_ingested_bytes_agg_sum",
        "browser_rum_lite_session_count_agg_sum": "browser_rum_lite_session_count_agg_sum",
        "browser_rum_replay_session_count_agg_sum": "browser_rum_replay_session_count_agg_sum",
        "browser_rum_units_agg_sum": "browser_rum_units_agg_sum",
        "ci_pipeline_indexed_spans_agg_sum": "ci_pipeline_indexed_spans_agg_sum",
        "ci_test_indexed_spans_agg_sum": "ci_test_indexed_spans_agg_sum",
        "ci_visibility_pipeline_committers_hwm_sum": "ci_visibility_pipeline_committers_hwm_sum",
        "ci_visibility_test_committers_hwm_sum": "ci_visibility_test_committers_hwm_sum",
        "container_avg_sum": "container_avg_sum",
        "container_hwm_sum": "container_hwm_sum",
        "cspm_aas_host_top99p_sum": "cspm_aas_host_top99p_sum",
        "cspm_azure_host_top99p_sum": "cspm_azure_host_top99p_sum",
        "cspm_container_avg_sum": "cspm_container_avg_sum",
        "cspm_container_hwm_sum": "cspm_container_hwm_sum",
        "cspm_host_top99p_sum": "cspm_host_top99p_sum",
        "custom_ts_sum": "custom_ts_sum",
        "cws_containers_avg_sum": "cws_containers_avg_sum",
        "cws_host_top99p_sum": "cws_host_top99p_sum",
        "dbm_host_top99p_sum": "dbm_host_top99p_sum",
        "dbm_queries_avg_sum": "dbm_queries_avg_sum",
        "end_date": "end_date",
        "fargate_tasks_count_avg_sum": "fargate_tasks_count_avg_sum",
        "fargate_tasks_count_hwm_sum": "fargate_tasks_count_hwm_sum",
        "gcp_host_top99p_sum": "gcp_host_top99p_sum",
        "heroku_host_top99p_sum": "heroku_host_top99p_sum",
        "incident_management_monthly_active_users_hwm_sum": "incident_management_monthly_active_users_hwm_sum",
        "indexed_events_count_agg_sum": "indexed_events_count_agg_sum",
        "infra_host_top99p_sum": "infra_host_top99p_sum",
        "ingested_events_bytes_agg_sum": "ingested_events_bytes_agg_sum",
        "iot_device_agg_sum": "iot_device_agg_sum",
        "iot_device_top99p_sum": "iot_device_top99p_sum",
        "last_updated": "last_updated",
        "live_indexed_events_agg_sum": "live_indexed_events_agg_sum",
        "live_ingested_bytes_agg_sum": "live_ingested_bytes_agg_sum",
        "logs_by_retention": "logs_by_retention",
        "mobile_rum_lite_session_count_agg_sum": "mobile_rum_lite_session_count_agg_sum",
        "mobile_rum_session_count_agg_sum": "mobile_rum_session_count_agg_sum",
        "mobile_rum_session_count_android_agg_sum": "mobile_rum_session_count_android_agg_sum",
        "mobile_rum_session_count_ios_agg_sum": "mobile_rum_session_count_ios_agg_sum",
        "mobile_rum_session_count_reactnative_agg_sum": "mobile_rum_session_count_reactnative_agg_sum",
        "mobile_rum_units_agg_sum": "mobile_rum_units_agg_sum",
        "netflow_indexed_events_count_agg_sum": "netflow_indexed_events_count_agg_sum",
        "npm_host_top99p_sum": "npm_host_top99p_sum",
        "observability_pipelines_bytes_processed_agg_sum": "observability_pipelines_bytes_processed_agg_sum",
        "online_archive_events_count_agg_sum": "online_archive_events_count_agg_sum",
        "opentelemetry_host_top99p_sum": "opentelemetry_host_top99p_sum",
        "profiling_container_agent_count_avg": "profiling_container_agent_count_avg",
        "profiling_host_count_top99p_sum": "profiling_host_count_top99p_sum",
        "rehydrated_indexed_events_agg_sum": "rehydrated_indexed_events_agg_sum",
        "rehydrated_ingested_bytes_agg_sum": "rehydrated_ingested_bytes_agg_sum",
        "rum_browser_and_mobile_session_count": "rum_browser_and_mobile_session_count",
        "rum_session_count_agg_sum": "rum_session_count_agg_sum",
        "rum_total_session_count_agg_sum": "rum_total_session_count_agg_sum",
        "rum_units_agg_sum": "rum_units_agg_sum",
        "sds_logs_scanned_bytes_sum": "sds_logs_scanned_bytes_sum",
        "sds_total_scanned_bytes_sum": "sds_total_scanned_bytes_sum",
        "start_date": "start_date",
        "synthetics_browser_check_calls_count_agg_sum": "synthetics_browser_check_calls_count_agg_sum",
        "synthetics_check_calls_count_agg_sum": "synthetics_check_calls_count_agg_sum",
        "trace_search_indexed_events_count_agg_sum": "trace_search_indexed_events_count_agg_sum",
        "twol_ingested_events_bytes_agg_sum": "twol_ingested_events_bytes_agg_sum",
        "usage": "usage",
        "vsphere_host_top99p_sum": "vsphere_host_top99p_sum",
    }

    def __init__(self, *args, **kwargs):
        """
        Response summarizing all usage aggregated across the months in the request for all organizations, and broken down by month and by organization.

        :param agent_host_top99p_sum: Shows the 99th percentile of all agent hosts over all hours in the current months for all organizations.
        :type agent_host_top99p_sum: int, optional

        :param apm_azure_app_service_host_top99p_sum: Shows the 99th percentile of all Azure app services using APM over all hours in the current months all organizations.
        :type apm_azure_app_service_host_top99p_sum: int, optional

        :param apm_host_top99p_sum: Shows the 99th percentile of all distinct APM hosts over all hours in the current months for all organizations.
        :type apm_host_top99p_sum: int, optional

        :param audit_logs_lines_indexed_agg_sum: Shows the sum of all audit logs lines indexed over all hours in the current months for all organizations.
        :type audit_logs_lines_indexed_agg_sum: int, optional

        :param avg_profiled_fargate_tasks_sum: Shows the average of all profiled Fargate tasks over all hours in the current months for all organizations.
        :type avg_profiled_fargate_tasks_sum: int, optional

        :param aws_host_top99p_sum: Shows the 99th percentile of all AWS hosts over all hours in the current months for all organizations.
        :type aws_host_top99p_sum: int, optional

        :param aws_lambda_func_count: Shows the average of the number of functions that executed 1 or more times each hour in the current months for all organizations.
        :type aws_lambda_func_count: int, optional

        :param aws_lambda_invocations_sum: Shows the sum of all AWS Lambda invocations over all hours in the current months for all organizations.
        :type aws_lambda_invocations_sum: int, optional

        :param azure_app_service_top99p_sum: Shows the 99th percentile of all Azure app services over all hours in the current months for all organizations.
        :type azure_app_service_top99p_sum: int, optional

        :param azure_host_top99p_sum: Shows the 99th percentile of all Azure hosts over all hours in the current months for all organizations.
        :type azure_host_top99p_sum: int, optional

        :param billable_ingested_bytes_agg_sum: Shows the sum of all log bytes ingested over all hours in the current months for all organizations.
        :type billable_ingested_bytes_agg_sum: int, optional

        :param browser_rum_lite_session_count_agg_sum: Shows the sum of all browser lite sessions over all hours in the current months for all organizations.
        :type browser_rum_lite_session_count_agg_sum: int, optional

        :param browser_rum_replay_session_count_agg_sum: Shows the sum of all browser replay sessions over all hours in the current months for all organizations.
        :type browser_rum_replay_session_count_agg_sum: int, optional

        :param browser_rum_units_agg_sum: Shows the sum of all browser RUM units over all hours in the current months for all organizations.
        :type browser_rum_units_agg_sum: int, optional

        :param ci_pipeline_indexed_spans_agg_sum: Shows the sum of all CI pipeline indexed spans over all hours in the current months for all organizations.
        :type ci_pipeline_indexed_spans_agg_sum: int, optional

        :param ci_test_indexed_spans_agg_sum: Shows the sum of all CI test indexed spans over all hours in the current months for all organizations.
        :type ci_test_indexed_spans_agg_sum: int, optional

        :param ci_visibility_pipeline_committers_hwm_sum: Shows the high-water mark of all CI visibility pipeline committers over all hours in the current months for all organizations.
        :type ci_visibility_pipeline_committers_hwm_sum: int, optional

        :param ci_visibility_test_committers_hwm_sum: Shows the high-water mark of all CI visibility test committers over all hours in the current months for all organizations.
        :type ci_visibility_test_committers_hwm_sum: int, optional

        :param container_avg_sum: Shows the average of all distinct containers over all hours in the current months for all organizations.
        :type container_avg_sum: int, optional

        :param container_hwm_sum: Shows the sum of the high-water marks of all distinct containers over all hours in the current months for all organizations.
        :type container_hwm_sum: int, optional

        :param cspm_aas_host_top99p_sum: Shows the 99th percentile of all Cloud Security Posture Management Azure app services hosts over all hours in the current months for all organizations.
        :type cspm_aas_host_top99p_sum: int, optional

        :param cspm_azure_host_top99p_sum: Shows the 99th percentile of all Cloud Security Posture Management Azure hosts over all hours in the current months for all organizations.
        :type cspm_azure_host_top99p_sum: int, optional

        :param cspm_container_avg_sum: Shows the average number of Cloud Security Posture Management containers over all hours in the current months for all organizations.
        :type cspm_container_avg_sum: int, optional

        :param cspm_container_hwm_sum: Shows the sum of the the high-water marks of Cloud Security Posture Management containers over all hours in the current months for all organizations.
        :type cspm_container_hwm_sum: int, optional

        :param cspm_host_top99p_sum: Shows the 99th percentile of all Cloud Security Posture Management hosts over all hours in the current months for all organizations.
        :type cspm_host_top99p_sum: int, optional

        :param custom_ts_sum: Shows the average number of distinct custom metrics over all hours in the current months for all organizations.
        :type custom_ts_sum: int, optional

        :param cws_containers_avg_sum: Shows the average of all distinct Cloud Workload Security containers over all hours in the current months for all organizations.
        :type cws_containers_avg_sum: int, optional

        :param cws_host_top99p_sum: Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current months for all organizations.
        :type cws_host_top99p_sum: int, optional

        :param dbm_host_top99p_sum: Shows the 99th percentile of all Database Monitoring hosts over all hours in the current month for all organizations.
        :type dbm_host_top99p_sum: int, optional

        :param dbm_queries_avg_sum: Shows the average of all distinct Database Monitoring Normalized Queries over all hours in the current month for all organizations.
        :type dbm_queries_avg_sum: int, optional

        :param end_date: Shows the last date of usage in the current months for all organizations.
        :type end_date: datetime, optional

        :param fargate_tasks_count_avg_sum: Shows the average of all Fargate tasks over all hours in the current months for all organizations.
        :type fargate_tasks_count_avg_sum: int, optional

        :param fargate_tasks_count_hwm_sum: Shows the sum of the high-water marks of all Fargate tasks over all hours in the current months for all organizations.
        :type fargate_tasks_count_hwm_sum: int, optional

        :param gcp_host_top99p_sum: Shows the 99th percentile of all GCP hosts over all hours in the current months for all organizations.
        :type gcp_host_top99p_sum: int, optional

        :param heroku_host_top99p_sum: Shows the 99th percentile of all Heroku dynos over all hours in the current months for all organizations.
        :type heroku_host_top99p_sum: int, optional

        :param incident_management_monthly_active_users_hwm_sum: Shows sum of the the high-water marks of incident management monthly active users in the current months for all organizations.
        :type incident_management_monthly_active_users_hwm_sum: int, optional

        :param indexed_events_count_agg_sum: Shows the sum of all log events indexed over all hours in the current months for all organizations.
        :type indexed_events_count_agg_sum: int, optional

        :param infra_host_top99p_sum: Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current months for all organizations.
        :type infra_host_top99p_sum: int, optional

        :param ingested_events_bytes_agg_sum: Shows the sum of all log bytes ingested over all hours in the current months for all organizations.
        :type ingested_events_bytes_agg_sum: int, optional

        :param iot_device_agg_sum: Shows the sum of all IoT devices over all hours in the current months for all organizations.
        :type iot_device_agg_sum: int, optional

        :param iot_device_top99p_sum: Shows the 99th percentile of all IoT devices over all hours in the current months of all organizations.
        :type iot_device_top99p_sum: int, optional

        :param last_updated: Shows the the most recent hour in the current months for all organizations for which all usages were calculated.
        :type last_updated: datetime, optional

        :param live_indexed_events_agg_sum: Shows the sum of all live logs indexed over all hours in the current months for all organizations (data available as of December 1, 2020).
        :type live_indexed_events_agg_sum: int, optional

        :param live_ingested_bytes_agg_sum: Shows the sum of all live logs bytes ingested over all hours in the current months for all organizations (data available as of December 1, 2020).
        :type live_ingested_bytes_agg_sum: int, optional

        :param logs_by_retention: Object containing logs usage data broken down by retention period.
        :type logs_by_retention: LogsByRetention, optional

        :param mobile_rum_lite_session_count_agg_sum: Shows the sum of all mobile lite sessions over all hours in the current months for all organizations.
        :type mobile_rum_lite_session_count_agg_sum: int, optional

        :param mobile_rum_session_count_agg_sum: Shows the sum of all mobile RUM Sessions over all hours in the current months for all organizations.
        :type mobile_rum_session_count_agg_sum: int, optional

        :param mobile_rum_session_count_android_agg_sum: Shows the sum of all mobile RUM Sessions on Android over all hours in the current months for all organizations.
        :type mobile_rum_session_count_android_agg_sum: int, optional

        :param mobile_rum_session_count_ios_agg_sum: Shows the sum of all mobile RUM Sessions on iOS over all hours in the current months for all organizations.
        :type mobile_rum_session_count_ios_agg_sum: int, optional

        :param mobile_rum_session_count_reactnative_agg_sum: Shows the sum of all mobile RUM Sessions on React Native over all hours in the current months for all organizations.
        :type mobile_rum_session_count_reactnative_agg_sum: int, optional

        :param mobile_rum_units_agg_sum: Shows the sum of all mobile RUM units over all hours in the current months for all organizations.
        :type mobile_rum_units_agg_sum: int, optional

        :param netflow_indexed_events_count_agg_sum: Shows the sum of all Network flows indexed over all hours in the current months for all organizations.
        :type netflow_indexed_events_count_agg_sum: int, optional

        :param npm_host_top99p_sum: Shows the 99th percentile of all distinct Networks hosts over all hours in the current months for all organizations.
        :type npm_host_top99p_sum: int, optional

        :param observability_pipelines_bytes_processed_agg_sum: Sum of all observability pipelines bytes processed over all hours in the current months for all organizations.
        :type observability_pipelines_bytes_processed_agg_sum: int, optional

        :param online_archive_events_count_agg_sum: Sum of all online archived events over all hours in the current months for all organizations.
        :type online_archive_events_count_agg_sum: int, optional

        :param opentelemetry_host_top99p_sum: Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current months for all organizations.
        :type opentelemetry_host_top99p_sum: int, optional

        :param profiling_container_agent_count_avg: Shows the average number of profiled containers over all hours in the current months for all organizations.
        :type profiling_container_agent_count_avg: int, optional

        :param profiling_host_count_top99p_sum: Shows the 99th percentile of all profiled hosts over all hours in the current months for all organizations.
        :type profiling_host_count_top99p_sum: int, optional

        :param rehydrated_indexed_events_agg_sum: Shows the sum of all rehydrated logs indexed over all hours in the current months for all organizations (data available as of December 1, 2020).
        :type rehydrated_indexed_events_agg_sum: int, optional

        :param rehydrated_ingested_bytes_agg_sum: Shows the sum of all rehydrated logs bytes ingested over all hours in the current months for all organizations (data available as of December 1, 2020).
        :type rehydrated_ingested_bytes_agg_sum: int, optional

        :param rum_browser_and_mobile_session_count: Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current month for all organizations.
        :type rum_browser_and_mobile_session_count: int, optional

        :param rum_session_count_agg_sum: Shows the sum of all browser RUM Lite Sessions over all hours in the current months for all organizations.
        :type rum_session_count_agg_sum: int, optional

        :param rum_total_session_count_agg_sum: Shows the sum of RUM Sessions (browser and mobile) over all hours in the current months for all organizations.
        :type rum_total_session_count_agg_sum: int, optional

        :param rum_units_agg_sum: Shows the sum of all browser and mobile RUM units over all hours in the current months for all organizations.
        :type rum_units_agg_sum: int, optional

        :param sds_logs_scanned_bytes_sum: Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for all organizations.
        :type sds_logs_scanned_bytes_sum: int, optional

        :param sds_total_scanned_bytes_sum: Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for all organizations.
        :type sds_total_scanned_bytes_sum: int, optional

        :param start_date: Shows the first date of usage in the current months for all organizations.
        :type start_date: datetime, optional

        :param synthetics_browser_check_calls_count_agg_sum: Shows the sum of all Synthetic browser tests over all hours in the current months for all organizations.
        :type synthetics_browser_check_calls_count_agg_sum: int, optional

        :param synthetics_check_calls_count_agg_sum: Shows the sum of all Synthetic API tests over all hours in the current months for all organizations.
        :type synthetics_check_calls_count_agg_sum: int, optional

        :param trace_search_indexed_events_count_agg_sum: Shows the sum of all Indexed Spans indexed over all hours in the current months for all organizations.
        :type trace_search_indexed_events_count_agg_sum: int, optional

        :param twol_ingested_events_bytes_agg_sum: Shows the sum of all ingested APM span bytes over all hours in the current months for all organizations.
        :type twol_ingested_events_bytes_agg_sum: int, optional

        :param usage: An array of objects regarding hourly usage.
        :type usage: [UsageSummaryDate], optional

        :param vsphere_host_top99p_sum: Shows the 99th percentile of all vSphere hosts over all hours in the current months for all organizations.
        :type vsphere_host_top99p_sum: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSummaryResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
