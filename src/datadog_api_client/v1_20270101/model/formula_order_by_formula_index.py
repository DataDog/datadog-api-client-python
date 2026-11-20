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
    from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
    from datadog_api_client.v1_20270101.model.formula_order_by_formula_index_type import FormulaOrderByFormulaIndexType


class FormulaOrderByFormulaIndex(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.query_sort_order import QuerySortOrder
        from datadog_api_client.v1_20270101.model.formula_order_by_formula_index_type import (
            FormulaOrderByFormulaIndexType,
        )

        return {
            "index": (float,),
            "order": (QuerySortOrder,),
            "type": (FormulaOrderByFormulaIndexType,),
        }

    attribute_map = {
        "index": "index",
        "order": "order",
        "type": "type",
    }

    def __init__(self_, index: float, order: QuerySortOrder, type: FormulaOrderByFormulaIndexType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param index: Test-only generated schema for the dashboard versioning proof of concept.
        :type index: float

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: QuerySortOrder

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: FormulaOrderByFormulaIndexType
        """
        super().__init__(kwargs)

        self_.index = index
        self_.order = order
        self_.type = type
