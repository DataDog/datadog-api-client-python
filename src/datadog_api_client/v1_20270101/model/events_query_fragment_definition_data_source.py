# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventsQueryFragmentDefinitionDataSource(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["events", "logs", "rum", "synthetics_test_runs", "product_analytics", "network_device_flows", "ci_pipelines", "database_queries", "llm_observability", "audit", "ci_tests", "spans"].
    :type value: str
    """

    allowed_values = {
        "events",
        "logs",
        "rum",
        "synthetics_test_runs",
        "product_analytics",
        "network_device_flows",
        "ci_pipelines",
        "database_queries",
        "llm_observability",
        "audit",
        "ci_tests",
        "spans",
    }
    EVENTS: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    LOGS: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    RUM: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    SYNTHETICS_TEST_RUNS: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    PRODUCT_ANALYTICS: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    NETWORK_DEVICE_FLOWS: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    CI_PIPELINES: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    DATABASE_QUERIES: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    LLM_OBSERVABILITY: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    AUDIT: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    CI_TESTS: ClassVar["EventsQueryFragmentDefinitionDataSource"]
    SPANS: ClassVar["EventsQueryFragmentDefinitionDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventsQueryFragmentDefinitionDataSource.EVENTS = EventsQueryFragmentDefinitionDataSource("events")
EventsQueryFragmentDefinitionDataSource.LOGS = EventsQueryFragmentDefinitionDataSource("logs")
EventsQueryFragmentDefinitionDataSource.RUM = EventsQueryFragmentDefinitionDataSource("rum")
EventsQueryFragmentDefinitionDataSource.SYNTHETICS_TEST_RUNS = EventsQueryFragmentDefinitionDataSource(
    "synthetics_test_runs"
)
EventsQueryFragmentDefinitionDataSource.PRODUCT_ANALYTICS = EventsQueryFragmentDefinitionDataSource("product_analytics")
EventsQueryFragmentDefinitionDataSource.NETWORK_DEVICE_FLOWS = EventsQueryFragmentDefinitionDataSource(
    "network_device_flows"
)
EventsQueryFragmentDefinitionDataSource.CI_PIPELINES = EventsQueryFragmentDefinitionDataSource("ci_pipelines")
EventsQueryFragmentDefinitionDataSource.DATABASE_QUERIES = EventsQueryFragmentDefinitionDataSource("database_queries")
EventsQueryFragmentDefinitionDataSource.LLM_OBSERVABILITY = EventsQueryFragmentDefinitionDataSource("llm_observability")
EventsQueryFragmentDefinitionDataSource.AUDIT = EventsQueryFragmentDefinitionDataSource("audit")
EventsQueryFragmentDefinitionDataSource.CI_TESTS = EventsQueryFragmentDefinitionDataSource("ci_tests")
EventsQueryFragmentDefinitionDataSource.SPANS = EventsQueryFragmentDefinitionDataSource("spans")
