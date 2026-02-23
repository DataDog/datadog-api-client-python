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
    from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_region import (
        ObservabilityPipelineSentinelOneDestinationRegion,
    )
    from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_type import (
        ObservabilityPipelineSentinelOneDestinationType,
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


class ObservabilityPipelineSentinelOneDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_region import (
            ObservabilityPipelineSentinelOneDestinationRegion,
        )
        from datadog_api_client.v2.model.observability_pipeline_sentinel_one_destination_type import (
            ObservabilityPipelineSentinelOneDestinationType,
        )

        return {
            "buffer": (ObservabilityPipelineBufferOptions,),
            "id": (str,),
            "inputs": ([str],),
            "region": (ObservabilityPipelineSentinelOneDestinationRegion,),
            "token_key": (str,),
            "type": (ObservabilityPipelineSentinelOneDestinationType,),
        }

    attribute_map = {
        "buffer": "buffer",
        "id": "id",
        "inputs": "inputs",
        "region": "region",
        "token_key": "token_key",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        region: ObservabilityPipelineSentinelOneDestinationRegion,
        type: ObservabilityPipelineSentinelOneDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        token_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``sentinel_one`` destination sends logs to SentinelOne.

        **Supported pipeline types:** logs

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param region: The SentinelOne region to send logs to.
        :type region: ObservabilityPipelineSentinelOneDestinationRegion

        :param token_key: Name of the environment variable or secret that holds the SentinelOne API token.
        :type token_key: str, optional

        :param type: The destination type. The value should always be ``sentinel_one``.
        :type type: ObservabilityPipelineSentinelOneDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if token_key is not unset:
            kwargs["token_key"] = token_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.region = region
        self_.type = type
