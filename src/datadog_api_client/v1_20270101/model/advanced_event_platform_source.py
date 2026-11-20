# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AdvancedEventPlatformSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["events", "logs", "rum", "synthetics_test_runs", "product_analytics", "network", "network_device_flows", "security_findings", "security_signals", "ci_pipelines", "database_queries", "llm_observability", "ai_usage", "audit", "ci_tests", "errors", "monitors", "monitor_groups", "spans", "security_runtime", "synthetics_matches"].
    :type value: str
    """

    allowed_values = {
        "events",
        "logs",
        "rum",
        "synthetics_test_runs",
        "product_analytics",
        "network",
        "network_device_flows",
        "security_findings",
        "security_signals",
        "ci_pipelines",
        "database_queries",
        "llm_observability",
        "ai_usage",
        "audit",
        "ci_tests",
        "errors",
        "monitors",
        "monitor_groups",
        "spans",
        "security_runtime",
        "synthetics_matches",
    }
    EVENTS: ClassVar["AdvancedEventPlatformSource"]
    LOGS: ClassVar["AdvancedEventPlatformSource"]
    RUM: ClassVar["AdvancedEventPlatformSource"]
    SYNTHETICS_TEST_RUNS: ClassVar["AdvancedEventPlatformSource"]
    PRODUCT_ANALYTICS: ClassVar["AdvancedEventPlatformSource"]
    NETWORK: ClassVar["AdvancedEventPlatformSource"]
    NETWORK_DEVICE_FLOWS: ClassVar["AdvancedEventPlatformSource"]
    SECURITY_FINDINGS: ClassVar["AdvancedEventPlatformSource"]
    SECURITY_SIGNALS: ClassVar["AdvancedEventPlatformSource"]
    CI_PIPELINES: ClassVar["AdvancedEventPlatformSource"]
    DATABASE_QUERIES: ClassVar["AdvancedEventPlatformSource"]
    LLM_OBSERVABILITY: ClassVar["AdvancedEventPlatformSource"]
    AI_USAGE: ClassVar["AdvancedEventPlatformSource"]
    AUDIT: ClassVar["AdvancedEventPlatformSource"]
    CI_TESTS: ClassVar["AdvancedEventPlatformSource"]
    ERRORS: ClassVar["AdvancedEventPlatformSource"]
    MONITORS: ClassVar["AdvancedEventPlatformSource"]
    MONITOR_GROUPS: ClassVar["AdvancedEventPlatformSource"]
    SPANS: ClassVar["AdvancedEventPlatformSource"]
    SECURITY_RUNTIME: ClassVar["AdvancedEventPlatformSource"]
    SYNTHETICS_MATCHES: ClassVar["AdvancedEventPlatformSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AdvancedEventPlatformSource.EVENTS = AdvancedEventPlatformSource("events")
AdvancedEventPlatformSource.LOGS = AdvancedEventPlatformSource("logs")
AdvancedEventPlatformSource.RUM = AdvancedEventPlatformSource("rum")
AdvancedEventPlatformSource.SYNTHETICS_TEST_RUNS = AdvancedEventPlatformSource("synthetics_test_runs")
AdvancedEventPlatformSource.PRODUCT_ANALYTICS = AdvancedEventPlatformSource("product_analytics")
AdvancedEventPlatformSource.NETWORK = AdvancedEventPlatformSource("network")
AdvancedEventPlatformSource.NETWORK_DEVICE_FLOWS = AdvancedEventPlatformSource("network_device_flows")
AdvancedEventPlatformSource.SECURITY_FINDINGS = AdvancedEventPlatformSource("security_findings")
AdvancedEventPlatformSource.SECURITY_SIGNALS = AdvancedEventPlatformSource("security_signals")
AdvancedEventPlatformSource.CI_PIPELINES = AdvancedEventPlatformSource("ci_pipelines")
AdvancedEventPlatformSource.DATABASE_QUERIES = AdvancedEventPlatformSource("database_queries")
AdvancedEventPlatformSource.LLM_OBSERVABILITY = AdvancedEventPlatformSource("llm_observability")
AdvancedEventPlatformSource.AI_USAGE = AdvancedEventPlatformSource("ai_usage")
AdvancedEventPlatformSource.AUDIT = AdvancedEventPlatformSource("audit")
AdvancedEventPlatformSource.CI_TESTS = AdvancedEventPlatformSource("ci_tests")
AdvancedEventPlatformSource.ERRORS = AdvancedEventPlatformSource("errors")
AdvancedEventPlatformSource.MONITORS = AdvancedEventPlatformSource("monitors")
AdvancedEventPlatformSource.MONITOR_GROUPS = AdvancedEventPlatformSource("monitor_groups")
AdvancedEventPlatformSource.SPANS = AdvancedEventPlatformSource("spans")
AdvancedEventPlatformSource.SECURITY_RUNTIME = AdvancedEventPlatformSource("security_runtime")
AdvancedEventPlatformSource.SYNTHETICS_MATCHES = AdvancedEventPlatformSource("synthetics_matches")
