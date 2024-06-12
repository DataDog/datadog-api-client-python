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
    from datadog_api_client.v1.model.widget_sort_order_by import WidgetSortOrderBy
    from datadog_api_client.v1.model.widget_formula_sort import WidgetFormulaSort
    from datadog_api_client.v1.model.widget_group_sort import WidgetGroupSort


class WidgetSortBy(ModelNormal):
    validations = {
        "count": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort_order_by import WidgetSortOrderBy

        return {
            "count": (int,),
            "order_by": ([WidgetSortOrderBy],),
        }

    attribute_map = {
        "count": "count",
        "order_by": "order_by",
    }

    def __init__(
        self_,
        count: Union[int, UnsetType] = unset,
        order_by: Union[List[Union[WidgetSortOrderBy, WidgetFormulaSort, WidgetGroupSort]], UnsetType] = unset,
        **kwargs,
    ):
        """
        The controls for sorting the widget.

        :param count: The number of items to limit the widget to.
        :type count: int, optional

        :param order_by: The array of items to sort the widget by in order.
        :type order_by: [WidgetSortOrderBy], optional
        """
        if count is not unset:
            kwargs["count"] = count
        if order_by is not unset:
            kwargs["order_by"] = order_by
        super().__init__(kwargs)
