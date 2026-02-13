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
    from datadog_api_client.v2.model.commit_coverage_summary_request_data import CommitCoverageSummaryRequestData


class CommitCoverageSummaryRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commit_coverage_summary_request_data import CommitCoverageSummaryRequestData

        return {
            "data": (CommitCoverageSummaryRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CommitCoverageSummaryRequestData, **kwargs):
        """
        Request object for getting code coverage summary for a commit.

        :param data: Data object for commit summary request.
        :type data: CommitCoverageSummaryRequestData
        """
        super().__init__(kwargs)

        self_.data = data
