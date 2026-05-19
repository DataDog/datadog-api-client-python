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
    from datadog_api_client.v2.model.log_formatting_issue_data import LogFormattingIssueData


class LogFormattingIssuesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.log_formatting_issue_data import LogFormattingIssueData

        return {
            "data": ([LogFormattingIssueData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[LogFormattingIssueData], **kwargs):
        """
        Response containing the list of log sources with formatting issues.

        :param data: The list of log sources with formatting issues.
        :type data: [LogFormattingIssueData]
        """
        super().__init__(kwargs)

        self_.data = data
