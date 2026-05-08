# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.replay_analysis_issue_session_data import ReplayAnalysisIssueSessionData
    from datadog_api_client.v2.model.replay_analysis_issue_meta import ReplayAnalysisIssueMeta


class ReplayAnalysisIssueSessionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_issue_session_data import ReplayAnalysisIssueSessionData
        from datadog_api_client.v2.model.replay_analysis_issue_meta import ReplayAnalysisIssueMeta

        return {
            "data": ([ReplayAnalysisIssueSessionData],),
            "meta": (ReplayAnalysisIssueMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[ReplayAnalysisIssueSessionData], meta: ReplayAnalysisIssueMeta, **kwargs):
        """
        A paginated list of sessions related to a RUM replay analysis issue.

        :param data: Array of session data objects related to the issue.
        :type data: [ReplayAnalysisIssueSessionData]

        :param meta: Metadata object for paginated issue list responses.
        :type meta: ReplayAnalysisIssueMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
