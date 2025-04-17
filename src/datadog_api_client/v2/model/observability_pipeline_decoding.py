# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDecoding(ModelSimple):
    """
    The decoding format used to interpret incoming logs.

    :param value: Must be one of ["bytes", "gelf", "json", "syslog"].
    :type value: str
    """

    allowed_values = {
        "bytes",
        "gelf",
        "json",
        "syslog",
    }
    DECODE_BYTES: ClassVar["ObservabilityPipelineDecoding"]
    DECODE_GELF: ClassVar["ObservabilityPipelineDecoding"]
    DECODE_JSON: ClassVar["ObservabilityPipelineDecoding"]
    DECODE_SYSLOG: ClassVar["ObservabilityPipelineDecoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDecoding.DECODE_BYTES = ObservabilityPipelineDecoding("bytes")
ObservabilityPipelineDecoding.DECODE_GELF = ObservabilityPipelineDecoding("gelf")
ObservabilityPipelineDecoding.DECODE_JSON = ObservabilityPipelineDecoding("json")
ObservabilityPipelineDecoding.DECODE_SYSLOG = ObservabilityPipelineDecoding("syslog")
