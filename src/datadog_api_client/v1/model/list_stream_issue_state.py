# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListStreamIssueState(ModelSimple):
    """
    Issue state filter for the `issue_stream` data source.

    :param value: Must be one of ["OPEN", "IGNORED", "ACKNOWLEDGED", "RESOLVED"].
    :type value: str
    """

    allowed_values = {
        "OPEN",
        "IGNORED",
        "ACKNOWLEDGED",
        "RESOLVED",
    }
    OPEN: ClassVar["ListStreamIssueState"]
    IGNORED: ClassVar["ListStreamIssueState"]
    ACKNOWLEDGED: ClassVar["ListStreamIssueState"]
    RESOLVED: ClassVar["ListStreamIssueState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListStreamIssueState.OPEN = ListStreamIssueState("OPEN")
ListStreamIssueState.IGNORED = ListStreamIssueState("IGNORED")
ListStreamIssueState.ACKNOWLEDGED = ListStreamIssueState("ACKNOWLEDGED")
ListStreamIssueState.RESOLVED = ListStreamIssueState("RESOLVED")
