# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsDecoderProcessorBinaryToTextEncoding(ModelSimple):
    """
    The encoding used to represent the binary data.

    :param value: Must be one of ["base64", "base16"].
    :type value: str
    """

    allowed_values = {
        "base64",
        "base16",
    }
    BASE64: ClassVar["LogsDecoderProcessorBinaryToTextEncoding"]
    BASE16: ClassVar["LogsDecoderProcessorBinaryToTextEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsDecoderProcessorBinaryToTextEncoding.BASE64 = LogsDecoderProcessorBinaryToTextEncoding("base64")
LogsDecoderProcessorBinaryToTextEncoding.BASE16 = LogsDecoderProcessorBinaryToTextEncoding("base16")
