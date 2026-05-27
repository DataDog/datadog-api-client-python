# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.replay_analysis_issue_data import ReplayAnalysisIssueData


class ReplayAnalysisIssueResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_issue_data import ReplayAnalysisIssueData

        return {
            "data": (ReplayAnalysisIssueData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ReplayAnalysisIssueData, **kwargs):
        """
        A single RUM replay analysis issue.

        :param data: Data object representing a RUM replay analysis issue.
        :type data: ReplayAnalysisIssueData
        """
        super().__init__(kwargs)

        self_.data = data
