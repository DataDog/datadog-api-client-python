# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AgentHealthIssuesResponsePage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "counts_by_issue_type": ({str: (int,)},),
            "total_count": (int,),
        }

    attribute_map = {
        "counts_by_issue_type": "counts_by_issue_type",
        "total_count": "total_count",
    }

    def __init__(self_, counts_by_issue_type: Dict[str, int], total_count: int, **kwargs):
        """
        Counts for the matching Agent Health issues.

        :param counts_by_issue_type: The number of open issues matching the filters in each issue-type group.
        :type counts_by_issue_type: {str: (int,)}

        :param total_count: The total number of open issues matching the filters.
        :type total_count: int
        """
        super().__init__(kwargs)

        self_.counts_by_issue_type = counts_by_issue_type
        self_.total_count = total_count
