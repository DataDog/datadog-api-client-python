# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueWatchConditionKind(ModelSimple):
    """
    Kind of watch condition.

    :param value: Must be one of ["OCCURRENCES", "CARDINALITY", "ELAPSED_TIME", "ANY", "ALL"].
    :type value: str
    """

    allowed_values = {
        "OCCURRENCES",
        "CARDINALITY",
        "ELAPSED_TIME",
        "ANY",
        "ALL",
    }
    OCCURRENCES: ClassVar["IssueWatchConditionKind"]
    CARDINALITY: ClassVar["IssueWatchConditionKind"]
    ELAPSED_TIME: ClassVar["IssueWatchConditionKind"]
    ANY: ClassVar["IssueWatchConditionKind"]
    ALL: ClassVar["IssueWatchConditionKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueWatchConditionKind.OCCURRENCES = IssueWatchConditionKind("OCCURRENCES")
IssueWatchConditionKind.CARDINALITY = IssueWatchConditionKind("CARDINALITY")
IssueWatchConditionKind.ELAPSED_TIME = IssueWatchConditionKind("ELAPSED_TIME")
IssueWatchConditionKind.ANY = IssueWatchConditionKind("ANY")
IssueWatchConditionKind.ALL = IssueWatchConditionKind("ALL")
