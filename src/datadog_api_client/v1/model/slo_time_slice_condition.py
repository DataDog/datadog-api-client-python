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
    from datadog_api_client.v1.model.slo_time_slice_comparator import SLOTimeSliceComparator
    from datadog_api_client.v1.model.slo_time_slice_query import SLOTimeSliceQuery


class SLOTimeSliceCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_time_slice_comparator import SLOTimeSliceComparator
        from datadog_api_client.v1.model.slo_time_slice_query import SLOTimeSliceQuery

        return {
            "comparator": (SLOTimeSliceComparator,),
            "query": (SLOTimeSliceQuery,),
            "threshold": (float,),
        }

    attribute_map = {
        "comparator": "comparator",
        "query": "query",
        "threshold": "threshold",
    }

    def __init__(self_, comparator: SLOTimeSliceComparator, query: SLOTimeSliceQuery, threshold: float, **kwargs):
        """
        The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator,
        and 3. the threshold.

        :param comparator: The comparator used to compare the SLI value to the threshold.
        :type comparator: SLOTimeSliceComparator

        :param query: The queries and formula used to calculate the SLI value.
        :type query: SLOTimeSliceQuery

        :param threshold: The threshold value to which each SLI value will be compared.
        :type threshold: float
        """
        super().__init__(kwargs)

        self_.comparator = comparator
        self_.query = query
        self_.threshold = threshold
