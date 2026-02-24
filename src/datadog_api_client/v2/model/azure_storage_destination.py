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
    from datadog_api_client.v2.model.azure_storage_destination_type import AzureStorageDestinationType
    from datadog_api_client.v2.model.observability_pipeline_disk_buffer_options import (
        ObservabilityPipelineDiskBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_options import (
        ObservabilityPipelineMemoryBufferOptions,
    )
    from datadog_api_client.v2.model.observability_pipeline_memory_buffer_size_options import (
        ObservabilityPipelineMemoryBufferSizeOptions,
    )


class AzureStorageDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.azure_storage_destination_type import AzureStorageDestinationType

        return {
            "blob_prefix": (str,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "connection_string_key": (str,),
            "container_name": (str,),
            "id": (str,),
            "inputs": ([str],),
            "type": (AzureStorageDestinationType,),
        }

    attribute_map = {
        "blob_prefix": "blob_prefix",
        "buffer": "buffer",
        "connection_string_key": "connection_string_key",
        "container_name": "container_name",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        container_name: str,
        id: str,
        inputs: List[str],
        type: AzureStorageDestinationType,
        blob_prefix: Union[str, UnsetType] = unset,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        connection_string_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``azure_storage`` destination forwards logs to an Azure Blob Storage container.

        **Supported pipeline types:** logs

        :param blob_prefix: Optional prefix for blobs written to the container.
        :type blob_prefix: str, optional

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param connection_string_key: Name of the environment variable or secret that holds the Azure Storage connection string.
        :type connection_string_key: str, optional

        :param container_name: The name of the Azure Blob Storage container to store logs in.
        :type container_name: str

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``azure_storage``.
        :type type: AzureStorageDestinationType
        """
        if blob_prefix is not unset:
            kwargs["blob_prefix"] = blob_prefix
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if connection_string_key is not unset:
            kwargs["connection_string_key"] = connection_string_key
        super().__init__(kwargs)

        self_.container_name = container_name
        self_.id = id
        self_.inputs = inputs
        self_.type = type
