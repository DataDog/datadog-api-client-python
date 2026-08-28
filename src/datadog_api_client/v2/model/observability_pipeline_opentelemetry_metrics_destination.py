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
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_opentelemetry_metrics_destination_type import (
        ObservabilityPipelineOpentelemetryMetricsDestinationType,
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


class ObservabilityPipelineOpentelemetryMetricsDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_opentelemetry_metrics_destination_type import (
            ObservabilityPipelineOpentelemetryMetricsDestinationType,
        )

        return {
            "buffer": (ObservabilityPipelineBufferOptions,),
            "http_client_uri_key": (str,),
            "id": (str,),
            "inputs": ([str],),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineOpentelemetryMetricsDestinationType,),
        }

    attribute_map = {
        "buffer": "buffer",
        "http_client_uri_key": "http_client_uri_key",
        "id": "id",
        "inputs": "inputs",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineOpentelemetryMetricsDestinationType,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        http_client_uri_key: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``opentelemetry`` destination forwards metrics using the OpenTelemetry Protocol (OTLP) over HTTP.

        **Supported pipeline types:** metrics

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param http_client_uri_key: Environment variable name containing the URI of the OTLP HTTP endpoint to send metrics to.
        :type http_client_uri_key: str, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. Always ``opentelemetry``.
        :type type: ObservabilityPipelineOpentelemetryMetricsDestinationType
        """
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if http_client_uri_key is not unset:
            kwargs["http_client_uri_key"] = http_client_uri_key
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
