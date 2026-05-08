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
    from datadog_api_client.v2.model.replay_analysis_issue_data_attributes import ReplayAnalysisIssueDataAttributes
    from datadog_api_client.v2.model.replay_analysis_issue_data_type import ReplayAnalysisIssueDataType


class ReplayAnalysisIssueData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_issue_data_attributes import ReplayAnalysisIssueDataAttributes
        from datadog_api_client.v2.model.replay_analysis_issue_data_type import ReplayAnalysisIssueDataType

        return {
            "attributes": (ReplayAnalysisIssueDataAttributes,),
            "id": (str,),
            "type": (ReplayAnalysisIssueDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ReplayAnalysisIssueDataAttributes, id: str, type: ReplayAnalysisIssueDataType, **kwargs
    ):
        """
        Data object representing a RUM replay analysis issue.

        :param attributes: Attributes of a RUM replay analysis issue.
        :type attributes: ReplayAnalysisIssueDataAttributes

        :param id: Unique identifier of the issue.
        :type id: str

        :param type: RUM replay analysis issue resource type.
        :type type: ReplayAnalysisIssueDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
