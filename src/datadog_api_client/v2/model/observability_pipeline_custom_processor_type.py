# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineCustomProcessorType(ModelSimple):
    """
    The processor type. The value should always be `custom_processor`.

    :param value: If omitted defaults to "custom_processor". Must be one of ["custom_processor"].
    :type value: str
    """

    allowed_values = {
        "custom_processor",
    }
    CUSTOM_PROCESSOR: ClassVar["ObservabilityPipelineCustomProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineCustomProcessorType.CUSTOM_PROCESSOR = ObservabilityPipelineCustomProcessorType("custom_processor")
