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


class SyntheticsTestResultNetstatsHops(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avg": (float,),
            "max": (int,),
            "min": (int,),
        }

    attribute_map = {
        "avg": "avg",
        "max": "max",
        "min": "min",
    }

    def __init__(
        self_,
        avg: Union[float, UnsetType] = unset,
        max: Union[int, UnsetType] = unset,
        min: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Statistics about the number of hops for a network test.

        :param avg: Average number of hops.
        :type avg: float, optional

        :param max: Maximum number of hops.
        :type max: int, optional

        :param min: Minimum number of hops.
        :type min: int, optional
        """
        if avg is not unset:
            kwargs["avg"] = avg
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        super().__init__(kwargs)
