# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventsDataSource(ModelSimple):
    """
    A data source that is powered by the Events Platform.

    :param value: If omitted defaults to "logs". Must be one of ["logs", "spans", "network", "rum", "security_signals", "profiles", "audit", "events", "ci_tests", "ci_pipelines", "incident_analytics", "product_analytics", "on_call_events", "dora"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "spans",
        "network",
        "rum",
        "security_signals",
        "profiles",
        "audit",
        "events",
        "ci_tests",
        "ci_pipelines",
        "incident_analytics",
        "product_analytics",
        "on_call_events",
        "dora",
    }
    LOGS: ClassVar["EventsDataSource"]
    SPANS: ClassVar["EventsDataSource"]
    NETWORK: ClassVar["EventsDataSource"]
    RUM: ClassVar["EventsDataSource"]
    SECURITY_SIGNALS: ClassVar["EventsDataSource"]
    PROFILES: ClassVar["EventsDataSource"]
    AUDIT: ClassVar["EventsDataSource"]
    EVENTS: ClassVar["EventsDataSource"]
    CI_TESTS: ClassVar["EventsDataSource"]
    CI_PIPELINES: ClassVar["EventsDataSource"]
    INCIDENT_ANALYTICS: ClassVar["EventsDataSource"]
    PRODUCT_ANALYTICS: ClassVar["EventsDataSource"]
    ON_CALL_EVENTS: ClassVar["EventsDataSource"]
    DORA: ClassVar["EventsDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventsDataSource.LOGS = EventsDataSource("logs")
EventsDataSource.SPANS = EventsDataSource("spans")
EventsDataSource.NETWORK = EventsDataSource("network")
EventsDataSource.RUM = EventsDataSource("rum")
EventsDataSource.SECURITY_SIGNALS = EventsDataSource("security_signals")
EventsDataSource.PROFILES = EventsDataSource("profiles")
EventsDataSource.AUDIT = EventsDataSource("audit")
EventsDataSource.EVENTS = EventsDataSource("events")
EventsDataSource.CI_TESTS = EventsDataSource("ci_tests")
EventsDataSource.CI_PIPELINES = EventsDataSource("ci_pipelines")
EventsDataSource.INCIDENT_ANALYTICS = EventsDataSource("incident_analytics")
EventsDataSource.PRODUCT_ANALYTICS = EventsDataSource("product_analytics")
EventsDataSource.ON_CALL_EVENTS = EventsDataSource("on_call_events")
EventsDataSource.DORA = EventsDataSource("dora")
