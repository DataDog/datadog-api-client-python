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
    from datadog_api_client.v1_20270101.model.query_table_projection_column_order import QueryTableProjectionColumnOrder
    from datadog_api_client.v1_20270101.model.query_table_projection_dimension import QueryTableProjectionDimension
    from datadog_api_client.v1_20270101.model.query_table_projection_type import QueryTableProjectionType
    from datadog_api_client.v1_20270101.model.query_table_projection_unlisted_columns import (
        QueryTableProjectionUnlistedColumns,
    )


class QueryTableProjection(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.query_table_projection_column_order import (
            QueryTableProjectionColumnOrder,
        )
        from datadog_api_client.v1_20270101.model.query_table_projection_dimension import QueryTableProjectionDimension
        from datadog_api_client.v1_20270101.model.query_table_projection_type import QueryTableProjectionType
        from datadog_api_client.v1_20270101.model.query_table_projection_unlisted_columns import (
            QueryTableProjectionUnlistedColumns,
        )

        return {
            "column_order": (QueryTableProjectionColumnOrder,),
            "dimensions": ([QueryTableProjectionDimension],),
            "type": (QueryTableProjectionType,),
            "unlisted_columns": (QueryTableProjectionUnlistedColumns,),
        }

    attribute_map = {
        "column_order": "column_order",
        "dimensions": "dimensions",
        "type": "type",
        "unlisted_columns": "unlisted_columns",
    }

    def __init__(
        self_,
        dimensions: List[QueryTableProjectionDimension],
        type: QueryTableProjectionType,
        column_order: Union[QueryTableProjectionColumnOrder, UnsetType] = unset,
        unlisted_columns: Union[QueryTableProjectionUnlistedColumns, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column_order: Test-only generated schema for the dashboard versioning proof of concept.
        :type column_order: QueryTableProjectionColumnOrder, optional

        :param dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type dimensions: [QueryTableProjectionDimension]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: QueryTableProjectionType

        :param unlisted_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type unlisted_columns: QueryTableProjectionUnlistedColumns, optional
        """
        if column_order is not unset:
            kwargs["column_order"] = column_order
        if unlisted_columns is not unset:
            kwargs["unlisted_columns"] = unlisted_columns
        super().__init__(kwargs)

        self_.dimensions = dimensions
        self_.type = type
