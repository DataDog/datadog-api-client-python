# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_buffer_options_memory_type import (
        ObservabilityPipelineBufferOptionsMemoryType,
    )


class ObservabilityPipelineMemoryBufferSizeOptions(ModelNormal):
    validations = {
        "max_events": {
            "inclusive_maximum": 268435456,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options_memory_type import (
            ObservabilityPipelineBufferOptionsMemoryType,
        )

        return {
            "max_events": (int,),
            "type": (ObservabilityPipelineBufferOptionsMemoryType,),
        }

    attribute_map = {
        "max_events": "max_events",
        "type": "type",
    }

    def __init__(
        self_,
        max_events: Union[int, UnsetType] = unset,
        type: Union[ObservabilityPipelineBufferOptionsMemoryType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options for configuring a memory buffer by queue length.

        :param max_events: The ``ObservabilityPipelineMemoryBufferSizeOptions`` ``max_events``.
        :type max_events: int, optional

        :param type: The type of the buffer that will be configured, a memory buffer.
        :type type: ObservabilityPipelineBufferOptionsMemoryType, optional
        """
        if max_events is not unset:
            kwargs["max_events"] = max_events
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
