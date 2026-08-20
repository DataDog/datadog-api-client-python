# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProductAnalyticsElapsedTime(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "avg": (int,),
            "max": (int,),
            "min": (int,),
        }

    attribute_map = {
        "avg": "avg",
        "max": "max",
        "min": "min",
    }

    def __init__(self_, avg: int, max: int, min: int, **kwargs):
        """
        Elapsed time statistics (min/max/avg in milliseconds).

        :param avg: Average elapsed time to reach the next step, in milliseconds.
        :type avg: int

        :param max: Maximum elapsed time to reach the next step, in milliseconds.
        :type max: int

        :param min: Minimum elapsed time to reach the next step, in milliseconds.
        :type min: int
        """
        super().__init__(kwargs)

        self_.avg = avg
        self_.max = max
        self_.min = min
