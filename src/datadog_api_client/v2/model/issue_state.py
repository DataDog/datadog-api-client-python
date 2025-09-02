# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueState(ModelSimple):
    """
    State of the issue

    :param value: Must be one of ["OPEN", "ACKNOWLEDGED", "RESOLVED", "IGNORED", "EXCLUDED"].
    :type value: str
    """

    allowed_values = {
        "OPEN",
        "ACKNOWLEDGED",
        "RESOLVED",
        "IGNORED",
        "EXCLUDED",
    }
    OPEN: ClassVar["IssueState"]
    ACKNOWLEDGED: ClassVar["IssueState"]
    RESOLVED: ClassVar["IssueState"]
    IGNORED: ClassVar["IssueState"]
    EXCLUDED: ClassVar["IssueState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueState.OPEN = IssueState("OPEN")
IssueState.ACKNOWLEDGED = IssueState("ACKNOWLEDGED")
IssueState.RESOLVED = IssueState("RESOLVED")
IssueState.IGNORED = IssueState("IGNORED")
IssueState.EXCLUDED = IssueState("EXCLUDED")
