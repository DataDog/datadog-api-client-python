# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.table_row_group_by import TableRowGroupBy
    from datadog_api_client.v1_20270101.model.table_rows_join_type import TableRowsJoinType
    from datadog_api_client.v1_20270101.model.table_sort import TableSort


class TableRows(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_row_group_by import TableRowGroupBy
        from datadog_api_client.v1_20270101.model.table_rows_join_type import TableRowsJoinType
        from datadog_api_client.v1_20270101.model.table_sort import TableSort

        return {
            "group_by": ([TableRowGroupBy],),
            "join_type": (TableRowsJoinType,),
            "sort": (TableSort,),
        }

    attribute_map = {
        "group_by": "group_by",
        "join_type": "join_type",
        "sort": "sort",
    }

    def __init__(
        self_,
        group_by: List[TableRowGroupBy],
        sort: TableSort,
        join_type: Union[TableRowsJoinType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [TableRowGroupBy]

        :param join_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_type: TableRowsJoinType, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: TableSort
        """
        if join_type is not unset:
            kwargs["join_type"] = join_type
        super().__init__(kwargs)

        self_.group_by = group_by
        self_.sort = sort
