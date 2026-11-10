# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuePullRequestReason(ModelSimple):
    """
    Why the pull request is linked to the issue. `fix` means the pull request fixes the issue, and `trigger` means the pull request introduced the issue.

    :param value: Must be one of ["unknown", "fix", "trigger"].
    :type value: str
    """

    allowed_values = {
        "unknown",
        "fix",
        "trigger",
    }
    UNKNOWN: ClassVar["IssuePullRequestReason"]
    FIX: ClassVar["IssuePullRequestReason"]
    TRIGGER: ClassVar["IssuePullRequestReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuePullRequestReason.UNKNOWN = IssuePullRequestReason("unknown")
IssuePullRequestReason.FIX = IssuePullRequestReason("fix")
IssuePullRequestReason.TRIGGER = IssuePullRequestReason("trigger")
