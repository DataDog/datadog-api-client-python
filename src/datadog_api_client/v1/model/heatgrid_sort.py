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
    from datadog_api_client.v1.model.heatgrid_nesting_display import HeatgridNestingDisplay
    from datadog_api_client.v1.model.heatgrid_sort_by import HeatgridSortBy
    from datadog_api_client.v1.model.heatgrid_sort_by_value import HeatgridSortByValue
    from datadog_api_client.v1.model.heatgrid_sort_by_label import HeatgridSortByLabel


class HeatgridSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.heatgrid_nesting_display import HeatgridNestingDisplay
        from datadog_api_client.v1.model.heatgrid_sort_by import HeatgridSortBy

        return {
            "nesting_display": (HeatgridNestingDisplay,),
            "sort_by": (HeatgridSortBy,),
        }

    attribute_map = {
        "nesting_display": "nesting_display",
        "sort_by": "sort_by",
    }

    def __init__(
        self_,
        nesting_display: HeatgridNestingDisplay,
        sort_by: Union[HeatgridSortBy, HeatgridSortByValue, HeatgridSortByLabel],
        **kwargs,
    ):
        """
        Ordering of the heatgrid rows.

        :param nesting_display: Display groups as flat rows.
        :type nesting_display: HeatgridNestingDisplay

        :param sort_by: Sort rows by aggregated value or group label.
        :type sort_by: HeatgridSortBy
        """
        super().__init__(kwargs)

        self_.nesting_display = nesting_display
        self_.sort_by = sort_by
