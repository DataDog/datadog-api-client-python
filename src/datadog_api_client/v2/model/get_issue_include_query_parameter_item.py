# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetIssueIncludeQueryParameterItem(ModelSimple):
    """
    Relationship object that should be included in the response.

    :param value: Must be one of ["assignee", "case", "team_owners"].
    :type value: str
    """

    allowed_values = {
        "assignee",
        "case",
        "team_owners",
    }
    ASSIGNEE: ClassVar["GetIssueIncludeQueryParameterItem"]
    CASE: ClassVar["GetIssueIncludeQueryParameterItem"]
    TEAM_OWNERS: ClassVar["GetIssueIncludeQueryParameterItem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetIssueIncludeQueryParameterItem.ASSIGNEE = GetIssueIncludeQueryParameterItem("assignee")
GetIssueIncludeQueryParameterItem.CASE = GetIssueIncludeQueryParameterItem("case")
GetIssueIncludeQueryParameterItem.TEAM_OWNERS = GetIssueIncludeQueryParameterItem("team_owners")
