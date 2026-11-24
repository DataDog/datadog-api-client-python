# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AgentHealthIssueResourceKind(ModelSimple):
    """
    The kind of affected resource. The meaning of `resource_id` depends on this: hostname for `host`, DaemonSet UID for `deployment` (node Agent), cluster UUID for `cluster`, hostname of the host running the Cluster Agent for `cluster_agent`, or OpenTelemetry collector ID for `otel`.

    :param value: Must be one of ["host", "deployment", "cluster", "cluster_agent", "otel"].
    :type value: str
    """

    allowed_values = {
        "host",
        "deployment",
        "cluster",
        "cluster_agent",
        "otel",
    }
    HOST: ClassVar["AgentHealthIssueResourceKind"]
    DEPLOYMENT: ClassVar["AgentHealthIssueResourceKind"]
    CLUSTER: ClassVar["AgentHealthIssueResourceKind"]
    CLUSTER_AGENT: ClassVar["AgentHealthIssueResourceKind"]
    OTEL: ClassVar["AgentHealthIssueResourceKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AgentHealthIssueResourceKind.HOST = AgentHealthIssueResourceKind("host")
AgentHealthIssueResourceKind.DEPLOYMENT = AgentHealthIssueResourceKind("deployment")
AgentHealthIssueResourceKind.CLUSTER = AgentHealthIssueResourceKind("cluster")
AgentHealthIssueResourceKind.CLUSTER_AGENT = AgentHealthIssueResourceKind("cluster_agent")
AgentHealthIssueResourceKind.OTEL = AgentHealthIssueResourceKind("otel")
