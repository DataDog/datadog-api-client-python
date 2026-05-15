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
    from datadog_api_client.v2.model.commitments_timeseries_series import CommitmentsTimeseriesSeries
    from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit


class CommitmentsUtilizationTimeseriesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_timeseries_series import CommitmentsTimeseriesSeries
        from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit

        return {
            "series": (CommitmentsTimeseriesSeries,),
            "times": ([int],),
            "unit": (CommitmentsUnit,),
        }

    attribute_map = {
        "series": "series",
        "times": "times",
        "unit": "unit",
    }

    def __init__(
        self_,
        series: CommitmentsTimeseriesSeries,
        times: List[int],
        unit: Union[CommitmentsUnit, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing timeseries utilization metrics for cloud commitment programs.

        :param series: Timeseries data as a map of series names to their corresponding value arrays.
        :type series: CommitmentsTimeseriesSeries

        :param times: Unix timestamps in seconds for the timeseries data points.
        :type times: [int]

        :param unit: Unit metadata for a numeric metric.
        :type unit: CommitmentsUnit, optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)

        self_.series = series
        self_.times = times
