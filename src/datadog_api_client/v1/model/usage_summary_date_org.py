# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageSummaryDateOrg(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "agent_host_top99p": (int,),
            "apm_azure_app_service_host_top99p": (int,),
            "apm_host_top99p": (int,),
            "audit_logs_lines_indexed_sum": (int,),
            "avg_profiled_fargate_tasks": (int,),
            "aws_host_top99p": (int,),
            "aws_lambda_func_count": (int,),
            "aws_lambda_invocations_sum": (int,),
            "azure_app_service_top99p": (int,),
            "billable_ingested_bytes_sum": (int,),
            "browser_rum_lite_session_count_sum": (int,),
            "browser_rum_replay_session_count_sum": (int,),
            "browser_rum_units_sum": (int,),
            "container_avg": (int,),
            "container_hwm": (int,),
            "cspm_aas_host_top99p": (int,),
            "cspm_azure_host_top99p": (int,),
            "cspm_container_avg": (int,),
            "cspm_container_hwm": (int,),
            "cspm_host_top99p": (int,),
            "custom_ts_avg": (int,),
            "cws_container_count_avg": (int,),
            "cws_host_top99p": (int,),
            "dbm_host_top99p_sum": (int,),
            "dbm_queries_avg_sum": (int,),
            "fargate_tasks_count_avg": (int,),
            "fargate_tasks_count_hwm": (int,),
            "gcp_host_top99p": (int,),
            "heroku_host_top99p": (int,),
            "id": (str,),
            "incident_management_monthly_active_users_hwm": (int,),
            "indexed_events_count_sum": (int,),
            "infra_host_top99p": (int,),
            "ingested_events_bytes_sum": (int,),
            "iot_device_agg_sum": (int,),
            "iot_device_top99p_sum": (int,),
            "mobile_rum_lite_session_count_sum": (int,),
            "mobile_rum_session_count_android_sum": (int,),
            "mobile_rum_session_count_ios_sum": (int,),
            "mobile_rum_session_count_sum": (int,),
            "mobile_rum_units_sum": (int,),
            "name": (str,),
            "netflow_indexed_events_count_sum": (int,),
            "npm_host_top99p": (int,),
            "opentelemetry_host_top99p": (int,),
            "profiling_host_top99p": (int,),
            "public_id": (str,),
            "rum_browser_and_mobile_session_count": (int,),
            "rum_session_count_sum": (int,),
            "rum_total_session_count_sum": (int,),
            "rum_units_sum": (int,),
            "sds_logs_scanned_bytes_sum": (int,),
            "sds_total_scanned_bytes_sum": (int,),
            "synthetics_browser_check_calls_count_sum": (int,),
            "synthetics_check_calls_count_sum": (int,),
            "trace_search_indexed_events_count_sum": (int,),
            "twol_ingested_events_bytes_sum": (int,),
            "vsphere_host_top99p": (int,),
        }

    attribute_map = {
        "agent_host_top99p": "agent_host_top99p",
        "apm_azure_app_service_host_top99p": "apm_azure_app_service_host_top99p",
        "apm_host_top99p": "apm_host_top99p",
        "audit_logs_lines_indexed_sum": "audit_logs_lines_indexed_sum",
        "avg_profiled_fargate_tasks": "avg_profiled_fargate_tasks",
        "aws_host_top99p": "aws_host_top99p",
        "aws_lambda_func_count": "aws_lambda_func_count",
        "aws_lambda_invocations_sum": "aws_lambda_invocations_sum",
        "azure_app_service_top99p": "azure_app_service_top99p",
        "billable_ingested_bytes_sum": "billable_ingested_bytes_sum",
        "browser_rum_lite_session_count_sum": "browser_rum_lite_session_count_sum",
        "browser_rum_replay_session_count_sum": "browser_rum_replay_session_count_sum",
        "browser_rum_units_sum": "browser_rum_units_sum",
        "container_avg": "container_avg",
        "container_hwm": "container_hwm",
        "cspm_aas_host_top99p": "cspm_aas_host_top99p",
        "cspm_azure_host_top99p": "cspm_azure_host_top99p",
        "cspm_container_avg": "cspm_container_avg",
        "cspm_container_hwm": "cspm_container_hwm",
        "cspm_host_top99p": "cspm_host_top99p",
        "custom_ts_avg": "custom_ts_avg",
        "cws_container_count_avg": "cws_container_count_avg",
        "cws_host_top99p": "cws_host_top99p",
        "dbm_host_top99p_sum": "dbm_host_top99p_sum",
        "dbm_queries_avg_sum": "dbm_queries_avg_sum",
        "fargate_tasks_count_avg": "fargate_tasks_count_avg",
        "fargate_tasks_count_hwm": "fargate_tasks_count_hwm",
        "gcp_host_top99p": "gcp_host_top99p",
        "heroku_host_top99p": "heroku_host_top99p",
        "id": "id",
        "incident_management_monthly_active_users_hwm": "incident_management_monthly_active_users_hwm",
        "indexed_events_count_sum": "indexed_events_count_sum",
        "infra_host_top99p": "infra_host_top99p",
        "ingested_events_bytes_sum": "ingested_events_bytes_sum",
        "iot_device_agg_sum": "iot_device_agg_sum",
        "iot_device_top99p_sum": "iot_device_top99p_sum",
        "mobile_rum_lite_session_count_sum": "mobile_rum_lite_session_count_sum",
        "mobile_rum_session_count_android_sum": "mobile_rum_session_count_android_sum",
        "mobile_rum_session_count_ios_sum": "mobile_rum_session_count_ios_sum",
        "mobile_rum_session_count_sum": "mobile_rum_session_count_sum",
        "mobile_rum_units_sum": "mobile_rum_units_sum",
        "name": "name",
        "netflow_indexed_events_count_sum": "netflow_indexed_events_count_sum",
        "npm_host_top99p": "npm_host_top99p",
        "opentelemetry_host_top99p": "opentelemetry_host_top99p",
        "profiling_host_top99p": "profiling_host_top99p",
        "public_id": "public_id",
        "rum_browser_and_mobile_session_count": "rum_browser_and_mobile_session_count",
        "rum_session_count_sum": "rum_session_count_sum",
        "rum_total_session_count_sum": "rum_total_session_count_sum",
        "rum_units_sum": "rum_units_sum",
        "sds_logs_scanned_bytes_sum": "sds_logs_scanned_bytes_sum",
        "sds_total_scanned_bytes_sum": "sds_total_scanned_bytes_sum",
        "synthetics_browser_check_calls_count_sum": "synthetics_browser_check_calls_count_sum",
        "synthetics_check_calls_count_sum": "synthetics_check_calls_count_sum",
        "trace_search_indexed_events_count_sum": "trace_search_indexed_events_count_sum",
        "twol_ingested_events_bytes_sum": "twol_ingested_events_bytes_sum",
        "vsphere_host_top99p": "vsphere_host_top99p",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Global hourly report of all data billed by Datadog for a given organization.

        :param agent_host_top99p: Shows the 99th percentile of all agent hosts over all hours in the current date for the given org.
        :type agent_host_top99p: int, optional

        :param apm_azure_app_service_host_top99p: Shows the 99th percentile of all Azure app services using APM over all hours in the current date for the given org.
        :type apm_azure_app_service_host_top99p: int, optional

        :param apm_host_top99p: Shows the 99th percentile of all distinct APM hosts over all hours in the current date for the given org.
        :type apm_host_top99p: int, optional

        :param audit_logs_lines_indexed_sum: Shows the sum of all audit logs lines indexed over all hours in the current date for the given org.
        :type audit_logs_lines_indexed_sum: int, optional

        :param avg_profiled_fargate_tasks: The average profiled task count for Fargate Profiling.
        :type avg_profiled_fargate_tasks: int, optional

        :param aws_host_top99p: Shows the 99th percentile of all AWS hosts over all hours in the current date for the given org.
        :type aws_host_top99p: int, optional

        :param aws_lambda_func_count: Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org.
        :type aws_lambda_func_count: int, optional

        :param aws_lambda_invocations_sum: Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org.
        :type aws_lambda_invocations_sum: int, optional

        :param azure_app_service_top99p: Shows the 99th percentile of all Azure app services over all hours in the current date for the given org.
        :type azure_app_service_top99p: int, optional

        :param billable_ingested_bytes_sum: Shows the sum of all log bytes ingested over all hours in the current date for the given org.
        :type billable_ingested_bytes_sum: int, optional

        :param browser_rum_lite_session_count_sum: Shows the sum of all browser lite sessions over all hours in the current date for the given org.
        :type browser_rum_lite_session_count_sum: int, optional

        :param browser_rum_replay_session_count_sum: Shows the sum of all browser replay sessions over all hours in the current date for the given org.
        :type browser_rum_replay_session_count_sum: int, optional

        :param browser_rum_units_sum: Shows the sum of all browser RUM units over all hours in the current date for the given org.
        :type browser_rum_units_sum: int, optional

        :param container_avg: Shows the average of all distinct containers over all hours in the current date for the given org.
        :type container_avg: int, optional

        :param container_hwm: Shows the high-water mark of all distinct containers over all hours in the current date for the given org.
        :type container_hwm: int, optional

        :param cspm_aas_host_top99p: Shows the 99th percentile of all Cloud Security Posture Management Azure app services hosts over all hours in the current date for the given org.
        :type cspm_aas_host_top99p: int, optional

        :param cspm_azure_host_top99p: Shows the 99th percentile of all Cloud Security Posture Management Azure hosts over all hours in the current date for the given org.
        :type cspm_azure_host_top99p: int, optional

        :param cspm_container_avg: Shows the average number of Cloud Security Posture Management containers over all hours in the current date for the given org.
        :type cspm_container_avg: int, optional

        :param cspm_container_hwm: Shows the high-water mark of Cloud Security Posture Management containers over all hours in the current date for the given org.
        :type cspm_container_hwm: int, optional

        :param cspm_host_top99p: Shows the 99th percentile of all Cloud Security Posture Management hosts over all hours in the current date for the given org.
        :type cspm_host_top99p: int, optional

        :param custom_ts_avg: Shows the average number of distinct custom metrics over all hours in the current date for the given org.
        :type custom_ts_avg: int, optional

        :param cws_container_count_avg: Shows the average of all distinct Cloud Workload Security containers over all hours in the current date for the given org.
        :type cws_container_count_avg: int, optional

        :param cws_host_top99p: Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current date for the given org.
        :type cws_host_top99p: int, optional

        :param dbm_host_top99p_sum: Shows the 99th percentile of all Database Monitoring hosts over all hours in the current month for the given org.
        :type dbm_host_top99p_sum: int, optional

        :param dbm_queries_avg_sum: Shows the average of all distinct Database Monitoring normalized queries over all hours in the current month for the given org.
        :type dbm_queries_avg_sum: int, optional

        :param fargate_tasks_count_avg: The average task count for Fargate.
        :type fargate_tasks_count_avg: int, optional

        :param fargate_tasks_count_hwm: Shows the high-water mark of all Fargate tasks over all hours in the current date for the given org.
        :type fargate_tasks_count_hwm: int, optional

        :param gcp_host_top99p: Shows the 99th percentile of all GCP hosts over all hours in the current date for the given org.
        :type gcp_host_top99p: int, optional

        :param heroku_host_top99p: Shows the 99th percentile of all Heroku dynos over all hours in the current date for the given org.
        :type heroku_host_top99p: int, optional

        :param id: The organization id.
        :type id: str, optional

        :param incident_management_monthly_active_users_hwm: Shows the high-water mark of incident management monthly active users over all hours in the current date for the given org.
        :type incident_management_monthly_active_users_hwm: int, optional

        :param indexed_events_count_sum: Shows the sum of all log events indexed over all hours in the current date for the given org.
        :type indexed_events_count_sum: int, optional

        :param infra_host_top99p: Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for the given org.
        :type infra_host_top99p: int, optional

        :param ingested_events_bytes_sum: Shows the sum of all log bytes ingested over all hours in the current date for the given org.
        :type ingested_events_bytes_sum: int, optional

        :param iot_device_agg_sum: Shows the sum of all IoT devices over all hours in the current date for the given org.
        :type iot_device_agg_sum: int, optional

        :param iot_device_top99p_sum: Shows the 99th percentile of all IoT devices over all hours in the current date for the given org.
        :type iot_device_top99p_sum: int, optional

        :param mobile_rum_lite_session_count_sum: Shows the sum of all mobile lite sessions over all hours in the current date for the given org.
        :type mobile_rum_lite_session_count_sum: int, optional

        :param mobile_rum_session_count_android_sum: Shows the sum of all mobile RUM Sessions on Android over all hours in the current date for the given org.
        :type mobile_rum_session_count_android_sum: int, optional

        :param mobile_rum_session_count_ios_sum: Shows the sum of all mobile RUM Sessions on iOS over all hours in the current date for the given org.
        :type mobile_rum_session_count_ios_sum: int, optional

        :param mobile_rum_session_count_sum: Shows the sum of all mobile RUM Sessions over all hours in the current date for the given org.
        :type mobile_rum_session_count_sum: int, optional

        :param mobile_rum_units_sum: Shows the sum of all mobile RUM units over all hours in the current date for the given org.
        :type mobile_rum_units_sum: int, optional

        :param name: The organization name.
        :type name: str, optional

        :param netflow_indexed_events_count_sum: Shows the sum of all Network flows indexed over all hours in the current date for the given org.
        :type netflow_indexed_events_count_sum: int, optional

        :param npm_host_top99p: Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for the given org.
        :type npm_host_top99p: int, optional

        :param opentelemetry_host_top99p: Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
        :type opentelemetry_host_top99p: int, optional

        :param profiling_host_top99p: Shows the 99th percentile of all profiled hosts over all hours in the current date for the given org.
        :type profiling_host_top99p: int, optional

        :param public_id: The organization public id.
        :type public_id: str, optional

        :param rum_browser_and_mobile_session_count: Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current date for the given org.
        :type rum_browser_and_mobile_session_count: int, optional

        :param rum_session_count_sum: Shows the sum of all browser RUM Lite Sessions over all hours in the current date for the given org.
        :type rum_session_count_sum: int, optional

        :param rum_total_session_count_sum: Shows the sum of RUM Sessions (browser and mobile) over all hours in the current date for the given org.
        :type rum_total_session_count_sum: int, optional

        :param rum_units_sum: Shows the sum of all browser and mobile RUM units over all hours in the current date for the given org.
        :type rum_units_sum: int, optional

        :param sds_logs_scanned_bytes_sum: Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for the given org.
        :type sds_logs_scanned_bytes_sum: int, optional

        :param sds_total_scanned_bytes_sum: Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for the given org.
        :type sds_total_scanned_bytes_sum: int, optional

        :param synthetics_browser_check_calls_count_sum: Shows the sum of all Synthetic browser tests over all hours in the current date for the given org.
        :type synthetics_browser_check_calls_count_sum: int, optional

        :param synthetics_check_calls_count_sum: Shows the sum of all Synthetic API tests over all hours in the current date for the given org.
        :type synthetics_check_calls_count_sum: int, optional

        :param trace_search_indexed_events_count_sum: Shows the sum of all Indexed Spans indexed over all hours in the current date for the given org.
        :type trace_search_indexed_events_count_sum: int, optional

        :param twol_ingested_events_bytes_sum: Shows the sum of all tracing without limits bytes ingested over all hours in the current date for the given org.
        :type twol_ingested_events_bytes_sum: int, optional

        :param vsphere_host_top99p: Shows the 99th percentile of all vSphere hosts over all hours in the current date for the given org.
        :type vsphere_host_top99p: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSummaryDateOrg, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
