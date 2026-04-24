# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultNetworkLatency(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avg": (float,),
            "max": (float,),
            "min": (float,),
        }

    attribute_map = {
        "avg": "avg",
        "max": "max",
        "min": "min",
    }

    def __init__(
        self_,
        avg: Union[float, UnsetType] = unset,
        max: Union[float, UnsetType] = unset,
        min: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Latency statistics for a network probe.

        :param avg: Average latency in milliseconds.
        :type avg: float, optional

        :param max: Maximum latency in milliseconds.
        :type max: float, optional

        :param min: Minimum latency in milliseconds.
        :type min: float, optional
        """
        if avg is not unset:
            kwargs["avg"] = avg
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        super().__init__(kwargs)
