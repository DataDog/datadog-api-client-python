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
    from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_source_auth_strategy import (
        ObservabilityPipelinePrometheusRemoteWriteSourceAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_mtls_server_tls import ObservabilityPipelineMtlsServerTls
    from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_source_type import (
        ObservabilityPipelinePrometheusRemoteWriteSourceType,
    )
    from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_source_valid_token import (
        ObservabilityPipelinePrometheusRemoteWriteSourceValidToken,
    )


class ObservabilityPipelinePrometheusRemoteWriteSource(ModelNormal):
    validations = {
        "valid_tokens": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_source_auth_strategy import (
            ObservabilityPipelinePrometheusRemoteWriteSourceAuthStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_mtls_server_tls import (
            ObservabilityPipelineMtlsServerTls,
        )
        from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_source_type import (
            ObservabilityPipelinePrometheusRemoteWriteSourceType,
        )
        from datadog_api_client.v2.model.observability_pipeline_prometheus_remote_write_source_valid_token import (
            ObservabilityPipelinePrometheusRemoteWriteSourceValidToken,
        )

        return {
            "address_key": (str,),
            "auth_strategy": (ObservabilityPipelinePrometheusRemoteWriteSourceAuthStrategy,),
            "id": (str,),
            "password_key": (str,),
            "path": (str,),
            "tls": (ObservabilityPipelineMtlsServerTls,),
            "type": (ObservabilityPipelinePrometheusRemoteWriteSourceType,),
            "username_key": (str,),
            "valid_tokens": ([ObservabilityPipelinePrometheusRemoteWriteSourceValidToken],),
        }

    attribute_map = {
        "address_key": "address_key",
        "auth_strategy": "auth_strategy",
        "id": "id",
        "password_key": "password_key",
        "path": "path",
        "tls": "tls",
        "type": "type",
        "username_key": "username_key",
        "valid_tokens": "valid_tokens",
    }

    def __init__(
        self_,
        auth_strategy: ObservabilityPipelinePrometheusRemoteWriteSourceAuthStrategy,
        id: str,
        type: ObservabilityPipelinePrometheusRemoteWriteSourceType,
        address_key: Union[str, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        path: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineMtlsServerTls, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        valid_tokens: Union[List[ObservabilityPipelinePrometheusRemoteWriteSourceValidToken], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``prometheus_remote_write`` source ingests metrics pushed over the Prometheus Remote Write protocol.

        **Supported pipeline types:** metrics

        :param address_key: Name of the environment variable or secret that holds the listen address for the Prometheus Remote Write endpoint.
        :type address_key: str, optional

        :param auth_strategy: HTTP authentication method.
        :type auth_strategy: ObservabilityPipelinePrometheusRemoteWriteSourceAuthStrategy

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param password_key: Name of the environment variable or secret that holds the password (used when ``auth_strategy`` is ``plain`` ).
        :type password_key: str, optional

        :param path: The HTTP path on which the source listens for incoming Prometheus Remote Write requests.
        :type path: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external connecting clients.
        :type tls: ObservabilityPipelineMtlsServerTls, optional

        :param type: The source type. The value should always be ``prometheus_remote_write``.
        :type type: ObservabilityPipelinePrometheusRemoteWriteSourceType

        :param username_key: Name of the environment variable or secret that holds the username (used when ``auth_strategy`` is ``plain`` ).
        :type username_key: str, optional

        :param valid_tokens: A list of tokens that are accepted for authenticating incoming requests. When set,
            the source rejects any request whose token does not match an enabled entry in this list.
        :type valid_tokens: [ObservabilityPipelinePrometheusRemoteWriteSourceValidToken], optional
        """
        if address_key is not unset:
            kwargs["address_key"] = address_key
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if path is not unset:
            kwargs["path"] = path
        if tls is not unset:
            kwargs["tls"] = tls
        if username_key is not unset:
            kwargs["username_key"] = username_key
        if valid_tokens is not unset:
            kwargs["valid_tokens"] = valid_tokens
        super().__init__(kwargs)

        self_.auth_strategy = auth_strategy
        self_.id = id
        self_.type = type
