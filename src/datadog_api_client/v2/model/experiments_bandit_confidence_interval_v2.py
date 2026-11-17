# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsBanditConfidenceIntervalV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "lower": (float,),
            "upper": (float,),
        }

    attribute_map = {
        "lower": "lower",
        "upper": "upper",
    }

    def __init__(self_, lower: float, upper: float, **kwargs):
        """
        A central interval around point_estimate at confidence_level.

        :param lower: Lower bound of the interval.
        :type lower: float

        :param upper: Upper bound of the interval.
        :type upper: float
        """
        super().__init__(kwargs)

        self_.lower = lower
        self_.upper = upper
