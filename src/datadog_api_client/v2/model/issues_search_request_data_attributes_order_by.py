# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuesSearchRequestDataAttributesOrderBy(ModelSimple):
    """
    The attribute to sort the search results by, in descending order. Defaults to `TOTAL_COUNT`.

    :param value: Must be one of ["TOTAL_COUNT", "FIRST_SEEN", "IMPACTED_SESSIONS", "PRIORITY", "IMPACTED_ACCOUNTS"].
    :type value: str
    """

    allowed_values = {
        "TOTAL_COUNT",
        "FIRST_SEEN",
        "IMPACTED_SESSIONS",
        "PRIORITY",
        "IMPACTED_ACCOUNTS",
    }
    TOTAL_COUNT: ClassVar["IssuesSearchRequestDataAttributesOrderBy"]
    FIRST_SEEN: ClassVar["IssuesSearchRequestDataAttributesOrderBy"]
    IMPACTED_SESSIONS: ClassVar["IssuesSearchRequestDataAttributesOrderBy"]
    PRIORITY: ClassVar["IssuesSearchRequestDataAttributesOrderBy"]
    IMPACTED_ACCOUNTS: ClassVar["IssuesSearchRequestDataAttributesOrderBy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuesSearchRequestDataAttributesOrderBy.TOTAL_COUNT = IssuesSearchRequestDataAttributesOrderBy("TOTAL_COUNT")
IssuesSearchRequestDataAttributesOrderBy.FIRST_SEEN = IssuesSearchRequestDataAttributesOrderBy("FIRST_SEEN")
IssuesSearchRequestDataAttributesOrderBy.IMPACTED_SESSIONS = IssuesSearchRequestDataAttributesOrderBy(
    "IMPACTED_SESSIONS"
)
IssuesSearchRequestDataAttributesOrderBy.PRIORITY = IssuesSearchRequestDataAttributesOrderBy("PRIORITY")
IssuesSearchRequestDataAttributesOrderBy.IMPACTED_ACCOUNTS = IssuesSearchRequestDataAttributesOrderBy(
    "IMPACTED_ACCOUNTS"
)
