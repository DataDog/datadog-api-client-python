# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.logs_by_retention import LogsByRetention
    from datadog_api_client.v1.model.usage_summary_date import UsageSummaryDate


class UsageSummaryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_by_retention import LogsByRetention
        from datadog_api_client.v1.model.usage_summary_date import UsageSummaryDate

        return {
            "agent_host_top99p_sum": (int,),
            "apm_azure_app_service_host_top99p_sum": (int,),
            "apm_devsecops_host_top99p_sum": (int,),
            "apm_fargate_count_avg_sum": (int,),
            "apm_host_top99p_sum": (int,),
            "appsec_fargate_count_avg_sum": (int,),
            "asm_serverless_agg_sum": (int,),
            "audit_logs_lines_indexed_agg_sum": (int,),
            "audit_trail_enabled_hwm_sum": (int,),
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
            "ci_visibility_itr_committers_hwm_sum": (int,),
            "ci_visibility_pipeline_committers_hwm_sum": (int,),
            "ci_visibility_test_committers_hwm_sum": (int,),
            "cloud_cost_management_aws_host_count_avg_sum": (int,),
            "cloud_cost_management_azure_host_count_avg_sum": (int,),
            "cloud_cost_management_gcp_host_count_avg_sum": (int,),
            "cloud_cost_management_host_count_avg_sum": (int,),
            "cloud_siem_events_agg_sum": (int,),
            "code_analysis_sa_committers_hwm_sum": (int,),
            "code_analysis_sca_committers_hwm_sum": (int,),
            "code_security_host_top99p_sum": (int,),
            "container_avg_sum": (int,),
            "container_excl_agent_avg_sum": (int,),
            "container_hwm_sum": (int,),
            "csm_container_enterprise_compliance_count_agg_sum": (int,),
            "csm_container_enterprise_cws_count_agg_sum": (int,),
            "csm_container_enterprise_total_count_agg_sum": (int,),
            "csm_host_enterprise_aas_host_count_top99p_sum": (int,),
            "csm_host_enterprise_aws_host_count_top99p_sum": (int,),
            "csm_host_enterprise_azure_host_count_top99p_sum": (int,),
            "csm_host_enterprise_compliance_host_count_top99p_sum": (int,),
            "csm_host_enterprise_cws_host_count_top99p_sum": (int,),
            "csm_host_enterprise_gcp_host_count_top99p_sum": (int,),
            "csm_host_enterprise_total_host_count_top99p_sum": (int,),
            "cspm_aas_host_top99p_sum": (int,),
            "cspm_aws_host_top99p_sum": (int,),
            "cspm_azure_host_top99p_sum": (int,),
            "cspm_container_avg_sum": (int,),
            "cspm_container_hwm_sum": (int,),
            "cspm_gcp_host_top99p_sum": (int,),
            "cspm_host_top99p_sum": (int,),
            "custom_historical_ts_sum": (int,),
            "custom_live_ts_sum": (int,),
            "custom_ts_sum": (int,),
            "cws_container_avg_sum": (int,),
            "cws_fargate_task_avg_sum": (int,),
            "cws_host_top99p_sum": (int,),
            "data_jobs_monitoring_host_hr_agg_sum": (int,),
            "dbm_host_top99p_sum": (int,),
            "dbm_queries_avg_sum": (int,),
            "end_date": (datetime,),
            "eph_infra_host_agent_agg_sum": (int,),
            "eph_infra_host_alibaba_agg_sum": (int,),
            "eph_infra_host_aws_agg_sum": (int,),
            "eph_infra_host_azure_agg_sum": (int,),
            "eph_infra_host_ent_agg_sum": (int,),
            "eph_infra_host_gcp_agg_sum": (int,),
            "eph_infra_host_heroku_agg_sum": (int,),
            "eph_infra_host_only_aas_agg_sum": (int,),
            "eph_infra_host_only_vsphere_agg_sum": (int,),
            "eph_infra_host_opentelemetry_agg_sum": (int,),
            "eph_infra_host_opentelemetry_apm_agg_sum": (int,),
            "eph_infra_host_pro_agg_sum": (int,),
            "eph_infra_host_proplus_agg_sum": (int,),
            "error_tracking_apm_error_events_agg_sum": (int,),
            "error_tracking_error_events_agg_sum": (int,),
            "error_tracking_events_agg_sum": (int,),
            "error_tracking_rum_error_events_agg_sum": (int,),
            "fargate_container_profiler_profiling_fargate_avg_sum": (int,),
            "fargate_container_profiler_profiling_fargate_eks_avg_sum": (int,),
            "fargate_tasks_count_avg_sum": (int,),
            "fargate_tasks_count_hwm_sum": (int,),
            "flex_logs_compute_large_avg_sum": (int,),
            "flex_logs_compute_medium_avg_sum": (int,),
            "flex_logs_compute_small_avg_sum": (int,),
            "flex_logs_compute_xsmall_avg_sum": (int,),
            "flex_logs_starter_avg_sum": (int,),
            "flex_logs_starter_storage_index_avg_sum": (int,),
            "flex_logs_starter_storage_retention_adjustment_avg_sum": (int,),
            "flex_stored_logs_avg_sum": (int,),
            "forwarding_events_bytes_agg_sum": (int,),
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
            "llm_observability_agg_sum": (int,),
            "llm_observability_min_spend_agg_sum": (int,),
            "logs_by_retention": (LogsByRetention,),
            "mobile_rum_lite_session_count_agg_sum": (int,),
            "mobile_rum_session_count_agg_sum": (int,),
            "mobile_rum_session_count_android_agg_sum": (int,),
            "mobile_rum_session_count_flutter_agg_sum": (int,),
            "mobile_rum_session_count_ios_agg_sum": (int,),
            "mobile_rum_session_count_reactnative_agg_sum": (int,),
            "mobile_rum_session_count_roku_agg_sum": (int,),
            "mobile_rum_units_agg_sum": (int,),
            "ndm_netflow_events_agg_sum": (int,),
            "netflow_indexed_events_count_agg_sum": (int,),
            "network_device_wireless_top99p_sum": (int,),
            "npm_host_top99p_sum": (int,),
            "observability_pipelines_bytes_processed_agg_sum": (int,),
            "oci_host_agg_sum": (int,),
            "oci_host_top99p_sum": (int,),
            "online_archive_events_count_agg_sum": (int,),
            "opentelemetry_apm_host_top99p_sum": (int,),
            "opentelemetry_host_top99p_sum": (int,),
            "product_analytics_agg_sum": (int,),
            "profiling_aas_count_top99p_sum": (int,),
            "profiling_container_agent_count_avg": (int,),
            "profiling_host_count_top99p_sum": (int,),
            "published_app_hwm_sum": (int,),
            "rehydrated_indexed_events_agg_sum": (int,),
            "rehydrated_ingested_bytes_agg_sum": (int,),
            "rum_browser_and_mobile_session_count": (int,),
            "rum_browser_legacy_session_count_agg_sum": (int,),
            "rum_browser_lite_session_count_agg_sum": (int,),
            "rum_browser_replay_session_count_agg_sum": (int,),
            "rum_indexed_sessions_agg_sum": (int,),
            "rum_ingested_sessions_agg_sum": (int,),
            "rum_lite_session_count_agg_sum": (int,),
            "rum_mobile_legacy_session_count_android_agg_sum": (int,),
            "rum_mobile_legacy_session_count_flutter_agg_sum": (int,),
            "rum_mobile_legacy_session_count_ios_agg_sum": (int,),
            "rum_mobile_legacy_session_count_reactnative_agg_sum": (int,),
            "rum_mobile_legacy_session_count_roku_agg_sum": (int,),
            "rum_mobile_lite_session_count_android_agg_sum": (int,),
            "rum_mobile_lite_session_count_flutter_agg_sum": (int,),
            "rum_mobile_lite_session_count_ios_agg_sum": (int,),
            "rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum": (int,),
            "rum_mobile_lite_session_count_reactnative_agg_sum": (int,),
            "rum_mobile_lite_session_count_roku_agg_sum": (int,),
            "rum_mobile_lite_session_count_unity_agg_sum": (int,),
            "rum_mobile_replay_session_count_android_agg_sum": (int,),
            "rum_mobile_replay_session_count_ios_agg_sum": (int,),
            "rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum": (int,),
            "rum_mobile_replay_session_count_reactnative_agg_sum": (int,),
            "rum_replay_session_count_agg_sum": (int,),
            "rum_session_count_agg_sum": (int,),
            "rum_session_replay_add_on_agg_sum": (int,),
            "rum_total_session_count_agg_sum": (int,),
            "rum_units_agg_sum": (int,),
            "sca_fargate_count_avg_sum": (int,),
            "sca_fargate_count_hwm_sum": (int,),
            "sds_apm_scanned_bytes_sum": (int,),
            "sds_events_scanned_bytes_sum": (int,),
            "sds_logs_scanned_bytes_sum": (int,),
            "sds_rum_scanned_bytes_sum": (int,),
            "sds_total_scanned_bytes_sum": (int,),
            "serverless_apps_azure_count_avg_sum": (int,),
            "serverless_apps_google_count_avg_sum": (int,),
            "serverless_apps_total_count_avg_sum": (int,),
            "siem_analyzed_logs_add_on_count_agg_sum": (int,),
            "start_date": (datetime,),
            "synthetics_browser_check_calls_count_agg_sum": (int,),
            "synthetics_check_calls_count_agg_sum": (int,),
            "synthetics_mobile_test_runs_agg_sum": (int,),
            "synthetics_parallel_testing_max_slots_hwm_sum": (int,),
            "trace_search_indexed_events_count_agg_sum": (int,),
            "twol_ingested_events_bytes_agg_sum": (int,),
            "universal_service_monitoring_host_top99p_sum": (int,),
            "usage": ([UsageSummaryDate],),
            "vsphere_host_top99p_sum": (int,),
            "vuln_management_host_count_top99p_sum": (int,),
            "workflow_executions_usage_agg_sum": (int,),
        }

    attribute_map = {
        "agent_host_top99p_sum": "agent_host_top99p_sum",
        "apm_azure_app_service_host_top99p_sum": "apm_azure_app_service_host_top99p_sum",
        "apm_devsecops_host_top99p_sum": "apm_devsecops_host_top99p_sum",
        "apm_fargate_count_avg_sum": "apm_fargate_count_avg_sum",
        "apm_host_top99p_sum": "apm_host_top99p_sum",
        "appsec_fargate_count_avg_sum": "appsec_fargate_count_avg_sum",
        "asm_serverless_agg_sum": "asm_serverless_agg_sum",
        "audit_logs_lines_indexed_agg_sum": "audit_logs_lines_indexed_agg_sum",
        "audit_trail_enabled_hwm_sum": "audit_trail_enabled_hwm_sum",
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
        "ci_visibility_itr_committers_hwm_sum": "ci_visibility_itr_committers_hwm_sum",
        "ci_visibility_pipeline_committers_hwm_sum": "ci_visibility_pipeline_committers_hwm_sum",
        "ci_visibility_test_committers_hwm_sum": "ci_visibility_test_committers_hwm_sum",
        "cloud_cost_management_aws_host_count_avg_sum": "cloud_cost_management_aws_host_count_avg_sum",
        "cloud_cost_management_azure_host_count_avg_sum": "cloud_cost_management_azure_host_count_avg_sum",
        "cloud_cost_management_gcp_host_count_avg_sum": "cloud_cost_management_gcp_host_count_avg_sum",
        "cloud_cost_management_host_count_avg_sum": "cloud_cost_management_host_count_avg_sum",
        "cloud_siem_events_agg_sum": "cloud_siem_events_agg_sum",
        "code_analysis_sa_committers_hwm_sum": "code_analysis_sa_committers_hwm_sum",
        "code_analysis_sca_committers_hwm_sum": "code_analysis_sca_committers_hwm_sum",
        "code_security_host_top99p_sum": "code_security_host_top99p_sum",
        "container_avg_sum": "container_avg_sum",
        "container_excl_agent_avg_sum": "container_excl_agent_avg_sum",
        "container_hwm_sum": "container_hwm_sum",
        "csm_container_enterprise_compliance_count_agg_sum": "csm_container_enterprise_compliance_count_agg_sum",
        "csm_container_enterprise_cws_count_agg_sum": "csm_container_enterprise_cws_count_agg_sum",
        "csm_container_enterprise_total_count_agg_sum": "csm_container_enterprise_total_count_agg_sum",
        "csm_host_enterprise_aas_host_count_top99p_sum": "csm_host_enterprise_aas_host_count_top99p_sum",
        "csm_host_enterprise_aws_host_count_top99p_sum": "csm_host_enterprise_aws_host_count_top99p_sum",
        "csm_host_enterprise_azure_host_count_top99p_sum": "csm_host_enterprise_azure_host_count_top99p_sum",
        "csm_host_enterprise_compliance_host_count_top99p_sum": "csm_host_enterprise_compliance_host_count_top99p_sum",
        "csm_host_enterprise_cws_host_count_top99p_sum": "csm_host_enterprise_cws_host_count_top99p_sum",
        "csm_host_enterprise_gcp_host_count_top99p_sum": "csm_host_enterprise_gcp_host_count_top99p_sum",
        "csm_host_enterprise_total_host_count_top99p_sum": "csm_host_enterprise_total_host_count_top99p_sum",
        "cspm_aas_host_top99p_sum": "cspm_aas_host_top99p_sum",
        "cspm_aws_host_top99p_sum": "cspm_aws_host_top99p_sum",
        "cspm_azure_host_top99p_sum": "cspm_azure_host_top99p_sum",
        "cspm_container_avg_sum": "cspm_container_avg_sum",
        "cspm_container_hwm_sum": "cspm_container_hwm_sum",
        "cspm_gcp_host_top99p_sum": "cspm_gcp_host_top99p_sum",
        "cspm_host_top99p_sum": "cspm_host_top99p_sum",
        "custom_historical_ts_sum": "custom_historical_ts_sum",
        "custom_live_ts_sum": "custom_live_ts_sum",
        "custom_ts_sum": "custom_ts_sum",
        "cws_container_avg_sum": "cws_container_avg_sum",
        "cws_fargate_task_avg_sum": "cws_fargate_task_avg_sum",
        "cws_host_top99p_sum": "cws_host_top99p_sum",
        "data_jobs_monitoring_host_hr_agg_sum": "data_jobs_monitoring_host_hr_agg_sum",
        "dbm_host_top99p_sum": "dbm_host_top99p_sum",
        "dbm_queries_avg_sum": "dbm_queries_avg_sum",
        "end_date": "end_date",
        "eph_infra_host_agent_agg_sum": "eph_infra_host_agent_agg_sum",
        "eph_infra_host_alibaba_agg_sum": "eph_infra_host_alibaba_agg_sum",
        "eph_infra_host_aws_agg_sum": "eph_infra_host_aws_agg_sum",
        "eph_infra_host_azure_agg_sum": "eph_infra_host_azure_agg_sum",
        "eph_infra_host_ent_agg_sum": "eph_infra_host_ent_agg_sum",
        "eph_infra_host_gcp_agg_sum": "eph_infra_host_gcp_agg_sum",
        "eph_infra_host_heroku_agg_sum": "eph_infra_host_heroku_agg_sum",
        "eph_infra_host_only_aas_agg_sum": "eph_infra_host_only_aas_agg_sum",
        "eph_infra_host_only_vsphere_agg_sum": "eph_infra_host_only_vsphere_agg_sum",
        "eph_infra_host_opentelemetry_agg_sum": "eph_infra_host_opentelemetry_agg_sum",
        "eph_infra_host_opentelemetry_apm_agg_sum": "eph_infra_host_opentelemetry_apm_agg_sum",
        "eph_infra_host_pro_agg_sum": "eph_infra_host_pro_agg_sum",
        "eph_infra_host_proplus_agg_sum": "eph_infra_host_proplus_agg_sum",
        "error_tracking_apm_error_events_agg_sum": "error_tracking_apm_error_events_agg_sum",
        "error_tracking_error_events_agg_sum": "error_tracking_error_events_agg_sum",
        "error_tracking_events_agg_sum": "error_tracking_events_agg_sum",
        "error_tracking_rum_error_events_agg_sum": "error_tracking_rum_error_events_agg_sum",
        "fargate_container_profiler_profiling_fargate_avg_sum": "fargate_container_profiler_profiling_fargate_avg_sum",
        "fargate_container_profiler_profiling_fargate_eks_avg_sum": "fargate_container_profiler_profiling_fargate_eks_avg_sum",
        "fargate_tasks_count_avg_sum": "fargate_tasks_count_avg_sum",
        "fargate_tasks_count_hwm_sum": "fargate_tasks_count_hwm_sum",
        "flex_logs_compute_large_avg_sum": "flex_logs_compute_large_avg_sum",
        "flex_logs_compute_medium_avg_sum": "flex_logs_compute_medium_avg_sum",
        "flex_logs_compute_small_avg_sum": "flex_logs_compute_small_avg_sum",
        "flex_logs_compute_xsmall_avg_sum": "flex_logs_compute_xsmall_avg_sum",
        "flex_logs_starter_avg_sum": "flex_logs_starter_avg_sum",
        "flex_logs_starter_storage_index_avg_sum": "flex_logs_starter_storage_index_avg_sum",
        "flex_logs_starter_storage_retention_adjustment_avg_sum": "flex_logs_starter_storage_retention_adjustment_avg_sum",
        "flex_stored_logs_avg_sum": "flex_stored_logs_avg_sum",
        "forwarding_events_bytes_agg_sum": "forwarding_events_bytes_agg_sum",
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
        "llm_observability_agg_sum": "llm_observability_agg_sum",
        "llm_observability_min_spend_agg_sum": "llm_observability_min_spend_agg_sum",
        "logs_by_retention": "logs_by_retention",
        "mobile_rum_lite_session_count_agg_sum": "mobile_rum_lite_session_count_agg_sum",
        "mobile_rum_session_count_agg_sum": "mobile_rum_session_count_agg_sum",
        "mobile_rum_session_count_android_agg_sum": "mobile_rum_session_count_android_agg_sum",
        "mobile_rum_session_count_flutter_agg_sum": "mobile_rum_session_count_flutter_agg_sum",
        "mobile_rum_session_count_ios_agg_sum": "mobile_rum_session_count_ios_agg_sum",
        "mobile_rum_session_count_reactnative_agg_sum": "mobile_rum_session_count_reactnative_agg_sum",
        "mobile_rum_session_count_roku_agg_sum": "mobile_rum_session_count_roku_agg_sum",
        "mobile_rum_units_agg_sum": "mobile_rum_units_agg_sum",
        "ndm_netflow_events_agg_sum": "ndm_netflow_events_agg_sum",
        "netflow_indexed_events_count_agg_sum": "netflow_indexed_events_count_agg_sum",
        "network_device_wireless_top99p_sum": "network_device_wireless_top99p_sum",
        "npm_host_top99p_sum": "npm_host_top99p_sum",
        "observability_pipelines_bytes_processed_agg_sum": "observability_pipelines_bytes_processed_agg_sum",
        "oci_host_agg_sum": "oci_host_agg_sum",
        "oci_host_top99p_sum": "oci_host_top99p_sum",
        "online_archive_events_count_agg_sum": "online_archive_events_count_agg_sum",
        "opentelemetry_apm_host_top99p_sum": "opentelemetry_apm_host_top99p_sum",
        "opentelemetry_host_top99p_sum": "opentelemetry_host_top99p_sum",
        "product_analytics_agg_sum": "product_analytics_agg_sum",
        "profiling_aas_count_top99p_sum": "profiling_aas_count_top99p_sum",
        "profiling_container_agent_count_avg": "profiling_container_agent_count_avg",
        "profiling_host_count_top99p_sum": "profiling_host_count_top99p_sum",
        "published_app_hwm_sum": "published_app_hwm_sum",
        "rehydrated_indexed_events_agg_sum": "rehydrated_indexed_events_agg_sum",
        "rehydrated_ingested_bytes_agg_sum": "rehydrated_ingested_bytes_agg_sum",
        "rum_browser_and_mobile_session_count": "rum_browser_and_mobile_session_count",
        "rum_browser_legacy_session_count_agg_sum": "rum_browser_legacy_session_count_agg_sum",
        "rum_browser_lite_session_count_agg_sum": "rum_browser_lite_session_count_agg_sum",
        "rum_browser_replay_session_count_agg_sum": "rum_browser_replay_session_count_agg_sum",
        "rum_indexed_sessions_agg_sum": "rum_indexed_sessions_agg_sum",
        "rum_ingested_sessions_agg_sum": "rum_ingested_sessions_agg_sum",
        "rum_lite_session_count_agg_sum": "rum_lite_session_count_agg_sum",
        "rum_mobile_legacy_session_count_android_agg_sum": "rum_mobile_legacy_session_count_android_agg_sum",
        "rum_mobile_legacy_session_count_flutter_agg_sum": "rum_mobile_legacy_session_count_flutter_agg_sum",
        "rum_mobile_legacy_session_count_ios_agg_sum": "rum_mobile_legacy_session_count_ios_agg_sum",
        "rum_mobile_legacy_session_count_reactnative_agg_sum": "rum_mobile_legacy_session_count_reactnative_agg_sum",
        "rum_mobile_legacy_session_count_roku_agg_sum": "rum_mobile_legacy_session_count_roku_agg_sum",
        "rum_mobile_lite_session_count_android_agg_sum": "rum_mobile_lite_session_count_android_agg_sum",
        "rum_mobile_lite_session_count_flutter_agg_sum": "rum_mobile_lite_session_count_flutter_agg_sum",
        "rum_mobile_lite_session_count_ios_agg_sum": "rum_mobile_lite_session_count_ios_agg_sum",
        "rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum": "rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum",
        "rum_mobile_lite_session_count_reactnative_agg_sum": "rum_mobile_lite_session_count_reactnative_agg_sum",
        "rum_mobile_lite_session_count_roku_agg_sum": "rum_mobile_lite_session_count_roku_agg_sum",
        "rum_mobile_lite_session_count_unity_agg_sum": "rum_mobile_lite_session_count_unity_agg_sum",
        "rum_mobile_replay_session_count_android_agg_sum": "rum_mobile_replay_session_count_android_agg_sum",
        "rum_mobile_replay_session_count_ios_agg_sum": "rum_mobile_replay_session_count_ios_agg_sum",
        "rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum": "rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum",
        "rum_mobile_replay_session_count_reactnative_agg_sum": "rum_mobile_replay_session_count_reactnative_agg_sum",
        "rum_replay_session_count_agg_sum": "rum_replay_session_count_agg_sum",
        "rum_session_count_agg_sum": "rum_session_count_agg_sum",
        "rum_session_replay_add_on_agg_sum": "rum_session_replay_add_on_agg_sum",
        "rum_total_session_count_agg_sum": "rum_total_session_count_agg_sum",
        "rum_units_agg_sum": "rum_units_agg_sum",
        "sca_fargate_count_avg_sum": "sca_fargate_count_avg_sum",
        "sca_fargate_count_hwm_sum": "sca_fargate_count_hwm_sum",
        "sds_apm_scanned_bytes_sum": "sds_apm_scanned_bytes_sum",
        "sds_events_scanned_bytes_sum": "sds_events_scanned_bytes_sum",
        "sds_logs_scanned_bytes_sum": "sds_logs_scanned_bytes_sum",
        "sds_rum_scanned_bytes_sum": "sds_rum_scanned_bytes_sum",
        "sds_total_scanned_bytes_sum": "sds_total_scanned_bytes_sum",
        "serverless_apps_azure_count_avg_sum": "serverless_apps_azure_count_avg_sum",
        "serverless_apps_google_count_avg_sum": "serverless_apps_google_count_avg_sum",
        "serverless_apps_total_count_avg_sum": "serverless_apps_total_count_avg_sum",
        "siem_analyzed_logs_add_on_count_agg_sum": "siem_analyzed_logs_add_on_count_agg_sum",
        "start_date": "start_date",
        "synthetics_browser_check_calls_count_agg_sum": "synthetics_browser_check_calls_count_agg_sum",
        "synthetics_check_calls_count_agg_sum": "synthetics_check_calls_count_agg_sum",
        "synthetics_mobile_test_runs_agg_sum": "synthetics_mobile_test_runs_agg_sum",
        "synthetics_parallel_testing_max_slots_hwm_sum": "synthetics_parallel_testing_max_slots_hwm_sum",
        "trace_search_indexed_events_count_agg_sum": "trace_search_indexed_events_count_agg_sum",
        "twol_ingested_events_bytes_agg_sum": "twol_ingested_events_bytes_agg_sum",
        "universal_service_monitoring_host_top99p_sum": "universal_service_monitoring_host_top99p_sum",
        "usage": "usage",
        "vsphere_host_top99p_sum": "vsphere_host_top99p_sum",
        "vuln_management_host_count_top99p_sum": "vuln_management_host_count_top99p_sum",
        "workflow_executions_usage_agg_sum": "workflow_executions_usage_agg_sum",
    }

    def __init__(
        self_,
        agent_host_top99p_sum: Union[int, UnsetType] = unset,
        apm_azure_app_service_host_top99p_sum: Union[int, UnsetType] = unset,
        apm_devsecops_host_top99p_sum: Union[int, UnsetType] = unset,
        apm_fargate_count_avg_sum: Union[int, UnsetType] = unset,
        apm_host_top99p_sum: Union[int, UnsetType] = unset,
        appsec_fargate_count_avg_sum: Union[int, UnsetType] = unset,
        asm_serverless_agg_sum: Union[int, UnsetType] = unset,
        audit_logs_lines_indexed_agg_sum: Union[int, UnsetType] = unset,
        audit_trail_enabled_hwm_sum: Union[int, UnsetType] = unset,
        avg_profiled_fargate_tasks_sum: Union[int, UnsetType] = unset,
        aws_host_top99p_sum: Union[int, UnsetType] = unset,
        aws_lambda_func_count: Union[int, UnsetType] = unset,
        aws_lambda_invocations_sum: Union[int, UnsetType] = unset,
        azure_app_service_top99p_sum: Union[int, UnsetType] = unset,
        azure_host_top99p_sum: Union[int, UnsetType] = unset,
        billable_ingested_bytes_agg_sum: Union[int, UnsetType] = unset,
        browser_rum_lite_session_count_agg_sum: Union[int, UnsetType] = unset,
        browser_rum_replay_session_count_agg_sum: Union[int, UnsetType] = unset,
        browser_rum_units_agg_sum: Union[int, UnsetType] = unset,
        ci_pipeline_indexed_spans_agg_sum: Union[int, UnsetType] = unset,
        ci_test_indexed_spans_agg_sum: Union[int, UnsetType] = unset,
        ci_visibility_itr_committers_hwm_sum: Union[int, UnsetType] = unset,
        ci_visibility_pipeline_committers_hwm_sum: Union[int, UnsetType] = unset,
        ci_visibility_test_committers_hwm_sum: Union[int, UnsetType] = unset,
        cloud_cost_management_aws_host_count_avg_sum: Union[int, UnsetType] = unset,
        cloud_cost_management_azure_host_count_avg_sum: Union[int, UnsetType] = unset,
        cloud_cost_management_gcp_host_count_avg_sum: Union[int, UnsetType] = unset,
        cloud_cost_management_host_count_avg_sum: Union[int, UnsetType] = unset,
        cloud_siem_events_agg_sum: Union[int, UnsetType] = unset,
        code_analysis_sa_committers_hwm_sum: Union[int, UnsetType] = unset,
        code_analysis_sca_committers_hwm_sum: Union[int, UnsetType] = unset,
        code_security_host_top99p_sum: Union[int, UnsetType] = unset,
        container_avg_sum: Union[int, UnsetType] = unset,
        container_excl_agent_avg_sum: Union[int, UnsetType] = unset,
        container_hwm_sum: Union[int, UnsetType] = unset,
        csm_container_enterprise_compliance_count_agg_sum: Union[int, UnsetType] = unset,
        csm_container_enterprise_cws_count_agg_sum: Union[int, UnsetType] = unset,
        csm_container_enterprise_total_count_agg_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_aas_host_count_top99p_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_aws_host_count_top99p_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_azure_host_count_top99p_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_compliance_host_count_top99p_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_cws_host_count_top99p_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_gcp_host_count_top99p_sum: Union[int, UnsetType] = unset,
        csm_host_enterprise_total_host_count_top99p_sum: Union[int, UnsetType] = unset,
        cspm_aas_host_top99p_sum: Union[int, UnsetType] = unset,
        cspm_aws_host_top99p_sum: Union[int, UnsetType] = unset,
        cspm_azure_host_top99p_sum: Union[int, UnsetType] = unset,
        cspm_container_avg_sum: Union[int, UnsetType] = unset,
        cspm_container_hwm_sum: Union[int, UnsetType] = unset,
        cspm_gcp_host_top99p_sum: Union[int, UnsetType] = unset,
        cspm_host_top99p_sum: Union[int, UnsetType] = unset,
        custom_historical_ts_sum: Union[int, UnsetType] = unset,
        custom_live_ts_sum: Union[int, UnsetType] = unset,
        custom_ts_sum: Union[int, UnsetType] = unset,
        cws_container_avg_sum: Union[int, UnsetType] = unset,
        cws_fargate_task_avg_sum: Union[int, UnsetType] = unset,
        cws_host_top99p_sum: Union[int, UnsetType] = unset,
        data_jobs_monitoring_host_hr_agg_sum: Union[int, UnsetType] = unset,
        dbm_host_top99p_sum: Union[int, UnsetType] = unset,
        dbm_queries_avg_sum: Union[int, UnsetType] = unset,
        end_date: Union[datetime, UnsetType] = unset,
        eph_infra_host_agent_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_alibaba_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_aws_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_azure_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_ent_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_gcp_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_heroku_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_only_aas_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_only_vsphere_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_opentelemetry_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_opentelemetry_apm_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_pro_agg_sum: Union[int, UnsetType] = unset,
        eph_infra_host_proplus_agg_sum: Union[int, UnsetType] = unset,
        error_tracking_apm_error_events_agg_sum: Union[int, UnsetType] = unset,
        error_tracking_error_events_agg_sum: Union[int, UnsetType] = unset,
        error_tracking_events_agg_sum: Union[int, UnsetType] = unset,
        error_tracking_rum_error_events_agg_sum: Union[int, UnsetType] = unset,
        fargate_container_profiler_profiling_fargate_avg_sum: Union[int, UnsetType] = unset,
        fargate_container_profiler_profiling_fargate_eks_avg_sum: Union[int, UnsetType] = unset,
        fargate_tasks_count_avg_sum: Union[int, UnsetType] = unset,
        fargate_tasks_count_hwm_sum: Union[int, UnsetType] = unset,
        flex_logs_compute_large_avg_sum: Union[int, UnsetType] = unset,
        flex_logs_compute_medium_avg_sum: Union[int, UnsetType] = unset,
        flex_logs_compute_small_avg_sum: Union[int, UnsetType] = unset,
        flex_logs_compute_xsmall_avg_sum: Union[int, UnsetType] = unset,
        flex_logs_starter_avg_sum: Union[int, UnsetType] = unset,
        flex_logs_starter_storage_index_avg_sum: Union[int, UnsetType] = unset,
        flex_logs_starter_storage_retention_adjustment_avg_sum: Union[int, UnsetType] = unset,
        flex_stored_logs_avg_sum: Union[int, UnsetType] = unset,
        forwarding_events_bytes_agg_sum: Union[int, UnsetType] = unset,
        gcp_host_top99p_sum: Union[int, UnsetType] = unset,
        heroku_host_top99p_sum: Union[int, UnsetType] = unset,
        incident_management_monthly_active_users_hwm_sum: Union[int, UnsetType] = unset,
        indexed_events_count_agg_sum: Union[int, UnsetType] = unset,
        infra_host_top99p_sum: Union[int, UnsetType] = unset,
        ingested_events_bytes_agg_sum: Union[int, UnsetType] = unset,
        iot_device_agg_sum: Union[int, UnsetType] = unset,
        iot_device_top99p_sum: Union[int, UnsetType] = unset,
        last_updated: Union[datetime, UnsetType] = unset,
        live_indexed_events_agg_sum: Union[int, UnsetType] = unset,
        live_ingested_bytes_agg_sum: Union[int, UnsetType] = unset,
        llm_observability_agg_sum: Union[int, UnsetType] = unset,
        llm_observability_min_spend_agg_sum: Union[int, UnsetType] = unset,
        logs_by_retention: Union[LogsByRetention, UnsetType] = unset,
        mobile_rum_lite_session_count_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_android_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_flutter_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_ios_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_reactnative_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_session_count_roku_agg_sum: Union[int, UnsetType] = unset,
        mobile_rum_units_agg_sum: Union[int, UnsetType] = unset,
        ndm_netflow_events_agg_sum: Union[int, UnsetType] = unset,
        netflow_indexed_events_count_agg_sum: Union[int, UnsetType] = unset,
        network_device_wireless_top99p_sum: Union[int, UnsetType] = unset,
        npm_host_top99p_sum: Union[int, UnsetType] = unset,
        observability_pipelines_bytes_processed_agg_sum: Union[int, UnsetType] = unset,
        oci_host_agg_sum: Union[int, UnsetType] = unset,
        oci_host_top99p_sum: Union[int, UnsetType] = unset,
        online_archive_events_count_agg_sum: Union[int, UnsetType] = unset,
        opentelemetry_apm_host_top99p_sum: Union[int, UnsetType] = unset,
        opentelemetry_host_top99p_sum: Union[int, UnsetType] = unset,
        product_analytics_agg_sum: Union[int, UnsetType] = unset,
        profiling_aas_count_top99p_sum: Union[int, UnsetType] = unset,
        profiling_container_agent_count_avg: Union[int, UnsetType] = unset,
        profiling_host_count_top99p_sum: Union[int, UnsetType] = unset,
        published_app_hwm_sum: Union[int, UnsetType] = unset,
        rehydrated_indexed_events_agg_sum: Union[int, UnsetType] = unset,
        rehydrated_ingested_bytes_agg_sum: Union[int, UnsetType] = unset,
        rum_browser_and_mobile_session_count: Union[int, UnsetType] = unset,
        rum_browser_legacy_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_browser_lite_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_browser_replay_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_indexed_sessions_agg_sum: Union[int, UnsetType] = unset,
        rum_ingested_sessions_agg_sum: Union[int, UnsetType] = unset,
        rum_lite_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_android_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_flutter_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_ios_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_reactnative_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_legacy_session_count_roku_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_android_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_flutter_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_ios_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_reactnative_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_roku_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_lite_session_count_unity_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_replay_session_count_android_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_replay_session_count_ios_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum: Union[int, UnsetType] = unset,
        rum_mobile_replay_session_count_reactnative_agg_sum: Union[int, UnsetType] = unset,
        rum_replay_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_session_replay_add_on_agg_sum: Union[int, UnsetType] = unset,
        rum_total_session_count_agg_sum: Union[int, UnsetType] = unset,
        rum_units_agg_sum: Union[int, UnsetType] = unset,
        sca_fargate_count_avg_sum: Union[int, UnsetType] = unset,
        sca_fargate_count_hwm_sum: Union[int, UnsetType] = unset,
        sds_apm_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_events_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_logs_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_rum_scanned_bytes_sum: Union[int, UnsetType] = unset,
        sds_total_scanned_bytes_sum: Union[int, UnsetType] = unset,
        serverless_apps_azure_count_avg_sum: Union[int, UnsetType] = unset,
        serverless_apps_google_count_avg_sum: Union[int, UnsetType] = unset,
        serverless_apps_total_count_avg_sum: Union[int, UnsetType] = unset,
        siem_analyzed_logs_add_on_count_agg_sum: Union[int, UnsetType] = unset,
        start_date: Union[datetime, UnsetType] = unset,
        synthetics_browser_check_calls_count_agg_sum: Union[int, UnsetType] = unset,
        synthetics_check_calls_count_agg_sum: Union[int, UnsetType] = unset,
        synthetics_mobile_test_runs_agg_sum: Union[int, UnsetType] = unset,
        synthetics_parallel_testing_max_slots_hwm_sum: Union[int, UnsetType] = unset,
        trace_search_indexed_events_count_agg_sum: Union[int, UnsetType] = unset,
        twol_ingested_events_bytes_agg_sum: Union[int, UnsetType] = unset,
        universal_service_monitoring_host_top99p_sum: Union[int, UnsetType] = unset,
        usage: Union[List[UsageSummaryDate], UnsetType] = unset,
        vsphere_host_top99p_sum: Union[int, UnsetType] = unset,
        vuln_management_host_count_top99p_sum: Union[int, UnsetType] = unset,
        workflow_executions_usage_agg_sum: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response summarizing all usage aggregated across the months in the request for all organizations, and broken down by month and by organization.

        :param agent_host_top99p_sum: Shows the 99th percentile of all agent hosts over all hours in the current month for all organizations.
        :type agent_host_top99p_sum: int, optional

        :param apm_azure_app_service_host_top99p_sum: Shows the 99th percentile of all Azure app services using APM over all hours in the current month all organizations.
        :type apm_azure_app_service_host_top99p_sum: int, optional

        :param apm_devsecops_host_top99p_sum: Shows the 99th percentile of all APM DevSecOps hosts over all hours in the current month for all organizations.
        :type apm_devsecops_host_top99p_sum: int, optional

        :param apm_fargate_count_avg_sum: Shows the average of all APM ECS Fargate tasks over all hours in the current month for all organizations.
        :type apm_fargate_count_avg_sum: int, optional

        :param apm_host_top99p_sum: Shows the 99th percentile of all distinct APM hosts over all hours in the current month for all organizations.
        :type apm_host_top99p_sum: int, optional

        :param appsec_fargate_count_avg_sum: Shows the average of all Application Security Monitoring ECS Fargate tasks over all hours in the current month for all organizations.
        :type appsec_fargate_count_avg_sum: int, optional

        :param asm_serverless_agg_sum: Shows the sum of all Application Security Monitoring Serverless invocations over all hours in the current months for all organizations.
        :type asm_serverless_agg_sum: int, optional

        :param audit_logs_lines_indexed_agg_sum: Shows the sum of all audit logs lines indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type audit_logs_lines_indexed_agg_sum: int, optional

        :param audit_trail_enabled_hwm_sum: Shows the total number of organizations that had Audit Trail enabled over a specific number of months.
        :type audit_trail_enabled_hwm_sum: int, optional

        :param avg_profiled_fargate_tasks_sum: The average total count for Fargate Container Profiler over all hours in the current month for all organizations.
        :type avg_profiled_fargate_tasks_sum: int, optional

        :param aws_host_top99p_sum: Shows the 99th percentile of all AWS hosts over all hours in the current month for all organizations.
        :type aws_host_top99p_sum: int, optional

        :param aws_lambda_func_count: Shows the average of the number of functions that executed 1 or more times each hour in the current month for all organizations.
        :type aws_lambda_func_count: int, optional

        :param aws_lambda_invocations_sum: Shows the sum of all AWS Lambda invocations over all hours in the current month for all organizations.
        :type aws_lambda_invocations_sum: int, optional

        :param azure_app_service_top99p_sum: Shows the 99th percentile of all Azure app services over all hours in the current month for all organizations.
        :type azure_app_service_top99p_sum: int, optional

        :param azure_host_top99p_sum: Shows the 99th percentile of all Azure hosts over all hours in the current month for all organizations.
        :type azure_host_top99p_sum: int, optional

        :param billable_ingested_bytes_agg_sum: Shows the sum of all log bytes ingested over all hours in the current month for all organizations.
        :type billable_ingested_bytes_agg_sum: int, optional

        :param browser_rum_lite_session_count_agg_sum: Shows the sum of all browser lite sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type browser_rum_lite_session_count_agg_sum: int, optional

        :param browser_rum_replay_session_count_agg_sum: Shows the sum of all browser replay sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
        :type browser_rum_replay_session_count_agg_sum: int, optional

        :param browser_rum_units_agg_sum: Shows the sum of all browser RUM units over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type browser_rum_units_agg_sum: int, optional

        :param ci_pipeline_indexed_spans_agg_sum: Shows the sum of all CI pipeline indexed spans over all hours in the current month for all organizations.
        :type ci_pipeline_indexed_spans_agg_sum: int, optional

        :param ci_test_indexed_spans_agg_sum: Shows the sum of all CI test indexed spans over all hours in the current month for all organizations.
        :type ci_test_indexed_spans_agg_sum: int, optional

        :param ci_visibility_itr_committers_hwm_sum: Shows the high-water mark of all CI visibility intelligent test runner committers over all hours in the current month for all organizations.
        :type ci_visibility_itr_committers_hwm_sum: int, optional

        :param ci_visibility_pipeline_committers_hwm_sum: Shows the high-water mark of all CI visibility pipeline committers over all hours in the current month for all organizations.
        :type ci_visibility_pipeline_committers_hwm_sum: int, optional

        :param ci_visibility_test_committers_hwm_sum: Shows the high-water mark of all CI visibility test committers over all hours in the current month for all organizations.
        :type ci_visibility_test_committers_hwm_sum: int, optional

        :param cloud_cost_management_aws_host_count_avg_sum: Sum of the host count average for Cloud Cost Management for AWS.
        :type cloud_cost_management_aws_host_count_avg_sum: int, optional

        :param cloud_cost_management_azure_host_count_avg_sum: Sum of the host count average for Cloud Cost Management for Azure.
        :type cloud_cost_management_azure_host_count_avg_sum: int, optional

        :param cloud_cost_management_gcp_host_count_avg_sum: Sum of the host count average for Cloud Cost Management for GCP.
        :type cloud_cost_management_gcp_host_count_avg_sum: int, optional

        :param cloud_cost_management_host_count_avg_sum: Sum of the host count average for Cloud Cost Management for all cloud providers.
        :type cloud_cost_management_host_count_avg_sum: int, optional

        :param cloud_siem_events_agg_sum: Shows the sum of all Cloud Security Information and Event Management events over all hours in the current month for all organizations.
        :type cloud_siem_events_agg_sum: int, optional

        :param code_analysis_sa_committers_hwm_sum: Shows the high-water mark of all Static Analysis committers over all hours in the current month for all organizations.
        :type code_analysis_sa_committers_hwm_sum: int, optional

        :param code_analysis_sca_committers_hwm_sum: Shows the high-water mark of all static Software Composition Analysis committers over all hours in the current month for all organizations.
        :type code_analysis_sca_committers_hwm_sum: int, optional

        :param code_security_host_top99p_sum: Shows the 99th percentile of all Code Security hosts over all hours in the current month for all organizations.
        :type code_security_host_top99p_sum: int, optional

        :param container_avg_sum: Shows the average of all distinct containers over all hours in the current month for all organizations.
        :type container_avg_sum: int, optional

        :param container_excl_agent_avg_sum: Shows the average of the containers without the Datadog Agent over all hours in the current month for all organizations.
        :type container_excl_agent_avg_sum: int, optional

        :param container_hwm_sum: Shows the sum of the high-water marks of all distinct containers over all hours in the current month for all organizations.
        :type container_hwm_sum: int, optional

        :param csm_container_enterprise_compliance_count_agg_sum: Shows the sum of all Cloud Security Management Enterprise compliance containers over all hours in the current month for all organizations.
        :type csm_container_enterprise_compliance_count_agg_sum: int, optional

        :param csm_container_enterprise_cws_count_agg_sum: Shows the sum of all Cloud Security Management Enterprise Cloud Workload Security containers over all hours in the current month for all organizations.
        :type csm_container_enterprise_cws_count_agg_sum: int, optional

        :param csm_container_enterprise_total_count_agg_sum: Shows the sum of all Cloud Security Management Enterprise containers over all hours in the current month for all organizations.
        :type csm_container_enterprise_total_count_agg_sum: int, optional

        :param csm_host_enterprise_aas_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise Azure app services hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_aas_host_count_top99p_sum: int, optional

        :param csm_host_enterprise_aws_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise AWS hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_aws_host_count_top99p_sum: int, optional

        :param csm_host_enterprise_azure_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise Azure hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_azure_host_count_top99p_sum: int, optional

        :param csm_host_enterprise_compliance_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise compliance hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_compliance_host_count_top99p_sum: int, optional

        :param csm_host_enterprise_cws_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise Cloud Workload Security hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_cws_host_count_top99p_sum: int, optional

        :param csm_host_enterprise_gcp_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise GCP hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_gcp_host_count_top99p_sum: int, optional

        :param csm_host_enterprise_total_host_count_top99p_sum: Shows the 99th percentile of all Cloud Security Management Enterprise hosts over all hours in the current month for all organizations.
        :type csm_host_enterprise_total_host_count_top99p_sum: int, optional

        :param cspm_aas_host_top99p_sum: Shows the 99th percentile of all Cloud Security Management Pro Azure app services hosts over all hours in the current month for all organizations.
        :type cspm_aas_host_top99p_sum: int, optional

        :param cspm_aws_host_top99p_sum: Shows the 99th percentile of all Cloud Security Management Pro AWS hosts over all hours in the current month for all organizations.
        :type cspm_aws_host_top99p_sum: int, optional

        :param cspm_azure_host_top99p_sum: Shows the 99th percentile of all Cloud Security Management Pro Azure hosts over all hours in the current month for all organizations.
        :type cspm_azure_host_top99p_sum: int, optional

        :param cspm_container_avg_sum: Shows the average number of Cloud Security Management Pro containers over all hours in the current month for all organizations.
        :type cspm_container_avg_sum: int, optional

        :param cspm_container_hwm_sum: Shows the sum of the high-water marks of Cloud Security Management Pro containers over all hours in the current month for all organizations.
        :type cspm_container_hwm_sum: int, optional

        :param cspm_gcp_host_top99p_sum: Shows the 99th percentile of all Cloud Security Management Pro GCP hosts over all hours in the current month for all organizations.
        :type cspm_gcp_host_top99p_sum: int, optional

        :param cspm_host_top99p_sum: Shows the 99th percentile of all Cloud Security Management Pro hosts over all hours in the current month for all organizations.
        :type cspm_host_top99p_sum: int, optional

        :param custom_historical_ts_sum: Shows the average number of distinct historical custom metrics over all hours in the current month for all organizations.
        :type custom_historical_ts_sum: int, optional

        :param custom_live_ts_sum: Shows the average number of distinct live custom metrics over all hours in the current month for all organizations.
        :type custom_live_ts_sum: int, optional

        :param custom_ts_sum: Shows the average number of distinct custom metrics over all hours in the current month for all organizations.
        :type custom_ts_sum: int, optional

        :param cws_container_avg_sum: Shows the average of all distinct Cloud Workload Security containers over all hours in the current month for all organizations.
        :type cws_container_avg_sum: int, optional

        :param cws_fargate_task_avg_sum: Shows the average of all distinct Cloud Workload Security Fargate tasks over all hours in the current month for all organizations.
        :type cws_fargate_task_avg_sum: int, optional

        :param cws_host_top99p_sum: Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current month for all organizations.
        :type cws_host_top99p_sum: int, optional

        :param data_jobs_monitoring_host_hr_agg_sum: Shows the sum of Data Jobs Monitoring hosts over all hours in the current months for all organizations
        :type data_jobs_monitoring_host_hr_agg_sum: int, optional

        :param dbm_host_top99p_sum: Shows the 99th percentile of all Database Monitoring hosts over all hours in the current month for all organizations.
        :type dbm_host_top99p_sum: int, optional

        :param dbm_queries_avg_sum: Shows the average of all distinct Database Monitoring Normalized Queries over all hours in the current month for all organizations.
        :type dbm_queries_avg_sum: int, optional

        :param end_date: Shows the last date of usage in the current month for all organizations.
        :type end_date: datetime, optional

        :param eph_infra_host_agent_agg_sum: Shows the sum of all ephemeral infrastructure hosts with the Datadog Agent over all hours in the current month for all organizations.
        :type eph_infra_host_agent_agg_sum: int, optional

        :param eph_infra_host_alibaba_agg_sum: Shows the sum of all ephemeral infrastructure hosts on Alibaba over all hours in the current month for all organizations.
        :type eph_infra_host_alibaba_agg_sum: int, optional

        :param eph_infra_host_aws_agg_sum: Shows the sum of all ephemeral infrastructure hosts on AWS over all hours in the current month for all organizations.
        :type eph_infra_host_aws_agg_sum: int, optional

        :param eph_infra_host_azure_agg_sum: Shows the sum of all ephemeral infrastructure hosts on Azure over all hours in the current month for all organizations.
        :type eph_infra_host_azure_agg_sum: int, optional

        :param eph_infra_host_ent_agg_sum: Shows the sum of all ephemeral infrastructure hosts for Enterprise over all hours in the current month for all organizations.
        :type eph_infra_host_ent_agg_sum: int, optional

        :param eph_infra_host_gcp_agg_sum: Shows the sum of all ephemeral infrastructure hosts on GCP over all hours in the current month for all organizations.
        :type eph_infra_host_gcp_agg_sum: int, optional

        :param eph_infra_host_heroku_agg_sum: Shows the sum of all ephemeral infrastructure hosts on Heroku over all hours in the current month for all organizations.
        :type eph_infra_host_heroku_agg_sum: int, optional

        :param eph_infra_host_only_aas_agg_sum: Shows the sum of all ephemeral infrastructure hosts with only Azure App Services over all hours in the current month for all organizations.
        :type eph_infra_host_only_aas_agg_sum: int, optional

        :param eph_infra_host_only_vsphere_agg_sum: Shows the sum of all ephemeral infrastructure hosts with only vSphere over all hours in the current month for all organizations.
        :type eph_infra_host_only_vsphere_agg_sum: int, optional

        :param eph_infra_host_opentelemetry_agg_sum: Shows the sum of all ephemeral hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
        :type eph_infra_host_opentelemetry_agg_sum: int, optional

        :param eph_infra_host_opentelemetry_apm_agg_sum: Shows the sum of all ephemeral APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
        :type eph_infra_host_opentelemetry_apm_agg_sum: int, optional

        :param eph_infra_host_pro_agg_sum: Shows the sum of all ephemeral infrastructure hosts for Pro over all hours in the current month for all organizations.
        :type eph_infra_host_pro_agg_sum: int, optional

        :param eph_infra_host_proplus_agg_sum: Shows the sum of all ephemeral infrastructure hosts for Pro Plus over all hours in the current month for all organizations.
        :type eph_infra_host_proplus_agg_sum: int, optional

        :param error_tracking_apm_error_events_agg_sum: Shows the sum of all Error Tracking APM error events over all hours in the current month for all organizations.
        :type error_tracking_apm_error_events_agg_sum: int, optional

        :param error_tracking_error_events_agg_sum: Shows the sum of all Error Tracking error events over all hours in the current month for all organizations.
        :type error_tracking_error_events_agg_sum: int, optional

        :param error_tracking_events_agg_sum: Shows the sum of all Error Tracking events over all hours in the current months for all organizations.
        :type error_tracking_events_agg_sum: int, optional

        :param error_tracking_rum_error_events_agg_sum: Shows the sum of all Error Tracking RUM error events over all hours in the current month for all organizations.
        :type error_tracking_rum_error_events_agg_sum: int, optional

        :param fargate_container_profiler_profiling_fargate_avg_sum: The average number of Profiling Fargate tasks over all hours in the current month for all organizations.
        :type fargate_container_profiler_profiling_fargate_avg_sum: int, optional

        :param fargate_container_profiler_profiling_fargate_eks_avg_sum: The average number of Profiling Fargate Elastic Kubernetes Service tasks over all hours in the current month for all organizations.
        :type fargate_container_profiler_profiling_fargate_eks_avg_sum: int, optional

        :param fargate_tasks_count_avg_sum: Shows the average of all Fargate tasks over all hours in the current month for all organizations.
        :type fargate_tasks_count_avg_sum: int, optional

        :param fargate_tasks_count_hwm_sum: Shows the sum of the high-water marks of all Fargate tasks over all hours in the current month for all organizations.
        :type fargate_tasks_count_hwm_sum: int, optional

        :param flex_logs_compute_large_avg_sum: Shows the average number of Flex Logs Compute Large Instances over all hours in the current months for all organizations.
        :type flex_logs_compute_large_avg_sum: int, optional

        :param flex_logs_compute_medium_avg_sum: Shows the average number of Flex Logs Compute Medium Instances over all hours in the current months for all organizations.
        :type flex_logs_compute_medium_avg_sum: int, optional

        :param flex_logs_compute_small_avg_sum: Shows the average number of Flex Logs Compute Small Instances over all hours in the current months for all organizations.
        :type flex_logs_compute_small_avg_sum: int, optional

        :param flex_logs_compute_xsmall_avg_sum: Shows the average number of Flex Logs Compute Extra Small Instances over all hours in the current months for all organizations.
        :type flex_logs_compute_xsmall_avg_sum: int, optional

        :param flex_logs_starter_avg_sum: Shows the average number of Flex Logs Starter Instances over all hours in the current months for all organizations.
        :type flex_logs_starter_avg_sum: int, optional

        :param flex_logs_starter_storage_index_avg_sum: Shows the average number of Flex Logs Starter Storage Index Instances over all hours in the current months for all organizations.
        :type flex_logs_starter_storage_index_avg_sum: int, optional

        :param flex_logs_starter_storage_retention_adjustment_avg_sum: Shows the average number of Flex Logs Starter Storage Retention Adjustment Instances over all hours in the current months for all organizations.
        :type flex_logs_starter_storage_retention_adjustment_avg_sum: int, optional

        :param flex_stored_logs_avg_sum: Shows the average of all Flex Stored Logs over all hours in the current months for all organizations.
        :type flex_stored_logs_avg_sum: int, optional

        :param forwarding_events_bytes_agg_sum: Shows the sum of all logs forwarding bytes over all hours in the current month for all organizations (data available as of April 1, 2023)
        :type forwarding_events_bytes_agg_sum: int, optional

        :param gcp_host_top99p_sum: Shows the 99th percentile of all GCP hosts over all hours in the current month for all organizations.
        :type gcp_host_top99p_sum: int, optional

        :param heroku_host_top99p_sum: Shows the 99th percentile of all Heroku dynos over all hours in the current month for all organizations.
        :type heroku_host_top99p_sum: int, optional

        :param incident_management_monthly_active_users_hwm_sum: Shows sum of the high-water marks of incident management monthly active users in the current month for all organizations.
        :type incident_management_monthly_active_users_hwm_sum: int, optional

        :param indexed_events_count_agg_sum: Shows the sum of all log events indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type indexed_events_count_agg_sum: int, optional

        :param infra_host_top99p_sum: Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current month for all organizations.
        :type infra_host_top99p_sum: int, optional

        :param ingested_events_bytes_agg_sum: Shows the sum of all log bytes ingested over all hours in the current month for all organizations.
        :type ingested_events_bytes_agg_sum: int, optional

        :param iot_device_agg_sum: Shows the sum of all IoT devices over all hours in the current month for all organizations.
        :type iot_device_agg_sum: int, optional

        :param iot_device_top99p_sum: Shows the 99th percentile of all IoT devices over all hours in the current month of all organizations.
        :type iot_device_top99p_sum: int, optional

        :param last_updated: Shows the most recent hour in the current month for all organizations for which all usages were calculated.
        :type last_updated: datetime, optional

        :param live_indexed_events_agg_sum: Shows the sum of all live logs indexed over all hours in the current month for all organization (To be deprecated on October 1st, 2024). **Deprecated**.
        :type live_indexed_events_agg_sum: int, optional

        :param live_ingested_bytes_agg_sum: Shows the sum of all live logs bytes ingested over all hours in the current month for all organizations (data available as of December 1, 2020).
        :type live_ingested_bytes_agg_sum: int, optional

        :param llm_observability_agg_sum: Sum of all LLM observability sessions for all hours in the current month for all organizations.
        :type llm_observability_agg_sum: int, optional

        :param llm_observability_min_spend_agg_sum: Minimum spend for LLM observability sessions for all hours in the current month for all organizations.
        :type llm_observability_min_spend_agg_sum: int, optional

        :param logs_by_retention: Object containing logs usage data broken down by retention period.
        :type logs_by_retention: LogsByRetention, optional

        :param mobile_rum_lite_session_count_agg_sum: Shows the sum of all mobile lite sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_lite_session_count_agg_sum: int, optional

        :param mobile_rum_session_count_agg_sum: Shows the sum of all mobile RUM sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_agg_sum: int, optional

        :param mobile_rum_session_count_android_agg_sum: Shows the sum of all mobile RUM sessions on Android over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_android_agg_sum: int, optional

        :param mobile_rum_session_count_flutter_agg_sum: Shows the sum of all mobile RUM sessions on Flutter over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_flutter_agg_sum: int, optional

        :param mobile_rum_session_count_ios_agg_sum: Shows the sum of all mobile RUM sessions on iOS over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_ios_agg_sum: int, optional

        :param mobile_rum_session_count_reactnative_agg_sum: Shows the sum of all mobile RUM sessions on React Native over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_reactnative_agg_sum: int, optional

        :param mobile_rum_session_count_roku_agg_sum: Shows the sum of all mobile RUM sessions on Roku over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_session_count_roku_agg_sum: int, optional

        :param mobile_rum_units_agg_sum: Shows the sum of all mobile RUM units over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type mobile_rum_units_agg_sum: int, optional

        :param ndm_netflow_events_agg_sum: Shows the sum of all Network Device Monitoring NetFlow events over all hours in the current month for all organizations.
        :type ndm_netflow_events_agg_sum: int, optional

        :param netflow_indexed_events_count_agg_sum: Shows the sum of all Network flows indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type netflow_indexed_events_count_agg_sum: int, optional

        :param network_device_wireless_top99p_sum: Shows the 99th percentile of all Network Device Monitoring wireless devices over all hours in the current month for all organizations.
        :type network_device_wireless_top99p_sum: int, optional

        :param npm_host_top99p_sum: Shows the 99th percentile of all distinct Cloud Network Monitoring hosts (formerly known as Network hosts) over all hours in the current month for all organizations.
        :type npm_host_top99p_sum: int, optional

        :param observability_pipelines_bytes_processed_agg_sum: Sum of all observability pipelines bytes processed over all hours in the current month for all organizations.
        :type observability_pipelines_bytes_processed_agg_sum: int, optional

        :param oci_host_agg_sum: Shows the sum of Oracle Cloud Infrastructure hosts over all hours in the current months for all organizations
        :type oci_host_agg_sum: int, optional

        :param oci_host_top99p_sum: Shows the 99th percentile of Oracle Cloud Infrastructure hosts over all hours in the current months for all organizations
        :type oci_host_top99p_sum: int, optional

        :param online_archive_events_count_agg_sum: Sum of all online archived events over all hours in the current month for all organizations.
        :type online_archive_events_count_agg_sum: int, optional

        :param opentelemetry_apm_host_top99p_sum: Shows the 99th percentile of APM hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
        :type opentelemetry_apm_host_top99p_sum: int, optional

        :param opentelemetry_host_top99p_sum: Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current month for all organizations.
        :type opentelemetry_host_top99p_sum: int, optional

        :param product_analytics_agg_sum: Sum of all product analytics sessions for all hours in the current month for all organizations.
        :type product_analytics_agg_sum: int, optional

        :param profiling_aas_count_top99p_sum: Shows the 99th percentile of all profiled Azure app services over all hours in the current month for all organizations.
        :type profiling_aas_count_top99p_sum: int, optional

        :param profiling_container_agent_count_avg: Shows the average number of profiled containers over all hours in the current month for all organizations.
        :type profiling_container_agent_count_avg: int, optional

        :param profiling_host_count_top99p_sum: Shows the 99th percentile of all profiled hosts over all hours in the current month for all organizations.
        :type profiling_host_count_top99p_sum: int, optional

        :param published_app_hwm_sum: Shows the high-water mark of all published applications over all hours in the current month for all organizations.
        :type published_app_hwm_sum: int, optional

        :param rehydrated_indexed_events_agg_sum: Shows the sum of all rehydrated logs indexed over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type rehydrated_indexed_events_agg_sum: int, optional

        :param rehydrated_ingested_bytes_agg_sum: Shows the sum of all rehydrated logs bytes ingested over all hours in the current month for all organizations (data available as of December 1, 2020).
        :type rehydrated_ingested_bytes_agg_sum: int, optional

        :param rum_browser_and_mobile_session_count: Shows the sum of all mobile sessions and all browser lite and legacy sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024).
        :type rum_browser_and_mobile_session_count: int, optional

        :param rum_browser_legacy_session_count_agg_sum: Shows the sum of all browser RUM legacy sessions over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_browser_legacy_session_count_agg_sum: int, optional

        :param rum_browser_lite_session_count_agg_sum: Shows the sum of all browser RUM lite sessions over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_browser_lite_session_count_agg_sum: int, optional

        :param rum_browser_replay_session_count_agg_sum: Shows the sum of all browser RUM Session Replay counts over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_browser_replay_session_count_agg_sum: int, optional

        :param rum_indexed_sessions_agg_sum: Sum of all RUM indexed sessions for all hours in the current month for all organizations.
        :type rum_indexed_sessions_agg_sum: int, optional

        :param rum_ingested_sessions_agg_sum: Sum of all RUM ingested sessions for all hours in the current month for all organizations.
        :type rum_ingested_sessions_agg_sum: int, optional

        :param rum_lite_session_count_agg_sum: Shows the sum of all RUM lite sessions (browser and mobile) over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_lite_session_count_agg_sum: int, optional

        :param rum_mobile_legacy_session_count_android_agg_sum: Shows the sum of all mobile RUM legacy sessions on Android over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_android_agg_sum: int, optional

        :param rum_mobile_legacy_session_count_flutter_agg_sum: Shows the sum of all mobile RUM legacy sessions on Flutter over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_flutter_agg_sum: int, optional

        :param rum_mobile_legacy_session_count_ios_agg_sum: Shows the sum of all mobile RUM legacy sessions on iOS over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_ios_agg_sum: int, optional

        :param rum_mobile_legacy_session_count_reactnative_agg_sum: Shows the sum of all mobile RUM legacy sessions on React Native over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_reactnative_agg_sum: int, optional

        :param rum_mobile_legacy_session_count_roku_agg_sum: Shows the sum of all mobile RUM legacy sessions on Roku over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_legacy_session_count_roku_agg_sum: int, optional

        :param rum_mobile_lite_session_count_android_agg_sum: Shows the sum of all mobile RUM lite sessions on Android over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_android_agg_sum: int, optional

        :param rum_mobile_lite_session_count_flutter_agg_sum: Shows the sum of all mobile RUM lite sessions on Flutter over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_flutter_agg_sum: int, optional

        :param rum_mobile_lite_session_count_ios_agg_sum: Shows the sum of all mobile RUM lite sessions on iOS over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_ios_agg_sum: int, optional

        :param rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum: Shows the sum of all mobile RUM lite sessions on Kotlin Multiplatform over all hours within the current month for all organizations.
        :type rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum: int, optional

        :param rum_mobile_lite_session_count_reactnative_agg_sum: Shows the sum of all mobile RUM lite sessions on React Native over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_reactnative_agg_sum: int, optional

        :param rum_mobile_lite_session_count_roku_agg_sum: Shows the sum of all mobile RUM lite sessions on Roku over all hours within the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_mobile_lite_session_count_roku_agg_sum: int, optional

        :param rum_mobile_lite_session_count_unity_agg_sum: Shows the sum of all mobile RUM lite sessions on Unity over all hours within the current month for all organizations.
        :type rum_mobile_lite_session_count_unity_agg_sum: int, optional

        :param rum_mobile_replay_session_count_android_agg_sum: Shows the sum of all mobile RUM replay sessions on Android over all hours within the current month for all organizations.
        :type rum_mobile_replay_session_count_android_agg_sum: int, optional

        :param rum_mobile_replay_session_count_ios_agg_sum: Shows the sum of all mobile RUM replay sessions on iOS over all hours within the current month for all organizations.
        :type rum_mobile_replay_session_count_ios_agg_sum: int, optional

        :param rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum: Shows the sum of all mobile RUM replay sessions on Kotlin Multiplatform over all hours within the current month for all organizations.
        :type rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum: int, optional

        :param rum_mobile_replay_session_count_reactnative_agg_sum: Shows the sum of all mobile RUM replay sessions on React Native over all hours within the current month for all organizations.
        :type rum_mobile_replay_session_count_reactnative_agg_sum: int, optional

        :param rum_replay_session_count_agg_sum: Shows the sum of all RUM Session Replay counts over all hours in the current month for all organizations (To be introduced on October 1st, 2024).
        :type rum_replay_session_count_agg_sum: int, optional

        :param rum_session_count_agg_sum: Shows the sum of all browser RUM lite sessions over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type rum_session_count_agg_sum: int, optional

        :param rum_session_replay_add_on_agg_sum: Sum of all RUM session replay add-on sessions for all hours in the current month for all organizations.
        :type rum_session_replay_add_on_agg_sum: int, optional

        :param rum_total_session_count_agg_sum: Shows the sum of RUM sessions (browser and mobile) over all hours in the current month for all organizations.
        :type rum_total_session_count_agg_sum: int, optional

        :param rum_units_agg_sum: Shows the sum of all browser and mobile RUM units over all hours in the current month for all organizations (To be deprecated on October 1st, 2024). **Deprecated**.
        :type rum_units_agg_sum: int, optional

        :param sca_fargate_count_avg_sum: Shows the average of all Software Composition Analysis Fargate tasks over all hours in the current months for all organizations.
        :type sca_fargate_count_avg_sum: int, optional

        :param sca_fargate_count_hwm_sum: Shows the sum of the high-water marks of all Software Composition Analysis Fargate tasks over all hours in the current months for all organizations.
        :type sca_fargate_count_hwm_sum: int, optional

        :param sds_apm_scanned_bytes_sum: Sum of all APM bytes scanned with sensitive data scanner in the current month for all organizations.
        :type sds_apm_scanned_bytes_sum: int, optional

        :param sds_events_scanned_bytes_sum: Sum of all event stream events bytes scanned with sensitive data scanner in the current month for all organizations.
        :type sds_events_scanned_bytes_sum: int, optional

        :param sds_logs_scanned_bytes_sum: Shows the sum of all bytes scanned of logs usage by the Sensitive Data Scanner over all hours in the current month for all organizations.
        :type sds_logs_scanned_bytes_sum: int, optional

        :param sds_rum_scanned_bytes_sum: Sum of all RUM bytes scanned with sensitive data scanner in the current month for all organizations.
        :type sds_rum_scanned_bytes_sum: int, optional

        :param sds_total_scanned_bytes_sum: Shows the sum of all bytes scanned across all usage types by the Sensitive Data Scanner over all hours in the current month for all organizations.
        :type sds_total_scanned_bytes_sum: int, optional

        :param serverless_apps_azure_count_avg_sum: Sum of the average number of Serverless Apps for Azure in the current month for all organizations.
        :type serverless_apps_azure_count_avg_sum: int, optional

        :param serverless_apps_google_count_avg_sum: Sum of the average number of Serverless Apps for Google Cloud in the current month for all organizations.
        :type serverless_apps_google_count_avg_sum: int, optional

        :param serverless_apps_total_count_avg_sum: Sum of the average number of Serverless Apps for Azure and Google Cloud in the current month for all organizations.
        :type serverless_apps_total_count_avg_sum: int, optional

        :param siem_analyzed_logs_add_on_count_agg_sum: Shows the sum of all log events analyzed by Cloud SIEM over all hours in the current month for all organizations.
        :type siem_analyzed_logs_add_on_count_agg_sum: int, optional

        :param start_date: Shows the first date of usage in the current month for all organizations.
        :type start_date: datetime, optional

        :param synthetics_browser_check_calls_count_agg_sum: Shows the sum of all Synthetic browser tests over all hours in the current month for all organizations.
        :type synthetics_browser_check_calls_count_agg_sum: int, optional

        :param synthetics_check_calls_count_agg_sum: Shows the sum of all Synthetic API tests over all hours in the current month for all organizations.
        :type synthetics_check_calls_count_agg_sum: int, optional

        :param synthetics_mobile_test_runs_agg_sum: Shows the sum of Synthetic mobile application tests over all hours in the current month for all organizations.
        :type synthetics_mobile_test_runs_agg_sum: int, optional

        :param synthetics_parallel_testing_max_slots_hwm_sum: Shows the sum of the high-water marks of used synthetics parallel testing slots over all hours in the current month for all organizations.
        :type synthetics_parallel_testing_max_slots_hwm_sum: int, optional

        :param trace_search_indexed_events_count_agg_sum: Shows the sum of all Indexed Spans indexed over all hours in the current month for all organizations.
        :type trace_search_indexed_events_count_agg_sum: int, optional

        :param twol_ingested_events_bytes_agg_sum: Shows the sum of all ingested APM span bytes over all hours in the current month for all organizations.
        :type twol_ingested_events_bytes_agg_sum: int, optional

        :param universal_service_monitoring_host_top99p_sum: Shows the 99th percentile of all Universal Service Monitoring hosts over all hours in the current month for all organizations.
        :type universal_service_monitoring_host_top99p_sum: int, optional

        :param usage: An array of objects regarding hourly usage.
        :type usage: [UsageSummaryDate], optional

        :param vsphere_host_top99p_sum: Shows the 99th percentile of all vSphere hosts over all hours in the current month for all organizations.
        :type vsphere_host_top99p_sum: int, optional

        :param vuln_management_host_count_top99p_sum: Shows the 99th percentile of all Application Vulnerability Management hosts over all hours in the current month for all organizations.
        :type vuln_management_host_count_top99p_sum: int, optional

        :param workflow_executions_usage_agg_sum: Sum of all workflows executed over all hours in the current month for all organizations.
        :type workflow_executions_usage_agg_sum: int, optional
        """
        if agent_host_top99p_sum is not unset:
            kwargs["agent_host_top99p_sum"] = agent_host_top99p_sum
        if apm_azure_app_service_host_top99p_sum is not unset:
            kwargs["apm_azure_app_service_host_top99p_sum"] = apm_azure_app_service_host_top99p_sum
        if apm_devsecops_host_top99p_sum is not unset:
            kwargs["apm_devsecops_host_top99p_sum"] = apm_devsecops_host_top99p_sum
        if apm_fargate_count_avg_sum is not unset:
            kwargs["apm_fargate_count_avg_sum"] = apm_fargate_count_avg_sum
        if apm_host_top99p_sum is not unset:
            kwargs["apm_host_top99p_sum"] = apm_host_top99p_sum
        if appsec_fargate_count_avg_sum is not unset:
            kwargs["appsec_fargate_count_avg_sum"] = appsec_fargate_count_avg_sum
        if asm_serverless_agg_sum is not unset:
            kwargs["asm_serverless_agg_sum"] = asm_serverless_agg_sum
        if audit_logs_lines_indexed_agg_sum is not unset:
            kwargs["audit_logs_lines_indexed_agg_sum"] = audit_logs_lines_indexed_agg_sum
        if audit_trail_enabled_hwm_sum is not unset:
            kwargs["audit_trail_enabled_hwm_sum"] = audit_trail_enabled_hwm_sum
        if avg_profiled_fargate_tasks_sum is not unset:
            kwargs["avg_profiled_fargate_tasks_sum"] = avg_profiled_fargate_tasks_sum
        if aws_host_top99p_sum is not unset:
            kwargs["aws_host_top99p_sum"] = aws_host_top99p_sum
        if aws_lambda_func_count is not unset:
            kwargs["aws_lambda_func_count"] = aws_lambda_func_count
        if aws_lambda_invocations_sum is not unset:
            kwargs["aws_lambda_invocations_sum"] = aws_lambda_invocations_sum
        if azure_app_service_top99p_sum is not unset:
            kwargs["azure_app_service_top99p_sum"] = azure_app_service_top99p_sum
        if azure_host_top99p_sum is not unset:
            kwargs["azure_host_top99p_sum"] = azure_host_top99p_sum
        if billable_ingested_bytes_agg_sum is not unset:
            kwargs["billable_ingested_bytes_agg_sum"] = billable_ingested_bytes_agg_sum
        if browser_rum_lite_session_count_agg_sum is not unset:
            kwargs["browser_rum_lite_session_count_agg_sum"] = browser_rum_lite_session_count_agg_sum
        if browser_rum_replay_session_count_agg_sum is not unset:
            kwargs["browser_rum_replay_session_count_agg_sum"] = browser_rum_replay_session_count_agg_sum
        if browser_rum_units_agg_sum is not unset:
            kwargs["browser_rum_units_agg_sum"] = browser_rum_units_agg_sum
        if ci_pipeline_indexed_spans_agg_sum is not unset:
            kwargs["ci_pipeline_indexed_spans_agg_sum"] = ci_pipeline_indexed_spans_agg_sum
        if ci_test_indexed_spans_agg_sum is not unset:
            kwargs["ci_test_indexed_spans_agg_sum"] = ci_test_indexed_spans_agg_sum
        if ci_visibility_itr_committers_hwm_sum is not unset:
            kwargs["ci_visibility_itr_committers_hwm_sum"] = ci_visibility_itr_committers_hwm_sum
        if ci_visibility_pipeline_committers_hwm_sum is not unset:
            kwargs["ci_visibility_pipeline_committers_hwm_sum"] = ci_visibility_pipeline_committers_hwm_sum
        if ci_visibility_test_committers_hwm_sum is not unset:
            kwargs["ci_visibility_test_committers_hwm_sum"] = ci_visibility_test_committers_hwm_sum
        if cloud_cost_management_aws_host_count_avg_sum is not unset:
            kwargs["cloud_cost_management_aws_host_count_avg_sum"] = cloud_cost_management_aws_host_count_avg_sum
        if cloud_cost_management_azure_host_count_avg_sum is not unset:
            kwargs["cloud_cost_management_azure_host_count_avg_sum"] = cloud_cost_management_azure_host_count_avg_sum
        if cloud_cost_management_gcp_host_count_avg_sum is not unset:
            kwargs["cloud_cost_management_gcp_host_count_avg_sum"] = cloud_cost_management_gcp_host_count_avg_sum
        if cloud_cost_management_host_count_avg_sum is not unset:
            kwargs["cloud_cost_management_host_count_avg_sum"] = cloud_cost_management_host_count_avg_sum
        if cloud_siem_events_agg_sum is not unset:
            kwargs["cloud_siem_events_agg_sum"] = cloud_siem_events_agg_sum
        if code_analysis_sa_committers_hwm_sum is not unset:
            kwargs["code_analysis_sa_committers_hwm_sum"] = code_analysis_sa_committers_hwm_sum
        if code_analysis_sca_committers_hwm_sum is not unset:
            kwargs["code_analysis_sca_committers_hwm_sum"] = code_analysis_sca_committers_hwm_sum
        if code_security_host_top99p_sum is not unset:
            kwargs["code_security_host_top99p_sum"] = code_security_host_top99p_sum
        if container_avg_sum is not unset:
            kwargs["container_avg_sum"] = container_avg_sum
        if container_excl_agent_avg_sum is not unset:
            kwargs["container_excl_agent_avg_sum"] = container_excl_agent_avg_sum
        if container_hwm_sum is not unset:
            kwargs["container_hwm_sum"] = container_hwm_sum
        if csm_container_enterprise_compliance_count_agg_sum is not unset:
            kwargs[
                "csm_container_enterprise_compliance_count_agg_sum"
            ] = csm_container_enterprise_compliance_count_agg_sum
        if csm_container_enterprise_cws_count_agg_sum is not unset:
            kwargs["csm_container_enterprise_cws_count_agg_sum"] = csm_container_enterprise_cws_count_agg_sum
        if csm_container_enterprise_total_count_agg_sum is not unset:
            kwargs["csm_container_enterprise_total_count_agg_sum"] = csm_container_enterprise_total_count_agg_sum
        if csm_host_enterprise_aas_host_count_top99p_sum is not unset:
            kwargs["csm_host_enterprise_aas_host_count_top99p_sum"] = csm_host_enterprise_aas_host_count_top99p_sum
        if csm_host_enterprise_aws_host_count_top99p_sum is not unset:
            kwargs["csm_host_enterprise_aws_host_count_top99p_sum"] = csm_host_enterprise_aws_host_count_top99p_sum
        if csm_host_enterprise_azure_host_count_top99p_sum is not unset:
            kwargs["csm_host_enterprise_azure_host_count_top99p_sum"] = csm_host_enterprise_azure_host_count_top99p_sum
        if csm_host_enterprise_compliance_host_count_top99p_sum is not unset:
            kwargs[
                "csm_host_enterprise_compliance_host_count_top99p_sum"
            ] = csm_host_enterprise_compliance_host_count_top99p_sum
        if csm_host_enterprise_cws_host_count_top99p_sum is not unset:
            kwargs["csm_host_enterprise_cws_host_count_top99p_sum"] = csm_host_enterprise_cws_host_count_top99p_sum
        if csm_host_enterprise_gcp_host_count_top99p_sum is not unset:
            kwargs["csm_host_enterprise_gcp_host_count_top99p_sum"] = csm_host_enterprise_gcp_host_count_top99p_sum
        if csm_host_enterprise_total_host_count_top99p_sum is not unset:
            kwargs["csm_host_enterprise_total_host_count_top99p_sum"] = csm_host_enterprise_total_host_count_top99p_sum
        if cspm_aas_host_top99p_sum is not unset:
            kwargs["cspm_aas_host_top99p_sum"] = cspm_aas_host_top99p_sum
        if cspm_aws_host_top99p_sum is not unset:
            kwargs["cspm_aws_host_top99p_sum"] = cspm_aws_host_top99p_sum
        if cspm_azure_host_top99p_sum is not unset:
            kwargs["cspm_azure_host_top99p_sum"] = cspm_azure_host_top99p_sum
        if cspm_container_avg_sum is not unset:
            kwargs["cspm_container_avg_sum"] = cspm_container_avg_sum
        if cspm_container_hwm_sum is not unset:
            kwargs["cspm_container_hwm_sum"] = cspm_container_hwm_sum
        if cspm_gcp_host_top99p_sum is not unset:
            kwargs["cspm_gcp_host_top99p_sum"] = cspm_gcp_host_top99p_sum
        if cspm_host_top99p_sum is not unset:
            kwargs["cspm_host_top99p_sum"] = cspm_host_top99p_sum
        if custom_historical_ts_sum is not unset:
            kwargs["custom_historical_ts_sum"] = custom_historical_ts_sum
        if custom_live_ts_sum is not unset:
            kwargs["custom_live_ts_sum"] = custom_live_ts_sum
        if custom_ts_sum is not unset:
            kwargs["custom_ts_sum"] = custom_ts_sum
        if cws_container_avg_sum is not unset:
            kwargs["cws_container_avg_sum"] = cws_container_avg_sum
        if cws_fargate_task_avg_sum is not unset:
            kwargs["cws_fargate_task_avg_sum"] = cws_fargate_task_avg_sum
        if cws_host_top99p_sum is not unset:
            kwargs["cws_host_top99p_sum"] = cws_host_top99p_sum
        if data_jobs_monitoring_host_hr_agg_sum is not unset:
            kwargs["data_jobs_monitoring_host_hr_agg_sum"] = data_jobs_monitoring_host_hr_agg_sum
        if dbm_host_top99p_sum is not unset:
            kwargs["dbm_host_top99p_sum"] = dbm_host_top99p_sum
        if dbm_queries_avg_sum is not unset:
            kwargs["dbm_queries_avg_sum"] = dbm_queries_avg_sum
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if eph_infra_host_agent_agg_sum is not unset:
            kwargs["eph_infra_host_agent_agg_sum"] = eph_infra_host_agent_agg_sum
        if eph_infra_host_alibaba_agg_sum is not unset:
            kwargs["eph_infra_host_alibaba_agg_sum"] = eph_infra_host_alibaba_agg_sum
        if eph_infra_host_aws_agg_sum is not unset:
            kwargs["eph_infra_host_aws_agg_sum"] = eph_infra_host_aws_agg_sum
        if eph_infra_host_azure_agg_sum is not unset:
            kwargs["eph_infra_host_azure_agg_sum"] = eph_infra_host_azure_agg_sum
        if eph_infra_host_ent_agg_sum is not unset:
            kwargs["eph_infra_host_ent_agg_sum"] = eph_infra_host_ent_agg_sum
        if eph_infra_host_gcp_agg_sum is not unset:
            kwargs["eph_infra_host_gcp_agg_sum"] = eph_infra_host_gcp_agg_sum
        if eph_infra_host_heroku_agg_sum is not unset:
            kwargs["eph_infra_host_heroku_agg_sum"] = eph_infra_host_heroku_agg_sum
        if eph_infra_host_only_aas_agg_sum is not unset:
            kwargs["eph_infra_host_only_aas_agg_sum"] = eph_infra_host_only_aas_agg_sum
        if eph_infra_host_only_vsphere_agg_sum is not unset:
            kwargs["eph_infra_host_only_vsphere_agg_sum"] = eph_infra_host_only_vsphere_agg_sum
        if eph_infra_host_opentelemetry_agg_sum is not unset:
            kwargs["eph_infra_host_opentelemetry_agg_sum"] = eph_infra_host_opentelemetry_agg_sum
        if eph_infra_host_opentelemetry_apm_agg_sum is not unset:
            kwargs["eph_infra_host_opentelemetry_apm_agg_sum"] = eph_infra_host_opentelemetry_apm_agg_sum
        if eph_infra_host_pro_agg_sum is not unset:
            kwargs["eph_infra_host_pro_agg_sum"] = eph_infra_host_pro_agg_sum
        if eph_infra_host_proplus_agg_sum is not unset:
            kwargs["eph_infra_host_proplus_agg_sum"] = eph_infra_host_proplus_agg_sum
        if error_tracking_apm_error_events_agg_sum is not unset:
            kwargs["error_tracking_apm_error_events_agg_sum"] = error_tracking_apm_error_events_agg_sum
        if error_tracking_error_events_agg_sum is not unset:
            kwargs["error_tracking_error_events_agg_sum"] = error_tracking_error_events_agg_sum
        if error_tracking_events_agg_sum is not unset:
            kwargs["error_tracking_events_agg_sum"] = error_tracking_events_agg_sum
        if error_tracking_rum_error_events_agg_sum is not unset:
            kwargs["error_tracking_rum_error_events_agg_sum"] = error_tracking_rum_error_events_agg_sum
        if fargate_container_profiler_profiling_fargate_avg_sum is not unset:
            kwargs[
                "fargate_container_profiler_profiling_fargate_avg_sum"
            ] = fargate_container_profiler_profiling_fargate_avg_sum
        if fargate_container_profiler_profiling_fargate_eks_avg_sum is not unset:
            kwargs[
                "fargate_container_profiler_profiling_fargate_eks_avg_sum"
            ] = fargate_container_profiler_profiling_fargate_eks_avg_sum
        if fargate_tasks_count_avg_sum is not unset:
            kwargs["fargate_tasks_count_avg_sum"] = fargate_tasks_count_avg_sum
        if fargate_tasks_count_hwm_sum is not unset:
            kwargs["fargate_tasks_count_hwm_sum"] = fargate_tasks_count_hwm_sum
        if flex_logs_compute_large_avg_sum is not unset:
            kwargs["flex_logs_compute_large_avg_sum"] = flex_logs_compute_large_avg_sum
        if flex_logs_compute_medium_avg_sum is not unset:
            kwargs["flex_logs_compute_medium_avg_sum"] = flex_logs_compute_medium_avg_sum
        if flex_logs_compute_small_avg_sum is not unset:
            kwargs["flex_logs_compute_small_avg_sum"] = flex_logs_compute_small_avg_sum
        if flex_logs_compute_xsmall_avg_sum is not unset:
            kwargs["flex_logs_compute_xsmall_avg_sum"] = flex_logs_compute_xsmall_avg_sum
        if flex_logs_starter_avg_sum is not unset:
            kwargs["flex_logs_starter_avg_sum"] = flex_logs_starter_avg_sum
        if flex_logs_starter_storage_index_avg_sum is not unset:
            kwargs["flex_logs_starter_storage_index_avg_sum"] = flex_logs_starter_storage_index_avg_sum
        if flex_logs_starter_storage_retention_adjustment_avg_sum is not unset:
            kwargs[
                "flex_logs_starter_storage_retention_adjustment_avg_sum"
            ] = flex_logs_starter_storage_retention_adjustment_avg_sum
        if flex_stored_logs_avg_sum is not unset:
            kwargs["flex_stored_logs_avg_sum"] = flex_stored_logs_avg_sum
        if forwarding_events_bytes_agg_sum is not unset:
            kwargs["forwarding_events_bytes_agg_sum"] = forwarding_events_bytes_agg_sum
        if gcp_host_top99p_sum is not unset:
            kwargs["gcp_host_top99p_sum"] = gcp_host_top99p_sum
        if heroku_host_top99p_sum is not unset:
            kwargs["heroku_host_top99p_sum"] = heroku_host_top99p_sum
        if incident_management_monthly_active_users_hwm_sum is not unset:
            kwargs[
                "incident_management_monthly_active_users_hwm_sum"
            ] = incident_management_monthly_active_users_hwm_sum
        if indexed_events_count_agg_sum is not unset:
            kwargs["indexed_events_count_agg_sum"] = indexed_events_count_agg_sum
        if infra_host_top99p_sum is not unset:
            kwargs["infra_host_top99p_sum"] = infra_host_top99p_sum
        if ingested_events_bytes_agg_sum is not unset:
            kwargs["ingested_events_bytes_agg_sum"] = ingested_events_bytes_agg_sum
        if iot_device_agg_sum is not unset:
            kwargs["iot_device_agg_sum"] = iot_device_agg_sum
        if iot_device_top99p_sum is not unset:
            kwargs["iot_device_top99p_sum"] = iot_device_top99p_sum
        if last_updated is not unset:
            kwargs["last_updated"] = last_updated
        if live_indexed_events_agg_sum is not unset:
            kwargs["live_indexed_events_agg_sum"] = live_indexed_events_agg_sum
        if live_ingested_bytes_agg_sum is not unset:
            kwargs["live_ingested_bytes_agg_sum"] = live_ingested_bytes_agg_sum
        if llm_observability_agg_sum is not unset:
            kwargs["llm_observability_agg_sum"] = llm_observability_agg_sum
        if llm_observability_min_spend_agg_sum is not unset:
            kwargs["llm_observability_min_spend_agg_sum"] = llm_observability_min_spend_agg_sum
        if logs_by_retention is not unset:
            kwargs["logs_by_retention"] = logs_by_retention
        if mobile_rum_lite_session_count_agg_sum is not unset:
            kwargs["mobile_rum_lite_session_count_agg_sum"] = mobile_rum_lite_session_count_agg_sum
        if mobile_rum_session_count_agg_sum is not unset:
            kwargs["mobile_rum_session_count_agg_sum"] = mobile_rum_session_count_agg_sum
        if mobile_rum_session_count_android_agg_sum is not unset:
            kwargs["mobile_rum_session_count_android_agg_sum"] = mobile_rum_session_count_android_agg_sum
        if mobile_rum_session_count_flutter_agg_sum is not unset:
            kwargs["mobile_rum_session_count_flutter_agg_sum"] = mobile_rum_session_count_flutter_agg_sum
        if mobile_rum_session_count_ios_agg_sum is not unset:
            kwargs["mobile_rum_session_count_ios_agg_sum"] = mobile_rum_session_count_ios_agg_sum
        if mobile_rum_session_count_reactnative_agg_sum is not unset:
            kwargs["mobile_rum_session_count_reactnative_agg_sum"] = mobile_rum_session_count_reactnative_agg_sum
        if mobile_rum_session_count_roku_agg_sum is not unset:
            kwargs["mobile_rum_session_count_roku_agg_sum"] = mobile_rum_session_count_roku_agg_sum
        if mobile_rum_units_agg_sum is not unset:
            kwargs["mobile_rum_units_agg_sum"] = mobile_rum_units_agg_sum
        if ndm_netflow_events_agg_sum is not unset:
            kwargs["ndm_netflow_events_agg_sum"] = ndm_netflow_events_agg_sum
        if netflow_indexed_events_count_agg_sum is not unset:
            kwargs["netflow_indexed_events_count_agg_sum"] = netflow_indexed_events_count_agg_sum
        if network_device_wireless_top99p_sum is not unset:
            kwargs["network_device_wireless_top99p_sum"] = network_device_wireless_top99p_sum
        if npm_host_top99p_sum is not unset:
            kwargs["npm_host_top99p_sum"] = npm_host_top99p_sum
        if observability_pipelines_bytes_processed_agg_sum is not unset:
            kwargs["observability_pipelines_bytes_processed_agg_sum"] = observability_pipelines_bytes_processed_agg_sum
        if oci_host_agg_sum is not unset:
            kwargs["oci_host_agg_sum"] = oci_host_agg_sum
        if oci_host_top99p_sum is not unset:
            kwargs["oci_host_top99p_sum"] = oci_host_top99p_sum
        if online_archive_events_count_agg_sum is not unset:
            kwargs["online_archive_events_count_agg_sum"] = online_archive_events_count_agg_sum
        if opentelemetry_apm_host_top99p_sum is not unset:
            kwargs["opentelemetry_apm_host_top99p_sum"] = opentelemetry_apm_host_top99p_sum
        if opentelemetry_host_top99p_sum is not unset:
            kwargs["opentelemetry_host_top99p_sum"] = opentelemetry_host_top99p_sum
        if product_analytics_agg_sum is not unset:
            kwargs["product_analytics_agg_sum"] = product_analytics_agg_sum
        if profiling_aas_count_top99p_sum is not unset:
            kwargs["profiling_aas_count_top99p_sum"] = profiling_aas_count_top99p_sum
        if profiling_container_agent_count_avg is not unset:
            kwargs["profiling_container_agent_count_avg"] = profiling_container_agent_count_avg
        if profiling_host_count_top99p_sum is not unset:
            kwargs["profiling_host_count_top99p_sum"] = profiling_host_count_top99p_sum
        if published_app_hwm_sum is not unset:
            kwargs["published_app_hwm_sum"] = published_app_hwm_sum
        if rehydrated_indexed_events_agg_sum is not unset:
            kwargs["rehydrated_indexed_events_agg_sum"] = rehydrated_indexed_events_agg_sum
        if rehydrated_ingested_bytes_agg_sum is not unset:
            kwargs["rehydrated_ingested_bytes_agg_sum"] = rehydrated_ingested_bytes_agg_sum
        if rum_browser_and_mobile_session_count is not unset:
            kwargs["rum_browser_and_mobile_session_count"] = rum_browser_and_mobile_session_count
        if rum_browser_legacy_session_count_agg_sum is not unset:
            kwargs["rum_browser_legacy_session_count_agg_sum"] = rum_browser_legacy_session_count_agg_sum
        if rum_browser_lite_session_count_agg_sum is not unset:
            kwargs["rum_browser_lite_session_count_agg_sum"] = rum_browser_lite_session_count_agg_sum
        if rum_browser_replay_session_count_agg_sum is not unset:
            kwargs["rum_browser_replay_session_count_agg_sum"] = rum_browser_replay_session_count_agg_sum
        if rum_indexed_sessions_agg_sum is not unset:
            kwargs["rum_indexed_sessions_agg_sum"] = rum_indexed_sessions_agg_sum
        if rum_ingested_sessions_agg_sum is not unset:
            kwargs["rum_ingested_sessions_agg_sum"] = rum_ingested_sessions_agg_sum
        if rum_lite_session_count_agg_sum is not unset:
            kwargs["rum_lite_session_count_agg_sum"] = rum_lite_session_count_agg_sum
        if rum_mobile_legacy_session_count_android_agg_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_android_agg_sum"] = rum_mobile_legacy_session_count_android_agg_sum
        if rum_mobile_legacy_session_count_flutter_agg_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_flutter_agg_sum"] = rum_mobile_legacy_session_count_flutter_agg_sum
        if rum_mobile_legacy_session_count_ios_agg_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_ios_agg_sum"] = rum_mobile_legacy_session_count_ios_agg_sum
        if rum_mobile_legacy_session_count_reactnative_agg_sum is not unset:
            kwargs[
                "rum_mobile_legacy_session_count_reactnative_agg_sum"
            ] = rum_mobile_legacy_session_count_reactnative_agg_sum
        if rum_mobile_legacy_session_count_roku_agg_sum is not unset:
            kwargs["rum_mobile_legacy_session_count_roku_agg_sum"] = rum_mobile_legacy_session_count_roku_agg_sum
        if rum_mobile_lite_session_count_android_agg_sum is not unset:
            kwargs["rum_mobile_lite_session_count_android_agg_sum"] = rum_mobile_lite_session_count_android_agg_sum
        if rum_mobile_lite_session_count_flutter_agg_sum is not unset:
            kwargs["rum_mobile_lite_session_count_flutter_agg_sum"] = rum_mobile_lite_session_count_flutter_agg_sum
        if rum_mobile_lite_session_count_ios_agg_sum is not unset:
            kwargs["rum_mobile_lite_session_count_ios_agg_sum"] = rum_mobile_lite_session_count_ios_agg_sum
        if rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum is not unset:
            kwargs[
                "rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum"
            ] = rum_mobile_lite_session_count_kotlinmultiplatform_agg_sum
        if rum_mobile_lite_session_count_reactnative_agg_sum is not unset:
            kwargs[
                "rum_mobile_lite_session_count_reactnative_agg_sum"
            ] = rum_mobile_lite_session_count_reactnative_agg_sum
        if rum_mobile_lite_session_count_roku_agg_sum is not unset:
            kwargs["rum_mobile_lite_session_count_roku_agg_sum"] = rum_mobile_lite_session_count_roku_agg_sum
        if rum_mobile_lite_session_count_unity_agg_sum is not unset:
            kwargs["rum_mobile_lite_session_count_unity_agg_sum"] = rum_mobile_lite_session_count_unity_agg_sum
        if rum_mobile_replay_session_count_android_agg_sum is not unset:
            kwargs["rum_mobile_replay_session_count_android_agg_sum"] = rum_mobile_replay_session_count_android_agg_sum
        if rum_mobile_replay_session_count_ios_agg_sum is not unset:
            kwargs["rum_mobile_replay_session_count_ios_agg_sum"] = rum_mobile_replay_session_count_ios_agg_sum
        if rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum is not unset:
            kwargs[
                "rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum"
            ] = rum_mobile_replay_session_count_kotlinmultiplatform_agg_sum
        if rum_mobile_replay_session_count_reactnative_agg_sum is not unset:
            kwargs[
                "rum_mobile_replay_session_count_reactnative_agg_sum"
            ] = rum_mobile_replay_session_count_reactnative_agg_sum
        if rum_replay_session_count_agg_sum is not unset:
            kwargs["rum_replay_session_count_agg_sum"] = rum_replay_session_count_agg_sum
        if rum_session_count_agg_sum is not unset:
            kwargs["rum_session_count_agg_sum"] = rum_session_count_agg_sum
        if rum_session_replay_add_on_agg_sum is not unset:
            kwargs["rum_session_replay_add_on_agg_sum"] = rum_session_replay_add_on_agg_sum
        if rum_total_session_count_agg_sum is not unset:
            kwargs["rum_total_session_count_agg_sum"] = rum_total_session_count_agg_sum
        if rum_units_agg_sum is not unset:
            kwargs["rum_units_agg_sum"] = rum_units_agg_sum
        if sca_fargate_count_avg_sum is not unset:
            kwargs["sca_fargate_count_avg_sum"] = sca_fargate_count_avg_sum
        if sca_fargate_count_hwm_sum is not unset:
            kwargs["sca_fargate_count_hwm_sum"] = sca_fargate_count_hwm_sum
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
        if serverless_apps_azure_count_avg_sum is not unset:
            kwargs["serverless_apps_azure_count_avg_sum"] = serverless_apps_azure_count_avg_sum
        if serverless_apps_google_count_avg_sum is not unset:
            kwargs["serverless_apps_google_count_avg_sum"] = serverless_apps_google_count_avg_sum
        if serverless_apps_total_count_avg_sum is not unset:
            kwargs["serverless_apps_total_count_avg_sum"] = serverless_apps_total_count_avg_sum
        if siem_analyzed_logs_add_on_count_agg_sum is not unset:
            kwargs["siem_analyzed_logs_add_on_count_agg_sum"] = siem_analyzed_logs_add_on_count_agg_sum
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if synthetics_browser_check_calls_count_agg_sum is not unset:
            kwargs["synthetics_browser_check_calls_count_agg_sum"] = synthetics_browser_check_calls_count_agg_sum
        if synthetics_check_calls_count_agg_sum is not unset:
            kwargs["synthetics_check_calls_count_agg_sum"] = synthetics_check_calls_count_agg_sum
        if synthetics_mobile_test_runs_agg_sum is not unset:
            kwargs["synthetics_mobile_test_runs_agg_sum"] = synthetics_mobile_test_runs_agg_sum
        if synthetics_parallel_testing_max_slots_hwm_sum is not unset:
            kwargs["synthetics_parallel_testing_max_slots_hwm_sum"] = synthetics_parallel_testing_max_slots_hwm_sum
        if trace_search_indexed_events_count_agg_sum is not unset:
            kwargs["trace_search_indexed_events_count_agg_sum"] = trace_search_indexed_events_count_agg_sum
        if twol_ingested_events_bytes_agg_sum is not unset:
            kwargs["twol_ingested_events_bytes_agg_sum"] = twol_ingested_events_bytes_agg_sum
        if universal_service_monitoring_host_top99p_sum is not unset:
            kwargs["universal_service_monitoring_host_top99p_sum"] = universal_service_monitoring_host_top99p_sum
        if usage is not unset:
            kwargs["usage"] = usage
        if vsphere_host_top99p_sum is not unset:
            kwargs["vsphere_host_top99p_sum"] = vsphere_host_top99p_sum
        if vuln_management_host_count_top99p_sum is not unset:
            kwargs["vuln_management_host_count_top99p_sum"] = vuln_management_host_count_top99p_sum
        if workflow_executions_usage_agg_sum is not unset:
            kwargs["workflow_executions_usage_agg_sum"] = workflow_executions_usage_agg_sum
        super().__init__(kwargs)
