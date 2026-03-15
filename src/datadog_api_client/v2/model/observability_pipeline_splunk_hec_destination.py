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
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_destination_encoding import (
        ObservabilityPipelineSplunkHecDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_destination_type import (
        ObservabilityPipelineSplunkHecDestinationType,
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


class ObservabilityPipelineSplunkHecDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_splunk_hec_destination_encoding import (
            ObservabilityPipelineSplunkHecDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_splunk_hec_destination_type import (
            ObservabilityPipelineSplunkHecDestinationType,
        )

        return {
            "auto_extract_timestamp": (bool,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "encoding": (ObservabilityPipelineSplunkHecDestinationEncoding,),
            "endpoint_url_key": (str,),
            "id": (str,),
            "index": (str,),
            "inputs": ([str],),
            "sourcetype": (str,),
            "token_key": (str,),
            "type": (ObservabilityPipelineSplunkHecDestinationType,),
        }

    attribute_map = {
        "auto_extract_timestamp": "auto_extract_timestamp",
        "buffer": "buffer",
        "encoding": "encoding",
        "endpoint_url_key": "endpoint_url_key",
        "id": "id",
        "index": "index",
        "inputs": "inputs",
        "sourcetype": "sourcetype",
        "token_key": "token_key",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineSplunkHecDestinationType,
        auto_extract_timestamp: Union[bool, UnsetType] = unset,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        encoding: Union[ObservabilityPipelineSplunkHecDestinationEncoding, UnsetType] = unset,
        endpoint_url_key: Union[str, UnsetType] = unset,
        index: Union[str, UnsetType] = unset,
        sourcetype: Union[str, UnsetType] = unset,
        token_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``splunk_hec`` destination forwards logs to Splunk using the HTTP Event Collector (HEC).

        **Supported pipeline types:** logs

        :param auto_extract_timestamp: If ``true`` , Splunk tries to extract timestamps from incoming log events.
            If ``false`` , Splunk assigns the time the event was received.
        :type auto_extract_timestamp: bool, optional

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineSplunkHecDestinationEncoding, optional

        :param endpoint_url_key: Name of the environment variable or secret that holds the Splunk HEC endpoint URL.
        :type endpoint_url_key: str, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param index: Optional name of the Splunk index where logs are written.
        :type index: str, optional

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param sourcetype: The Splunk sourcetype to assign to log events.
        :type sourcetype: str, optional

        :param token_key: Name of the environment variable or secret that holds the Splunk HEC token.
        :type token_key: str, optional

        :param type: The destination type. Always ``splunk_hec``.
        :type type: ObservabilityPipelineSplunkHecDestinationType
        """
        if auto_extract_timestamp is not unset:
            kwargs["auto_extract_timestamp"] = auto_extract_timestamp
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if encoding is not unset:
            kwargs["encoding"] = encoding
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        if index is not unset:
            kwargs["index"] = index
        if sourcetype is not unset:
            kwargs["sourcetype"] = sourcetype
        if token_key is not unset:
            kwargs["token_key"] = token_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
