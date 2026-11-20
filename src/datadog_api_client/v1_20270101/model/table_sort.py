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
    from datadog_api_client.v1_20270101.model.table_sort_columns_items import TableSortColumnsItems


class TableSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.table_sort_columns_items import TableSortColumnsItems

        return {
            "columns": ([TableSortColumnsItems],),
            "limit": (float,),
        }

    attribute_map = {
        "columns": "columns",
        "limit": "limit",
    }

    def __init__(self_, columns: List[TableSortColumnsItems], limit: float, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [TableSortColumnsItems]

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.limit = limit
