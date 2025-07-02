# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketDestinationFramingBytesMethod(ModelSimple):
    """
    The definition of `ObservabilityPipelineSocketDestinationFramingBytesMethod` object.

    :param value: If omitted defaults to "bytes". Must be one of ["bytes"].
    :type value: str
    """

    allowed_values = {
        "bytes",
    }
    BYTES: ClassVar["ObservabilityPipelineSocketDestinationFramingBytesMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketDestinationFramingBytesMethod.BYTES = (
    ObservabilityPipelineSocketDestinationFramingBytesMethod("bytes")
)
