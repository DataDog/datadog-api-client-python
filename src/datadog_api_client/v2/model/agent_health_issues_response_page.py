# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AgentHealthIssuesResponsePage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "counts_by_issue_type": ({str: (int,)},),
            "limit": (int,),
            "offset": (int,),
            "total_count": (int,),
        }

    attribute_map = {
        "counts_by_issue_type": "counts_by_issue_type",
        "limit": "limit",
        "offset": "offset",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        limit: int,
        offset: int,
        total_count: int,
        counts_by_issue_type: Union[Dict[str, int], UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination details and counts for the matching Agent Health issues.

        :param counts_by_issue_type: The number of open issues matching the filters in each issue-type group.
        :type counts_by_issue_type: {str: (int,)}, optional

        :param limit: The maximum number of issues returned, echoing the requested ``page[limit]``.
        :type limit: int

        :param offset: The number of issues skipped, echoing the requested ``page[offset]``.
        :type offset: int

        :param total_count: The total number of open issues matching the filters.
        :type total_count: int
        """
        if counts_by_issue_type is not unset:
            kwargs["counts_by_issue_type"] = counts_by_issue_type
        super().__init__(kwargs)

        self_.limit = limit
        self_.offset = offset
        self_.total_count = total_count
