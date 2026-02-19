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
    from datadog_api_client.v2.model.rum_segment_reference_table_column import RumSegmentReferenceTableColumn
    from datadog_api_client.v2.model.rum_segment_reference_table_join_condition import (
        RumSegmentReferenceTableJoinCondition,
    )


class RumSegmentReferenceTable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_segment_reference_table_column import RumSegmentReferenceTableColumn
        from datadog_api_client.v2.model.rum_segment_reference_table_join_condition import (
            RumSegmentReferenceTableJoinCondition,
        )

        return {
            "columns": ([RumSegmentReferenceTableColumn],),
            "filter_query": (str,),
            "join_condition": (RumSegmentReferenceTableJoinCondition,),
            "name": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "columns": "columns",
        "filter_query": "filter_query",
        "join_condition": "join_condition",
        "name": "name",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        columns: List[RumSegmentReferenceTableColumn],
        join_condition: RumSegmentReferenceTableJoinCondition,
        name: str,
        table_name: str,
        filter_query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A reference table query block within a segment data query.

        :param columns: The columns to include from the reference table.
        :type columns: [RumSegmentReferenceTableColumn]

        :param filter_query: An optional filter query for the reference table data.
        :type filter_query: str, optional

        :param join_condition: The join condition for a reference table query block.
        :type join_condition: RumSegmentReferenceTableJoinCondition

        :param name: The name of this query block.
        :type name: str

        :param table_name: The name of the reference table.
        :type table_name: str
        """
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query
        super().__init__(kwargs)

        self_.columns = columns
        self_.join_condition = join_condition
        self_.name = name
        self_.table_name = table_name
