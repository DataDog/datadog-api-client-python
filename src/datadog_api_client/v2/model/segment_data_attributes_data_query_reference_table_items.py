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
    from datadog_api_client.v2.model.segment_data_attributes_data_query_reference_table_items_columns_items import (
        SegmentDataAttributesDataQueryReferenceTableItemsColumnsItems,
    )
    from datadog_api_client.v2.model.segment_data_attributes_data_query_reference_table_items_join_condition import (
        SegmentDataAttributesDataQueryReferenceTableItemsJoinCondition,
    )


class SegmentDataAttributesDataQueryReferenceTableItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_data_attributes_data_query_reference_table_items_columns_items import (
            SegmentDataAttributesDataQueryReferenceTableItemsColumnsItems,
        )
        from datadog_api_client.v2.model.segment_data_attributes_data_query_reference_table_items_join_condition import (
            SegmentDataAttributesDataQueryReferenceTableItemsJoinCondition,
        )

        return {
            "columns": ([SegmentDataAttributesDataQueryReferenceTableItemsColumnsItems],),
            "filter_query": (str,),
            "join_condition": (SegmentDataAttributesDataQueryReferenceTableItemsJoinCondition,),
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
        join_condition: SegmentDataAttributesDataQueryReferenceTableItemsJoinCondition,
        table_name: str,
        columns: Union[List[SegmentDataAttributesDataQueryReferenceTableItemsColumnsItems], UnsetType] = unset,
        filter_query: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param columns:
        :type columns: [SegmentDataAttributesDataQueryReferenceTableItemsColumnsItems], optional

        :param filter_query:
        :type filter_query: str, optional

        :param join_condition:
        :type join_condition: SegmentDataAttributesDataQueryReferenceTableItemsJoinCondition

        :param name:
        :type name: str, optional

        :param table_name:
        :type table_name: str
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if filter_query is not unset:
            kwargs["filter_query"] = filter_query
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.join_condition = join_condition
        self_.table_name = table_name
