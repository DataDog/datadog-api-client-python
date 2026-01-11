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


class FunnelResponseElapsedTime(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avg": (int,),
            "max": (int,),
            "min": (int,),
            "p5": (int,),
            "p50": (int,),
            "p95": (int,),
        }

    attribute_map = {
        "avg": "avg",
        "max": "max",
        "min": "min",
        "p5": "p5",
        "p50": "p50",
        "p95": "p95",
    }

    def __init__(
        self_,
        avg: Union[int, UnsetType] = unset,
        max: Union[int, UnsetType] = unset,
        min: Union[int, UnsetType] = unset,
        p5: Union[int, UnsetType] = unset,
        p50: Union[int, UnsetType] = unset,
        p95: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param avg:
        :type avg: int, optional

        :param max:
        :type max: int, optional

        :param min:
        :type min: int, optional

        :param p5:
        :type p5: int, optional

        :param p50:
        :type p50: int, optional

        :param p95:
        :type p95: int, optional
        """
        if avg is not unset:
            kwargs["avg"] = avg
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        if p5 is not unset:
            kwargs["p5"] = p5
        if p50 is not unset:
            kwargs["p50"] = p50
        if p95 is not unset:
            kwargs["p95"] = p95
        super().__init__(kwargs)
