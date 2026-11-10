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
    from datadog_api_client.v2.model.issue_watch_reference import IssueWatchReference


class IssueWatchesRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_watch_reference import IssueWatchReference

        return {
            "data": ([IssueWatchReference],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[IssueWatchReference], **kwargs):
        """
        Relationship between the issue and its active watches. Returned when ``watches`` is included and the issue has an active watch.

        :param data: Array of active watches on the issue.
        :type data: [IssueWatchReference]
        """
        super().__init__(kwargs)

        self_.data = data
