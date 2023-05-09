# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_response_series import TimeseriesResponseSeries


class TimeseriesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_response_series import TimeseriesResponseSeries

        return {
            "series": ([TimeseriesResponseSeries],),
            "times": ([int],),
            "values": ([[float, none_type]],),
        }

    attribute_map = {
        "series": "series",
        "times": "times",
        "values": "values",
    }

    def __init__(
        self_,
        series: Union[List[TimeseriesResponseSeries], UnsetType] = unset,
        times: Union[List[int], UnsetType] = unset,
        values: Union[List[List[float]], UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing a timeseries response.

        :param series: Array of response series. The index here corresponds to the index in the ``formulas`` or ``queries`` array from the request.
        :type series: [TimeseriesResponseSeries], optional

        :param times: Array of times, 1-1 match with individual values arrays.
        :type times: [int], optional

        :param values: Array of value-arrays. The index here corresponds to the index in the ``formulas`` or ``queries`` array from the request.
        :type values: [[float, none_type]], optional
        """
        if series is not unset:
            kwargs["series"] = series
        if times is not unset:
            kwargs["times"] = times
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
