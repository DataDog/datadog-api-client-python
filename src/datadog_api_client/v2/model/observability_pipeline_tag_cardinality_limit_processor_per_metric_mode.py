# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode(ModelSimple):
    """
    How the per-metric override is applied. `tracked` enforces a custom limit; `excluded` skips the metric entirely.

    :param value: Must be one of ["tracked", "excluded"].
    :type value: str
    """

    allowed_values = {
        "tracked",
        "excluded",
    }
    TRACKED: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode"]
    EXCLUDED: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode.TRACKED = (
    ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode("tracked")
)
ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode.EXCLUDED = (
    ObservabilityPipelineTagCardinalityLimitProcessorPerMetricMode("excluded")
)
