# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineBufferOptionsDiskType(ModelSimple):
    """
    The type of the buffer that will be configured, a disk buffer.

    :param value: If omitted defaults to "disk". Must be one of ["disk"].
    :type value: str
    """

    allowed_values = {
        "disk",
    }
    DISK: ClassVar["ObservabilityPipelineBufferOptionsDiskType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineBufferOptionsDiskType.DISK = ObservabilityPipelineBufferOptionsDiskType("disk")
