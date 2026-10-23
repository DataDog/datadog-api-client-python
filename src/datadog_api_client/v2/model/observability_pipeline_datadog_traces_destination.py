# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_datadog_traces_destination_type import (
        ObservabilityPipelineDatadogTracesDestinationType,
    )
    from datadog_api_client.v2.model.observability_pipeline_disk_buffer_options import (
        ObservabilityPipelineDiskBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_options import (
        ObservabilityPipelineMemoryBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_size_options import (
        ObservabilityPipelineMemoryBufferSizeOptions,
    )


class ObservabilityPipelineDatadogTracesDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_datadog_traces_destination_type import (
            ObservabilityPipelineDatadogTracesDestinationType,
        )

        return {
            "buffer": (ObservabilityPipelineBufferOptions,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineDatadogTracesDestinationType,),
        }

    attribute_map = {
        "buffer": "buffer",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineDatadogTracesDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        The ``datadog_traces`` destination forwards traces to Datadog.

        **Supported pipeline types:** traces

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the input for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``datadog_traces``.
        :type type: ObservabilityPipelineDatadogTracesDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
