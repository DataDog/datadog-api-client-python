# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RemediationPullRequestStatus(ModelSimple):
    """
    Pull request status for a linked code session.

    :param value: Must be one of ["open", "closed", "merged"].
    :type value: str
    """

    allowed_values = {
        "open",
        "closed",
        "merged",
    }
    OPEN: ClassVar["RemediationPullRequestStatus"]
    CLOSED: ClassVar["RemediationPullRequestStatus"]
    MERGED: ClassVar["RemediationPullRequestStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RemediationPullRequestStatus.OPEN = RemediationPullRequestStatus("open")
RemediationPullRequestStatus.CLOSED = RemediationPullRequestStatus("closed")
RemediationPullRequestStatus.MERGED = RemediationPullRequestStatus("merged")
