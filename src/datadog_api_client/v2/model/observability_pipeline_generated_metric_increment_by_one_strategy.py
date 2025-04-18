# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGeneratedMetricIncrementByOneStrategy(ModelSimple):
    """
    Increments the metric by 1 for each matching event.

    :param value: If omitted defaults to "increment_by_one". Must be one of ["increment_by_one"].
    :type value: str
    """

    allowed_values = {
        "increment_by_one",
    }
    INCREMENT_BY_ONE: ClassVar["ObservabilityPipelineGeneratedMetricIncrementByOneStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGeneratedMetricIncrementByOneStrategy.INCREMENT_BY_ONE = (
    ObservabilityPipelineGeneratedMetricIncrementByOneStrategy("increment_by_one")
)
