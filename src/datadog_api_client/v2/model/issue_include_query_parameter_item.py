# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueIncludeQueryParameterItem(ModelSimple):
    """
    Relationship object that should be included in the response.

    :param value: Must be one of ["case", "teams"].
    :type value: str
    """

    allowed_values = {
        "case",
        "teams",
    }
    CASE: ClassVar["IssueIncludeQueryParameterItem"]
    TEAMS: ClassVar["IssueIncludeQueryParameterItem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueIncludeQueryParameterItem.CASE = IssueIncludeQueryParameterItem("case")
IssueIncludeQueryParameterItem.TEAMS = IssueIncludeQueryParameterItem("teams")
