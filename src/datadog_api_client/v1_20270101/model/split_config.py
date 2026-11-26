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
    from datadog_api_client.v1_20270101.model.calendar_shift_split_config import CalendarShiftSplitConfig
    from datadog_api_client.v1_20270101.model.split_config_sort import SplitConfigSort
    from datadog_api_client.v1_20270101.model.split_dimension import SplitDimension
    from datadog_api_client.v1_20270101.model.split_vector_tag_filter import SplitVectorTagFilter


class SplitConfig(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.calendar_shift_split_config import CalendarShiftSplitConfig
        from datadog_api_client.v1_20270101.model.split_config_sort import SplitConfigSort
        from datadog_api_client.v1_20270101.model.split_dimension import SplitDimension
        from datadog_api_client.v1_20270101.model.split_vector_tag_filter import SplitVectorTagFilter

        return {
            "calendar_shift": (CalendarShiftSplitConfig,),
            "limit": (float,),
            "sort": (SplitConfigSort,),
            "split_dimensions": ([SplitDimension],),
            "static_splits": ([[SplitVectorTagFilter]],),
        }

    attribute_map = {
        "calendar_shift": "calendar_shift",
        "limit": "limit",
        "sort": "sort",
        "split_dimensions": "split_dimensions",
        "static_splits": "static_splits",
    }

    def __init__(
        self_,
        limit: float,
        sort: SplitConfigSort,
        split_dimensions: List[SplitDimension],
        calendar_shift: Union[CalendarShiftSplitConfig, UnsetType] = unset,
        static_splits: Union[List[List[SplitVectorTagFilter]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param calendar_shift: Test-only generated schema for the dashboard versioning proof of concept.
        :type calendar_shift: CalendarShiftSplitConfig, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: SplitConfigSort

        :param split_dimensions: Test-only generated schema for the dashboard versioning proof of concept.
        :type split_dimensions: [SplitDimension]

        :param static_splits: Test-only generated schema for the dashboard versioning proof of concept.
        :type static_splits: [[SplitVectorTagFilter]], optional
        """
        if calendar_shift is not unset:
            kwargs["calendar_shift"] = calendar_shift
        if static_splits is not unset:
            kwargs["static_splits"] = static_splits
        super().__init__(kwargs)

        self_.limit = limit
        self_.sort = sort
        self_.split_dimensions = split_dimensions
