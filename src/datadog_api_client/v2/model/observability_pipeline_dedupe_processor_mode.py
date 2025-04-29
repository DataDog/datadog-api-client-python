# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDedupeProcessorMode(ModelSimple):
    """
    The deduplication mode to apply to the fields.

    :param value: Must be one of ["match", "ignore"].
    :type value: str
    """

    allowed_values = {
        "match",
        "ignore",
    }
    MATCH: ClassVar["ObservabilityPipelineDedupeProcessorMode"]
    IGNORE: ClassVar["ObservabilityPipelineDedupeProcessorMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDedupeProcessorMode.MATCH = ObservabilityPipelineDedupeProcessorMode("match")
ObservabilityPipelineDedupeProcessorMode.IGNORE = ObservabilityPipelineDedupeProcessorMode("ignore")
