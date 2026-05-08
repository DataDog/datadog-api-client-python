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
    from datadog_api_client.v2.model.replay_analysis_issue_session_data_attributes import (
        ReplayAnalysisIssueSessionDataAttributes,
    )
    from datadog_api_client.v2.model.replay_analysis_issue_session_data_type import ReplayAnalysisIssueSessionDataType


class ReplayAnalysisIssueSessionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.replay_analysis_issue_session_data_attributes import (
            ReplayAnalysisIssueSessionDataAttributes,
        )
        from datadog_api_client.v2.model.replay_analysis_issue_session_data_type import (
            ReplayAnalysisIssueSessionDataType,
        )

        return {
            "attributes": (ReplayAnalysisIssueSessionDataAttributes,),
            "id": (str,),
            "type": (ReplayAnalysisIssueSessionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ReplayAnalysisIssueSessionDataAttributes,
        id: str,
        type: ReplayAnalysisIssueSessionDataType,
        **kwargs,
    ):
        """
        Data object representing a session related to a RUM replay analysis issue.

        :param attributes: Attributes of a session related to a RUM replay analysis issue.
        :type attributes: ReplayAnalysisIssueSessionDataAttributes

        :param id: Unique identifier of the session.
        :type id: str

        :param type: RUM replay analysis issue session resource type.
        :type type: ReplayAnalysisIssueSessionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
