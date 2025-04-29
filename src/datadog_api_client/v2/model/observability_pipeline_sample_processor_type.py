# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSampleProcessorType(ModelSimple):
    """
    The processor type. The value should always be `sample`.

    :param value: If omitted defaults to "sample". Must be one of ["sample"].
    :type value: str
    """

    allowed_values = {
        "sample",
    }
    SAMPLE: ClassVar["ObservabilityPipelineSampleProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSampleProcessorType.SAMPLE = ObservabilityPipelineSampleProcessorType("sample")
