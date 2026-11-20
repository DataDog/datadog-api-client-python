# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventPlatformStreamDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["logs_stream", "audit_stream", "trace_stream", "errors_stream", "event_stream", "rum_stream", "ci_pipeline_stream", "ci_test_stream", "ci_gate_stream", "ci_code_scan_stream", "ci_dependency_stream", "deployment_stream", "recommendations_stream", "synthetics_batch_stream", "synthetics_test_runs_stream", "observability_pipelines_stream", "security_runtime_stream", "security_signals_stream", "product_analytics_stream", "app_sec_span_stream", "app_sec_entities_stream", "compliance_event_stream", "compliance_findings_stream", "security_findings_stream", "supply_chain_firewall_report_stream", "data_observability_stream", "database_query_stream", "database_raw_query_stream", "deployment_gates_stream", "llm_observability_stream", "network_device_flow_stream", "network_flow_stream", "network_path_stream", "on_call_events_stream", "profile_stream", "security_dump_stream", "security_historical_results_stream", "session_replay_stream", "software_inventory_stream", "critical_asset_stream"].
    :type value: str
    """

    allowed_values = {
        "logs_stream",
        "audit_stream",
        "trace_stream",
        "errors_stream",
        "event_stream",
        "rum_stream",
        "ci_pipeline_stream",
        "ci_test_stream",
        "ci_gate_stream",
        "ci_code_scan_stream",
        "ci_dependency_stream",
        "deployment_stream",
        "recommendations_stream",
        "synthetics_batch_stream",
        "synthetics_test_runs_stream",
        "observability_pipelines_stream",
        "security_runtime_stream",
        "security_signals_stream",
        "product_analytics_stream",
        "app_sec_span_stream",
        "app_sec_entities_stream",
        "compliance_event_stream",
        "compliance_findings_stream",
        "security_findings_stream",
        "supply_chain_firewall_report_stream",
        "data_observability_stream",
        "database_query_stream",
        "database_raw_query_stream",
        "deployment_gates_stream",
        "llm_observability_stream",
        "network_device_flow_stream",
        "network_flow_stream",
        "network_path_stream",
        "on_call_events_stream",
        "profile_stream",
        "security_dump_stream",
        "security_historical_results_stream",
        "session_replay_stream",
        "software_inventory_stream",
        "critical_asset_stream",
    }
    LOGS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    AUDIT_STREAM: ClassVar["EventPlatformStreamDataSource"]
    TRACE_STREAM: ClassVar["EventPlatformStreamDataSource"]
    ERRORS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    EVENT_STREAM: ClassVar["EventPlatformStreamDataSource"]
    RUM_STREAM: ClassVar["EventPlatformStreamDataSource"]
    CI_PIPELINE_STREAM: ClassVar["EventPlatformStreamDataSource"]
    CI_TEST_STREAM: ClassVar["EventPlatformStreamDataSource"]
    CI_GATE_STREAM: ClassVar["EventPlatformStreamDataSource"]
    CI_CODE_SCAN_STREAM: ClassVar["EventPlatformStreamDataSource"]
    CI_DEPENDENCY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    DEPLOYMENT_STREAM: ClassVar["EventPlatformStreamDataSource"]
    RECOMMENDATIONS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SYNTHETICS_BATCH_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SYNTHETICS_TEST_RUNS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    OBSERVABILITY_PIPELINES_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SECURITY_RUNTIME_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SECURITY_SIGNALS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    PRODUCT_ANALYTICS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    APP_SEC_SPAN_STREAM: ClassVar["EventPlatformStreamDataSource"]
    APP_SEC_ENTITIES_STREAM: ClassVar["EventPlatformStreamDataSource"]
    COMPLIANCE_EVENT_STREAM: ClassVar["EventPlatformStreamDataSource"]
    COMPLIANCE_FINDINGS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SECURITY_FINDINGS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SUPPLY_CHAIN_FIREWALL_REPORT_STREAM: ClassVar["EventPlatformStreamDataSource"]
    DATA_OBSERVABILITY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    DATABASE_QUERY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    DATABASE_RAW_QUERY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    DEPLOYMENT_GATES_STREAM: ClassVar["EventPlatformStreamDataSource"]
    LLM_OBSERVABILITY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    NETWORK_DEVICE_FLOW_STREAM: ClassVar["EventPlatformStreamDataSource"]
    NETWORK_FLOW_STREAM: ClassVar["EventPlatformStreamDataSource"]
    NETWORK_PATH_STREAM: ClassVar["EventPlatformStreamDataSource"]
    ON_CALL_EVENTS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    PROFILE_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SECURITY_DUMP_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SECURITY_HISTORICAL_RESULTS_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SESSION_REPLAY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    SOFTWARE_INVENTORY_STREAM: ClassVar["EventPlatformStreamDataSource"]
    CRITICAL_ASSET_STREAM: ClassVar["EventPlatformStreamDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventPlatformStreamDataSource.LOGS_STREAM = EventPlatformStreamDataSource("logs_stream")
EventPlatformStreamDataSource.AUDIT_STREAM = EventPlatformStreamDataSource("audit_stream")
EventPlatformStreamDataSource.TRACE_STREAM = EventPlatformStreamDataSource("trace_stream")
EventPlatformStreamDataSource.ERRORS_STREAM = EventPlatformStreamDataSource("errors_stream")
EventPlatformStreamDataSource.EVENT_STREAM = EventPlatformStreamDataSource("event_stream")
EventPlatformStreamDataSource.RUM_STREAM = EventPlatformStreamDataSource("rum_stream")
EventPlatformStreamDataSource.CI_PIPELINE_STREAM = EventPlatformStreamDataSource("ci_pipeline_stream")
EventPlatformStreamDataSource.CI_TEST_STREAM = EventPlatformStreamDataSource("ci_test_stream")
EventPlatformStreamDataSource.CI_GATE_STREAM = EventPlatformStreamDataSource("ci_gate_stream")
EventPlatformStreamDataSource.CI_CODE_SCAN_STREAM = EventPlatformStreamDataSource("ci_code_scan_stream")
EventPlatformStreamDataSource.CI_DEPENDENCY_STREAM = EventPlatformStreamDataSource("ci_dependency_stream")
EventPlatformStreamDataSource.DEPLOYMENT_STREAM = EventPlatformStreamDataSource("deployment_stream")
EventPlatformStreamDataSource.RECOMMENDATIONS_STREAM = EventPlatformStreamDataSource("recommendations_stream")
EventPlatformStreamDataSource.SYNTHETICS_BATCH_STREAM = EventPlatformStreamDataSource("synthetics_batch_stream")
EventPlatformStreamDataSource.SYNTHETICS_TEST_RUNS_STREAM = EventPlatformStreamDataSource("synthetics_test_runs_stream")
EventPlatformStreamDataSource.OBSERVABILITY_PIPELINES_STREAM = EventPlatformStreamDataSource(
    "observability_pipelines_stream"
)
EventPlatformStreamDataSource.SECURITY_RUNTIME_STREAM = EventPlatformStreamDataSource("security_runtime_stream")
EventPlatformStreamDataSource.SECURITY_SIGNALS_STREAM = EventPlatformStreamDataSource("security_signals_stream")
EventPlatformStreamDataSource.PRODUCT_ANALYTICS_STREAM = EventPlatformStreamDataSource("product_analytics_stream")
EventPlatformStreamDataSource.APP_SEC_SPAN_STREAM = EventPlatformStreamDataSource("app_sec_span_stream")
EventPlatformStreamDataSource.APP_SEC_ENTITIES_STREAM = EventPlatformStreamDataSource("app_sec_entities_stream")
EventPlatformStreamDataSource.COMPLIANCE_EVENT_STREAM = EventPlatformStreamDataSource("compliance_event_stream")
EventPlatformStreamDataSource.COMPLIANCE_FINDINGS_STREAM = EventPlatformStreamDataSource("compliance_findings_stream")
EventPlatformStreamDataSource.SECURITY_FINDINGS_STREAM = EventPlatformStreamDataSource("security_findings_stream")
EventPlatformStreamDataSource.SUPPLY_CHAIN_FIREWALL_REPORT_STREAM = EventPlatformStreamDataSource(
    "supply_chain_firewall_report_stream"
)
EventPlatformStreamDataSource.DATA_OBSERVABILITY_STREAM = EventPlatformStreamDataSource("data_observability_stream")
EventPlatformStreamDataSource.DATABASE_QUERY_STREAM = EventPlatformStreamDataSource("database_query_stream")
EventPlatformStreamDataSource.DATABASE_RAW_QUERY_STREAM = EventPlatformStreamDataSource("database_raw_query_stream")
EventPlatformStreamDataSource.DEPLOYMENT_GATES_STREAM = EventPlatformStreamDataSource("deployment_gates_stream")
EventPlatformStreamDataSource.LLM_OBSERVABILITY_STREAM = EventPlatformStreamDataSource("llm_observability_stream")
EventPlatformStreamDataSource.NETWORK_DEVICE_FLOW_STREAM = EventPlatformStreamDataSource("network_device_flow_stream")
EventPlatformStreamDataSource.NETWORK_FLOW_STREAM = EventPlatformStreamDataSource("network_flow_stream")
EventPlatformStreamDataSource.NETWORK_PATH_STREAM = EventPlatformStreamDataSource("network_path_stream")
EventPlatformStreamDataSource.ON_CALL_EVENTS_STREAM = EventPlatformStreamDataSource("on_call_events_stream")
EventPlatformStreamDataSource.PROFILE_STREAM = EventPlatformStreamDataSource("profile_stream")
EventPlatformStreamDataSource.SECURITY_DUMP_STREAM = EventPlatformStreamDataSource("security_dump_stream")
EventPlatformStreamDataSource.SECURITY_HISTORICAL_RESULTS_STREAM = EventPlatformStreamDataSource(
    "security_historical_results_stream"
)
EventPlatformStreamDataSource.SESSION_REPLAY_STREAM = EventPlatformStreamDataSource("session_replay_stream")
EventPlatformStreamDataSource.SOFTWARE_INVENTORY_STREAM = EventPlatformStreamDataSource("software_inventory_stream")
EventPlatformStreamDataSource.CRITICAL_ASSET_STREAM = EventPlatformStreamDataSource("critical_asset_stream")
