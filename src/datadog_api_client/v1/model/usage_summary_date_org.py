# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class UsageSummaryDateOrg(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_host_top99p": (int,),
            "apm_azure_app_service_host_top99p": (int,),
            "apm_devsecops_host_top99p": (int,),
            "apm_fargate_count_avg": (int,),
            "apm_host_top99p": (int,),
            "appsec_fargate_count_avg": (int,),
            "asm_serverless_sum": (int,),
            "audit_logs_lines_indexed_sum": (int,),
            "audit_trail_enabled_hwm": (int,),
            "avg_profiled_fargate_tasks": (int,),
            "aws_host_top99p": (int,),
            "aws_lambda_func_count": (int,),
            "aws_lambda_invocations_sum": (int,),
            "azure_app_service_top99p": (int,),
            "billable_ingested_bytes_sum": (int,),
            "browser_rum_lite_session_count_sum": (int,),
            "browser_rum_replay_session_count_sum": (int,),
            "browser_rum_units_sum": (int,),
            "ci_pipeline_indexed_spans_sum": (int,),
            "ci_test_indexed_spans_sum": (int,),
            "ci_visibility_itr_committers_hwm": (int,),
            "ci_visibility_pipeline_committers_hwm": (int,),
            "ci_visibility_test_committers_hwm": (int,),
            "cloud_cost_management_aws_host_count_avg": (int,),
            "cloud_cost_management_azure_host_count_avg": (int,),
            "cloud_cost_management_gcp_host_count_avg": (int,),
            "cloud_cost_management_host_count_avg": (int,),
            "cloud_siem_events_sum": (int,),
            "container_avg": (int,),
            "container_excl_agent_avg": (int,),
            "container_hwm": (int,),
            "csm_container_enterprise_compliance_count_sum": (int,),
            "csm_container_enterprise_cws_count_sum": (int,),
            "csm_container_enterprise_total_count_sum": (int,),
            "csm_host_enterprise_aas_host_count_top99p": (int,),
            "csm_host_enterprise_aws_host_count_top99p": (int,),
            "csm_host_enterprise_azure_host_count_top99p": (int,),
            "csm_host_enterprise_compliance_host_count_top99p": (int,),
            "csm_host_enterprise_cws_host_count_top99p": (int,),
            "csm_host_enterprise_gcp_host_count_top99p": (int,),
            "csm_host_enterprise_total_host_count_top99p": (int,),
            "cspm_aas_host_top99p": (int,),
            "cspm_aws_host_top99p": (int,),
            "cspm_azure_host_top99p": (int,),
            "cspm_container_avg": (int,),
            "cspm_container_hwm": (int,),
            "cspm_gcp_host_top99p": (int,),
            "cspm_host_top99p": (int,),
            "custom_historical_ts_avg": (int,),
            "custom_live_ts_avg": (int,),
            "custom_ts_avg": (int,),
            "cws_container_count_avg": (int,),
            "cws_host_top99p": (int,),
            "dbm_host_top99p_sum": (int,),
            "dbm_queries_avg_sum": (int,),
            "error_tracking_events_sum": (int,),
            "fargate_tasks_count_avg": (int,),
            "fargate_tasks_count_hwm": (int,),
            "flex_logs_compute_large_avg": (int,),
            "flex_logs_compute_medium_avg": (int,),
            "flex_logs_compute_small_avg": (int,),
            "flex_logs_compute_xsmall_avg": (int,),
            "flex_stored_logs_avg": (int,),
            "forwarding_events_bytes_sum": (int,),
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
            "mobile_rum_session_count_flutter_sum": (int,),
            "mobile_rum_session_count_ios_sum": (int,),
            "mobile_rum_session_count_reactnative_sum": (int,),
            "mobile_rum_session_count_roku_sum": (int,),
            "mobile_rum_session_count_sum": (int,),
            "mobile_rum_units_sum": (int,),
            "name": (str,),
            "ndm_netflow_events_sum": (int,),
            "netflow_indexed_events_count_sum": (int,),
            "npm_host_top99p": (int,),
            "observability_pipelines_bytes_processed_sum": (int,),
            "online_archive_events_count_sum": (int,),
            "opentelemetry_apm_host_top99p": (int,),
            "opentelemetry_host_top99p": (int,),
            "profiling_aas_count_top99p": (int,),
            "profiling_host_top99p": (int,),
            "public_id": (str,),
            "region": (str,),
            "rum_browser_and_mobile_session_count": (int,),
            "rum_browser_legacy_session_count_sum": (int,),
            "rum_browser_lite_session_count_sum": (int,),
            "rum_browser_replay_session_count_sum": (int,),
            "rum_lite_session_count_sum": (int,),
            "rum_mobile_legacy_session_count_android_sum": (int,),
            "rum_mobile_legacy_session_count_flutter_sum": (int,),
            "rum_mobile_legacy_session_count_ios_sum": (int,),
            "rum_mobile_legacy_session_count_reactnative_sum": (int,),
            "rum_mobile_legacy_session_count_roku_sum": (int,),
            "rum_mobile_lite_session_count_android_sum": (int,),
            "rum_mobile_lite_session_count_flutter_sum": (int,),
            "rum_mobile_lite_session_count_ios_sum": (int,),
            "rum_mobile_lite_session_count_reactnative_sum": (int,),
            "rum_mobile_lite_session_count_roku_sum": (int,),
            "rum_replay_session_count_sum": (int,),
            "rum_session_count_sum": (int,),
            "rum_total_session_count_sum": (int,),
            "rum_units_sum": (int,),
            "sds_apm_scanned_bytes_sum": (int,),
            "sds_events_scanned_bytes_sum": (int,),
            "sds_logs_scanned_bytes_sum": (int,),
            "sds_rum_scanned_bytes_sum": (int,),
            "sds_total_scanned_bytes_sum": (int,),
            "serverless_apps_azure_count_avg": (int,),
            "serverless_apps_google_count_avg": (int,),
            "serverless_apps_total_count_avg": (int,),
            "synthetics_browser_check_calls_count_sum": (int,),
            "synthetics_check_calls_count_sum": (int,),
            "synthetics_mobile_test_runs_sum": (int,),
            "synthetics_parallel_testing_max_slots_hwm": (int,),
            "trace_search_indexed_events_count_sum": (int,),
            "twol_ingested_events_bytes_sum": (int,),
            "universal_service_monitoring_host_top99p": (int,),
            "vsphere_host_top99p": (int,),
            "vuln_management_host_count_top99p": (int,),
            "workflow_executions_usage_sum": (int,),
        }

    attribute_map = {
        "agent_host_top99p": "agent_host_top99p",
        "apm_azure_app_service_host_top99p": "apm_azure_app_service_host_top99p",
        "apm_devsecops_host_top99p": "apm_devsecops_host_top99p",
        "apm_fargate_count_avg": "apm_fargate_count_avg",
        "apm_host_top99p": "apm_host_top99p",
        "appsec_fargate_count_avg": "appsec_fargate_count_avg",
        "asm_serverless_sum": "asm_serverless_sum",
        "audit_logs_lines_indexed_sum": "audit_logs_lines_indexed_sum",
        "audit_trail_enabled_hwm": "audit_trail_enabled_hwm",
        "avg_profiled_fargate_tasks": "avg_profiled_fargate_tasks",
        "aws_host_top99p": "aws_host_top99p",
        "aws_lambda_func_count": "aws_lambda_func_count",
        "aws_lambda_invocations_sum": "aws_lambda_invocations_sum",
        "azure_app_service_top99p": "azure_app_service_top99p",
        "billable_ingested_bytes_sum": "billable_ingested_bytes_sum",
        "browser_rum_lite_session_count_sum": "browser_rum_lite_session_count_sum",
        "browser_rum_replay_session_count_sum": "browser_rum_replay_session_count_sum",
        "browser_rum_units_sum": "browser_rum_units_sum",
        "ci_pipeline_indexed_spans_sum": "ci_pipeline_indexed_spans_sum",
        "ci_test_indexed_spans_sum": "ci_test_indexed_spans_sum",
        "ci_visibility_itr_committers_hwm": "ci_visibility_itr_committers_hwm",
        "ci_visibility_pipeline_committers_hwm": "ci_visibility_pipeline_committers_hwm",
        "ci_visibility_test_committers_hwm": "ci_visibility_test_committers_hwm",
        "cloud_cost_management_aws_host_count_avg": "cloud_cost_management_aws_host_count_avg",
        "cloud_cost_management_azure_host_count_avg": "cloud_cost_management_azure_host_count_avg",
        "cloud_cost_management_gcp_host_count_avg": "cloud_cost_management_gcp_host_count_avg",
        "cloud_cost_management_host_count_avg": "cloud_cost_management_host_count_avg",
        "cloud_siem_events_sum": "cloud_siem_events_sum",
        "container_avg": "container_avg",
        "container_excl_agent_avg": "container_excl_agent_avg",
        "container_hwm": "container_hwm",
        "csm_container_enterprise_compliance_count_sum": "csm_container_enterprise_compliance_count_sum",
        "csm_container_enterprise_cws_count_sum": "csm_container_enterprise_cws_count_sum",
        "csm_container_enterprise_total_count_sum": "csm_container_enterprise_total_count_sum",
        "csm_host_enterprise_aas_host_count_top99p": "csm_host_enterprise_aas_host_count_top99p",
        "csm_host_enterprise_aws_host_count_top99p": "csm_host_enterprise_aws_host_count_top99p",
        "csm_host_enterprise_azure_host_count_top99p": "csm_host_enterprise_azure_host_count_top99p",
        "csm_host_enterprise_compliance_host_count_top99p": "csm_host_enterprise_compliance_host_count_top99p",
        "csm_host_enterprise_cws_host_count_top99p": "csm_host_enterprise_cws_host_count_top99p",
        "csm_host_enterprise_gcp_host_count_top99p": "csm_host_enterprise_gcp_host_count_top99p",
        "csm_host_enterprise_total_host_count_top99p": "csm_host_enterprise_total_host_count_top99p",
        "cspm_aas_host_top99p": "cspm_aas_host_top99p",
        "cspm_aws_host_top99p": "cspm_aws_host_top99p",
        "cspm_azure_host_top99p": "cspm_azure_host_top99p",
        "cspm_container_avg": "cspm_container_avg",
        "cspm_container_hwm": "cspm_container_hwm",
        "cspm_gcp_host_top99p": "cspm_gcp_host_top99p",
        "cspm_host_top99p": "cspm_host_top99p",
        "custom_historical_ts_avg": "custom_historical_ts_avg",
        "custom_live_ts_avg": "custom_live_ts_avg",
        "custom_ts_avg": "custom_ts_avg",
        "cws_container_count_avg": "cws_container_count_avg",
        "cws_host_top99p": "cws_host_top99p",
        "dbm_host_top99p_sum": "dbm_host_top99p_sum",
        "dbm_queries_avg_sum": "dbm_queries_avg_sum",
        "error_tracking_events_sum": "error_tracking_events_sum",
        "fargate_tasks_count_avg": "fargate_tasks_count_avg",
        "fargate_tasks_count_hwm": "fargate_tasks_count_hwm",
        "flex_logs_compute_large_avg": "flex_logs_compute_large_avg",
        "flex_logs_compute_medium_avg": "flex_logs_compute_medium_avg",
        "flex_logs_compute_small_avg": "flex_logs_compute_small_avg",
        "flex_logs_compute_xsmall_avg": "flex_logs_compute_xsmall_avg",
        "flex_stored_logs_avg": "flex_stored_logs_avg",
        "forwarding_events_bytes_sum": "forwarding_events_bytes_sum",
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
        "mobile_rum_session_count_flutter_sum": "mobile_rum_session_count_flutter_sum",
        "mobile_rum_session_count_ios_sum": "mobile_rum_session_count_ios_sum",
        "mobile_rum_session_count_reactnative_sum": "mobile_rum_session_count_reactnative_sum",
        "mobile_rum_session_count_roku_sum": "mobile_rum_session_count_roku_sum",
        "mobile_rum_session_count_sum": "mobile_rum_session_count_sum",
        "mobile_rum_units_sum": "mobile_rum_units_sum",
        "name": "name",
        "ndm_netflow_events_sum": "ndm_netflow_events_sum",
        "netflow_indexed_events_count_sum": "netflow_indexed_events_count_sum",
        "npm_host_top99p": "npm_host_top99p",
        "observability_pipelines_bytes_processed_sum": "observability_pipelines_bytes_processed_sum",
        "online_archive_events_count_sum": "online_archive_events_count_sum",
        "opentelemetry_apm_host_top99p": "opentelemetry_apm_host_top99p",
        "opentelemetry_host_top99p": "opentelemetry_host_top99p",
        "profiling_aas_count_top99p": "profiling_aas_count_top99p",
        "profiling_host_top99p": "profiling_host_top99p",
        "public_id": "public_id",
        "region": "region",
        "rum_browser_and_mobile_session_count": "rum_browser_and_mobile_session_count",
        "rum_browser_legacy_session_count_sum": "rum_browser_legacy_session_count_sum",
        "rum_browser_lite_session_count_sum": "rum_browser_lite_session_count_sum",
        "rum_browser_replay_session_count_sum": "rum_browser_replay_session_count_sum",
        "rum_lite_session_count_sum": "rum_lite_session_count_sum",
        "rum_mobile_legacy_session_count_android_sum": "rum_mobile_legacy_session_count_android_sum",
        "rum_mobile_legacy_session_count_flutter_sum": "rum_mobile_legacy_session_count_flutter_sum",
        "rum_mobile_legacy_session_count_ios_sum": "rum_mobile_legacy_session_count_ios_sum",
        "rum_mobile_legacy_session_count_reactnative_sum": "rum_mobile_legacy_session_count_reactnative_sum",
        "rum_mobile_legacy_session_count_roku_sum": "rum_mobile_legacy_session_count_roku_sum",
        "rum_mobile_lite_session_count_android_sum": "rum_mobile_lite_session_count_android_sum",
        "rum_mobile_lite_session_count_flutter_sum": "rum_mobile_lite_session_count_flutter_sum",
        "rum_mobile_lite_session_count_ios_sum": "rum_mobile_lite_session_count_ios_sum",
        "rum_mobile_lite_session_count_reactnative_sum": "rum_mobile_lite_session_count_reactnative_sum",
        "rum_mobile_lite_session_count_roku_sum": "rum_mobile_lite_session_count_roku_sum",
        "rum_replay_session_count_sum": "rum_replay_session_count_sum",
        "rum_session_count_sum": "rum_session_count_sum",
        "rum_total_session_count_sum": "rum_total_session_count_sum",
        "rum_units_sum": "rum_units_sum",
        "sds_apm_scanned_bytes_sum": "sds_apm_scanned_bytes_sum",
        "sds_events_scanned_bytes_sum": "sds_events_scanned_bytes_sum",
        "sds_logs_scanned_bytes_sum": "sds_logs_scanned_bytes_sum",
        "sds_rum_scanned_bytes_sum": "sds_rum_scanned_bytes_sum",
        "sds_total_scanned_bytes_sum": "sds_total_scanned_bytes_sum",
        "serverless_apps_azure_count_avg": "serverless_apps_azure_count_avg",
        "serverless_apps_google_count_avg": "serverless_apps_google_count_avg",
        "serverless_apps_total_count_avg": "serverless_apps_total_count_avg",
        "synthetics_browser_check_calls_count_sum": "synthetics_browser_check_calls_count_sum",
        "synthetics_check_calls_count_sum": "synthetics_check_calls_count_sum",
        "synthetics_mobile_test_runs_sum": "synthetics_mobile_test_runs_sum",
        "synthetics_parallel_testing_max_slots_hwm": "synthetics_parallel_testing_max_slots_hwm",
        "trace_search_indexed_events_count_sum": "trace_search_indexed_events_count_sum",
        "twol_ingested_events_bytes_sum": "twol_ingested_events_bytes_sum",
        "universal_service_monitoring_host_top99p": "universal_service_monitoring_host_top99p",
        "vsphere_host_top99p": "vsphere_host_top99p",
        "vuln_management_host_count_top99p": "vuln_management_host_count_top99p",
        "workflow_executions_usage_sum": "workflow_executions_usage_sum",
    }

    def __init__(
        self_,
        agent_host_top99p: Union[int, UnsetType] = unset,
        apm_azure_app_service_host_top99p: Union[int, UnsetType] = unset,
        apm_devsecops_host_top99p: Union[int, UnsetType] = unset,
        apm_fargate_count_avg: Union[int, UnsetType] = unset,
        apm_host_top99p: Union[int, UnsetType] = unset,
        appsec_fargate_count_avg: Union[int, UnsetType] = unset,
        asm_serverless_sum: Union[int, UnsetType] = unset,
        audit_logs_lines_indexed_sum: Union[int, UnsetType] = unset,
        audit_trail_enabled_hwm: Union[int, UnsetType] = unset,
        avg_profiled_fargate_tasks: Union[int, UnsetType] = unset,
        aws_host_top99p: Union[int, UnsetType] = unset,
        aws_lambda_func_count: Union[int, UnsetType] = unset,
        aws_lambda_invocations_sum: Union[int, UnsetType] = unset,
        azure_app_service_top99p: Union[int, UnsetType] = unset,
        billable_ingested_bytes_sum: Union[int, UnsetType] = unset,
        browser_rum_lite_session_count_sum: Union[int, UnsetType] = unset,
        browser_rum_replay_session_count_sum: Union[int, UnsetType] = unset,
        browser_rum_units_sum: Union[int, UnsetType] = unset,
        ci_pipeline_indexed_spans_sum: Union[int, UnsetType] = unset,
        ci_test_indexed_spans_sum: Union[int, UnsetType] = unset,
        ci_visibility_itr_committers_hwm: Union[int, UnsetType] = unset,
        ci_visibility_pipeline_committers_hwm: Union[int, UnsetType] = unset,
        ci_visibility_test_committers_hwm: Union[int, UnsetType] = unset,
        cloud_cost_management_aws_host_count_avg: Union[int, UnsetType] = unset,
        cloud_cost_management_azure_host_count_avg: Union[int, UnsetType] = unset,
        cloud_cost_management_gcp_host_count_avg: Union[int, UnsetType] = unset,
        cloud_cost_management_host_count_avg: Union[int, UnsetType] = unset,
        cloud_siem_events_sum: Union[int, UnsetType] = unset,
        container_avg: Union[int, UnsetType] = unset,
        container_excl_agent_avg: Union[int, UnsetType] = unset,
        container_hwm: Union[int, UnsetType] = unset,
        csm_container_enterprise_compliance_count_sum: Union[int, UnsetType] = unset,
        csm_container_enterprise_cws_count_sum: Union[int, UnsetType] = unset,
        csm_container_enterprise_total_count_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_aas_host_count_top99p: Union[int, UnsetType] = unset,
        csm_host_enterprise_aws_host_count_top99p: Union[int, UnsetType] = unset,
        csm_host_enterprise_azure_host_count_top99p: Union[int, UnsetType] = unset,
        csm_host_enterprise_compliance_host_count_top99p: Union[int, UnsetType] = unset,
        csm_host_enterprise_cws_host_count_top99p: Union[int, UnsetType] = unset,
        csm_host_enterprise_gcp_host_count_top99p: Union[int, UnsetType] = unset,
        csm_host_enterprise_total_host_count_top99p: Union[int, UnsetType] = unset,
        cspm_aas_host_top99p: Union[int, UnsetType] = unset,
        cspm_aws_host_top99p: Union[int, UnsetType] = unset,
        cspm_azure_host_top99p: Union[int, UnsetType] = unset,
        cspm_container_avg: Union[int, UnsetType] = unset,
        cspm_container_hwm: Union[int, UnsetType] = unset,
        cspm_gcp_host_top99p: Union[int, UnsetType] = unset,
        cspm_host_top99p: Union[int, UnsetType] = unset,
        custom_historical_ts_avg: Union[int, UnsetType] = unset,
        custom_live_ts_avg: Union[int, UnsetType] = unset,
        custom_ts_avg: Union[int, UnsetType] = unset,
        cws_container_count_avg: Union[int, UnsetType] = unset,
        cws_host_top99p: Union[int, UnsetType] = unset,
        dbm_host_top99p_sum: Union[int, UnsetType] = unset,
        dbm_queries_avg_sum: Union[int, UnsetType] = unset,
        error_tracking_events_sum: Union[int, UnsetType] = unset,
        fargate_tasks_count_avg: Union[int, UnsetType] = unset,
        fargate_tasks_count_hwm: Union[int, UnsetType] = unset,
        flex_logs_compute_large_avg: Union[int, UnsetType] = unset,
        flex_logs_compute_medium_avg: Union[int, UnsetType] = unset,
        flex_logs_compute_small_avg: Union[int, UnsetType] = unset,
        flex_logs_compute_xsmall_avg: Union[int, UnsetType] = unset,
        flex_stored_logs_avg: Union[int, UnsetType] = unset,
        forwarding_events_bytes_sum: Union[int, UnsetType] = unset,
        gcp_host_top99p: Union[int, UnsetType] = unset,
        heroku_host_top99p: Union[int, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        incident_management_monthly_active_users_hwm: Union[int, UnsetType] = unset,
        indexed_events_count_sum: Union[int, UnsetType] = unset,
        infra_host_top99p: Union[int, UnsetType] = unset,
        ingested_events_bytes_sum: Union[int, UnsetType] = unset,
        iot_device_agg_sum: Union[int, UnsetType] = unset,
        iot_device_top99p_sum: Union[int, UnsetType] = unset,
        mobile_rum_lite_session_count_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_android_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_flutter_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_ios_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_reactnative_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_roku_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_sum: Union[int, UnsetType] = unset,
        mobile_rum_units_sum: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        ndm_netflow_events_sum: Union[int, UnsetType] = unset,
        netflow_indexed_events_count_sum: Union[int, UnsetType] = unset,
        npm_host_top99p: Union[int, UnsetType] = unset,
        observability_pipelines_bytes_processed_sum: Union[int, UnsetType] = unset,
        online_archive_events_count_sum: Union[int, UnsetType] = unset,
        opentelemetry_apm_host_top99p: Union[int, UnsetType] = unset,
        opentelemetry_host_top99p: Union[int, UnsetType] = unset,
        profiling_aas_count_top99p: Union[int, UnsetType] = unset,
        profiling_host_top99p: Union[int, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        rum_browser_and_mobile_session_count: Union[int, UnsetType] = unset,
        rum_browser_legacy_session_count_sum: Union[int, UnsetType] = unset,
        rum_browser_lite_session_count_sum: Union[int, UnsetType] = unset,
        rum_browser_replay_session_count_sum: Union[int, UnsetType] = unset,
        rum_lite_session_count_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_android_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_flutter_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_ios_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_reactnative_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_roku_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_android_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_flutter_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_ios_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_reactnative_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_roku_sum: Union[int, UnsetType] = unset,
        rum_replay_session_count_sum: Union[int, UnsetType] = unset,
        rum_session_count_sum: Union[int, UnsetType] = unset,
        rum_total_session_count_sum: Union[int, UnsetType] = unset,
        rum_units_sum: Union[int, UnsetType] = unset,
        sds_apm_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_events_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_logs_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_rum_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_total_scanned_bytes_sum: Union[int, UnsetType] = unset,
        serverless_apps_azure_count_avg: Union[int, UnsetType] = unset,
        serverless_apps_google_count_avg: Union[int, UnsetType] = unset,
        serverless_apps_total_count_avg: Union[int, UnsetType] = unset,
        synthetics_browser_check_calls_count_sum: Union[int, UnsetType] = unset,
        synthetics_check_calls_count_sum: Union[int, UnsetType] = unset,
        synthetics_mobile_test_runs_sum: Union[int, UnsetType] = unset,
        synthetics_parallel_testing_max_slots_hwm: Union[int, UnsetType] = unset,
        trace_search_indexed_events_count_sum: Union[int, UnsetType] = unset,
        twol_ingested_events_bytes_sum: Union[int, UnsetType] = unset,
        universal_service_monitoring_host_top99p: Union[int, UnsetType] = unset,
        vsphere_host_top99p: Union[int, UnsetType] = unset,
        vuln_management_host_count_top99p: Union[int, UnsetType] = unset,
        workflow_executions_usage_sum: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Global hourly report of all data billed by Datadog for a given organization.

        :param agent_host_top99p: Shows the 99th percentile of all agent hosts over all hours in the current date for the given org.
        :type agent_host_top99p: int, optional

        :param apm_azure_app_service_host_top99p: Shows the 99th percentile of all Azure app services using APM over all hours in the current date for the given org.
        :type apm_azure_app_service_host_top99p: int, optional

        :param apm_devsecops_host_top99p: Shows the 99th percentile of all APM DevSecOps hosts over all hours in the current date for the given org.
        :type apm_devsecops_host_top99p: int, optional

        :param apm_fargate_count_avg: Shows the average of all APM ECS Fargate tasks over all hours in the current month for the given org.
        :type apm_fargate_count_avg: int, optional

        :param apm_host_top99p: Shows the 99th percentile of all distinct APM hosts over all hours in the current date for the given org.
        :type apm_host_top99p: int, optional

        :param appsec_fargate_count_avg: Shows the average of all Application Security Monitoring ECS Fargate tasks over all hours in the current month for the given org.
        :type appsec_fargate_count_avg: int, optional

        :param asm_serverless_sum: Shows the sum of all Application Security Monitoring Serverless invocations over all hours in the current month for the given org.
        :type asm_serverless_sum: int, optional

        :param audit_logs_lines_indexed_sum: Shows the sum of all audit logs lines indexed over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type audit_logs_lines_indexed_sum: int, optional

        :param audit_trail_enabled_hwm: Shows whether Audit Trail is enabled for the current date for the given org.
        :type audit_trail_enabled_hwm: int, optional

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

        :param browser_rum_lite_session_count_sum: Shows the sum of all browser lite sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type browser_rum_lite_session_count_sum: int, optional

        :param browser_rum_replay_session_count_sum: Shows the sum of all browser replay sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
        :type browser_rum_replay_session_count_sum: int, optional

        :param browser_rum_units_sum: Shows the sum of all browser RUM units over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type browser_rum_units_sum: int, optional

        :param ci_pipeline_indexed_spans_sum: Shows the sum of all CI pipeline indexed spans over all hours in the current date for the given org.
        :type ci_pipeline_indexed_spans_sum: int, optional

        :param ci_test_indexed_spans_sum: Shows the sum of all CI test indexed spans over all hours in the current date for the given org.
        :type ci_test_indexed_spans_sum: int, optional

        :param ci_visibility_itr_committers_hwm: Shows the high-water mark of all CI visibility intelligent test runner committers over all hours in the current date for the given org.
        :type ci_visibility_itr_committers_hwm: int, optional

        :param ci_visibility_pipeline_committers_hwm: Shows the high-water mark of all CI visibility pipeline committers over all hours in the current date for the given org.
        :type ci_visibility_pipeline_committers_hwm: int, optional

        :param ci_visibility_test_committers_hwm: Shows the high-water mark of all CI visibility test committers over all hours in the current date for the given org.
        :type ci_visibility_test_committers_hwm: int, optional

        :param cloud_cost_management_aws_host_count_avg: Host count average of Cloud Cost Management for AWS for the given date and given org.
        :type cloud_cost_management_aws_host_count_avg: int, optional

        :param cloud_cost_management_azure_host_count_avg: Host count average of Cloud Cost Management for Azure for the given date and given org.
        :type cloud_cost_management_azure_host_count_avg: int, optional

        :param cloud_cost_management_gcp_host_count_avg: Host count average of Cloud Cost Management for GCP for the given date and given org.
        :type cloud_cost_management_gcp_host_count_avg: int, optional

        :param cloud_cost_management_host_count_avg: Host count average of Cloud Cost Management for all cloud providers for the given date and given org.
        :type cloud_cost_management_host_count_avg: int, optional

        :param cloud_siem_events_sum: Shows the sum of all Cloud Security Information and Event Management events over all hours in the current date for the given org.
        :type cloud_siem_events_sum: int, optional

        :param container_avg: Shows the average of all distinct containers over all hours in the current date for the given org.
        :type container_avg: int, optional

        :param container_excl_agent_avg: Shows the average of containers without the Datadog Agent over all hours in the current date for the given organization.
        :type container_excl_agent_avg: int, optional

        :param container_hwm: Shows the high-water mark of all distinct containers over all hours in the current date for the given org.
        :type container_hwm: int, optional

        :param csm_container_enterprise_compliance_count_sum: Shows the sum of all Cloud Security Management Enterprise compliance containers over all hours in the current date for the given org.
        :type csm_container_enterprise_compliance_count_sum: int, optional

        :param csm_container_enterprise_cws_count_sum: Shows the sum of all Cloud Security Management Enterprise Cloud Workload Security containers over all hours in the current date for the given org.
        :type csm_container_enterprise_cws_count_sum: int, optional

        :param csm_container_enterprise_total_count_sum: Shows the sum of all Cloud Security Management Enterprise containers over all hours in the current date for the given org.
        :type csm_container_enterprise_total_count_sum: int, optional

        :param csm_host_enterprise_aas_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise Azure app services hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_aas_host_count_top99p: int, optional

        :param csm_host_enterprise_aws_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise AWS hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_aws_host_count_top99p: int, optional

        :param csm_host_enterprise_azure_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise Azure hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_azure_host_count_top99p: int, optional

        :param csm_host_enterprise_compliance_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise compliance hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_compliance_host_count_top99p: int, optional

        :param csm_host_enterprise_cws_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise Cloud Workload Security hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_cws_host_count_top99p: int, optional

        :param csm_host_enterprise_gcp_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise GCP hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_gcp_host_count_top99p: int, optional

        :param csm_host_enterprise_total_host_count_top99p: Shows the 99th percentile of all Cloud Security Management Enterprise hosts over all hours in the current date for the given org.
        :type csm_host_enterprise_total_host_count_top99p: int, optional

        :param cspm_aas_host_top99p: Shows the 99th percentile of all Cloud Security Management Pro Azure app services hosts over all hours in the current date for the given org.
        :type cspm_aas_host_top99p: int, optional

        :param cspm_aws_host_top99p: Shows the 99th percentile of all Cloud Security Management Pro AWS hosts over all hours in the current date for the given org.
        :type cspm_aws_host_top99p: int, optional

        :param cspm_azure_host_top99p: Shows the 99th percentile of all Cloud Security Management Pro Azure hosts over all hours in the current date for the given org.
        :type cspm_azure_host_top99p: int, optional

        :param cspm_container_avg: Shows the average number of Cloud Security Management Pro containers over all hours in the current date for the given org.
        :type cspm_container_avg: int, optional

        :param cspm_container_hwm: Shows the high-water mark of Cloud Security Management Pro containers over all hours in the current date for the given org.
        :type cspm_container_hwm: int, optional

        :param cspm_gcp_host_top99p: Shows the 99th percentile of all Cloud Security Management Pro GCP hosts over all hours in the current date for the given org.
        :type cspm_gcp_host_top99p: int, optional

        :param cspm_host_top99p: Shows the 99th percentile of all Cloud Security Management Pro hosts over all hours in the current date for the given org.
        :type cspm_host_top99p: int, optional

        :param custom_historical_ts_avg: Shows the average number of distinct historical custom metrics over all hours in the current date for the given org.
        :type custom_historical_ts_avg: int, optional

        :param custom_live_ts_avg: Shows the average number of distinct live custom metrics over all hours in the current date for the given org.
        :type custom_live_ts_avg: int, optional

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

        :param error_tracking_events_sum: Shows the sum of all Error Tracking events over all hours in the current date for the given org.
        :type error_tracking_events_sum: int, optional

        :param fargate_tasks_count_avg: The average task count for Fargate.
        :type fargate_tasks_count_avg: int, optional

        :param fargate_tasks_count_hwm: Shows the high-water mark of all Fargate tasks over all hours in the current date for the given org.
        :type fargate_tasks_count_hwm: int, optional

        :param flex_logs_compute_large_avg: Shows the average number of Flex Logs Compute Large Instances over all hours in the current date for the given org.
        :type flex_logs_compute_large_avg: int, optional

        :param flex_logs_compute_medium_avg: Shows the average number of Flex Logs Compute Medium Instances over all hours in the current date for the given org.
        :type flex_logs_compute_medium_avg: int, optional

        :param flex_logs_compute_small_avg: Shows the average number of Flex Logs Compute Small Instances over all hours in the current date for the given org.
        :type flex_logs_compute_small_avg: int, optional

        :param flex_logs_compute_xsmall_avg: Shows the average number of Flex Logs Compute Extra Small Instances over all hours in the current date for the given org.
        :type flex_logs_compute_xsmall_avg: int, optional

        :param flex_stored_logs_avg: Shows the average of all Flex Stored Logs over all hours in the current date for the given org.
        :type flex_stored_logs_avg: int, optional

        :param forwarding_events_bytes_sum: Shows the sum of all log bytes forwarded over all hours in the current date for the given org.
        :type forwarding_events_bytes_sum: int, optional

        :param gcp_host_top99p: Shows the 99th percentile of all GCP hosts over all hours in the current date for the given org.
        :type gcp_host_top99p: int, optional

        :param heroku_host_top99p: Shows the 99th percentile of all Heroku dynos over all hours in the current date for the given org.
        :type heroku_host_top99p: int, optional

        :param id: The organization id.
        :type id: str, optional

        :param incident_management_monthly_active_users_hwm: Shows the high-water mark of incident management monthly active users over all hours in the current date for the given org.
        :type incident_management_monthly_active_users_hwm: int, optional

        :param indexed_events_count_sum: Shows the sum of all log events indexed over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type indexed_events_count_sum: int, optional

        :param infra_host_top99p: Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for the given org.
        :type infra_host_top99p: int, optional

        :param ingested_events_bytes_sum: Shows the sum of all log bytes ingested over all hours in the current date for the given org.
        :type ingested_events_bytes_sum: int, optional

        :param iot_device_agg_sum: Shows the sum of all IoT devices over all hours in the current date for the given org.
        :type iot_device_agg_sum: int, optional

        :param iot_device_top99p_sum: Shows the 99th percentile of all IoT devices over all hours in the current date for the given org.
        :type iot_device_top99p_sum: int, optional

        :param mobile_rum_lite_session_count_sum: Shows the sum of all mobile lite sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_lite_session_count_sum: int, optional

        :param mobile_rum_session_count_android_sum: Shows the sum of all mobile RUM sessions on Android over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_android_sum: int, optional

        :param mobile_rum_session_count_flutter_sum: Shows the sum of all mobile RUM sessions on Flutter over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_flutter_sum: int, optional

        :param mobile_rum_session_count_ios_sum: Shows the sum of all mobile RUM sessions on iOS over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_ios_sum: int, optional

        :param mobile_rum_session_count_reactnative_sum: Shows the sum of all mobile RUM sessions on React Native over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_reactnative_sum: int, optional

        :param mobile_rum_session_count_roku_sum: Shows the sum of all mobile RUM sessions on Roku over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_roku_sum: int, optional

        :param mobile_rum_session_count_sum: Shows the sum of all mobile RUM sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_sum: int, optional

        :param mobile_rum_units_sum: Shows the sum of all mobile RUM units over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_units_sum: int, optional

        :param name: The organization name.
        :type name: str, optional

        :param ndm_netflow_events_sum: Shows the sum of all Network Device Monitoring NetFlow events over all hours in the current date for the given org.
        :type ndm_netflow_events_sum: int, optional

        :param netflow_indexed_events_count_sum: Shows the sum of all Network flows indexed over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type netflow_indexed_events_count_sum: int, optional

        :param npm_host_top99p: Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for the given org.
        :type npm_host_top99p: int, optional

        :param observability_pipelines_bytes_processed_sum: Sum of all observability pipelines bytes processed over all hours in the current date for the given org.
        :type observability_pipelines_bytes_processed_sum: int, optional

        :param online_archive_events_count_sum: Sum of all online archived events over all hours in the current date for the given org.
        :type online_archive_events_count_sum: int, optional

        :param opentelemetry_apm_host_top99p: Shows the 99th percentile of APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
        :type opentelemetry_apm_host_top99p: int, optional

        :param opentelemetry_host_top99p: Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.
        :type opentelemetry_host_top99p: int, optional

        :param profiling_aas_count_top99p: Shows the 99th percentile of all profiled Azure app services over all hours in the current date for all organizations.
        :type profiling_aas_count_top99p: int, optional

        :param profiling_host_top99p: Shows the 99th percentile of all profiled hosts over all hours in the current date for the given org.
        :type profiling_host_top99p: int, optional

        :param public_id: The organization public id.
        :type public_id: str, optional

        :param region: The region of the organization.
        :type region: str, optional

        :param rum_browser_and_mobile_session_count: Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024).
        :type rum_browser_and_mobile_session_count: int, optional

        :param rum_browser_legacy_session_count_sum: Shows the sum of all browser RUM legacy sessions over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_browser_legacy_session_count_sum: int, optional

        :param rum_browser_lite_session_count_sum: Shows the sum of all browser RUM lite sessions over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_browser_lite_session_count_sum: int, optional

        :param rum_browser_replay_session_count_sum: Shows the sum of all browser RUM Session Replay counts over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_browser_replay_session_count_sum: int, optional

        :param rum_lite_session_count_sum: Shows the sum of all RUM lite sessions (browser and mobile) over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_lite_session_count_sum: int, optional

        :param rum_mobile_legacy_session_count_android_sum: Shows the sum of all mobile RUM legacy sessions on Android over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_android_sum: int, optional

        :param rum_mobile_legacy_session_count_flutter_sum: Shows the sum of all mobile RUM legacy sessions on Flutter over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_flutter_sum: int, optional

        :param rum_mobile_legacy_session_count_ios_sum: Shows the sum of all mobile RUM legacy sessions on iOS over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_ios_sum: int, optional

        :param rum_mobile_legacy_session_count_reactnative_sum: Shows the sum of all mobile RUM legacy sessions on React Native over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_reactnative_sum: int, optional

        :param rum_mobile_legacy_session_count_roku_sum: Shows the sum of all mobile RUM legacy sessions on Roku over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_roku_sum: int, optional

        :param rum_mobile_lite_session_count_android_sum: Shows the sum of all mobile RUM lite sessions on Android over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_android_sum: int, optional

        :param rum_mobile_lite_session_count_flutter_sum: Shows the sum of all mobile RUM lite sessions on Flutter over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_flutter_sum: int, optional

        :param rum_mobile_lite_session_count_ios_sum: Shows the sum of all mobile RUM lite sessions on iOS over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_ios_sum: int, optional

        :param rum_mobile_lite_session_count_reactnative_sum: Shows the sum of all mobile RUM lite sessions on React Native over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_reactnative_sum: int, optional

        :param rum_mobile_lite_session_count_roku_sum: Shows the sum of all mobile RUM lite sessions on Roku over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_roku_sum: int, optional

        :param rum_replay_session_count_sum: Shows the sum of all RUM Session Replay counts over all hours in the current date for the given org (To be introduced on October 1st, 2024).
        :type rum_replay_session_count_sum: int, optional

        :param rum_session_count_sum: Shows the sum of all browser RUM lite sessions over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type rum_session_count_sum: int, optional

        :param rum_total_session_count_sum: Shows the sum of RUM sessions (browser and mobile) over all hours in the current date for the given org.
        :type rum_total_session_count_sum: int, optional

        :param rum_units_sum: Shows the sum of all browser and mobile RUM units over all hours in the current date for the given org (To be deprecated on October 1st, 2024). **Deprecated**.
        :type rum_units_sum: int, optional

        :param sds_apm_scanned_bytes_sum: Sum of all APM bytes scanned with sensitive data scanner over all hours in the current date for the given org.
        :type sds_apm_scanned_bytes_sum: int, optional

        :param sds_events_scanned_bytes_sum: Sum of all event stream events bytes scanned with sensitive data scanner over all hours in the current date for the given org.
        :type sds_events_scanned_bytes_sum: int, optional

        :param sds_logs_scanned_bytes_sum: Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for the given org.
        :type sds_logs_scanned_bytes_sum: int, optional

        :param sds_rum_scanned_bytes_sum: Sum of all RUM bytes scanned with sensitive data scanner over all hours in the current date for the given org.
        :type sds_rum_scanned_bytes_sum: int, optional

        :param sds_total_scanned_bytes_sum: Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for the given org.
        :type sds_total_scanned_bytes_sum: int, optional

        :param serverless_apps_azure_count_avg: Shows the average of the number of Serverless Apps for Azure for the given date and given org.
        :type serverless_apps_azure_count_avg: int, optional

        :param serverless_apps_google_count_avg: Shows the average of the number of Serverless Apps for Google Cloud for the given date and given org.
        :type serverless_apps_google_count_avg: int, optional

        :param serverless_apps_total_count_avg: Shows the average of the number of Serverless Apps for Azure and Google Cloud for the given date and given org.
        :type serverless_apps_total_count_avg: int, optional

        :param synthetics_browser_check_calls_count_sum: Shows the sum of all Synthetic browser tests over all hours in the current date for the given org.
        :type synthetics_browser_check_calls_count_sum: int, optional

        :param synthetics_check_calls_count_sum: Shows the sum of all Synthetic API tests over all hours in the current date for the given org.
        :type synthetics_check_calls_count_sum: int, optional

        :param synthetics_mobile_test_runs_sum: Shows the sum of all Synthetic mobile application tests over all hours in the current date for the given org.
        :type synthetics_mobile_test_runs_sum: int, optional

        :param synthetics_parallel_testing_max_slots_hwm: Shows the high-water mark of used synthetics parallel testing slots over all hours in the current date for the given org.
        :type synthetics_parallel_testing_max_slots_hwm: int, optional

        :param trace_search_indexed_events_count_sum: Shows the sum of all Indexed Spans indexed over all hours in the current date for the given org.
        :type trace_search_indexed_events_count_sum: int, optional

        :param twol_ingested_events_bytes_sum: Shows the sum of all ingested APM span bytes over all hours in the current date for the given org.
        :type twol_ingested_events_bytes_sum: int, optional

        :param universal_service_monitoring_host_top99p: Shows the 99th percentile of all Universal Service Monitoring hosts over all hours in the current date for the given org.
        :type universal_service_monitoring_host_top99p: int, optional

        :param vsphere_host_top99p: Shows the 99th percentile of all vSphere hosts over all hours in the current date for the given org.
        :type vsphere_host_top99p: int, optional

        :param vuln_management_host_count_top99p: Shows the 99th percentile of all Application Vulnerability Management hosts over all hours in the current date for the given org.
        :type vuln_management_host_count_top99p: int, optional

        :param workflow_executions_usage_sum: Sum of all workflows executed over all hours in the current date for the given org.
        :type workflow_executions_usage_sum: int, optional
        """
        if agent_host_top99p is not unset:
            kwargs["agent_host_top99p"] = agent_host_top99p
        if apm_azure_app_service_host_top99p is not unset:
            kwargs["apm_azure_app_service_host_top99p"] = apm_azure_app_service_host_top99p
        if apm_devsecops_host_top99p is not unset:
            kwargs["apm_devsecops_host_top99p"] = apm_devsecops_host_top99p
        if apm_fargate_count_avg is not unset:
            kwargs["apm_fargate_count_avg"] = apm_fargate_count_avg
        if apm_host_top99p is not unset:
            kwargs["apm_host_top99p"] = apm_host_top99p
        if appsec_fargate_count_avg is not unset:
            kwargs["appsec_fargate_count_avg"] = appsec_fargate_count_avg
        if asm_serverless_sum is not unset:
            kwargs["asm_serverless_sum"] = asm_serverless_sum
        if audit_logs_lines_indexed_sum is not unset:
            kwargs["audit_logs_lines_indexed_sum"] = audit_logs_lines_indexed_sum
        if audit_trail_enabled_hwm is not unset:
            kwargs["audit_trail_enabled_hwm"] = audit_trail_enabled_hwm
        if avg_profiled_fargate_tasks is not unset:
            kwargs["avg_profiled_fargate_tasks"] = avg_profiled_fargate_tasks
        if aws_host_top99p is not unset:
            kwargs["aws_host_top99p"] = aws_host_top99p
        if aws_lambda_func_count is not unset:
            kwargs["aws_lambda_func_count"] = aws_lambda_func_count
        if aws_lambda_invocations_sum is not unset:
            kwargs["aws_lambda_invocations_sum"] = aws_lambda_invocations_sum
        if azure_app_service_top99p is not unset:
            kwargs["azure_app_service_top99p"] = azure_app_service_top99p
        if billable_ingested_bytes_sum is not unset:
            kwargs["billable_ingested_bytes_sum"] = billable_ingested_bytes_sum
        if browser_rum_lite_session_count_sum is not unset:
            kwargs["browser_rum_lite_session_count_sum"] = browser_rum_lite_session_count_sum
        if browser_rum_replay_session_count_sum is not unset:
            kwargs["browser_rum_replay_session_count_sum"] = browser_rum_replay_session_count_sum
        if browser_rum_units_sum is not unset:
            kwargs["browser_rum_units_sum"] = browser_rum_units_sum
        if ci_pipeline_indexed_spans_sum is not unset:
            kwargs["ci_pipeline_indexed_spans_sum"] = ci_pipeline_indexed_spans_sum
        if ci_test_indexed_spans_sum is not unset:
            kwargs["ci_test_indexed_spans_sum"] = ci_test_indexed_spans_sum
        if ci_visibility_itr_committers_hwm is not unset:
            kwargs["ci_visibility_itr_committers_hwm"] = ci_visibility_itr_committers_hwm
        if ci_visibility_pipeline_committers_hwm is not unset:
            kwargs["ci_visibility_pipeline_committers_hwm"] = ci_visibility_pipeline_committers_hwm
        if ci_visibility_test_committers_hwm is not unset:
            kwargs["ci_visibility_test_committers_hwm"] = ci_visibility_test_committers_hwm
        if cloud_cost_management_aws_host_count_avg is not unset:
            kwargs["cloud_cost_management_aws_host_count_avg"] = cloud_cost_management_aws_host_count_avg
        if cloud_cost_management_azure_host_count_avg is not unset:
            kwargs["cloud_cost_management_azure_host_count_avg"] = cloud_cost_management_azure_host_count_avg
        if cloud_cost_management_gcp_host_count_avg is not unset:
            kwargs["cloud_cost_management_gcp_host_count_avg"] = cloud_cost_management_gcp_host_count_avg
        if cloud_cost_management_host_count_avg is not unset:
            kwargs["cloud_cost_management_host_count_avg"] = cloud_cost_management_host_count_avg
        if cloud_siem_events_sum is not unset:
            kwargs["cloud_siem_events_sum"] = cloud_siem_events_sum
        if container_avg is not unset:
            kwargs["container_avg"] = container_avg
        if container_excl_agent_avg is not unset:
            kwargs["container_excl_agent_avg"] = container_excl_agent_avg
        if container_hwm is not unset:
            kwargs["container_hwm"] = container_hwm
        if csm_container_enterprise_compliance_count_sum is not unset:
            kwargs["csm_container_enterprise_compliance_count_sum"] = csm_container_enterprise_compliance_count_sum
        if csm_container_enterprise_cws_count_sum is not unset:
            kwargs["csm_container_enterprise_cws_count_sum"] = csm_container_enterprise_cws_count_sum
        if csm_container_enterprise_total_count_sum is not unset:
            kwargs["csm_container_enterprise_total_count_sum"] = csm_container_enterprise_total_count_sum
        if csm_host_enterprise_aas_host_count_top99p is not unset:
            kwargs["csm_host_enterprise_aas_host_count_top99p"] = csm_host_enterprise_aas_host_count_top99p
        if csm_host_enterprise_aws_host_count_top99p is not unset:
            kwargs["csm_host_enterprise_aws_host_count_top99p"] = csm_host_enterprise_aws_host_count_top99p
        if csm_host_enterprise_azure_host_count_top99p is not unset:
            kwargs["csm_host_enterprise_azure_host_count_top99p"] = csm_host_enterprise_azure_host_count_top99p
        if csm_host_enterprise_compliance_host_count_top99p is not unset:
            kwargs[
                "csm_host_enterprise_compliance_host_count_top99p"
            ] = csm_host_enterprise_compliance_host_count_top99p
        if csm_host_enterprise_cws_host_count_top99p is not unset:
            kwargs["csm_host_enterprise_cws_host_count_top99p"] = csm_host_enterprise_cws_host_count_top99p
        if csm_host_enterprise_gcp_host_count_top99p is not unset:
            kwargs["csm_host_enterprise_gcp_host_count_top99p"] = csm_host_enterprise_gcp_host_count_top99p
        if csm_host_enterprise_total_host_count_top99p is not unset:
            kwargs["csm_host_enterprise_total_host_count_top99p"] = csm_host_enterprise_total_host_count_top99p
        if cspm_aas_host_top99p is not unset:
            kwargs["cspm_aas_host_top99p"] = cspm_aas_host_top99p
        if cspm_aws_host_top99p is not unset:
            kwargs["cspm_aws_host_top99p"] = cspm_aws_host_top99p
        if cspm_azure_host_top99p is not unset:
            kwargs["cspm_azure_host_top99p"] = cspm_azure_host_top99p
        if cspm_container_avg is not unset:
            kwargs["cspm_container_avg"] = cspm_container_avg
        if cspm_container_hwm is not unset:
            kwargs["cspm_container_hwm"] = cspm_container_hwm
        if cspm_gcp_host_top99p is not unset:
            kwargs["cspm_gcp_host_top99p"] = cspm_gcp_host_top99p
        if cspm_host_top99p is not unset:
            kwargs["cspm_host_top99p"] = cspm_host_top99p
        if custom_historical_ts_avg is not unset:
            kwargs["custom_historical_ts_avg"] = custom_historical_ts_avg
        if custom_live_ts_avg is not unset:
            kwargs["custom_live_ts_avg"] = custom_live_ts_avg
        if custom_ts_avg is not unset:
            kwargs["custom_ts_avg"] = custom_ts_avg
        if cws_container_count_avg is not unset:
            kwargs["cws_container_count_avg"] = cws_container_count_avg
        if cws_host_top99p is not unset:
            kwargs["cws_host_top99p"] = cws_host_top99p
        if dbm_host_top99p_sum is not unset:
            kwargs["dbm_host_top99p_sum"] = dbm_host_top99p_sum
        if dbm_queries_avg_sum is not unset:
            kwargs["dbm_queries_avg_sum"] = dbm_queries_avg_sum
        if error_tracking_events_sum is not unset:
            kwargs["error_tracking_events_sum"] = error_tracking_events_sum
        if fargate_tasks_count_avg is not unset:
            kwargs["fargate_tasks_count_avg"] = fargate_tasks_count_avg
        if fargate_tasks_count_hwm is not unset:
            kwargs["fargate_tasks_count_hwm"] = fargate_tasks_count_hwm
        if flex_logs_compute_large_avg is not unset:
            kwargs["flex_logs_compute_large_avg"] = flex_logs_compute_large_avg
        if flex_logs_compute_medium_avg is not unset:
            kwargs["flex_logs_compute_medium_avg"] = flex_logs_compute_medium_avg
        if flex_logs_compute_small_avg is not unset:
            kwargs["flex_logs_compute_small_avg"] = flex_logs_compute_small_avg
        if flex_logs_compute_xsmall_avg is not unset:
            kwargs["flex_logs_compute_xsmall_avg"] = flex_logs_compute_xsmall_avg
        if flex_stored_logs_avg is not unset:
            kwargs["flex_stored_logs_avg"] = flex_stored_logs_avg
        if forwarding_events_bytes_sum is not unset:
            kwargs["forwarding_events_bytes_sum"] = forwarding_events_bytes_sum
        if gcp_host_top99p is not unset:
            kwargs["gcp_host_top99p"] = gcp_host_top99p
        if heroku_host_top99p is not unset:
            kwargs["heroku_host_top99p"] = heroku_host_top99p
        if id is not unset:
            kwargs["id"] = id
        if incident_management_monthly_active_users_hwm is not unset:
            kwargs["incident_management_monthly_active_users_hwm"] = incident_management_monthly_active_users_hwm
        if indexed_events_count_sum is not unset:
            kwargs["indexed_events_count_sum"] = indexed_events_count_sum
        if infra_host_top99p is not unset:
            kwargs["infra_host_top99p"] = infra_host_top99p
        if ingested_events_bytes_sum is not unset:
            kwargs["ingested_events_bytes_sum"] = ingested_events_bytes_sum
        if iot_device_agg_sum is not unset:
            kwargs["iot_device_agg_sum"] = iot_device_agg_sum
        if iot_device_top99p_sum is not unset:
            kwargs["iot_device_top99p_sum"] = iot_device_top99p_sum
        if mobile_rum_lite_session_count_sum is not unset:
            kwargs["mobile_rum_lite_session_count_sum"] = mobile_rum_lite_session_count_sum
        if mobile_rum_session_count_android_sum is not unset:
            kwargs["mobile_rum_session_count_android_sum"] = mobile_rum_session_count_android_sum
        if mobile_rum_session_count_flutter_sum is not unset:
            kwargs["mobile_rum_session_count_flutter_sum"] = mobile_rum_session_count_flutter_sum
        if mobile_rum_session_count_ios_sum is not unset:
            kwargs["mobile_rum_session_count_ios_sum"] = mobile_rum_session_count_ios_sum
        if mobile_rum_session_count_reactnative_sum is not unset:
            kwargs["mobile_rum_session_count_reactnative_sum"] = mobile_rum_session_count_reactnative_sum
        if mobile_rum_session_count_roku_sum is not unset:
            kwargs["mobile_rum_session_count_roku_sum"] = mobile_rum_session_count_roku_sum
        if mobile_rum_session_count_sum is not unset:
            kwargs["mobile_rum_session_count_sum"] = mobile_rum_session_count_sum
        if mobile_rum_units_sum is not unset:
            kwargs["mobile_rum_units_sum"] = mobile_rum_units_sum
        if name is not unset:
            kwargs["name"] = name
        if ndm_netflow_events_sum is not unset:
            kwargs["ndm_netflow_events_sum"] = ndm_netflow_events_sum
        if netflow_indexed_events_count_sum is not unset:
            kwargs["netflow_indexed_events_count_sum"] = netflow_indexed_events_count_sum
        if npm_host_top99p is not unset:
            kwargs["npm_host_top99p"] = npm_host_top99p
        if observability_pipelines_bytes_processed_sum is not unset:
            kwargs["observability_pipelines_bytes_processed_sum"] = observability_pipelines_bytes_processed_sum
        if online_archive_events_count_sum is not unset:
            kwargs["online_archive_events_count_sum"] = online_archive_events_count_sum
        if opentelemetry_apm_host_top99p is not unset:
            kwargs["opentelemetry_apm_host_top99p"] = opentelemetry_apm_host_top99p
        if opentelemetry_host_top99p is not unset:
            kwargs["opentelemetry_host_top99p"] = opentelemetry_host_top99p
        if profiling_aas_count_top99p is not unset:
            kwargs["profiling_aas_count_top99p"] = profiling_aas_count_top99p
        if profiling_host_top99p is not unset:
            kwargs["profiling_host_top99p"] = profiling_host_top99p
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if region is not unset:
            kwargs["region"] = region
        if rum_browser_and_mobile_session_count is not unset:
            kwargs["rum_browser_and_mobile_session_count"] = rum_browser_and_mobile_session_count
        if rum_browser_legacy_session_count_sum is not unset:
            kwargs["rum_browser_legacy_session_count_sum"] = rum_browser_legacy_session_count_sum
        if rum_browser_lite_session_count_sum is not unset:
            kwargs["rum_browser_lite_session_count_sum"] = rum_browser_lite_session_count_sum
        if rum_browser_replay_session_count_sum is not unset:
            kwargs["rum_browser_replay_session_count_sum"] = rum_browser_replay_session_count_sum
        if rum_lite_session_count_sum is not unset:
            kwargs["rum_lite_session_count_sum"] = rum_lite_session_count_sum
        if rum_mobile_legacy_session_count_android_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_android_sum"] = rum_mobile_legacy_session_count_android_sum
        if rum_mobile_legacy_session_count_flutter_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_flutter_sum"] = rum_mobile_legacy_session_count_flutter_sum
        if rum_mobile_legacy_session_count_ios_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_ios_sum"] = rum_mobile_legacy_session_count_ios_sum
        if rum_mobile_legacy_session_count_reactnative_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_reactnative_sum"] = rum_mobile_legacy_session_count_reactnative_sum
        if rum_mobile_legacy_session_count_roku_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_roku_sum"] = rum_mobile_legacy_session_count_roku_sum
        if rum_mobile_lite_session_count_android_sum is not unset:
            kwargs["rum_mobile_lite_session_count_android_sum"] = rum_mobile_lite_session_count_android_sum
        if rum_mobile_lite_session_count_flutter_sum is not unset:
            kwargs["rum_mobile_lite_session_count_flutter_sum"] = rum_mobile_lite_session_count_flutter_sum
        if rum_mobile_lite_session_count_ios_sum is not unset:
            kwargs["rum_mobile_lite_session_count_ios_sum"] = rum_mobile_lite_session_count_ios_sum
        if rum_mobile_lite_session_count_reactnative_sum is not unset:
            kwargs["rum_mobile_lite_session_count_reactnative_sum"] = rum_mobile_lite_session_count_reactnative_sum
        if rum_mobile_lite_session_count_roku_sum is not unset:
            kwargs["rum_mobile_lite_session_count_roku_sum"] = rum_mobile_lite_session_count_roku_sum
        if rum_replay_session_count_sum is not unset:
            kwargs["rum_replay_session_count_sum"] = rum_replay_session_count_sum
        if rum_session_count_sum is not unset:
            kwargs["rum_session_count_sum"] = rum_session_count_sum
        if rum_total_session_count_sum is not unset:
            kwargs["rum_total_session_count_sum"] = rum_total_session_count_sum
        if rum_units_sum is not unset:
            kwargs["rum_units_sum"] = rum_units_sum
        if sds_apm_scanned_bytes_sum is not unset:
            kwargs["sds_apm_scanned_bytes_sum"] = sds_apm_scanned_bytes_sum
        if sds_events_scanned_bytes_sum is not unset:
            kwargs["sds_events_scanned_bytes_sum"] = sds_events_scanned_bytes_sum
        if sds_logs_scanned_bytes_sum is not unset:
            kwargs["sds_logs_scanned_bytes_sum"] = sds_logs_scanned_bytes_sum
        if sds_rum_scanned_bytes_sum is not unset:
            kwargs["sds_rum_scanned_bytes_sum"] = sds_rum_scanned_bytes_sum
        if sds_total_scanned_bytes_sum is not unset:
            kwargs["sds_total_scanned_bytes_sum"] = sds_total_scanned_bytes_sum
        if serverless_apps_azure_count_avg is not unset:
            kwargs["serverless_apps_azure_count_avg"] = serverless_apps_azure_count_avg
        if serverless_apps_google_count_avg is not unset:
            kwargs["serverless_apps_google_count_avg"] = serverless_apps_google_count_avg
        if serverless_apps_total_count_avg is not unset:
            kwargs["serverless_apps_total_count_avg"] = serverless_apps_total_count_avg
        if synthetics_browser_check_calls_count_sum is not unset:
            kwargs["synthetics_browser_check_calls_count_sum"] = synthetics_browser_check_calls_count_sum
        if synthetics_check_calls_count_sum is not unset:
            kwargs["synthetics_check_calls_count_sum"] = synthetics_check_calls_count_sum
        if synthetics_mobile_test_runs_sum is not unset:
            kwargs["synthetics_mobile_test_runs_sum"] = synthetics_mobile_test_runs_sum
        if synthetics_parallel_testing_max_slots_hwm is not unset:
            kwargs["synthetics_parallel_testing_max_slots_hwm"] = synthetics_parallel_testing_max_slots_hwm
        if trace_search_indexed_events_count_sum is not unset:
            kwargs["trace_search_indexed_events_count_sum"] = trace_search_indexed_events_count_sum
        if twol_ingested_events_bytes_sum is not unset:
            kwargs["twol_ingested_events_bytes_sum"] = twol_ingested_events_bytes_sum
        if universal_service_monitoring_host_top99p is not unset:
            kwargs["universal_service_monitoring_host_top99p"] = universal_service_monitoring_host_top99p
        if vsphere_host_top99p is not unset:
            kwargs["vsphere_host_top99p"] = vsphere_host_top99p
        if vuln_management_host_count_top99p is not unset:
            kwargs["vuln_management_host_count_top99p"] = vuln_management_host_count_top99p
        if workflow_executions_usage_sum is not unset:
            kwargs["workflow_executions_usage_sum"] = workflow_executions_usage_sum
        super().__init__(kwargs)
