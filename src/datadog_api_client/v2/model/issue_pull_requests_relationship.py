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
    from datadog_api_client.v2.model.issue_pull_request_reference import IssuePullRequestReference


class IssuePullRequestsRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_pull_request_reference import IssuePullRequestReference

        return {
            "data": ([IssuePullRequestReference],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[IssuePullRequestReference], **kwargs):
        """
        Relationship between the issue and its linked pull requests. Returned when ``pull_requests`` is included and the issue has linked pull requests.

        :param data: Array of pull requests linked to the issue.
        :type data: [IssuePullRequestReference]
        """
        super().__init__(kwargs)

        self_.data = data
