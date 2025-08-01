# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsDecoderProcessorType(ModelSimple):
    """
    Type of logs decoder processor.

    :param value: If omitted defaults to "decoder-processor". Must be one of ["decoder-processor"].
    :type value: str
    """

    allowed_values = {
        "decoder-processor",
    }
    DECODER_PROCESSOR: ClassVar["LogsDecoderProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsDecoderProcessorType.DECODER_PROCESSOR = LogsDecoderProcessorType("decoder-processor")
