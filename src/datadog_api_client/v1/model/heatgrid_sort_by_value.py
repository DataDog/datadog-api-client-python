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
    from datadog_api_client.v1.model.heatgrid_sort_aggregation import HeatgridSortAggregation
    from datadog_api_client.v1.model.heatgrid_sort_order import HeatgridSortOrder
    from datadog_api_client.v1.model.heatgrid_sort_by_value_property import HeatgridSortByValueProperty


class HeatgridSortByValue(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_sort_aggregation import HeatgridSortAggregation
        from datadog_api_client.v1.model.heatgrid_sort_order import HeatgridSortOrder
        from datadog_api_client.v1.model.heatgrid_sort_by_value_property import HeatgridSortByValueProperty

        return {
            "aggregation": (HeatgridSortAggregation,),
            "order": (HeatgridSortOrder,),
            "_property": (HeatgridSortByValueProperty,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "order": "order",
        "_property": "property",
    }

    def __init__(
        self_,
        aggregation: HeatgridSortAggregation,
        order: HeatgridSortOrder,
        _property: HeatgridSortByValueProperty,
        **kwargs,
    ):
        """
        Sort rows by their aggregated values.

        :param aggregation: Aggregation used to order rows over the displayed time range.
        :type aggregation: HeatgridSortAggregation

        :param order: Sort direction.
        :type order: HeatgridSortOrder

        :param _property: Sort by value.
        :type _property: HeatgridSortByValueProperty
        """
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.order = order
        self_._property = _property
