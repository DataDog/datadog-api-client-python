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
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_api_version import (
        ObservabilityPipelineElasticsearchDestinationApiVersion,
    )
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_auth import (
        ObservabilityPipelineElasticsearchDestinationAuth,
    )
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_data_stream import (
        ObservabilityPipelineElasticsearchDestinationDataStream,
    )
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_type import (
        ObservabilityPipelineElasticsearchDestinationType,
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


class ObservabilityPipelineElasticsearchDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_api_version import (
            ObservabilityPipelineElasticsearchDestinationApiVersion,
        )
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_auth import (
            ObservabilityPipelineElasticsearchDestinationAuth,
        )
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_data_stream import (
            ObservabilityPipelineElasticsearchDestinationDataStream,
        )
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_type import (
            ObservabilityPipelineElasticsearchDestinationType,
        )

        return {
            "api_version": (ObservabilityPipelineElasticsearchDestinationApiVersion,),
            "auth": (ObservabilityPipelineElasticsearchDestinationAuth,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "bulk_index": (str,),
            "data_stream": (ObservabilityPipelineElasticsearchDestinationDataStream,),
            "endpoint_url_key": (str,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineElasticsearchDestinationType,),
        }

    attribute_map = {
        "api_version": "api_version",
        "auth": "auth",
        "buffer": "buffer",
        "bulk_index": "bulk_index",
        "data_stream": "data_stream",
        "endpoint_url_key": "endpoint_url_key",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineElasticsearchDestinationType,
        api_version: Union[ObservabilityPipelineElasticsearchDestinationApiVersion, UnsetType] = unset,
        auth: Union[ObservabilityPipelineElasticsearchDestinationAuth, UnsetType] = unset,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        bulk_index: Union[str, UnsetType] = unset,
        data_stream: Union[ObservabilityPipelineElasticsearchDestinationDataStream, UnsetType] = unset,
        endpoint_url_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``elasticsearch`` destination writes logs to an Elasticsearch cluster.

        **Supported pipeline types:** logs

        :param api_version: The Elasticsearch API version to use. Set to ``auto`` to auto-detect.
        :type api_version: ObservabilityPipelineElasticsearchDestinationApiVersion, optional

        :param auth: Authentication settings for the Elasticsearch destination.
            When ``strategy`` is ``basic`` , use ``username_key`` and ``password_key`` to reference credentials stored in environment variables or secrets.
        :type auth: ObservabilityPipelineElasticsearchDestinationAuth, optional

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param bulk_index: The index to write logs to in Elasticsearch.
        :type bulk_index: str, optional

        :param data_stream: Configuration options for writing to Elasticsearch Data Streams instead of a fixed index.
        :type data_stream: ObservabilityPipelineElasticsearchDestinationDataStream, optional

        :param endpoint_url_key: Name of the environment variable or secret that holds the Elasticsearch endpoint URL.
        :type endpoint_url_key: str, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``elasticsearch``.
        :type type: ObservabilityPipelineElasticsearchDestinationType
        """
        if api_version is not unset:
            kwargs["api_version"] = api_version
        if auth is not unset:
            kwargs["auth"] = auth
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if bulk_index is not unset:
            kwargs["bulk_index"] = bulk_index
        if data_stream is not unset:
            kwargs["data_stream"] = data_stream
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
