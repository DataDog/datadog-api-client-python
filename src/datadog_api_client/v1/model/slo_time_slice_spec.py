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
    from datadog_api_client.v1.model.slo_time_slice_condition import SLOTimeSliceCondition


class SLOTimeSliceSpec(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_time_slice_condition import SLOTimeSliceCondition

        return {
            "time_slice": (SLOTimeSliceCondition,),
        }

    attribute_map = {
        "time_slice": "time_slice",
    }

    def __init__(self_, time_slice: SLOTimeSliceCondition, **kwargs):
        """
        A time-slice SLI specification.

        :param time_slice: The time-slice condition, composed of 3 parts: 1. the metric timeseries query, 2. the comparator,
            and 3. the threshold. Optionally, a fourth part, the query interval, can be provided.
        :type time_slice: SLOTimeSliceCondition
        """
        super().__init__(kwargs)

        self_.time_slice = time_slice
