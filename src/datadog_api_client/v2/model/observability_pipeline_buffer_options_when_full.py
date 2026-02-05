# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineBufferOptionsWhenFull(ModelSimple):
    """
    Behavior when the buffer is full (block and stop accepting new events, or drop new events)

    :param value: If omitted defaults to "block". Must be one of ["block", "drop_newest"].
    :type value: str
    """

    allowed_values = {
        "block",
        "drop_newest",
    }
    BLOCK: ClassVar["ObservabilityPipelineBufferOptionsWhenFull"]
    DROP_NEWEST: ClassVar["ObservabilityPipelineBufferOptionsWhenFull"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineBufferOptionsWhenFull.BLOCK = ObservabilityPipelineBufferOptionsWhenFull("block")
ObservabilityPipelineBufferOptionsWhenFull.DROP_NEWEST = ObservabilityPipelineBufferOptionsWhenFull("drop_newest")
