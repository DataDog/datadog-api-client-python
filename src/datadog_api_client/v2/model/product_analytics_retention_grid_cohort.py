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
    from datadog_api_client.v2.model.product_analytics_retention_grid_cohort_cell import (
        ProductAnalyticsRetentionGridCohortCell,
    )
    from datadog_api_client.v2.model.product_analytics_retention_grid_cohort_type import (
        ProductAnalyticsRetentionGridCohortType,
    )
    from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit


class ProductAnalyticsRetentionGridCohort(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_cohort_cell import (
            ProductAnalyticsRetentionGridCohortCell,
        )
        from datadog_api_client.v2.model.product_analytics_retention_grid_cohort_type import (
            ProductAnalyticsRetentionGridCohortType,
        )
        from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit

        return {
            "cells": ([ProductAnalyticsRetentionGridCohortCell],),
            "cohort_end_time": (int,),
            "cohort_index": (int,),
            "cohort_size": (int,),
            "cohort_start_time": (int,),
            "group_tags": ([str],),
            "name": (str,),
            "type": (ProductAnalyticsRetentionGridCohortType,),
            "unit": ([ProductAnalyticsUnit],),
        }

    attribute_map = {
        "cells": "cells",
        "cohort_end_time": "cohort_end_time",
        "cohort_index": "cohort_index",
        "cohort_size": "cohort_size",
        "cohort_start_time": "cohort_start_time",
        "group_tags": "group_tags",
        "name": "name",
        "type": "type",
        "unit": "unit",
    }

    def __init__(
        self_,
        cells: Union[List[ProductAnalyticsRetentionGridCohortCell], UnsetType] = unset,
        cohort_end_time: Union[int, UnsetType] = unset,
        cohort_index: Union[int, UnsetType] = unset,
        cohort_size: Union[int, UnsetType] = unset,
        cohort_start_time: Union[int, UnsetType] = unset,
        group_tags: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        type: Union[ProductAnalyticsRetentionGridCohortType, UnsetType] = unset,
        unit: Union[List[ProductAnalyticsUnit], UnsetType] = unset,
        **kwargs,
    ):
        """
        One row of the retention grid, holding the results for a single cohort.

        :param cells: The cells of the row, one per return period.
        :type cells: [ProductAnalyticsRetentionGridCohortCell], optional

        :param cohort_end_time: End of the cohort window, in epoch milliseconds.
        :type cohort_end_time: int, optional

        :param cohort_index: Zero-based index of the cohort in the grid.
        :type cohort_index: int, optional

        :param cohort_size: Number of entities in the cohort.
        :type cohort_size: int, optional

        :param cohort_start_time: Start of the cohort window, in epoch milliseconds.
        :type cohort_start_time: int, optional

        :param group_tags: The group-by facet values that identify this row.
        :type group_tags: [str], optional

        :param name: Label identifying the cohort, such as the week it started.
        :type name: str, optional

        :param type: Whether the row holds one cohort's own numbers, or the weighted roll-up across every cohort.
        :type type: ProductAnalyticsRetentionGridCohortType, optional

        :param unit: Unit definitions for the cell values.
        :type unit: [ProductAnalyticsUnit], optional
        """
        if cells is not unset:
            kwargs["cells"] = cells
        if cohort_end_time is not unset:
            kwargs["cohort_end_time"] = cohort_end_time
        if cohort_index is not unset:
            kwargs["cohort_index"] = cohort_index
        if cohort_size is not unset:
            kwargs["cohort_size"] = cohort_size
        if cohort_start_time is not unset:
            kwargs["cohort_start_time"] = cohort_start_time
        if group_tags is not unset:
            kwargs["group_tags"] = group_tags
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)
