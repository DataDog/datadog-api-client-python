# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.heatgrid_sort_and_order_by_nesting_display import (
        HeatgridSortAndOrderByNestingDisplay,
    )
    from datadog_api_client.v1_20270101.model.flat_sort_by import FlatSortBy
    from datadog_api_client.v1_20270101.model.flat_sort_by20270101_one_of import FlatSortBy20270101OneOf
    from datadog_api_client.v1_20270101.model.flat_sort_by20270101_one_of4456386848 import (
        FlatSortBy20270101OneOf4456386848,
    )


class HeatgridSortAndOrderBy(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.heatgrid_sort_and_order_by_nesting_display import (
            HeatgridSortAndOrderByNestingDisplay,
        )
        from datadog_api_client.v1_20270101.model.flat_sort_by import FlatSortBy

        return {
            "nesting_display": (HeatgridSortAndOrderByNestingDisplay,),
            "sort_by": (FlatSortBy,),
        }

    attribute_map = {
        "nesting_display": "nesting_display",
        "sort_by": "sort_by",
    }

    def __init__(
        self_,
        nesting_display: HeatgridSortAndOrderByNestingDisplay,
        sort_by: Union[FlatSortBy, FlatSortBy20270101OneOf, FlatSortBy20270101OneOf4456386848],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param nesting_display: Test-only generated schema for the dashboard versioning proof of concept.
        :type nesting_display: HeatgridSortAndOrderByNestingDisplay

        :param sort_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort_by: FlatSortBy
        """
        super().__init__(kwargs)

        self_.nesting_display = nesting_display
        self_.sort_by = sort_by
