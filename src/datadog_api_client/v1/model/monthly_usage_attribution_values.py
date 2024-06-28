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


class MonthlyUsageAttributionValues(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_percentage": (float,),
            "api_usage": (float,),
            "apm_fargate_percentage": (float,),
            "apm_fargate_usage": (float,),
            "apm_host_percentage": (float,),
            "apm_host_usage": (float,),
            "apm_usm_percentage": (float,),
            "apm_usm_usage": (float,),
            "appsec_fargate_percentage": (float,),
            "appsec_fargate_usage": (float,),
            "appsec_percentage": (float,),
            "appsec_usage": (float,),
            "asm_serverless_traced_invocations_percentage": (float,),
            "asm_serverless_traced_invocations_usage": (float,),
            "browser_percentage": (float,),
            "browser_usage": (float,),
            "ci_pipeline_indexed_spans_percentage": (float,),
            "ci_pipeline_indexed_spans_usage": (float,),
            "ci_test_indexed_spans_percentage": (float,),
            "ci_test_indexed_spans_usage": (float,),
            "ci_visibility_itr_percentage": (float,),
            "ci_visibility_itr_usage": (float,),
            "cloud_siem_percentage": (float,),
            "cloud_siem_usage": (float,),
            "container_excl_agent_percentage": (float,),
            "container_excl_agent_usage": (float,),
            "container_percentage": (float,),
            "container_usage": (float,),
            "cspm_containers_percentage": (float,),
            "cspm_containers_usage": (float,),
            "cspm_hosts_percentage": (float,),
            "cspm_hosts_usage": (float,),
            "custom_event_percentage": (float,),
            "custom_event_usage": (float,),
            "custom_ingested_timeseries_percentage": (float,),
            "custom_ingested_timeseries_usage": (float,),
            "custom_timeseries_percentage": (float,),
            "custom_timeseries_usage": (float,),
            "cws_containers_percentage": (float,),
            "cws_containers_usage": (float,),
            "cws_hosts_percentage": (float,),
            "cws_hosts_usage": (float,),
            "dbm_hosts_percentage": (float,),
            "dbm_hosts_usage": (float,),
            "dbm_queries_percentage": (float,),
            "dbm_queries_usage": (float,),
            "error_tracking_percentage": (float,),
            "error_tracking_usage": (float,),
            "estimated_indexed_logs_percentage": (float,),
            "estimated_indexed_logs_usage": (float,),
            "estimated_indexed_spans_percentage": (float,),
            "estimated_indexed_spans_usage": (float,),
            "estimated_ingested_logs_percentage": (float,),
            "estimated_ingested_logs_usage": (float,),
            "estimated_ingested_spans_percentage": (float,),
            "estimated_ingested_spans_usage": (float,),
            "estimated_rum_sessions_percentage": (float,),
            "estimated_rum_sessions_usage": (float,),
            "fargate_percentage": (float,),
            "fargate_usage": (float,),
            "functions_percentage": (float,),
            "functions_usage": (float,),
            "incident_management_monthly_active_users_percentage": (float,),
            "incident_management_monthly_active_users_usage": (float,),
            "indexed_spans_percentage": (float,),
            "indexed_spans_usage": (float,),
            "infra_host_percentage": (float,),
            "infra_host_usage": (float,),
            "ingested_logs_bytes_percentage": (float,),
            "ingested_logs_bytes_usage": (float,),
            "ingested_spans_bytes_percentage": (float,),
            "ingested_spans_bytes_usage": (float,),
            "invocations_percentage": (float,),
            "invocations_usage": (float,),
            "lambda_traced_invocations_percentage": (float,),
            "lambda_traced_invocations_usage": (float,),
            "logs_indexed_15day_percentage": (float,),
            "logs_indexed_15day_usage": (float,),
            "logs_indexed_180day_percentage": (float,),
            "logs_indexed_180day_usage": (float,),
            "logs_indexed_1day_percentage": (float,),
            "logs_indexed_1day_usage": (float,),
            "logs_indexed_30day_percentage": (float,),
            "logs_indexed_30day_usage": (float,),
            "logs_indexed_360day_percentage": (float,),
            "logs_indexed_360day_usage": (float,),
            "logs_indexed_3day_percentage": (float,),
            "logs_indexed_3day_usage": (float,),
            "logs_indexed_45day_percentage": (float,),
            "logs_indexed_45day_usage": (float,),
            "logs_indexed_60day_percentage": (float,),
            "logs_indexed_60day_usage": (float,),
            "logs_indexed_7day_percentage": (float,),
            "logs_indexed_7day_usage": (float,),
            "logs_indexed_90day_percentage": (float,),
            "logs_indexed_90day_usage": (float,),
            "logs_indexed_custom_retention_percentage": (float,),
            "logs_indexed_custom_retention_usage": (float,),
            "mobile_app_testing_percentage": (float,),
            "mobile_app_testing_usage": (float,),
            "ndm_netflow_percentage": (float,),
            "ndm_netflow_usage": (float,),
            "npm_host_percentage": (float,),
            "npm_host_usage": (float,),
            "obs_pipeline_bytes_percentage": (float,),
            "obs_pipeline_bytes_usage": (float,),
            "obs_pipelines_vcpu_percentage": (float,),
            "obs_pipelines_vcpu_usage": (float,),
            "online_archive_percentage": (float,),
            "online_archive_usage": (float,),
            "profiled_container_percentage": (float,),
            "profiled_container_usage": (float,),
            "profiled_fargate_percentage": (float,),
            "profiled_fargate_usage": (float,),
            "profiled_host_percentage": (float,),
            "profiled_host_usage": (float,),
            "rum_browser_mobile_sessions_percentage": (float,),
            "rum_browser_mobile_sessions_usage": (float,),
            "rum_replay_sessions_percentage": (float,),
            "rum_replay_sessions_usage": (float,),
            "sds_scanned_bytes_percentage": (float,),
            "sds_scanned_bytes_usage": (float,),
            "serverless_apps_percentage": (float,),
            "serverless_apps_usage": (float,),
            "siem_ingested_bytes_percentage": (float,),
            "siem_ingested_bytes_usage": (float,),
            "snmp_percentage": (float,),
            "snmp_usage": (float,),
            "universal_service_monitoring_percentage": (float,),
            "universal_service_monitoring_usage": (float,),
            "vuln_management_hosts_percentage": (float,),
            "vuln_management_hosts_usage": (float,),
            "workflow_executions_percentage": (float,),
            "workflow_executions_usage": (float,),
        }

    attribute_map = {
        "api_percentage": "api_percentage",
        "api_usage": "api_usage",
        "apm_fargate_percentage": "apm_fargate_percentage",
        "apm_fargate_usage": "apm_fargate_usage",
        "apm_host_percentage": "apm_host_percentage",
        "apm_host_usage": "apm_host_usage",
        "apm_usm_percentage": "apm_usm_percentage",
        "apm_usm_usage": "apm_usm_usage",
        "appsec_fargate_percentage": "appsec_fargate_percentage",
        "appsec_fargate_usage": "appsec_fargate_usage",
        "appsec_percentage": "appsec_percentage",
        "appsec_usage": "appsec_usage",
        "asm_serverless_traced_invocations_percentage": "asm_serverless_traced_invocations_percentage",
        "asm_serverless_traced_invocations_usage": "asm_serverless_traced_invocations_usage",
        "browser_percentage": "browser_percentage",
        "browser_usage": "browser_usage",
        "ci_pipeline_indexed_spans_percentage": "ci_pipeline_indexed_spans_percentage",
        "ci_pipeline_indexed_spans_usage": "ci_pipeline_indexed_spans_usage",
        "ci_test_indexed_spans_percentage": "ci_test_indexed_spans_percentage",
        "ci_test_indexed_spans_usage": "ci_test_indexed_spans_usage",
        "ci_visibility_itr_percentage": "ci_visibility_itr_percentage",
        "ci_visibility_itr_usage": "ci_visibility_itr_usage",
        "cloud_siem_percentage": "cloud_siem_percentage",
        "cloud_siem_usage": "cloud_siem_usage",
        "container_excl_agent_percentage": "container_excl_agent_percentage",
        "container_excl_agent_usage": "container_excl_agent_usage",
        "container_percentage": "container_percentage",
        "container_usage": "container_usage",
        "cspm_containers_percentage": "cspm_containers_percentage",
        "cspm_containers_usage": "cspm_containers_usage",
        "cspm_hosts_percentage": "cspm_hosts_percentage",
        "cspm_hosts_usage": "cspm_hosts_usage",
        "custom_event_percentage": "custom_event_percentage",
        "custom_event_usage": "custom_event_usage",
        "custom_ingested_timeseries_percentage": "custom_ingested_timeseries_percentage",
        "custom_ingested_timeseries_usage": "custom_ingested_timeseries_usage",
        "custom_timeseries_percentage": "custom_timeseries_percentage",
        "custom_timeseries_usage": "custom_timeseries_usage",
        "cws_containers_percentage": "cws_containers_percentage",
        "cws_containers_usage": "cws_containers_usage",
        "cws_hosts_percentage": "cws_hosts_percentage",
        "cws_hosts_usage": "cws_hosts_usage",
        "dbm_hosts_percentage": "dbm_hosts_percentage",
        "dbm_hosts_usage": "dbm_hosts_usage",
        "dbm_queries_percentage": "dbm_queries_percentage",
        "dbm_queries_usage": "dbm_queries_usage",
        "error_tracking_percentage": "error_tracking_percentage",
        "error_tracking_usage": "error_tracking_usage",
        "estimated_indexed_logs_percentage": "estimated_indexed_logs_percentage",
        "estimated_indexed_logs_usage": "estimated_indexed_logs_usage",
        "estimated_indexed_spans_percentage": "estimated_indexed_spans_percentage",
        "estimated_indexed_spans_usage": "estimated_indexed_spans_usage",
        "estimated_ingested_logs_percentage": "estimated_ingested_logs_percentage",
        "estimated_ingested_logs_usage": "estimated_ingested_logs_usage",
        "estimated_ingested_spans_percentage": "estimated_ingested_spans_percentage",
        "estimated_ingested_spans_usage": "estimated_ingested_spans_usage",
        "estimated_rum_sessions_percentage": "estimated_rum_sessions_percentage",
        "estimated_rum_sessions_usage": "estimated_rum_sessions_usage",
        "fargate_percentage": "fargate_percentage",
        "fargate_usage": "fargate_usage",
        "functions_percentage": "functions_percentage",
        "functions_usage": "functions_usage",
        "incident_management_monthly_active_users_percentage": "incident_management_monthly_active_users_percentage",
        "incident_management_monthly_active_users_usage": "incident_management_monthly_active_users_usage",
        "indexed_spans_percentage": "indexed_spans_percentage",
        "indexed_spans_usage": "indexed_spans_usage",
        "infra_host_percentage": "infra_host_percentage",
        "infra_host_usage": "infra_host_usage",
        "ingested_logs_bytes_percentage": "ingested_logs_bytes_percentage",
        "ingested_logs_bytes_usage": "ingested_logs_bytes_usage",
        "ingested_spans_bytes_percentage": "ingested_spans_bytes_percentage",
        "ingested_spans_bytes_usage": "ingested_spans_bytes_usage",
        "invocations_percentage": "invocations_percentage",
        "invocations_usage": "invocations_usage",
        "lambda_traced_invocations_percentage": "lambda_traced_invocations_percentage",
        "lambda_traced_invocations_usage": "lambda_traced_invocations_usage",
        "logs_indexed_15day_percentage": "logs_indexed_15day_percentage",
        "logs_indexed_15day_usage": "logs_indexed_15day_usage",
        "logs_indexed_180day_percentage": "logs_indexed_180day_percentage",
        "logs_indexed_180day_usage": "logs_indexed_180day_usage",
        "logs_indexed_1day_percentage": "logs_indexed_1day_percentage",
        "logs_indexed_1day_usage": "logs_indexed_1day_usage",
        "logs_indexed_30day_percentage": "logs_indexed_30day_percentage",
        "logs_indexed_30day_usage": "logs_indexed_30day_usage",
        "logs_indexed_360day_percentage": "logs_indexed_360day_percentage",
        "logs_indexed_360day_usage": "logs_indexed_360day_usage",
        "logs_indexed_3day_percentage": "logs_indexed_3day_percentage",
        "logs_indexed_3day_usage": "logs_indexed_3day_usage",
        "logs_indexed_45day_percentage": "logs_indexed_45day_percentage",
        "logs_indexed_45day_usage": "logs_indexed_45day_usage",
        "logs_indexed_60day_percentage": "logs_indexed_60day_percentage",
        "logs_indexed_60day_usage": "logs_indexed_60day_usage",
        "logs_indexed_7day_percentage": "logs_indexed_7day_percentage",
        "logs_indexed_7day_usage": "logs_indexed_7day_usage",
        "logs_indexed_90day_percentage": "logs_indexed_90day_percentage",
        "logs_indexed_90day_usage": "logs_indexed_90day_usage",
        "logs_indexed_custom_retention_percentage": "logs_indexed_custom_retention_percentage",
        "logs_indexed_custom_retention_usage": "logs_indexed_custom_retention_usage",
        "mobile_app_testing_percentage": "mobile_app_testing_percentage",
        "mobile_app_testing_usage": "mobile_app_testing_usage",
        "ndm_netflow_percentage": "ndm_netflow_percentage",
        "ndm_netflow_usage": "ndm_netflow_usage",
        "npm_host_percentage": "npm_host_percentage",
        "npm_host_usage": "npm_host_usage",
        "obs_pipeline_bytes_percentage": "obs_pipeline_bytes_percentage",
        "obs_pipeline_bytes_usage": "obs_pipeline_bytes_usage",
        "obs_pipelines_vcpu_percentage": "obs_pipelines_vcpu_percentage",
        "obs_pipelines_vcpu_usage": "obs_pipelines_vcpu_usage",
        "online_archive_percentage": "online_archive_percentage",
        "online_archive_usage": "online_archive_usage",
        "profiled_container_percentage": "profiled_container_percentage",
        "profiled_container_usage": "profiled_container_usage",
        "profiled_fargate_percentage": "profiled_fargate_percentage",
        "profiled_fargate_usage": "profiled_fargate_usage",
        "profiled_host_percentage": "profiled_host_percentage",
        "profiled_host_usage": "profiled_host_usage",
        "rum_browser_mobile_sessions_percentage": "rum_browser_mobile_sessions_percentage",
        "rum_browser_mobile_sessions_usage": "rum_browser_mobile_sessions_usage",
        "rum_replay_sessions_percentage": "rum_replay_sessions_percentage",
        "rum_replay_sessions_usage": "rum_replay_sessions_usage",
        "sds_scanned_bytes_percentage": "sds_scanned_bytes_percentage",
        "sds_scanned_bytes_usage": "sds_scanned_bytes_usage",
        "serverless_apps_percentage": "serverless_apps_percentage",
        "serverless_apps_usage": "serverless_apps_usage",
        "siem_ingested_bytes_percentage": "siem_ingested_bytes_percentage",
        "siem_ingested_bytes_usage": "siem_ingested_bytes_usage",
        "snmp_percentage": "snmp_percentage",
        "snmp_usage": "snmp_usage",
        "universal_service_monitoring_percentage": "universal_service_monitoring_percentage",
        "universal_service_monitoring_usage": "universal_service_monitoring_usage",
        "vuln_management_hosts_percentage": "vuln_management_hosts_percentage",
        "vuln_management_hosts_usage": "vuln_management_hosts_usage",
        "workflow_executions_percentage": "workflow_executions_percentage",
        "workflow_executions_usage": "workflow_executions_usage",
    }

    def __init__(
        self_,
        api_percentage: Union[float, UnsetType] = unset,
        api_usage: Union[float, UnsetType] = unset,
        apm_fargate_percentage: Union[float, UnsetType] = unset,
        apm_fargate_usage: Union[float, UnsetType] = unset,
        apm_host_percentage: Union[float, UnsetType] = unset,
        apm_host_usage: Union[float, UnsetType] = unset,
        apm_usm_percentage: Union[float, UnsetType] = unset,
        apm_usm_usage: Union[float, UnsetType] = unset,
        appsec_fargate_percentage: Union[float, UnsetType] = unset,
        appsec_fargate_usage: Union[float, UnsetType] = unset,
        appsec_percentage: Union[float, UnsetType] = unset,
        appsec_usage: Union[float, UnsetType] = unset,
        asm_serverless_traced_invocations_percentage: Union[float, UnsetType] = unset,
        asm_serverless_traced_invocations_usage: Union[float, UnsetType] = unset,
        browser_percentage: Union[float, UnsetType] = unset,
        browser_usage: Union[float, UnsetType] = unset,
        ci_pipeline_indexed_spans_percentage: Union[float, UnsetType] = unset,
        ci_pipeline_indexed_spans_usage: Union[float, UnsetType] = unset,
        ci_test_indexed_spans_percentage: Union[float, UnsetType] = unset,
        ci_test_indexed_spans_usage: Union[float, UnsetType] = unset,
        ci_visibility_itr_percentage: Union[float, UnsetType] = unset,
        ci_visibility_itr_usage: Union[float, UnsetType] = unset,
        cloud_siem_percentage: Union[float, UnsetType] = unset,
        cloud_siem_usage: Union[float, UnsetType] = unset,
        container_excl_agent_percentage: Union[float, UnsetType] = unset,
        container_excl_agent_usage: Union[float, UnsetType] = unset,
        container_percentage: Union[float, UnsetType] = unset,
        container_usage: Union[float, UnsetType] = unset,
        cspm_containers_percentage: Union[float, UnsetType] = unset,
        cspm_containers_usage: Union[float, UnsetType] = unset,
        cspm_hosts_percentage: Union[float, UnsetType] = unset,
        cspm_hosts_usage: Union[float, UnsetType] = unset,
        custom_event_percentage: Union[float, UnsetType] = unset,
        custom_event_usage: Union[float, UnsetType] = unset,
        custom_ingested_timeseries_percentage: Union[float, UnsetType] = unset,
        custom_ingested_timeseries_usage: Union[float, UnsetType] = unset,
        custom_timeseries_percentage: Union[float, UnsetType] = unset,
        custom_timeseries_usage: Union[float, UnsetType] = unset,
        cws_containers_percentage: Union[float, UnsetType] = unset,
        cws_containers_usage: Union[float, UnsetType] = unset,
        cws_hosts_percentage: Union[float, UnsetType] = unset,
        cws_hosts_usage: Union[float, UnsetType] = unset,
        dbm_hosts_percentage: Union[float, UnsetType] = unset,
        dbm_hosts_usage: Union[float, UnsetType] = unset,
        dbm_queries_percentage: Union[float, UnsetType] = unset,
        dbm_queries_usage: Union[float, UnsetType] = unset,
        error_tracking_percentage: Union[float, UnsetType] = unset,
        error_tracking_usage: Union[float, UnsetType] = unset,
        estimated_indexed_logs_percentage: Union[float, UnsetType] = unset,
        estimated_indexed_logs_usage: Union[float, UnsetType] = unset,
        estimated_indexed_spans_percentage: Union[float, UnsetType] = unset,
        estimated_indexed_spans_usage: Union[float, UnsetType] = unset,
        estimated_ingested_logs_percentage: Union[float, UnsetType] = unset,
        estimated_ingested_logs_usage: Union[float, UnsetType] = unset,
        estimated_ingested_spans_percentage: Union[float, UnsetType] = unset,
        estimated_ingested_spans_usage: Union[float, UnsetType] = unset,
        estimated_rum_sessions_percentage: Union[float, UnsetType] = unset,
        estimated_rum_sessions_usage: Union[float, UnsetType] = unset,
        fargate_percentage: Union[float, UnsetType] = unset,
        fargate_usage: Union[float, UnsetType] = unset,
        functions_percentage: Union[float, UnsetType] = unset,
        functions_usage: Union[float, UnsetType] = unset,
        incident_management_monthly_active_users_percentage: Union[float, UnsetType] = unset,
        incident_management_monthly_active_users_usage: Union[float, UnsetType] = unset,
        indexed_spans_percentage: Union[float, UnsetType] = unset,
        indexed_spans_usage: Union[float, UnsetType] = unset,
        infra_host_percentage: Union[float, UnsetType] = unset,
        infra_host_usage: Union[float, UnsetType] = unset,
        ingested_logs_bytes_percentage: Union[float, UnsetType] = unset,
        ingested_logs_bytes_usage: Union[float, UnsetType] = unset,
        ingested_spans_bytes_percentage: Union[float, UnsetType] = unset,
        ingested_spans_bytes_usage: Union[float, UnsetType] = unset,
        invocations_percentage: Union[float, UnsetType] = unset,
        invocations_usage: Union[float, UnsetType] = unset,
        lambda_traced_invocations_percentage: Union[float, UnsetType] = unset,
        lambda_traced_invocations_usage: Union[float, UnsetType] = unset,
        logs_indexed_15day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_15day_usage: Union[float, UnsetType] = unset,
        logs_indexed_180day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_180day_usage: Union[float, UnsetType] = unset,
        logs_indexed_1day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_1day_usage: Union[float, UnsetType] = unset,
        logs_indexed_30day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_30day_usage: Union[float, UnsetType] = unset,
        logs_indexed_360day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_360day_usage: Union[float, UnsetType] = unset,
        logs_indexed_3day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_3day_usage: Union[float, UnsetType] = unset,
        logs_indexed_45day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_45day_usage: Union[float, UnsetType] = unset,
        logs_indexed_60day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_60day_usage: Union[float, UnsetType] = unset,
        logs_indexed_7day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_7day_usage: Union[float, UnsetType] = unset,
        logs_indexed_90day_percentage: Union[float, UnsetType] = unset,
        logs_indexed_90day_usage: Union[float, UnsetType] = unset,
        logs_indexed_custom_retention_percentage: Union[float, UnsetType] = unset,
        logs_indexed_custom_retention_usage: Union[float, UnsetType] = unset,
        mobile_app_testing_percentage: Union[float, UnsetType] = unset,
        mobile_app_testing_usage: Union[float, UnsetType] = unset,
        ndm_netflow_percentage: Union[float, UnsetType] = unset,
        ndm_netflow_usage: Union[float, UnsetType] = unset,
        npm_host_percentage: Union[float, UnsetType] = unset,
        npm_host_usage: Union[float, UnsetType] = unset,
        obs_pipeline_bytes_percentage: Union[float, UnsetType] = unset,
        obs_pipeline_bytes_usage: Union[float, UnsetType] = unset,
        obs_pipelines_vcpu_percentage: Union[float, UnsetType] = unset,
        obs_pipelines_vcpu_usage: Union[float, UnsetType] = unset,
        online_archive_percentage: Union[float, UnsetType] = unset,
        online_archive_usage: Union[float, UnsetType] = unset,
        profiled_container_percentage: Union[float, UnsetType] = unset,
        profiled_container_usage: Union[float, UnsetType] = unset,
        profiled_fargate_percentage: Union[float, UnsetType] = unset,
        profiled_fargate_usage: Union[float, UnsetType] = unset,
        profiled_host_percentage: Union[float, UnsetType] = unset,
        profiled_host_usage: Union[float, UnsetType] = unset,
        rum_browser_mobile_sessions_percentage: Union[float, UnsetType] = unset,
        rum_browser_mobile_sessions_usage: Union[float, UnsetType] = unset,
        rum_replay_sessions_percentage: Union[float, UnsetType] = unset,
        rum_replay_sessions_usage: Union[float, UnsetType] = unset,
        sds_scanned_bytes_percentage: Union[float, UnsetType] = unset,
        sds_scanned_bytes_usage: Union[float, UnsetType] = unset,
        serverless_apps_percentage: Union[float, UnsetType] = unset,
        serverless_apps_usage: Union[float, UnsetType] = unset,
        siem_ingested_bytes_percentage: Union[float, UnsetType] = unset,
        siem_ingested_bytes_usage: Union[float, UnsetType] = unset,
        snmp_percentage: Union[float, UnsetType] = unset,
        snmp_usage: Union[float, UnsetType] = unset,
        universal_service_monitoring_percentage: Union[float, UnsetType] = unset,
        universal_service_monitoring_usage: Union[float, UnsetType] = unset,
        vuln_management_hosts_percentage: Union[float, UnsetType] = unset,
        vuln_management_hosts_usage: Union[float, UnsetType] = unset,
        workflow_executions_percentage: Union[float, UnsetType] = unset,
        workflow_executions_usage: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fields in Usage Summary by tag(s).

        :param api_percentage: The percentage of synthetic API test usage by tag(s).
        :type api_percentage: float, optional

        :param api_usage: The synthetic API test usage by tag(s).
        :type api_usage: float, optional

        :param apm_fargate_percentage: The percentage of APM ECS Fargate task usage by tag(s).
        :type apm_fargate_percentage: float, optional

        :param apm_fargate_usage: The APM ECS Fargate task usage by tag(s).
        :type apm_fargate_usage: float, optional

        :param apm_host_percentage: The percentage of APM host usage by tag(s).
        :type apm_host_percentage: float, optional

        :param apm_host_usage: The APM host usage by tag(s).
        :type apm_host_usage: float, optional

        :param apm_usm_percentage: The percentage of APM and Universal Service Monitoring host usage by tag(s).
        :type apm_usm_percentage: float, optional

        :param apm_usm_usage: The APM and Universal Service Monitoring host usage by tag(s).
        :type apm_usm_usage: float, optional

        :param appsec_fargate_percentage: The percentage of Application Security Monitoring ECS Fargate task usage by tag(s).
        :type appsec_fargate_percentage: float, optional

        :param appsec_fargate_usage: The Application Security Monitoring ECS Fargate task usage by tag(s).
        :type appsec_fargate_usage: float, optional

        :param appsec_percentage: The percentage of Application Security Monitoring host usage by tag(s).
        :type appsec_percentage: float, optional

        :param appsec_usage: The Application Security Monitoring host usage by tag(s).
        :type appsec_usage: float, optional

        :param asm_serverless_traced_invocations_percentage: The percentage of Application Security Monitoring Serverless traced invocations usage by tag(s).
        :type asm_serverless_traced_invocations_percentage: float, optional

        :param asm_serverless_traced_invocations_usage: The Application Security Monitoring Serverless traced invocations usage by tag(s).
        :type asm_serverless_traced_invocations_usage: float, optional

        :param browser_percentage: The percentage of synthetic browser test usage by tag(s).
        :type browser_percentage: float, optional

        :param browser_usage: The synthetic browser test usage by tag(s).
        :type browser_usage: float, optional

        :param ci_pipeline_indexed_spans_percentage: The percentage of CI Pipeline Indexed Spans usage by tag(s).
        :type ci_pipeline_indexed_spans_percentage: float, optional

        :param ci_pipeline_indexed_spans_usage: The total CI Pipeline Indexed Spans usage by tag(s).
        :type ci_pipeline_indexed_spans_usage: float, optional

        :param ci_test_indexed_spans_percentage: The percentage of CI Test Indexed Spans usage by tag(s).
        :type ci_test_indexed_spans_percentage: float, optional

        :param ci_test_indexed_spans_usage: The total CI Test Indexed Spans usage by tag(s).
        :type ci_test_indexed_spans_usage: float, optional

        :param ci_visibility_itr_percentage: The percentage of Git committers for Intelligent Test Runner usage by tag(s).
        :type ci_visibility_itr_percentage: float, optional

        :param ci_visibility_itr_usage: The Git committers for Intelligent Test Runner usage by tag(s).
        :type ci_visibility_itr_usage: float, optional

        :param cloud_siem_percentage: The percentage of Cloud Security Information and Event Management usage by tag(s).
        :type cloud_siem_percentage: float, optional

        :param cloud_siem_usage: The Cloud Security Information and Event Management usage by tag(s).
        :type cloud_siem_usage: float, optional

        :param container_excl_agent_percentage: The percentage of container usage without the Datadog Agent by tag(s).
        :type container_excl_agent_percentage: float, optional

        :param container_excl_agent_usage: The container usage without the Datadog Agent by tag(s).
        :type container_excl_agent_usage: float, optional

        :param container_percentage: The percentage of container usage by tag(s).
        :type container_percentage: float, optional

        :param container_usage: The container usage by tag(s).
        :type container_usage: float, optional

        :param cspm_containers_percentage: The percentage of Cloud Security Management Pro container usage by tag(s).
        :type cspm_containers_percentage: float, optional

        :param cspm_containers_usage: The Cloud Security Management Pro container usage by tag(s).
        :type cspm_containers_usage: float, optional

        :param cspm_hosts_percentage: The percentage of Cloud Security Management Pro host usage by tag(s).
        :type cspm_hosts_percentage: float, optional

        :param cspm_hosts_usage: The Cloud Security Management Pro host usage by tag(s).
        :type cspm_hosts_usage: float, optional

        :param custom_event_percentage: The percentage of Custom Events usage by tag(s).
        :type custom_event_percentage: float, optional

        :param custom_event_usage: The total Custom Events usage by tag(s).
        :type custom_event_usage: float, optional

        :param custom_ingested_timeseries_percentage: The percentage of ingested custom metrics usage by tag(s).
        :type custom_ingested_timeseries_percentage: float, optional

        :param custom_ingested_timeseries_usage: The ingested custom metrics usage by tag(s).
        :type custom_ingested_timeseries_usage: float, optional

        :param custom_timeseries_percentage: The percentage of indexed custom metrics usage by tag(s).
        :type custom_timeseries_percentage: float, optional

        :param custom_timeseries_usage: The indexed custom metrics usage by tag(s).
        :type custom_timeseries_usage: float, optional

        :param cws_containers_percentage: The percentage of Cloud Workload Security container usage by tag(s).
        :type cws_containers_percentage: float, optional

        :param cws_containers_usage: The Cloud Workload Security container usage by tag(s).
        :type cws_containers_usage: float, optional

        :param cws_hosts_percentage: The percentage of Cloud Workload Security host usage by tag(s).
        :type cws_hosts_percentage: float, optional

        :param cws_hosts_usage: The Cloud Workload Security host usage by tag(s).
        :type cws_hosts_usage: float, optional

        :param dbm_hosts_percentage: The percentage of Database Monitoring host usage by tag(s).
        :type dbm_hosts_percentage: float, optional

        :param dbm_hosts_usage: The Database Monitoring host usage by tag(s).
        :type dbm_hosts_usage: float, optional

        :param dbm_queries_percentage: The percentage of Database Monitoring queries usage by tag(s).
        :type dbm_queries_percentage: float, optional

        :param dbm_queries_usage: The Database Monitoring queries usage by tag(s).
        :type dbm_queries_usage: float, optional

        :param error_tracking_percentage: The percentage of error tracking events usage by tag(s).
        :type error_tracking_percentage: float, optional

        :param error_tracking_usage: The error tracking events usage by tag(s).
        :type error_tracking_usage: float, optional

        :param estimated_indexed_logs_percentage: The percentage of estimated live indexed logs usage by tag(s).
        :type estimated_indexed_logs_percentage: float, optional

        :param estimated_indexed_logs_usage: The estimated live indexed logs usage by tag(s).
        :type estimated_indexed_logs_usage: float, optional

        :param estimated_indexed_spans_percentage: The percentage of estimated indexed spans usage by tag(s).
        :type estimated_indexed_spans_percentage: float, optional

        :param estimated_indexed_spans_usage: The estimated indexed spans usage by tag(s).
        :type estimated_indexed_spans_usage: float, optional

        :param estimated_ingested_logs_percentage: The percentage of estimated live ingested logs usage by tag(s).
        :type estimated_ingested_logs_percentage: float, optional

        :param estimated_ingested_logs_usage: The estimated live ingested logs usage by tag(s).
        :type estimated_ingested_logs_usage: float, optional

        :param estimated_ingested_spans_percentage: The percentage of estimated ingested spans usage by tag(s).
        :type estimated_ingested_spans_percentage: float, optional

        :param estimated_ingested_spans_usage: The estimated ingested spans usage by tag(s).
        :type estimated_ingested_spans_usage: float, optional

        :param estimated_rum_sessions_percentage: The percentage of estimated rum sessions usage by tag(s).
        :type estimated_rum_sessions_percentage: float, optional

        :param estimated_rum_sessions_usage: The estimated rum sessions usage by tag(s).
        :type estimated_rum_sessions_usage: float, optional

        :param fargate_percentage: The percentage of Fargate usage by tags.
        :type fargate_percentage: float, optional

        :param fargate_usage: The Fargate usage by tags.
        :type fargate_usage: float, optional

        :param functions_percentage: The percentage of Lambda function usage by tag(s).
        :type functions_percentage: float, optional

        :param functions_usage: The Lambda function usage by tag(s).
        :type functions_usage: float, optional

        :param incident_management_monthly_active_users_percentage: The percentage of Incident Management monthly active users usage by tag(s).
        :type incident_management_monthly_active_users_percentage: float, optional

        :param incident_management_monthly_active_users_usage: The Incident Management monthly active users usage by tag(s).
        :type incident_management_monthly_active_users_usage: float, optional

        :param indexed_spans_percentage: The percentage of APM Indexed Spans usage by tag(s).
        :type indexed_spans_percentage: float, optional

        :param indexed_spans_usage: The total APM Indexed Spans usage by tag(s).
        :type indexed_spans_usage: float, optional

        :param infra_host_percentage: The percentage of infrastructure host usage by tag(s).
        :type infra_host_percentage: float, optional

        :param infra_host_usage: The infrastructure host usage by tag(s).
        :type infra_host_usage: float, optional

        :param ingested_logs_bytes_percentage: The percentage of Ingested Logs usage by tag(s).
        :type ingested_logs_bytes_percentage: float, optional

        :param ingested_logs_bytes_usage: The total Ingested Logs usage by tag(s).
        :type ingested_logs_bytes_usage: float, optional

        :param ingested_spans_bytes_percentage: The percentage of APM Ingested Spans usage by tag(s).
        :type ingested_spans_bytes_percentage: float, optional

        :param ingested_spans_bytes_usage: The total APM Ingested Spans usage by tag(s).
        :type ingested_spans_bytes_usage: float, optional

        :param invocations_percentage: The percentage of Lambda invocation usage by tag(s).
        :type invocations_percentage: float, optional

        :param invocations_usage: The Lambda invocation usage by tag(s).
        :type invocations_usage: float, optional

        :param lambda_traced_invocations_percentage: The percentage of Serverless APM usage by tag(s).
        :type lambda_traced_invocations_percentage: float, optional

        :param lambda_traced_invocations_usage: The Serverless APM usage by tag(s).
        :type lambda_traced_invocations_usage: float, optional

        :param logs_indexed_15day_percentage: The percentage of Indexed Logs (15-day Retention) usage by tag(s).
        :type logs_indexed_15day_percentage: float, optional

        :param logs_indexed_15day_usage: The total Indexed Logs (15-day Retention) usage by tag(s).
        :type logs_indexed_15day_usage: float, optional

        :param logs_indexed_180day_percentage: The percentage of Indexed Logs (180-day Retention) usage by tag(s).
        :type logs_indexed_180day_percentage: float, optional

        :param logs_indexed_180day_usage: The total Indexed Logs (180-day Retention) usage by tag(s).
        :type logs_indexed_180day_usage: float, optional

        :param logs_indexed_1day_percentage: The percentage of Indexed Logs (1-day Retention) usage by tag(s).
        :type logs_indexed_1day_percentage: float, optional

        :param logs_indexed_1day_usage: The total Indexed Logs (1-day Retention) usage by tag(s).
        :type logs_indexed_1day_usage: float, optional

        :param logs_indexed_30day_percentage: The percentage of Indexed Logs (30-day Retention) usage by tag(s).
        :type logs_indexed_30day_percentage: float, optional

        :param logs_indexed_30day_usage: The total Indexed Logs (30-day Retention) usage by tag(s).
        :type logs_indexed_30day_usage: float, optional

        :param logs_indexed_360day_percentage: The percentage of Indexed Logs (360-day Retention) usage by tag(s).
        :type logs_indexed_360day_percentage: float, optional

        :param logs_indexed_360day_usage: The total Indexed Logs (360-day Retention) usage by tag(s).
        :type logs_indexed_360day_usage: float, optional

        :param logs_indexed_3day_percentage: The percentage of Indexed Logs (3-day Retention) usage by tag(s).
        :type logs_indexed_3day_percentage: float, optional

        :param logs_indexed_3day_usage: The total Indexed Logs (3-day Retention) usage by tag(s).
        :type logs_indexed_3day_usage: float, optional

        :param logs_indexed_45day_percentage: The percentage of Indexed Logs (45-day Retention) usage by tag(s).
        :type logs_indexed_45day_percentage: float, optional

        :param logs_indexed_45day_usage: The total Indexed Logs (45-day Retention) usage by tag(s).
        :type logs_indexed_45day_usage: float, optional

        :param logs_indexed_60day_percentage: The percentage of Indexed Logs (60-day Retention) usage by tag(s).
        :type logs_indexed_60day_percentage: float, optional

        :param logs_indexed_60day_usage: The total Indexed Logs (60-day Retention) usage by tag(s).
        :type logs_indexed_60day_usage: float, optional

        :param logs_indexed_7day_percentage: The percentage of Indexed Logs (7-day Retention) usage by tag(s).
        :type logs_indexed_7day_percentage: float, optional

        :param logs_indexed_7day_usage: The total Indexed Logs (7-day Retention) usage by tag(s).
        :type logs_indexed_7day_usage: float, optional

        :param logs_indexed_90day_percentage: The percentage of Indexed Logs (90-day Retention) usage by tag(s).
        :type logs_indexed_90day_percentage: float, optional

        :param logs_indexed_90day_usage: The total Indexed Logs (90-day Retention) usage by tag(s).
        :type logs_indexed_90day_usage: float, optional

        :param logs_indexed_custom_retention_percentage: The percentage of Indexed Logs (Custom Retention) usage by tag(s).
        :type logs_indexed_custom_retention_percentage: float, optional

        :param logs_indexed_custom_retention_usage: The total Indexed Logs (Custom Retention) usage by tag(s).
        :type logs_indexed_custom_retention_usage: float, optional

        :param mobile_app_testing_percentage: The percentage of Synthetic mobile application test usage by tag(s).
        :type mobile_app_testing_percentage: float, optional

        :param mobile_app_testing_usage: The Synthetic mobile application test usage by tag(s).
        :type mobile_app_testing_usage: float, optional

        :param ndm_netflow_percentage: The percentage of Network Device Monitoring NetFlow usage by tag(s).
        :type ndm_netflow_percentage: float, optional

        :param ndm_netflow_usage: The Network Device Monitoring NetFlow usage by tag(s).
        :type ndm_netflow_usage: float, optional

        :param npm_host_percentage: The percentage of network host usage by tag(s).
        :type npm_host_percentage: float, optional

        :param npm_host_usage: The network host usage by tag(s).
        :type npm_host_usage: float, optional

        :param obs_pipeline_bytes_percentage: The percentage of observability pipeline bytes usage by tag(s).
        :type obs_pipeline_bytes_percentage: float, optional

        :param obs_pipeline_bytes_usage: The observability pipeline bytes usage by tag(s).
        :type obs_pipeline_bytes_usage: float, optional

        :param obs_pipelines_vcpu_percentage: The percentage of observability pipeline per core usage by tag(s).
        :type obs_pipelines_vcpu_percentage: float, optional

        :param obs_pipelines_vcpu_usage: The observability pipeline per core usage by tag(s).
        :type obs_pipelines_vcpu_usage: float, optional

        :param online_archive_percentage: The percentage of online archive usage by tag(s).
        :type online_archive_percentage: float, optional

        :param online_archive_usage: The online archive usage by tag(s).
        :type online_archive_usage: float, optional

        :param profiled_container_percentage: The percentage of profiled container usage by tag(s).
        :type profiled_container_percentage: float, optional

        :param profiled_container_usage: The profiled container usage by tag(s).
        :type profiled_container_usage: float, optional

        :param profiled_fargate_percentage: The percentage of profiled Fargate task usage by tag(s).
        :type profiled_fargate_percentage: float, optional

        :param profiled_fargate_usage: The profiled Fargate task usage by tag(s).
        :type profiled_fargate_usage: float, optional

        :param profiled_host_percentage: The percentage of profiled hosts usage by tag(s).
        :type profiled_host_percentage: float, optional

        :param profiled_host_usage: The profiled hosts usage by tag(s).
        :type profiled_host_usage: float, optional

        :param rum_browser_mobile_sessions_percentage: The percentage of RUM Browser and Mobile usage by tag(s).
        :type rum_browser_mobile_sessions_percentage: float, optional

        :param rum_browser_mobile_sessions_usage: The total RUM Browser and Mobile usage by tag(s).
        :type rum_browser_mobile_sessions_usage: float, optional

        :param rum_replay_sessions_percentage: The percentage of RUM Session Replay usage by tag(s).
        :type rum_replay_sessions_percentage: float, optional

        :param rum_replay_sessions_usage: The total RUM Session Replay usage by tag(s).
        :type rum_replay_sessions_usage: float, optional

        :param sds_scanned_bytes_percentage: The percentage of Sensitive Data Scanner usage by tag(s).
        :type sds_scanned_bytes_percentage: float, optional

        :param sds_scanned_bytes_usage: The total Sensitive Data Scanner usage by tag(s).
        :type sds_scanned_bytes_usage: float, optional

        :param serverless_apps_percentage: The percentage of Serverless Apps usage by tag(s).
        :type serverless_apps_percentage: float, optional

        :param serverless_apps_usage: The total Serverless Apps usage by tag(s).
        :type serverless_apps_usage: float, optional

        :param siem_ingested_bytes_percentage: The percentage of SIEM usage by tag(s).
        :type siem_ingested_bytes_percentage: float, optional

        :param siem_ingested_bytes_usage: The total SIEM usage by tag(s).
        :type siem_ingested_bytes_usage: float, optional

        :param snmp_percentage: The percentage of network device usage by tag(s).
        :type snmp_percentage: float, optional

        :param snmp_usage: The network device usage by tag(s).
        :type snmp_usage: float, optional

        :param universal_service_monitoring_percentage: The percentage of universal service monitoring usage by tag(s).
        :type universal_service_monitoring_percentage: float, optional

        :param universal_service_monitoring_usage: The universal service monitoring usage by tag(s).
        :type universal_service_monitoring_usage: float, optional

        :param vuln_management_hosts_percentage: The percentage of Application Vulnerability Management usage by tag(s).
        :type vuln_management_hosts_percentage: float, optional

        :param vuln_management_hosts_usage: The Application Vulnerability Management usage by tag(s).
        :type vuln_management_hosts_usage: float, optional

        :param workflow_executions_percentage: The percentage of workflow executions usage by tag(s).
        :type workflow_executions_percentage: float, optional

        :param workflow_executions_usage: The total workflow executions usage by tag(s).
        :type workflow_executions_usage: float, optional
        """
        if api_percentage is not unset:
            kwargs["api_percentage"] = api_percentage
        if api_usage is not unset:
            kwargs["api_usage"] = api_usage
        if apm_fargate_percentage is not unset:
            kwargs["apm_fargate_percentage"] = apm_fargate_percentage
        if apm_fargate_usage is not unset:
            kwargs["apm_fargate_usage"] = apm_fargate_usage
        if apm_host_percentage is not unset:
            kwargs["apm_host_percentage"] = apm_host_percentage
        if apm_host_usage is not unset:
            kwargs["apm_host_usage"] = apm_host_usage
        if apm_usm_percentage is not unset:
            kwargs["apm_usm_percentage"] = apm_usm_percentage
        if apm_usm_usage is not unset:
            kwargs["apm_usm_usage"] = apm_usm_usage
        if appsec_fargate_percentage is not unset:
            kwargs["appsec_fargate_percentage"] = appsec_fargate_percentage
        if appsec_fargate_usage is not unset:
            kwargs["appsec_fargate_usage"] = appsec_fargate_usage
        if appsec_percentage is not unset:
            kwargs["appsec_percentage"] = appsec_percentage
        if appsec_usage is not unset:
            kwargs["appsec_usage"] = appsec_usage
        if asm_serverless_traced_invocations_percentage is not unset:
            kwargs["asm_serverless_traced_invocations_percentage"] = asm_serverless_traced_invocations_percentage
        if asm_serverless_traced_invocations_usage is not unset:
            kwargs["asm_serverless_traced_invocations_usage"] = asm_serverless_traced_invocations_usage
        if browser_percentage is not unset:
            kwargs["browser_percentage"] = browser_percentage
        if browser_usage is not unset:
            kwargs["browser_usage"] = browser_usage
        if ci_pipeline_indexed_spans_percentage is not unset:
            kwargs["ci_pipeline_indexed_spans_percentage"] = ci_pipeline_indexed_spans_percentage
        if ci_pipeline_indexed_spans_usage is not unset:
            kwargs["ci_pipeline_indexed_spans_usage"] = ci_pipeline_indexed_spans_usage
        if ci_test_indexed_spans_percentage is not unset:
            kwargs["ci_test_indexed_spans_percentage"] = ci_test_indexed_spans_percentage
        if ci_test_indexed_spans_usage is not unset:
            kwargs["ci_test_indexed_spans_usage"] = ci_test_indexed_spans_usage
        if ci_visibility_itr_percentage is not unset:
            kwargs["ci_visibility_itr_percentage"] = ci_visibility_itr_percentage
        if ci_visibility_itr_usage is not unset:
            kwargs["ci_visibility_itr_usage"] = ci_visibility_itr_usage
        if cloud_siem_percentage is not unset:
            kwargs["cloud_siem_percentage"] = cloud_siem_percentage
        if cloud_siem_usage is not unset:
            kwargs["cloud_siem_usage"] = cloud_siem_usage
        if container_excl_agent_percentage is not unset:
            kwargs["container_excl_agent_percentage"] = container_excl_agent_percentage
        if container_excl_agent_usage is not unset:
            kwargs["container_excl_agent_usage"] = container_excl_agent_usage
        if container_percentage is not unset:
            kwargs["container_percentage"] = container_percentage
        if container_usage is not unset:
            kwargs["container_usage"] = container_usage
        if cspm_containers_percentage is not unset:
            kwargs["cspm_containers_percentage"] = cspm_containers_percentage
        if cspm_containers_usage is not unset:
            kwargs["cspm_containers_usage"] = cspm_containers_usage
        if cspm_hosts_percentage is not unset:
            kwargs["cspm_hosts_percentage"] = cspm_hosts_percentage
        if cspm_hosts_usage is not unset:
            kwargs["cspm_hosts_usage"] = cspm_hosts_usage
        if custom_event_percentage is not unset:
            kwargs["custom_event_percentage"] = custom_event_percentage
        if custom_event_usage is not unset:
            kwargs["custom_event_usage"] = custom_event_usage
        if custom_ingested_timeseries_percentage is not unset:
            kwargs["custom_ingested_timeseries_percentage"] = custom_ingested_timeseries_percentage
        if custom_ingested_timeseries_usage is not unset:
            kwargs["custom_ingested_timeseries_usage"] = custom_ingested_timeseries_usage
        if custom_timeseries_percentage is not unset:
            kwargs["custom_timeseries_percentage"] = custom_timeseries_percentage
        if custom_timeseries_usage is not unset:
            kwargs["custom_timeseries_usage"] = custom_timeseries_usage
        if cws_containers_percentage is not unset:
            kwargs["cws_containers_percentage"] = cws_containers_percentage
        if cws_containers_usage is not unset:
            kwargs["cws_containers_usage"] = cws_containers_usage
        if cws_hosts_percentage is not unset:
            kwargs["cws_hosts_percentage"] = cws_hosts_percentage
        if cws_hosts_usage is not unset:
            kwargs["cws_hosts_usage"] = cws_hosts_usage
        if dbm_hosts_percentage is not unset:
            kwargs["dbm_hosts_percentage"] = dbm_hosts_percentage
        if dbm_hosts_usage is not unset:
            kwargs["dbm_hosts_usage"] = dbm_hosts_usage
        if dbm_queries_percentage is not unset:
            kwargs["dbm_queries_percentage"] = dbm_queries_percentage
        if dbm_queries_usage is not unset:
            kwargs["dbm_queries_usage"] = dbm_queries_usage
        if error_tracking_percentage is not unset:
            kwargs["error_tracking_percentage"] = error_tracking_percentage
        if error_tracking_usage is not unset:
            kwargs["error_tracking_usage"] = error_tracking_usage
        if estimated_indexed_logs_percentage is not unset:
            kwargs["estimated_indexed_logs_percentage"] = estimated_indexed_logs_percentage
        if estimated_indexed_logs_usage is not unset:
            kwargs["estimated_indexed_logs_usage"] = estimated_indexed_logs_usage
        if estimated_indexed_spans_percentage is not unset:
            kwargs["estimated_indexed_spans_percentage"] = estimated_indexed_spans_percentage
        if estimated_indexed_spans_usage is not unset:
            kwargs["estimated_indexed_spans_usage"] = estimated_indexed_spans_usage
        if estimated_ingested_logs_percentage is not unset:
            kwargs["estimated_ingested_logs_percentage"] = estimated_ingested_logs_percentage
        if estimated_ingested_logs_usage is not unset:
            kwargs["estimated_ingested_logs_usage"] = estimated_ingested_logs_usage
        if estimated_ingested_spans_percentage is not unset:
            kwargs["estimated_ingested_spans_percentage"] = estimated_ingested_spans_percentage
        if estimated_ingested_spans_usage is not unset:
            kwargs["estimated_ingested_spans_usage"] = estimated_ingested_spans_usage
        if estimated_rum_sessions_percentage is not unset:
            kwargs["estimated_rum_sessions_percentage"] = estimated_rum_sessions_percentage
        if estimated_rum_sessions_usage is not unset:
            kwargs["estimated_rum_sessions_usage"] = estimated_rum_sessions_usage
        if fargate_percentage is not unset:
            kwargs["fargate_percentage"] = fargate_percentage
        if fargate_usage is not unset:
            kwargs["fargate_usage"] = fargate_usage
        if functions_percentage is not unset:
            kwargs["functions_percentage"] = functions_percentage
        if functions_usage is not unset:
            kwargs["functions_usage"] = functions_usage
        if incident_management_monthly_active_users_percentage is not unset:
            kwargs[
                "incident_management_monthly_active_users_percentage"
            ] = incident_management_monthly_active_users_percentage
        if incident_management_monthly_active_users_usage is not unset:
            kwargs["incident_management_monthly_active_users_usage"] = incident_management_monthly_active_users_usage
        if indexed_spans_percentage is not unset:
            kwargs["indexed_spans_percentage"] = indexed_spans_percentage
        if indexed_spans_usage is not unset:
            kwargs["indexed_spans_usage"] = indexed_spans_usage
        if infra_host_percentage is not unset:
            kwargs["infra_host_percentage"] = infra_host_percentage
        if infra_host_usage is not unset:
            kwargs["infra_host_usage"] = infra_host_usage
        if ingested_logs_bytes_percentage is not unset:
            kwargs["ingested_logs_bytes_percentage"] = ingested_logs_bytes_percentage
        if ingested_logs_bytes_usage is not unset:
            kwargs["ingested_logs_bytes_usage"] = ingested_logs_bytes_usage
        if ingested_spans_bytes_percentage is not unset:
            kwargs["ingested_spans_bytes_percentage"] = ingested_spans_bytes_percentage
        if ingested_spans_bytes_usage is not unset:
            kwargs["ingested_spans_bytes_usage"] = ingested_spans_bytes_usage
        if invocations_percentage is not unset:
            kwargs["invocations_percentage"] = invocations_percentage
        if invocations_usage is not unset:
            kwargs["invocations_usage"] = invocations_usage
        if lambda_traced_invocations_percentage is not unset:
            kwargs["lambda_traced_invocations_percentage"] = lambda_traced_invocations_percentage
        if lambda_traced_invocations_usage is not unset:
            kwargs["lambda_traced_invocations_usage"] = lambda_traced_invocations_usage
        if logs_indexed_15day_percentage is not unset:
            kwargs["logs_indexed_15day_percentage"] = logs_indexed_15day_percentage
        if logs_indexed_15day_usage is not unset:
            kwargs["logs_indexed_15day_usage"] = logs_indexed_15day_usage
        if logs_indexed_180day_percentage is not unset:
            kwargs["logs_indexed_180day_percentage"] = logs_indexed_180day_percentage
        if logs_indexed_180day_usage is not unset:
            kwargs["logs_indexed_180day_usage"] = logs_indexed_180day_usage
        if logs_indexed_1day_percentage is not unset:
            kwargs["logs_indexed_1day_percentage"] = logs_indexed_1day_percentage
        if logs_indexed_1day_usage is not unset:
            kwargs["logs_indexed_1day_usage"] = logs_indexed_1day_usage
        if logs_indexed_30day_percentage is not unset:
            kwargs["logs_indexed_30day_percentage"] = logs_indexed_30day_percentage
        if logs_indexed_30day_usage is not unset:
            kwargs["logs_indexed_30day_usage"] = logs_indexed_30day_usage
        if logs_indexed_360day_percentage is not unset:
            kwargs["logs_indexed_360day_percentage"] = logs_indexed_360day_percentage
        if logs_indexed_360day_usage is not unset:
            kwargs["logs_indexed_360day_usage"] = logs_indexed_360day_usage
        if logs_indexed_3day_percentage is not unset:
            kwargs["logs_indexed_3day_percentage"] = logs_indexed_3day_percentage
        if logs_indexed_3day_usage is not unset:
            kwargs["logs_indexed_3day_usage"] = logs_indexed_3day_usage
        if logs_indexed_45day_percentage is not unset:
            kwargs["logs_indexed_45day_percentage"] = logs_indexed_45day_percentage
        if logs_indexed_45day_usage is not unset:
            kwargs["logs_indexed_45day_usage"] = logs_indexed_45day_usage
        if logs_indexed_60day_percentage is not unset:
            kwargs["logs_indexed_60day_percentage"] = logs_indexed_60day_percentage
        if logs_indexed_60day_usage is not unset:
            kwargs["logs_indexed_60day_usage"] = logs_indexed_60day_usage
        if logs_indexed_7day_percentage is not unset:
            kwargs["logs_indexed_7day_percentage"] = logs_indexed_7day_percentage
        if logs_indexed_7day_usage is not unset:
            kwargs["logs_indexed_7day_usage"] = logs_indexed_7day_usage
        if logs_indexed_90day_percentage is not unset:
            kwargs["logs_indexed_90day_percentage"] = logs_indexed_90day_percentage
        if logs_indexed_90day_usage is not unset:
            kwargs["logs_indexed_90day_usage"] = logs_indexed_90day_usage
        if logs_indexed_custom_retention_percentage is not unset:
            kwargs["logs_indexed_custom_retention_percentage"] = logs_indexed_custom_retention_percentage
        if logs_indexed_custom_retention_usage is not unset:
            kwargs["logs_indexed_custom_retention_usage"] = logs_indexed_custom_retention_usage
        if mobile_app_testing_percentage is not unset:
            kwargs["mobile_app_testing_percentage"] = mobile_app_testing_percentage
        if mobile_app_testing_usage is not unset:
            kwargs["mobile_app_testing_usage"] = mobile_app_testing_usage
        if ndm_netflow_percentage is not unset:
            kwargs["ndm_netflow_percentage"] = ndm_netflow_percentage
        if ndm_netflow_usage is not unset:
            kwargs["ndm_netflow_usage"] = ndm_netflow_usage
        if npm_host_percentage is not unset:
            kwargs["npm_host_percentage"] = npm_host_percentage
        if npm_host_usage is not unset:
            kwargs["npm_host_usage"] = npm_host_usage
        if obs_pipeline_bytes_percentage is not unset:
            kwargs["obs_pipeline_bytes_percentage"] = obs_pipeline_bytes_percentage
        if obs_pipeline_bytes_usage is not unset:
            kwargs["obs_pipeline_bytes_usage"] = obs_pipeline_bytes_usage
        if obs_pipelines_vcpu_percentage is not unset:
            kwargs["obs_pipelines_vcpu_percentage"] = obs_pipelines_vcpu_percentage
        if obs_pipelines_vcpu_usage is not unset:
            kwargs["obs_pipelines_vcpu_usage"] = obs_pipelines_vcpu_usage
        if online_archive_percentage is not unset:
            kwargs["online_archive_percentage"] = online_archive_percentage
        if online_archive_usage is not unset:
            kwargs["online_archive_usage"] = online_archive_usage
        if profiled_container_percentage is not unset:
            kwargs["profiled_container_percentage"] = profiled_container_percentage
        if profiled_container_usage is not unset:
            kwargs["profiled_container_usage"] = profiled_container_usage
        if profiled_fargate_percentage is not unset:
            kwargs["profiled_fargate_percentage"] = profiled_fargate_percentage
        if profiled_fargate_usage is not unset:
            kwargs["profiled_fargate_usage"] = profiled_fargate_usage
        if profiled_host_percentage is not unset:
            kwargs["profiled_host_percentage"] = profiled_host_percentage
        if profiled_host_usage is not unset:
            kwargs["profiled_host_usage"] = profiled_host_usage
        if rum_browser_mobile_sessions_percentage is not unset:
            kwargs["rum_browser_mobile_sessions_percentage"] = rum_browser_mobile_sessions_percentage
        if rum_browser_mobile_sessions_usage is not unset:
            kwargs["rum_browser_mobile_sessions_usage"] = rum_browser_mobile_sessions_usage
        if rum_replay_sessions_percentage is not unset:
            kwargs["rum_replay_sessions_percentage"] = rum_replay_sessions_percentage
        if rum_replay_sessions_usage is not unset:
            kwargs["rum_replay_sessions_usage"] = rum_replay_sessions_usage
        if sds_scanned_bytes_percentage is not unset:
            kwargs["sds_scanned_bytes_percentage"] = sds_scanned_bytes_percentage
        if sds_scanned_bytes_usage is not unset:
            kwargs["sds_scanned_bytes_usage"] = sds_scanned_bytes_usage
        if serverless_apps_percentage is not unset:
            kwargs["serverless_apps_percentage"] = serverless_apps_percentage
        if serverless_apps_usage is not unset:
            kwargs["serverless_apps_usage"] = serverless_apps_usage
        if siem_ingested_bytes_percentage is not unset:
            kwargs["siem_ingested_bytes_percentage"] = siem_ingested_bytes_percentage
        if siem_ingested_bytes_usage is not unset:
            kwargs["siem_ingested_bytes_usage"] = siem_ingested_bytes_usage
        if snmp_percentage is not unset:
            kwargs["snmp_percentage"] = snmp_percentage
        if snmp_usage is not unset:
            kwargs["snmp_usage"] = snmp_usage
        if universal_service_monitoring_percentage is not unset:
            kwargs["universal_service_monitoring_percentage"] = universal_service_monitoring_percentage
        if universal_service_monitoring_usage is not unset:
            kwargs["universal_service_monitoring_usage"] = universal_service_monitoring_usage
        if vuln_management_hosts_percentage is not unset:
            kwargs["vuln_management_hosts_percentage"] = vuln_management_hosts_percentage
        if vuln_management_hosts_usage is not unset:
            kwargs["vuln_management_hosts_usage"] = vuln_management_hosts_usage
        if workflow_executions_percentage is not unset:
            kwargs["workflow_executions_percentage"] = workflow_executions_percentage
        if workflow_executions_usage is not unset:
            kwargs["workflow_executions_usage"] = workflow_executions_usage
        super().__init__(kwargs)
