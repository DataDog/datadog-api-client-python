# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LegacyFormulaBackedDataProjectionSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["events", "logs", "rum", "synthetics_test_runs", "product_analytics", "network", "network_device_flows", "security_findings", "security_signals", "ci_pipelines", "database_queries", "llm_observability", "ai_usage", "ci_tests", "errors", "spans", "security_runtime"].
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
        "ci_tests",
        "errors",
        "spans",
        "security_runtime",
    }
    EVENTS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    LOGS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    RUM: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    SYNTHETICS_TEST_RUNS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    PRODUCT_ANALYTICS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    NETWORK: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    NETWORK_DEVICE_FLOWS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    SECURITY_FINDINGS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    SECURITY_SIGNALS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    CI_PIPELINES: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    DATABASE_QUERIES: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    LLM_OBSERVABILITY: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    AI_USAGE: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    CI_TESTS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    ERRORS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    SPANS: ClassVar["LegacyFormulaBackedDataProjectionSource"]
    SECURITY_RUNTIME: ClassVar["LegacyFormulaBackedDataProjectionSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LegacyFormulaBackedDataProjectionSource.EVENTS = LegacyFormulaBackedDataProjectionSource("events")
LegacyFormulaBackedDataProjectionSource.LOGS = LegacyFormulaBackedDataProjectionSource("logs")
LegacyFormulaBackedDataProjectionSource.RUM = LegacyFormulaBackedDataProjectionSource("rum")
LegacyFormulaBackedDataProjectionSource.SYNTHETICS_TEST_RUNS = LegacyFormulaBackedDataProjectionSource(
    "synthetics_test_runs"
)
LegacyFormulaBackedDataProjectionSource.PRODUCT_ANALYTICS = LegacyFormulaBackedDataProjectionSource("product_analytics")
LegacyFormulaBackedDataProjectionSource.NETWORK = LegacyFormulaBackedDataProjectionSource("network")
LegacyFormulaBackedDataProjectionSource.NETWORK_DEVICE_FLOWS = LegacyFormulaBackedDataProjectionSource(
    "network_device_flows"
)
LegacyFormulaBackedDataProjectionSource.SECURITY_FINDINGS = LegacyFormulaBackedDataProjectionSource("security_findings")
LegacyFormulaBackedDataProjectionSource.SECURITY_SIGNALS = LegacyFormulaBackedDataProjectionSource("security_signals")
LegacyFormulaBackedDataProjectionSource.CI_PIPELINES = LegacyFormulaBackedDataProjectionSource("ci_pipelines")
LegacyFormulaBackedDataProjectionSource.DATABASE_QUERIES = LegacyFormulaBackedDataProjectionSource("database_queries")
LegacyFormulaBackedDataProjectionSource.LLM_OBSERVABILITY = LegacyFormulaBackedDataProjectionSource("llm_observability")
LegacyFormulaBackedDataProjectionSource.AI_USAGE = LegacyFormulaBackedDataProjectionSource("ai_usage")
LegacyFormulaBackedDataProjectionSource.CI_TESTS = LegacyFormulaBackedDataProjectionSource("ci_tests")
LegacyFormulaBackedDataProjectionSource.ERRORS = LegacyFormulaBackedDataProjectionSource("errors")
LegacyFormulaBackedDataProjectionSource.SPANS = LegacyFormulaBackedDataProjectionSource("spans")
LegacyFormulaBackedDataProjectionSource.SECURITY_RUNTIME = LegacyFormulaBackedDataProjectionSource("security_runtime")
