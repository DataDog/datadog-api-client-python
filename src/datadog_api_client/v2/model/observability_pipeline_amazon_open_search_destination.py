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
    from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_auth import (
        ObservabilityPipelineAmazonOpenSearchDestinationAuth,
    )
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_type import (
        ObservabilityPipelineAmazonOpenSearchDestinationType,
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


class ObservabilityPipelineAmazonOpenSearchDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_auth import (
            ObservabilityPipelineAmazonOpenSearchDestinationAuth,
        )
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_amazon_open_search_destination_type import (
            ObservabilityPipelineAmazonOpenSearchDestinationType,
        )

        return {
            "auth": (ObservabilityPipelineAmazonOpenSearchDestinationAuth,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "bulk_index": (str,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineAmazonOpenSearchDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "buffer": "buffer",
        "bulk_index": "bulk_index",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        auth: ObservabilityPipelineAmazonOpenSearchDestinationAuth,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineAmazonOpenSearchDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        bulk_index: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``amazon_opensearch`` destination writes logs to Amazon OpenSearch.

        :param auth: Authentication settings for the Amazon OpenSearch destination.
            The ``strategy`` field determines whether basic or AWS-based authentication is used.
        :type auth: ObservabilityPipelineAmazonOpenSearchDestinationAuth

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param bulk_index: The index to write logs to.
        :type bulk_index: str, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``amazon_opensearch``.
        :type type: ObservabilityPipelineAmazonOpenSearchDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if bulk_index is not unset:
            kwargs["bulk_index"] = bulk_index
        super().__init__(kwargs)

        self_.auth = auth
        self_.id = id
        self_.inputs = inputs
        self_.type = type
