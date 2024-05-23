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
    from datadog_api_client.v1.model.widget_sort import WidgetSort
    from datadog_api_client.v1.model.formula_type import FormulaType


class WidgetFormulaSort(ModelNormal):
    validations = {
        "index": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.widget_sort import WidgetSort
        from datadog_api_client.v1.model.formula_type import FormulaType

        return {
            "index": (int,),
            "order": (WidgetSort,),
            "type": (FormulaType,),
        }

    attribute_map = {
        "index": "index",
        "order": "order",
        "type": "type",
    }

    def __init__(self_, index: int, order: WidgetSort, type: FormulaType, **kwargs):
        """
        The formula to sort the widget by.

        :param index: The index of the formula to sort by.
        :type index: int

        :param order: Widget sorting methods.
        :type order: WidgetSort

        :param type: Set the sort type to formula.
        :type type: FormulaType
        """
        super().__init__(kwargs)

        self_.index = index
        self_.order = order
        self_.type = type
