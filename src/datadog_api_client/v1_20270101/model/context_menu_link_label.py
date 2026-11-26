# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ContextMenuLinkLabel(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["events", "logs", "rum", "product_analytics", "network", "cloud_cost", "functions", "hosts", "traces", "profiles", "processes", "containers", "change_tracking", "audit_trail", "network_device_flows", "devices", "recommendations", "security_findings", "security_signals", "security_traces", "incidents", "cases", "metrics_summary", "pods", "ci_pipelines", "database_queries", "watch_sessions", "gpu_monitoring", "llm_observability"].
    :type value: str
    """

    allowed_values = {
        "events",
        "logs",
        "rum",
        "product_analytics",
        "network",
        "cloud_cost",
        "functions",
        "hosts",
        "traces",
        "profiles",
        "processes",
        "containers",
        "change_tracking",
        "audit_trail",
        "network_device_flows",
        "devices",
        "recommendations",
        "security_findings",
        "security_signals",
        "security_traces",
        "incidents",
        "cases",
        "metrics_summary",
        "pods",
        "ci_pipelines",
        "database_queries",
        "watch_sessions",
        "gpu_monitoring",
        "llm_observability",
    }
    EVENTS: ClassVar["ContextMenuLinkLabel"]
    LOGS: ClassVar["ContextMenuLinkLabel"]
    RUM: ClassVar["ContextMenuLinkLabel"]
    PRODUCT_ANALYTICS: ClassVar["ContextMenuLinkLabel"]
    NETWORK: ClassVar["ContextMenuLinkLabel"]
    CLOUD_COST: ClassVar["ContextMenuLinkLabel"]
    FUNCTIONS: ClassVar["ContextMenuLinkLabel"]
    HOSTS: ClassVar["ContextMenuLinkLabel"]
    TRACES: ClassVar["ContextMenuLinkLabel"]
    PROFILES: ClassVar["ContextMenuLinkLabel"]
    PROCESSES: ClassVar["ContextMenuLinkLabel"]
    CONTAINERS: ClassVar["ContextMenuLinkLabel"]
    CHANGE_TRACKING: ClassVar["ContextMenuLinkLabel"]
    AUDIT_TRAIL: ClassVar["ContextMenuLinkLabel"]
    NETWORK_DEVICE_FLOWS: ClassVar["ContextMenuLinkLabel"]
    DEVICES: ClassVar["ContextMenuLinkLabel"]
    RECOMMENDATIONS: ClassVar["ContextMenuLinkLabel"]
    SECURITY_FINDINGS: ClassVar["ContextMenuLinkLabel"]
    SECURITY_SIGNALS: ClassVar["ContextMenuLinkLabel"]
    SECURITY_TRACES: ClassVar["ContextMenuLinkLabel"]
    INCIDENTS: ClassVar["ContextMenuLinkLabel"]
    CASES: ClassVar["ContextMenuLinkLabel"]
    METRICS_SUMMARY: ClassVar["ContextMenuLinkLabel"]
    PODS: ClassVar["ContextMenuLinkLabel"]
    CI_PIPELINES: ClassVar["ContextMenuLinkLabel"]
    DATABASE_QUERIES: ClassVar["ContextMenuLinkLabel"]
    WATCH_SESSIONS: ClassVar["ContextMenuLinkLabel"]
    GPU_MONITORING: ClassVar["ContextMenuLinkLabel"]
    LLM_OBSERVABILITY: ClassVar["ContextMenuLinkLabel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ContextMenuLinkLabel.EVENTS = ContextMenuLinkLabel("events")
ContextMenuLinkLabel.LOGS = ContextMenuLinkLabel("logs")
ContextMenuLinkLabel.RUM = ContextMenuLinkLabel("rum")
ContextMenuLinkLabel.PRODUCT_ANALYTICS = ContextMenuLinkLabel("product_analytics")
ContextMenuLinkLabel.NETWORK = ContextMenuLinkLabel("network")
ContextMenuLinkLabel.CLOUD_COST = ContextMenuLinkLabel("cloud_cost")
ContextMenuLinkLabel.FUNCTIONS = ContextMenuLinkLabel("functions")
ContextMenuLinkLabel.HOSTS = ContextMenuLinkLabel("hosts")
ContextMenuLinkLabel.TRACES = ContextMenuLinkLabel("traces")
ContextMenuLinkLabel.PROFILES = ContextMenuLinkLabel("profiles")
ContextMenuLinkLabel.PROCESSES = ContextMenuLinkLabel("processes")
ContextMenuLinkLabel.CONTAINERS = ContextMenuLinkLabel("containers")
ContextMenuLinkLabel.CHANGE_TRACKING = ContextMenuLinkLabel("change_tracking")
ContextMenuLinkLabel.AUDIT_TRAIL = ContextMenuLinkLabel("audit_trail")
ContextMenuLinkLabel.NETWORK_DEVICE_FLOWS = ContextMenuLinkLabel("network_device_flows")
ContextMenuLinkLabel.DEVICES = ContextMenuLinkLabel("devices")
ContextMenuLinkLabel.RECOMMENDATIONS = ContextMenuLinkLabel("recommendations")
ContextMenuLinkLabel.SECURITY_FINDINGS = ContextMenuLinkLabel("security_findings")
ContextMenuLinkLabel.SECURITY_SIGNALS = ContextMenuLinkLabel("security_signals")
ContextMenuLinkLabel.SECURITY_TRACES = ContextMenuLinkLabel("security_traces")
ContextMenuLinkLabel.INCIDENTS = ContextMenuLinkLabel("incidents")
ContextMenuLinkLabel.CASES = ContextMenuLinkLabel("cases")
ContextMenuLinkLabel.METRICS_SUMMARY = ContextMenuLinkLabel("metrics_summary")
ContextMenuLinkLabel.PODS = ContextMenuLinkLabel("pods")
ContextMenuLinkLabel.CI_PIPELINES = ContextMenuLinkLabel("ci_pipelines")
ContextMenuLinkLabel.DATABASE_QUERIES = ContextMenuLinkLabel("database_queries")
ContextMenuLinkLabel.WATCH_SESSIONS = ContextMenuLinkLabel("watch_sessions")
ContextMenuLinkLabel.GPU_MONITORING = ContextMenuLinkLabel("gpu_monitoring")
ContextMenuLinkLabel.LLM_OBSERVABILITY = ContextMenuLinkLabel("llm_observability")
