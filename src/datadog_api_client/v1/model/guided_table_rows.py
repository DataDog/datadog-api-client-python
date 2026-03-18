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
    from datadog_api_client.v1.model.guided_table_row_group_by import GuidedTableRowGroupBy
    from datadog_api_client.v1.model.guided_table_sort import GuidedTableSort


class GuidedTableRows(ModelNormal):
    validations = {
        "group_by": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.guided_table_row_group_by import GuidedTableRowGroupBy
        from datadog_api_client.v1.model.guided_table_sort import GuidedTableSort

        return {
            "group_by": ([GuidedTableRowGroupBy],),
            "sort": (GuidedTableSort,),
        }

    attribute_map = {
        "group_by": "group_by",
        "sort": "sort",
    }

    def __init__(self_, group_by: List[GuidedTableRowGroupBy], sort: GuidedTableSort, **kwargs):
        """
        Defines how to compute the rows of a guided table.

        :param group_by: Grouping dimensions that form each row. Must be non-empty.
        :type group_by: [GuidedTableRowGroupBy]

        :param sort: Sort configuration for a guided table.
        :type sort: GuidedTableSort
        """
        super().__init__(kwargs)

        self_.group_by = group_by
        self_.sort = sort
