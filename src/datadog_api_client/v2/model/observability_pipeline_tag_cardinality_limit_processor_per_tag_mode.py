# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode(ModelSimple):
    """
    How the per-tag override is applied. `limit_override` enforces a custom limit on the tag; `excluded` skips the tag from cardinality tracking.

    :param value: Must be one of ["limit_override", "excluded"].
    :type value: str
    """

    allowed_values = {
        "limit_override",
        "excluded",
    }
    LIMIT_OVERRIDE: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode"]
    EXCLUDED: ClassVar["ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode.LIMIT_OVERRIDE = (
    ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode("limit_override")
)
ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode.EXCLUDED = (
    ObservabilityPipelineTagCardinalityLimitProcessorPerTagMode("excluded")
)
