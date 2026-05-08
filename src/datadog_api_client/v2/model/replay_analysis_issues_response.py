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
    from datadog_api_client.v2.model.replay_analysis_issue_data import ReplayAnalysisIssueData
    from datadog_api_client.v2.model.replay_analysis_issue_meta import ReplayAnalysisIssueMeta


class ReplayAnalysisIssuesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_issue_data import ReplayAnalysisIssueData
        from datadog_api_client.v2.model.replay_analysis_issue_meta import ReplayAnalysisIssueMeta

        return {
            "data": ([ReplayAnalysisIssueData],),
            "meta": (ReplayAnalysisIssueMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[ReplayAnalysisIssueData], meta: ReplayAnalysisIssueMeta, **kwargs):
        """
        A paginated list of RUM replay analysis issues.

        :param data: Array of RUM replay analysis issue data objects.
        :type data: [ReplayAnalysisIssueData]

        :param meta: Metadata object for paginated issue list responses.
        :type meta: ReplayAnalysisIssueMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
