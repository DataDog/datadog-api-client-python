# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDedupeProcessorType(ModelSimple):
    """
    The processor type. The value should always be `dedupe`.

    :param value: If omitted defaults to "dedupe". Must be one of ["dedupe"].
    :type value: str
    """

    allowed_values = {
        "dedupe",
    }
    DEDUPE: ClassVar["ObservabilityPipelineDedupeProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDedupeProcessorType.DEDUPE = ObservabilityPipelineDedupeProcessorType("dedupe")
