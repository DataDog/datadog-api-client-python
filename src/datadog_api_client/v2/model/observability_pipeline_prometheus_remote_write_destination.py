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
    from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_destination_auth_strategy import (
        ObservabilityPipelinePrometheusRemoteWriteDestinationAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
    from datadog_api_client.v2.model.observability_pipeline_client_tls import ObservabilityPipelineClientTls
    from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_destination_type import (
        ObservabilityPipelinePrometheusRemoteWriteDestinationType,
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


class ObservabilityPipelinePrometheusRemoteWriteDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_destination_auth_strategy import (
            ObservabilityPipelinePrometheusRemoteWriteDestinationAuthStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_buffer_options import ObservabilityPipelineBufferOptions
        from datadog_api_client.v2.model.observability_pipeline_client_tls import ObservabilityPipelineClientTls
        from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_destination_type import (
            ObservabilityPipelinePrometheusRemoteWriteDestinationType,
        )

        return {
            "auth_strategy": (ObservabilityPipelinePrometheusRemoteWriteDestinationAuthStrategy,),
            "buffer": (ObservabilityPipelineBufferOptions,),
            "default_namespace": (str,),
            "endpoint_url_key": (str,),
            "id": (str,),
            "inputs": ([str],),
            "password_key": (str,),
            "tenant_id": (str,),
            "tls": (ObservabilityPipelineClientTls,),
            "token_key": (str,),
            "type": (ObservabilityPipelinePrometheusRemoteWriteDestinationType,),
            "username_key": (str,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "buffer": "buffer",
        "default_namespace": "default_namespace",
        "endpoint_url_key": "endpoint_url_key",
        "id": "id",
        "inputs": "inputs",
        "password_key": "password_key",
        "tenant_id": "tenant_id",
        "tls": "tls",
        "token_key": "token_key",
        "type": "type",
        "username_key": "username_key",
    }

    def __init__(
        self_,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelinePrometheusRemoteWriteDestinationType,
        auth_strategy: Union[ObservabilityPipelinePrometheusRemoteWriteDestinationAuthStrategy, UnsetType] = unset,
        buffer: Union[
            ObservabilityPipelineBufferOptions,
            ObservabilityPipelineDiskBufferOptions,
            ObservabilityPipelineMemoryBufferOptions,
            ObservabilityPipelineMemoryBufferSizeOptions,
            UnsetType,
        ] = unset,
        default_namespace: Union[str, UnsetType] = unset,
        endpoint_url_key: Union[str, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        tenant_id: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineClientTls, UnsetType] = unset,
        token_key: Union[str, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``prometheus_remote_write`` destination forwards metrics to an endpoint that supports the Prometheus Remote Write protocol.

        **Supported pipeline types:** metrics

        :param auth_strategy: The authentication strategy to use for outgoing Prometheus Remote Write requests.
        :type auth_strategy: ObservabilityPipelinePrometheusRemoteWriteDestinationAuthStrategy, optional

        :param buffer: Configuration for buffer settings on destination components.
        :type buffer: ObservabilityPipelineBufferOptions, optional

        :param default_namespace: The default namespace to add as a prefix to metric names that do not already have one.
        :type default_namespace: str, optional

        :param endpoint_url_key: Name of the environment variable or secret that holds the Prometheus Remote Write endpoint URL.
            Defaults to ``DESTINATION_PROMETHEUS_REMOTE_WRITE_ENDPOINT_URL`` (prefixed with ``DD_OP_`` at runtime).
        :type endpoint_url_key: str, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param password_key: Name of the environment variable or secret that holds the password (used when ``auth_strategy`` is ``basic`` ).
        :type password_key: str, optional

        :param tenant_id: The tenant ID to include with outgoing requests. Used by multi-tenant Prometheus Remote Write receivers.
        :type tenant_id: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineClientTls, optional

        :param token_key: Name of the environment variable or secret that holds the bearer token (used when ``auth_strategy`` is ``bearer`` ).
        :type token_key: str, optional

        :param type: The destination type. The value should always be ``prometheus_remote_write``.
        :type type: ObservabilityPipelinePrometheusRemoteWriteDestinationType

        :param username_key: Name of the environment variable or secret that holds the username (used when ``auth_strategy`` is ``basic`` ).
        :type username_key: str, optional
        """
        if auth_strategy is not unset:
            kwargs["auth_strategy"] = auth_strategy
        if buffer is not unset:
            kwargs["buffer"] = buffer
        if default_namespace is not unset:
            kwargs["default_namespace"] = default_namespace
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if tenant_id is not unset:
            kwargs["tenant_id"] = tenant_id
        if tls is not unset:
            kwargs["tls"] = tls
        if token_key is not unset:
            kwargs["token_key"] = token_key
        if username_key is not unset:
            kwargs["username_key"] = username_key
        super().__init__(kwargs)

        self_.id = id
        self_.inputs = inputs
        self_.type = type
