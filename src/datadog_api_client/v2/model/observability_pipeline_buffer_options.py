# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineBufferOptions(ModelComposed):
    def __init__(self, **kwargs):
        """
        Configuration for buffer settings on destination components.

        :param max_size: Maximum size of the disk buffer.
        :type max_size: int, optional

        :param type: Specifies the buffer type to configure. This option supports only a disk buffer.
        :type type: ObservabilityPipelineBufferOptionsDiskType, optional

        :param max_events: Maximum events for the memory buffer.
        :type max_events: int, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.observability_pipeline_disk_buffer_options import (
            ObservabilityPipelineDiskBufferOptions,
        )
        from datadog_api_client.v2.model.observability_pipeline_memory_buffer_options import (
            ObservabilityPipelineMemoryBufferOptions,
        )
        from datadog_api_client.v2.model.observability_pipeline_memory_buffer_size_options import (
            ObservabilityPipelineMemoryBufferSizeOptions,
        )

        return {
            "oneOf": [
                ObservabilityPipelineDiskBufferOptions,
                ObservabilityPipelineMemoryBufferOptions,
                ObservabilityPipelineMemoryBufferSizeOptions,
            ],
        }
