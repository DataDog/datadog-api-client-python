# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ModelLabNumericRange(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "max": (float,),
            "min": (float,),
        }

    attribute_map = {
        "max": "max",
        "min": "min",
    }

    def __init__(self_, max: float, min: float, **kwargs):
        """
        The numeric range of values for a facet.

        :param max: The maximum value.
        :type max: float

        :param min: The minimum value.
        :type min: float
        """
        super().__init__(kwargs)

        self_.max = max
        self_.min = min
