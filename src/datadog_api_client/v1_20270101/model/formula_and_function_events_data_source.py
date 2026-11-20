# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionEventsDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["events", "logs", "rum", "synthetics_test_runs", "product_analytics", "network", "profiles", "network_device_flows", "recommendations", "security_findings", "security_signals", "ci_pipelines", "database_queries", "llm_observability", "ai_usage", "audit", "ci_tests", "errors", "spans", "security_runtime", "app_sec_spans", "app_sec_entities", "bits_ai_investigations", "ci_code_scan", "ci_dependencies", "ci_gates", "ci_coverage_reports", "data_observability_events", "dora_metrics", "compliance_findings", "deployments", "deployment_gates", "exposures", "flag_evaluations", "network_path", "observability_pipelines", "on_call_events", "orchestration_troubleshooting", "security_historical_results", "security_info", "software_inventory", "synthetics_batches", "synthetics_map", "replay", "behavior"].
    :type value: str
    """

    allowed_values = {
        "events",
        "logs",
        "rum",
        "synthetics_test_runs",
        "product_analytics",
        "network",
        "profiles",
        "network_device_flows",
        "recommendations",
        "security_findings",
        "security_signals",
        "ci_pipelines",
        "database_queries",
        "llm_observability",
        "ai_usage",
        "audit",
        "ci_tests",
        "errors",
        "spans",
        "security_runtime",
        "app_sec_spans",
        "app_sec_entities",
        "bits_ai_investigations",
        "ci_code_scan",
        "ci_dependencies",
        "ci_gates",
        "ci_coverage_reports",
        "data_observability_events",
        "dora_metrics",
        "compliance_findings",
        "deployments",
        "deployment_gates",
        "exposures",
        "flag_evaluations",
        "network_path",
        "observability_pipelines",
        "on_call_events",
        "orchestration_troubleshooting",
        "security_historical_results",
        "security_info",
        "software_inventory",
        "synthetics_batches",
        "synthetics_map",
        "replay",
        "behavior",
    }
    EVENTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    LOGS: ClassVar["FormulaAndFunctionEventsDataSource"]
    RUM: ClassVar["FormulaAndFunctionEventsDataSource"]
    SYNTHETICS_TEST_RUNS: ClassVar["FormulaAndFunctionEventsDataSource"]
    PRODUCT_ANALYTICS: ClassVar["FormulaAndFunctionEventsDataSource"]
    NETWORK: ClassVar["FormulaAndFunctionEventsDataSource"]
    PROFILES: ClassVar["FormulaAndFunctionEventsDataSource"]
    NETWORK_DEVICE_FLOWS: ClassVar["FormulaAndFunctionEventsDataSource"]
    RECOMMENDATIONS: ClassVar["FormulaAndFunctionEventsDataSource"]
    SECURITY_FINDINGS: ClassVar["FormulaAndFunctionEventsDataSource"]
    SECURITY_SIGNALS: ClassVar["FormulaAndFunctionEventsDataSource"]
    CI_PIPELINES: ClassVar["FormulaAndFunctionEventsDataSource"]
    DATABASE_QUERIES: ClassVar["FormulaAndFunctionEventsDataSource"]
    LLM_OBSERVABILITY: ClassVar["FormulaAndFunctionEventsDataSource"]
    AI_USAGE: ClassVar["FormulaAndFunctionEventsDataSource"]
    AUDIT: ClassVar["FormulaAndFunctionEventsDataSource"]
    CI_TESTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    ERRORS: ClassVar["FormulaAndFunctionEventsDataSource"]
    SPANS: ClassVar["FormulaAndFunctionEventsDataSource"]
    SECURITY_RUNTIME: ClassVar["FormulaAndFunctionEventsDataSource"]
    APP_SEC_SPANS: ClassVar["FormulaAndFunctionEventsDataSource"]
    APP_SEC_ENTITIES: ClassVar["FormulaAndFunctionEventsDataSource"]
    BITS_AI_INVESTIGATIONS: ClassVar["FormulaAndFunctionEventsDataSource"]
    CI_CODE_SCAN: ClassVar["FormulaAndFunctionEventsDataSource"]
    CI_DEPENDENCIES: ClassVar["FormulaAndFunctionEventsDataSource"]
    CI_GATES: ClassVar["FormulaAndFunctionEventsDataSource"]
    CI_COVERAGE_REPORTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    DATA_OBSERVABILITY_EVENTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    DORA_METRICS: ClassVar["FormulaAndFunctionEventsDataSource"]
    COMPLIANCE_FINDINGS: ClassVar["FormulaAndFunctionEventsDataSource"]
    DEPLOYMENTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    DEPLOYMENT_GATES: ClassVar["FormulaAndFunctionEventsDataSource"]
    EXPOSURES: ClassVar["FormulaAndFunctionEventsDataSource"]
    FLAG_EVALUATIONS: ClassVar["FormulaAndFunctionEventsDataSource"]
    NETWORK_PATH: ClassVar["FormulaAndFunctionEventsDataSource"]
    OBSERVABILITY_PIPELINES: ClassVar["FormulaAndFunctionEventsDataSource"]
    ON_CALL_EVENTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    ORCHESTRATION_TROUBLESHOOTING: ClassVar["FormulaAndFunctionEventsDataSource"]
    SECURITY_HISTORICAL_RESULTS: ClassVar["FormulaAndFunctionEventsDataSource"]
    SECURITY_INFO: ClassVar["FormulaAndFunctionEventsDataSource"]
    SOFTWARE_INVENTORY: ClassVar["FormulaAndFunctionEventsDataSource"]
    SYNTHETICS_BATCHES: ClassVar["FormulaAndFunctionEventsDataSource"]
    SYNTHETICS_MAP: ClassVar["FormulaAndFunctionEventsDataSource"]
    REPLAY: ClassVar["FormulaAndFunctionEventsDataSource"]
    BEHAVIOR: ClassVar["FormulaAndFunctionEventsDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionEventsDataSource.EVENTS = FormulaAndFunctionEventsDataSource("events")
FormulaAndFunctionEventsDataSource.LOGS = FormulaAndFunctionEventsDataSource("logs")
FormulaAndFunctionEventsDataSource.RUM = FormulaAndFunctionEventsDataSource("rum")
FormulaAndFunctionEventsDataSource.SYNTHETICS_TEST_RUNS = FormulaAndFunctionEventsDataSource("synthetics_test_runs")
FormulaAndFunctionEventsDataSource.PRODUCT_ANALYTICS = FormulaAndFunctionEventsDataSource("product_analytics")
FormulaAndFunctionEventsDataSource.NETWORK = FormulaAndFunctionEventsDataSource("network")
FormulaAndFunctionEventsDataSource.PROFILES = FormulaAndFunctionEventsDataSource("profiles")
FormulaAndFunctionEventsDataSource.NETWORK_DEVICE_FLOWS = FormulaAndFunctionEventsDataSource("network_device_flows")
FormulaAndFunctionEventsDataSource.RECOMMENDATIONS = FormulaAndFunctionEventsDataSource("recommendations")
FormulaAndFunctionEventsDataSource.SECURITY_FINDINGS = FormulaAndFunctionEventsDataSource("security_findings")
FormulaAndFunctionEventsDataSource.SECURITY_SIGNALS = FormulaAndFunctionEventsDataSource("security_signals")
FormulaAndFunctionEventsDataSource.CI_PIPELINES = FormulaAndFunctionEventsDataSource("ci_pipelines")
FormulaAndFunctionEventsDataSource.DATABASE_QUERIES = FormulaAndFunctionEventsDataSource("database_queries")
FormulaAndFunctionEventsDataSource.LLM_OBSERVABILITY = FormulaAndFunctionEventsDataSource("llm_observability")
FormulaAndFunctionEventsDataSource.AI_USAGE = FormulaAndFunctionEventsDataSource("ai_usage")
FormulaAndFunctionEventsDataSource.AUDIT = FormulaAndFunctionEventsDataSource("audit")
FormulaAndFunctionEventsDataSource.CI_TESTS = FormulaAndFunctionEventsDataSource("ci_tests")
FormulaAndFunctionEventsDataSource.ERRORS = FormulaAndFunctionEventsDataSource("errors")
FormulaAndFunctionEventsDataSource.SPANS = FormulaAndFunctionEventsDataSource("spans")
FormulaAndFunctionEventsDataSource.SECURITY_RUNTIME = FormulaAndFunctionEventsDataSource("security_runtime")
FormulaAndFunctionEventsDataSource.APP_SEC_SPANS = FormulaAndFunctionEventsDataSource("app_sec_spans")
FormulaAndFunctionEventsDataSource.APP_SEC_ENTITIES = FormulaAndFunctionEventsDataSource("app_sec_entities")
FormulaAndFunctionEventsDataSource.BITS_AI_INVESTIGATIONS = FormulaAndFunctionEventsDataSource("bits_ai_investigations")
FormulaAndFunctionEventsDataSource.CI_CODE_SCAN = FormulaAndFunctionEventsDataSource("ci_code_scan")
FormulaAndFunctionEventsDataSource.CI_DEPENDENCIES = FormulaAndFunctionEventsDataSource("ci_dependencies")
FormulaAndFunctionEventsDataSource.CI_GATES = FormulaAndFunctionEventsDataSource("ci_gates")
FormulaAndFunctionEventsDataSource.CI_COVERAGE_REPORTS = FormulaAndFunctionEventsDataSource("ci_coverage_reports")
FormulaAndFunctionEventsDataSource.DATA_OBSERVABILITY_EVENTS = FormulaAndFunctionEventsDataSource(
    "data_observability_events"
)
FormulaAndFunctionEventsDataSource.DORA_METRICS = FormulaAndFunctionEventsDataSource("dora_metrics")
FormulaAndFunctionEventsDataSource.COMPLIANCE_FINDINGS = FormulaAndFunctionEventsDataSource("compliance_findings")
FormulaAndFunctionEventsDataSource.DEPLOYMENTS = FormulaAndFunctionEventsDataSource("deployments")
FormulaAndFunctionEventsDataSource.DEPLOYMENT_GATES = FormulaAndFunctionEventsDataSource("deployment_gates")
FormulaAndFunctionEventsDataSource.EXPOSURES = FormulaAndFunctionEventsDataSource("exposures")
FormulaAndFunctionEventsDataSource.FLAG_EVALUATIONS = FormulaAndFunctionEventsDataSource("flag_evaluations")
FormulaAndFunctionEventsDataSource.NETWORK_PATH = FormulaAndFunctionEventsDataSource("network_path")
FormulaAndFunctionEventsDataSource.OBSERVABILITY_PIPELINES = FormulaAndFunctionEventsDataSource(
    "observability_pipelines"
)
FormulaAndFunctionEventsDataSource.ON_CALL_EVENTS = FormulaAndFunctionEventsDataSource("on_call_events")
FormulaAndFunctionEventsDataSource.ORCHESTRATION_TROUBLESHOOTING = FormulaAndFunctionEventsDataSource(
    "orchestration_troubleshooting"
)
FormulaAndFunctionEventsDataSource.SECURITY_HISTORICAL_RESULTS = FormulaAndFunctionEventsDataSource(
    "security_historical_results"
)
FormulaAndFunctionEventsDataSource.SECURITY_INFO = FormulaAndFunctionEventsDataSource("security_info")
FormulaAndFunctionEventsDataSource.SOFTWARE_INVENTORY = FormulaAndFunctionEventsDataSource("software_inventory")
FormulaAndFunctionEventsDataSource.SYNTHETICS_BATCHES = FormulaAndFunctionEventsDataSource("synthetics_batches")
FormulaAndFunctionEventsDataSource.SYNTHETICS_MAP = FormulaAndFunctionEventsDataSource("synthetics_map")
FormulaAndFunctionEventsDataSource.REPLAY = FormulaAndFunctionEventsDataSource("replay")
FormulaAndFunctionEventsDataSource.BEHAVIOR = FormulaAndFunctionEventsDataSource("behavior")
