# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_retention_grid_cohort_type import (
        ProductAnalyticsRetentionGridCohortType,
    )


class ProductAnalyticsRetentionGridCohortCell(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_cohort_type import (
            ProductAnalyticsRetentionGridCohortType,
        )

        return {
            "cell_count": (int,),
            "cell_rate": (float,),
            "cell_relative_value_change": (float, none_type),
            "cell_value": (float, none_type),
            "is_partial_data": (bool,),
            "return_period_end_time": (int,),
            "return_period_index": (int,),
            "return_period_start_time": (int,),
            "type": (ProductAnalyticsRetentionGridCohortType,),
        }

    attribute_map = {
        "cell_count": "cell_count",
        "cell_rate": "cell_rate",
        "cell_relative_value_change": "cell_relative_value_change",
        "cell_value": "cell_value",
        "is_partial_data": "is_partial_data",
        "return_period_end_time": "return_period_end_time",
        "return_period_index": "return_period_index",
        "return_period_start_time": "return_period_start_time",
        "type": "type",
    }

    def __init__(
        self_,
        cell_count: Union[int, UnsetType] = unset,
        cell_rate: Union[float, UnsetType] = unset,
        cell_relative_value_change: Union[float, none_type, UnsetType] = unset,
        cell_value: Union[float, none_type, UnsetType] = unset,
        is_partial_data: Union[bool, UnsetType] = unset,
        return_period_end_time: Union[int, UnsetType] = unset,
        return_period_index: Union[int, UnsetType] = unset,
        return_period_start_time: Union[int, UnsetType] = unset,
        type: Union[ProductAnalyticsRetentionGridCohortType, UnsetType] = unset,
        **kwargs,
    ):
        """
        One cell of the retention grid, holding the result for a single cohort over a single return period.
        Aggregated rows omit the time and count fields.

        :param cell_count: Number of entities that returned during the period.
        :type cell_count: int, optional

        :param cell_rate: Fraction of the cohort that returned, between ``0`` and ``1``.
        :type cell_rate: float, optional

        :param cell_relative_value_change: Change in the metric relative to the cohort baseline.
        :type cell_relative_value_change: float, none_type, optional

        :param cell_value: Value of the computed metric, when a metric other than the retention rate is requested.
        :type cell_value: float, none_type, optional

        :param is_partial_data: Whether the return period is still open, so the numbers are not yet final.
        :type is_partial_data: bool, optional

        :param return_period_end_time: End of the return period, in epoch milliseconds.
        :type return_period_end_time: int, optional

        :param return_period_index: Zero-based index of the return period this cell belongs to.
        :type return_period_index: int, optional

        :param return_period_start_time: Start of the return period, in epoch milliseconds.
        :type return_period_start_time: int, optional

        :param type: Whether the row holds one cohort's own numbers, or the weighted roll-up across every cohort.
        :type type: ProductAnalyticsRetentionGridCohortType, optional
        """
        if cell_count is not unset:
            kwargs["cell_count"] = cell_count
        if cell_rate is not unset:
            kwargs["cell_rate"] = cell_rate
        if cell_relative_value_change is not unset:
            kwargs["cell_relative_value_change"] = cell_relative_value_change
        if cell_value is not unset:
            kwargs["cell_value"] = cell_value
        if is_partial_data is not unset:
            kwargs["is_partial_data"] = is_partial_data
        if return_period_end_time is not unset:
            kwargs["return_period_end_time"] = return_period_end_time
        if return_period_index is not unset:
            kwargs["return_period_index"] = return_period_index
        if return_period_start_time is not unset:
            kwargs["return_period_start_time"] = return_period_start_time
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
