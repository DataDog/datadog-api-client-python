# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class ExperimentsCreateExperimentV2RequestDataAttributesTrafficExposureStepsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "duration_ms": (int, none_type),
            "fraction": (float,),
        }

    attribute_map = {
        "duration_ms": "duration_ms",
        "fraction": "fraction",
    }

    def __init__(self_, duration_ms: Union[int, none_type], fraction: float, **kwargs):
        """
        Configured exposure plan rather than wall-clock history. At least two steps must have strictly increasing fractions and no gaps. Warehouse steps start at assignments_start_date and can use different durations. New Datadog plans have at most five steps and a first fraction above zero. Their nonfinal durations must be equal and exclude time paused. Datadog steps start with the experiment. Running warehouse experiments can replace step fractions, durations, and the exposure mode. After start, Datadog exposure plans cannot change through the public API. The final duration is null and its fraction holds until assignment ends.

        :param duration_ms: Positive step duration in milliseconds. Datadog durations exclude pauses. Send null for the final step.
        :type duration_ms: int, none_type

        :param fraction: Fraction of traffic exposed during this step.
        :type fraction: float
        """
        super().__init__(kwargs)

        self_.duration_ms = duration_ms
        self_.fraction = fraction
