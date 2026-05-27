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
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_metrics_destination_compression import (
        ObservabilityPipelineSplunkHecMetricsDestinationCompression,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_splunk_hec_metrics_destination_type import (
        ObservabilityPipelineSplunkHecMetricsDestinationType,
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


class ObservabilityPipelineSplunkHecMetricsDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_splunk_hec_metrics_destination_compression import (
            ObservabilityPipelineSplunkHecMetricsDestinationCompression,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_splunk_hec_metrics_destination_type import (
            ObservabilityPipelineSplunkHecMetricsDestinationType,
        )

        return {
            "buffer": (ObservabilityPipelineBufferOptions,),
            "compression": (ObservabilityPipelineSplunkHecMetricsDestinationCompression,),
            "default_namespace": (str,),
            "endpoint_url_key": (str,),
            "id": (str,),
            "index": (str,),
            "inputs": ([str],),
            "source": (str,),
            "sourcetype": (str,),
            "tls": (ObservabilityPipelineTls,),
            "token_key": (str,),
            "type": (ObservabilityPipelineSplunkHecMetricsDestinationType,),
        }

    attribute_map = {
        "buffer": "buffer",
        "compression": "compression",
        "default_namespace": "default_namespace",
        "endpoint_url_key": "endpoint_url_key",
        "id": "id",
        "index": "index",
        "inputs": "inputs",
        "source": "source",
        "sourcetype": "sourcetype",
        "tls": "tls",
        "token_key": "token_key",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineSplunkHecMetricsDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        compression: Union[ObservabilityPipelineSplunkHecMetricsDestinationCompression, UnsetType] = unset,
        default_namespace: Union[str, UnsetType] = unset,
        endpoint_url_key: Union[str, UnsetType] = unset,
        index: Union[str, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        sourcetype: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        token_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``splunk_hec_metrics`` destination forwards metrics to Splunk using the HTTP Event Collector (HEC).

        **Supported pipeline types:** metrics

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param compression: Compression algorithm applied when sending metrics to Splunk HEC.
        :type compression: ObservabilityPipelineSplunkHecMetricsDestinationCompression, optional

        :param default_namespace: Optional default namespace for metrics sent to Splunk HEC.
        :type default_namespace: str, optional

        :param endpoint_url_key: Name of the environment variable or secret that holds the Splunk HEC endpoint URL.
        :type endpoint_url_key: str, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param index: Optional name of the Splunk index where metrics are written.
        :type index: str, optional

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param source: The Splunk source field value for metric events.
        :type source: str, optional

        :param sourcetype: The Splunk sourcetype to assign to metric events.
        :type sourcetype: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param token_key: Name of the environment variable or secret that holds the Splunk HEC token.
        :type token_key: str, optional

        :param type: The destination type. Always ``splunk_hec_metrics``.
        :type type: ObservabilityPipelineSplunkHecMetricsDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if compression is not unset:
            kwargs["compression"] = compression
        if default_namespace is not unset:
            kwargs["default_namespace"] = default_namespace
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        if index is not unset:
            kwargs["index"] = index
        if source is not unset:
            kwargs["source"] = source
        if sourcetype is not unset:
            kwargs["sourcetype"] = sourcetype
        if tls is not unset:
            kwargs["tls"] = tls
        if token_key is not unset:
            kwargs["token_key"] = token_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
