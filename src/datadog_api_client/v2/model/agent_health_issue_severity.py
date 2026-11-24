# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AgentHealthIssueSeverity(ModelSimple):
    """
    The severity of the issue.

    :param value: Must be one of ["low", "medium", "high", "unknown"].
    :type value: str
    """

    allowed_values = {
        "low",
        "medium",
        "high",
        "unknown",
    }
    LOW: ClassVar["AgentHealthIssueSeverity"]
    MEDIUM: ClassVar["AgentHealthIssueSeverity"]
    HIGH: ClassVar["AgentHealthIssueSeverity"]
    UNKNOWN: ClassVar["AgentHealthIssueSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AgentHealthIssueSeverity.LOW = AgentHealthIssueSeverity("low")
AgentHealthIssueSeverity.MEDIUM = AgentHealthIssueSeverity("medium")
AgentHealthIssueSeverity.HIGH = AgentHealthIssueSeverity("high")
AgentHealthIssueSeverity.UNKNOWN = AgentHealthIssueSeverity("unknown")
