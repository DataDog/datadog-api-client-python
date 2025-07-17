# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod(ModelSimple):
    """
    Byte frames which are delimited by a newline character.

    :param value: If omitted defaults to "newline_delimited". Must be one of ["newline_delimited"].
    :type value: str
    """

    allowed_values = {
        "newline_delimited",
    }
    NEWLINE_DELIMITED: ClassVar["ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod.NEWLINE_DELIMITED = (
    ObservabilityPipelineSocketSourceFramingNewlineDelimitedMethod("newline_delimited")
)
