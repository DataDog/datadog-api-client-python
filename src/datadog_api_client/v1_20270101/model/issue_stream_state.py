# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueStreamState(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["OPEN", "RESOLVED", "IGNORED", "EXCLUDED", "IN_PROGRESS", "ACKNOWLEDGED"].
    :type value: str
    """

    allowed_values = {
        "OPEN",
        "RESOLVED",
        "IGNORED",
        "EXCLUDED",
        "IN_PROGRESS",
        "ACKNOWLEDGED",
    }
    OPEN: ClassVar["IssueStreamState"]
    RESOLVED: ClassVar["IssueStreamState"]
    IGNORED: ClassVar["IssueStreamState"]
    EXCLUDED: ClassVar["IssueStreamState"]
    IN_PROGRESS: ClassVar["IssueStreamState"]
    ACKNOWLEDGED: ClassVar["IssueStreamState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueStreamState.OPEN = IssueStreamState("OPEN")
IssueStreamState.RESOLVED = IssueStreamState("RESOLVED")
IssueStreamState.IGNORED = IssueStreamState("IGNORED")
IssueStreamState.EXCLUDED = IssueStreamState("EXCLUDED")
IssueStreamState.IN_PROGRESS = IssueStreamState("IN_PROGRESS")
IssueStreamState.ACKNOWLEDGED = IssueStreamState("ACKNOWLEDGED")
