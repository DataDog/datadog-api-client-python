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
    from datadog_api_client.v2.model.case_aggregate_group import CaseAggregateGroup


class CaseAggregateResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_aggregate_group import CaseAggregateGroup

        return {
            "groups": ([CaseAggregateGroup],),
            "total": (float,),
        }

    attribute_map = {
        "groups": "groups",
        "total": "total",
    }

    def __init__(self_, groups: List[CaseAggregateGroup], total: float, **kwargs):
        """
        Attributes of the aggregation result, including the total count across all groups and the per-group breakdowns.

        :param groups: Aggregated groups.
        :type groups: [CaseAggregateGroup]

        :param total: Total count of aggregated cases.
        :type total: float
        """
        super().__init__(kwargs)

        self_.groups = groups
        self_.total = total
