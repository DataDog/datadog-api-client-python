# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketSourceFramingChunkedGelfMethod(ModelSimple):
    """
    Byte frames which are chunked GELF messages.

    :param value: If omitted defaults to "chunked_gelf". Must be one of ["chunked_gelf"].
    :type value: str
    """

    allowed_values = {
        "chunked_gelf",
    }
    CHUNKED_GELF: ClassVar["ObservabilityPipelineSocketSourceFramingChunkedGelfMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketSourceFramingChunkedGelfMethod.CHUNKED_GELF = (
    ObservabilityPipelineSocketSourceFramingChunkedGelfMethod("chunked_gelf")
)
