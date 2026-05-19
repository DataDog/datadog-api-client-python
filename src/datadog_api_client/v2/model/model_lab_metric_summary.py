# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ModelLabMetricSummary(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "first_step": (int, none_type),
            "key": (str,),
            "last_step": (int, none_type),
            "latest": (float, none_type),
            "max": (float, none_type),
            "mean": (float, none_type),
            "min": (float, none_type),
            "stddev": (float, none_type),
        }

    attribute_map = {
        "count": "count",
        "first_step": "first_step",
        "key": "key",
        "last_step": "last_step",
        "latest": "latest",
        "max": "max",
        "mean": "mean",
        "min": "min",
        "stddev": "stddev",
    }

    def __init__(
        self_,
        count: int,
        key: str,
        first_step: Union[int, none_type, UnsetType] = unset,
        last_step: Union[int, none_type, UnsetType] = unset,
        latest: Union[float, none_type, UnsetType] = unset,
        max: Union[float, none_type, UnsetType] = unset,
        mean: Union[float, none_type, UnsetType] = unset,
        min: Union[float, none_type, UnsetType] = unset,
        stddev: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Summary statistics for a metric recorded during a Model Lab run.

        :param count: The total number of recorded values.
        :type count: int

        :param first_step: The first step at which the metric was recorded.
        :type first_step: int, none_type, optional

        :param key: The metric name.
        :type key: str

        :param last_step: The last step at which the metric was recorded.
        :type last_step: int, none_type, optional

        :param latest: The most recently recorded value.
        :type latest: float, none_type, optional

        :param max: The maximum recorded value.
        :type max: float, none_type, optional

        :param mean: The mean of recorded values.
        :type mean: float, none_type, optional

        :param min: The minimum recorded value.
        :type min: float, none_type, optional

        :param stddev: The standard deviation of recorded values.
        :type stddev: float, none_type, optional
        """
        if first_step is not unset:
            kwargs["first_step"] = first_step
        if last_step is not unset:
            kwargs["last_step"] = last_step
        if latest is not unset:
            kwargs["latest"] = latest
        if max is not unset:
            kwargs["max"] = max
        if mean is not unset:
            kwargs["mean"] = mean
        if min is not unset:
            kwargs["min"] = min
        if stddev is not unset:
            kwargs["stddev"] = stddev
        super().__init__(kwargs)

        self_.count = count
        self_.key = key
