# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineClickhouseDestinationBatchEncodingCodec(ModelSimple):
    """
    The codec used for batch encoding. Only `arrow_stream` is supported.

    :param value: If omitted defaults to "arrow_stream". Must be one of ["arrow_stream"].
    :type value: str
    """

    allowed_values = {
        "arrow_stream",
    }
    ARROW_STREAM: ClassVar["ObservabilityPipelineClickhouseDestinationBatchEncodingCodec"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineClickhouseDestinationBatchEncodingCodec.ARROW_STREAM = (
    ObservabilityPipelineClickhouseDestinationBatchEncodingCodec("arrow_stream")
)
