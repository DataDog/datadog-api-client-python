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
    from datadog_api_client.v2.model.case_aggregate_group_by import CaseAggregateGroupBy


class CaseAggregateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_aggregate_group_by import CaseAggregateGroupBy

        return {
            "group_by": (CaseAggregateGroupBy,),
            "query_filter": (str,),
        }

    attribute_map = {
        "group_by": "group_by",
        "query_filter": "query_filter",
    }

    def __init__(self_, group_by: CaseAggregateGroupBy, query_filter: str, **kwargs):
        """
        Attributes for the aggregation request, including the search query and grouping configuration.

        :param group_by: Configuration for grouping aggregated results by one or more case fields.
        :type group_by: CaseAggregateGroupBy

        :param query_filter: A search query to filter which cases are included in the aggregation. Uses the same syntax as the Case Management search bar.
        :type query_filter: str
        """
        super().__init__(kwargs)

        self_.group_by = group_by
        self_.query_filter = query_filter
