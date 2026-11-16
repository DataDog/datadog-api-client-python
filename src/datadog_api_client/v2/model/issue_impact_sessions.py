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
    from datadog_api_client.v2.model.issue_impact_session import IssueImpactSession


class IssueImpactSessions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact_session import IssueImpactSession

        return {
            "distinct_count": (int,),
            "top": ([IssueImpactSession],),
        }

    attribute_map = {
        "distinct_count": "distinct_count",
        "top": "top",
    }

    def __init__(self_, distinct_count: int, top: List[IssueImpactSession], **kwargs):
        """
        RUM sessions where the issue occurred.

        :param distinct_count: Number of distinct sessions where the issue occurred in the time window.
        :type distinct_count: int

        :param top: Up to five sessions with the most errors, most affected first.
        :type top: [IssueImpactSession]
        """
        super().__init__(kwargs)

        self_.distinct_count = distinct_count
        self_.top = top
