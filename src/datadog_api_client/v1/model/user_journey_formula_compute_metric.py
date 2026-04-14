# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UserJourneyFormulaComputeMetric(ModelSimple):
    """
    Metric for User Journey formula compute. `__dd.conversion` and `__dd.conversion_rate` accept `count` and `cardinality` as aggregations. `__dd.time_to_convert` accepts `avg`, `median`, `pc75`, `pc95`, `pc98`, `pc99`, `min`, and `max`.

    :param value: Must be one of ["__dd.conversion", "__dd.conversion_rate", "__dd.time_to_convert"].
    :type value: str
    """

    allowed_values = {
        "__dd.conversion",
        "__dd.conversion_rate",
        "__dd.time_to_convert",
    }
    CONVERSION: ClassVar["UserJourneyFormulaComputeMetric"]
    CONVERSION_RATE: ClassVar["UserJourneyFormulaComputeMetric"]
    TIME_TO_CONVERT: ClassVar["UserJourneyFormulaComputeMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UserJourneyFormulaComputeMetric.CONVERSION = UserJourneyFormulaComputeMetric("__dd.conversion")
UserJourneyFormulaComputeMetric.CONVERSION_RATE = UserJourneyFormulaComputeMetric("__dd.conversion_rate")
UserJourneyFormulaComputeMetric.TIME_TO_CONVERT = UserJourneyFormulaComputeMetric("__dd.time_to_convert")
