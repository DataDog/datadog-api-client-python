# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueWatchActionKind(ModelSimple):
    """
    Kind of watch action.

    :param value: If omitted defaults to "CHANGE_ISSUE_STATE". Must be one of ["CHANGE_ISSUE_STATE"].
    :type value: str
    """

    allowed_values = {
        "CHANGE_ISSUE_STATE",
    }
    CHANGE_ISSUE_STATE: ClassVar["IssueWatchActionKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueWatchActionKind.CHANGE_ISSUE_STATE = IssueWatchActionKind("CHANGE_ISSUE_STATE")
