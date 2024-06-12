# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.slo_time_slice_comparator import SLOTimeSliceComparator
    from datadog_api_client.v1.model.slo_time_slice_query import SLOTimeSliceQuery
    from datadog_api_client.v1.model.slo_time_slice_interval import SLOTimeSliceInterval


class SLOTimeSliceCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_time_slice_comparator import SLOTimeSliceComparator
        from datadog_api_client.v1.model.slo_time_slice_query import SLOTimeSliceQuery
        from datadog_api_client.v1.model.slo_time_slice_interval import SLOTimeSliceInterval

        return {
            "comparator": (SLOTimeSliceComparator,),
            "query": (SLOTimeSliceQuery,),
            "query_interval_seconds": (SLOTimeSliceInterval,),
            "threshold": (float,),
        }

    attribute_map = {
        "comparator": "comparator",
        "query": "query",
        "query_interval_seconds": "query_interval_seconds",
        "threshold": "threshold",
    }

    def __init__(
        self_,
        comparator: SLOTimeSliceComparator,
        query: SLOTimeSliceQuery,
        threshold: float,
        query_interval_seconds: Union[SLOTimeSliceInterval, UnsetType] = unset,
        **kwargs,
    ):
        """
        The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator,
        and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.

        :param comparator: The comparator used to compare the SLI value to the threshold.
        :type comparator: SLOTimeSliceComparator

        :param query: The queries and formula used to calculate the SLI value.
        :type query: SLOTimeSliceQuery

        :param query_interval_seconds: The interval used when querying data, which defines the size of a time slice.
            Two values are allowed: 60 (1 minute) and 300 (5 minutes).
            If not provided, the value defaults to 300 (5 minutes).
        :type query_interval_seconds: SLOTimeSliceInterval, optional

        :param threshold: The threshold value to which each SLI value will be compared.
        :type threshold: float
        """
        if query_interval_seconds is not unset:
            kwargs["query_interval_seconds"] = query_interval_seconds
        super().__init__(kwargs)

        self_.comparator = comparator
        self_.query = query
        self_.threshold = threshold
