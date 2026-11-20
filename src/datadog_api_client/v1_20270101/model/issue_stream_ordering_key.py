# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueStreamOrderingKey(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["TOTAL_COUNT", "FIRST_SEEN", "IMPACTED_SESSIONS", "IMPACTED_ACCOUNTS", "PRIORITY"].
    :type value: str
    """

    allowed_values = {
        "TOTAL_COUNT",
        "FIRST_SEEN",
        "IMPACTED_SESSIONS",
        "IMPACTED_ACCOUNTS",
        "PRIORITY",
    }
    TOTAL_COUNT: ClassVar["IssueStreamOrderingKey"]
    FIRST_SEEN: ClassVar["IssueStreamOrderingKey"]
    IMPACTED_SESSIONS: ClassVar["IssueStreamOrderingKey"]
    IMPACTED_ACCOUNTS: ClassVar["IssueStreamOrderingKey"]
    PRIORITY: ClassVar["IssueStreamOrderingKey"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueStreamOrderingKey.TOTAL_COUNT = IssueStreamOrderingKey("TOTAL_COUNT")
IssueStreamOrderingKey.FIRST_SEEN = IssueStreamOrderingKey("FIRST_SEEN")
IssueStreamOrderingKey.IMPACTED_SESSIONS = IssueStreamOrderingKey("IMPACTED_SESSIONS")
IssueStreamOrderingKey.IMPACTED_ACCOUNTS = IssueStreamOrderingKey("IMPACTED_ACCOUNTS")
IssueStreamOrderingKey.PRIORITY = IssueStreamOrderingKey("PRIORITY")
