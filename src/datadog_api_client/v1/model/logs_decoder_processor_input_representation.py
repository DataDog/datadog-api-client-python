# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogsDecoderProcessorInputRepresentation(ModelSimple):
    """
    The original representation of input string.

    :param value: Must be one of ["utf_8", "integer"].
    :type value: str
    """

    allowed_values = {
        "utf_8",
        "integer",
    }
    UTF_8: ClassVar["LogsDecoderProcessorInputRepresentation"]
    INTEGER: ClassVar["LogsDecoderProcessorInputRepresentation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsDecoderProcessorInputRepresentation.UTF_8 = LogsDecoderProcessorInputRepresentation("utf_8")
LogsDecoderProcessorInputRepresentation.INTEGER = LogsDecoderProcessorInputRepresentation("integer")
