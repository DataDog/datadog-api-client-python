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
    from datadog_api_client.v2.model.observability_pipeline_buffer_options_when_full import (
        ObservabilityPipelineBufferOptionsWhenFull,
    )


class ObservabilityPipelineMemoryBufferOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options_memory_type import (
            ObservabilityPipelineBufferOptionsMemoryType,
        )
        from datadog_api_client.v2.model.observability_pipeline_buffer_options_when_full import (
            ObservabilityPipelineBufferOptionsWhenFull,
        )

        return {
            "max_size": (int,),
            "type": (ObservabilityPipelineBufferOptionsMemoryType,),
            "when_full": (ObservabilityPipelineBufferOptionsWhenFull,),
        }

    attribute_map = {
        "max_size": "max_size",
        "type": "type",
        "when_full": "when_full",
    }

    def __init__(
        self_,
        max_size: int,
        type: Union[ObservabilityPipelineBufferOptionsMemoryType, UnsetType] = unset,
        when_full: Union[ObservabilityPipelineBufferOptionsWhenFull, UnsetType] = unset,
        **kwargs,
    ):
        """
        Options for configuring a memory buffer by byte size.

        :param max_size: Maximum size of the memory buffer.
        :type max_size: int

        :param type: The type of the buffer that will be configured, a memory buffer.
        :type type: ObservabilityPipelineBufferOptionsMemoryType, optional

        :param when_full: Behavior when the buffer is full (block and stop accepting new events, or drop new events)
        :type when_full: ObservabilityPipelineBufferOptionsWhenFull, optional
        """
        if type is not unset:
            kwargs["type"] = type
        if when_full is not unset:
            kwargs["when_full"] = when_full
        super().__init__(kwargs)

        self_.max_size = max_size
