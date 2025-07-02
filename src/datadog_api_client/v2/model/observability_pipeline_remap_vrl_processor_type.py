# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineRemapVrlProcessorType(ModelSimple):
    """
    The processor type. The value should always be `remap_vrl`.

    :param value: If omitted defaults to "remap_vrl". Must be one of ["remap_vrl"].
    :type value: str
    """

    allowed_values = {
        "remap_vrl",
    }
    REMAP_VRL: ClassVar["ObservabilityPipelineRemapVrlProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineRemapVrlProcessorType.REMAP_VRL = ObservabilityPipelineRemapVrlProcessorType("remap_vrl")
