# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProductAnalyticsJourneyDropOffIssue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error_count": (int,),
            "issue_id": (str,),
            "session_count": (int,),
        }

    attribute_map = {
        "error_count": "error_count",
        "issue_id": "issue_id",
        "session_count": "session_count",
    }

    def __init__(self_, error_count: int, issue_id: str, session_count: int, **kwargs):
        """
        An issue contributing to drop-off at the target step.

        :param error_count: Number of errors attributed to this issue.
        :type error_count: int

        :param issue_id: Identifier of the issue.
        :type issue_id: str

        :param session_count: Number of sessions affected by this issue.
        :type session_count: int
        """
        super().__init__(kwargs)

        self_.error_count = error_count
        self_.issue_id = issue_id
        self_.session_count = session_count
