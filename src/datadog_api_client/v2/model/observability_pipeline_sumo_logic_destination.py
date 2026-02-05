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
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination_encoding import (
        ObservabilityPipelineSumoLogicDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination_header_custom_fields_item import (
        ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem,
    )
    from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination_type import (
        ObservabilityPipelineSumoLogicDestinationType,
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


class ObservabilityPipelineSumoLogicDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination_encoding import (
            ObservabilityPipelineSumoLogicDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination_header_custom_fields_item import (
            ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem,
        )
        from datadog_api_client.v2.model.observability_pipeline_sumo_logic_destination_type import (
            ObservabilityPipelineSumoLogicDestinationType,
        )

        return {
            "buffer": (ObservabilityPipelineBufferOptions,),
            "encoding": (ObservabilityPipelineSumoLogicDestinationEncoding,),
            "header_custom_fields": ([ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem],),
            "header_host_name": (str,),
            "header_source_category": (str,),
            "header_source_name": (str,),
            "id": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineSumoLogicDestinationType,),
        }

    attribute_map = {
        "buffer": "buffer",
        "encoding": "encoding",
        "header_custom_fields": "header_custom_fields",
        "header_host_name": "header_host_name",
        "header_source_category": "header_source_category",
        "header_source_name": "header_source_name",
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineSumoLogicDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        encoding: Union[ObservabilityPipelineSumoLogicDestinationEncoding, UnsetType] = unset,
        header_custom_fields: Union[
            List[ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem], UnsetType
        ] = unset,
        header_host_name: Union[str, UnsetType] = unset,
        header_source_category: Union[str, UnsetType] = unset,
        header_source_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``sumo_logic`` destination forwards logs to Sumo Logic.

        **Supported pipeline types:** logs

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param encoding: The output encoding format.
        :type encoding: ObservabilityPipelineSumoLogicDestinationEncoding, optional

        :param header_custom_fields: A list of custom headers to include in the request to Sumo Logic.
        :type header_custom_fields: [ObservabilityPipelineSumoLogicDestinationHeaderCustomFieldsItem], optional

        :param header_host_name: Optional override for the host name header.
        :type header_host_name: str, optional

        :param header_source_category: Optional override for the source category header.
        :type header_source_category: str, optional

        :param header_source_name: Optional override for the source name header.
        :type header_source_name: str, optional

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param type: The destination type. The value should always be ``sumo_logic``.
        :type type: ObservabilityPipelineSumoLogicDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if encoding is not unset:
            kwargs["encoding"] = encoding
        if header_custom_fields is not unset:
            kwargs["header_custom_fields"] = header_custom_fields
        if header_host_name is not unset:
            kwargs["header_host_name"] = header_host_name
        if header_source_category is not unset:
            kwargs["header_source_category"] = header_source_category
        if header_source_name is not unset:
            kwargs["header_source_name"] = header_source_name
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
