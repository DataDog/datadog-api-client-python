# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LongTaskMetricStats(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "average": (float,),
            "max": (float,),
            "min": (float,),
        }

    attribute_map = {
        "average": "average",
        "max": "max",
        "min": "min",
    }

    def __init__(self_, average: float, max: float, min: float, **kwargs):
        """
        Statistical distribution (average, min, max) of a long task metric across sampled views.

        :param average: Average value across sampled views.
        :type average: float

        :param max: Maximum value across sampled views.
        :type max: float

        :param min: Minimum value across sampled views.
        :type min: float
        """
        super().__init__(kwargs)

        self_.average = average
        self_.max = max
        self_.min = min
