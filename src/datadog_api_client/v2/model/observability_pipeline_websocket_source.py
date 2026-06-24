# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_auth_strategy import (
        ObservabilityPipelineWebsocketSourceAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls import (
        ObservabilityPipelineWebsocketSourceTls,
    )
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_type import (
        ObservabilityPipelineWebsocketSourceType,
    )
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_enabled import (
        ObservabilityPipelineWebsocketSourceTlsEnabled,
    )
    from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls_with_client_cert import (
        ObservabilityPipelineWebsocketSourceTlsWithClientCert,
    )


class ObservabilityPipelineWebsocketSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_auth_strategy import (
            ObservabilityPipelineWebsocketSourceAuthStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_tls import (
            ObservabilityPipelineWebsocketSourceTls,
        )
        from datadog_api_client.v2.model.observability_pipeline_websocket_source_type import (
            ObservabilityPipelineWebsocketSourceType,
        )

        return {
            "auth_strategy": (ObservabilityPipelineWebsocketSourceAuthStrategy,),
            "custom_key": (str,),
            "decoding": (ObservabilityPipelineDecoding,),
            "id": (str,),
            "password_key": (str,),
            "tls": (ObservabilityPipelineWebsocketSourceTls,),
            "token_key": (str,),
            "type": (ObservabilityPipelineWebsocketSourceType,),
            "uri_key": (str,),
            "username_key": (str,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "custom_key": "custom_key",
        "decoding": "decoding",
        "id": "id",
        "password_key": "password_key",
        "tls": "tls",
        "token_key": "token_key",
        "type": "type",
        "uri_key": "uri_key",
        "username_key": "username_key",
    }

    def __init__(
        self_,
        auth_strategy: ObservabilityPipelineWebsocketSourceAuthStrategy,
        decoding: ObservabilityPipelineDecoding,
        id: str,
        type: ObservabilityPipelineWebsocketSourceType,
        custom_key: Union[str, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        tls: Union[
            ObservabilityPipelineWebsocketSourceTls,
            ObservabilityPipelineWebsocketSourceTlsEnabled,
            ObservabilityPipelineWebsocketSourceTlsWithClientCert,
            UnsetType,
        ] = unset,
        token_key: Union[str, UnsetType] = unset,
        uri_key: Union[str, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``websocket`` source ingests logs from a WebSocket server using the ``ws://`` or ``wss://`` protocol.

        **Supported pipeline types:** logs.

        :param auth_strategy: Authentication strategy for the WebSocket source connection.
        :type auth_strategy: ObservabilityPipelineWebsocketSourceAuthStrategy

        :param custom_key: Name of the environment variable or secret that holds the custom authorization header value. Used when ``auth_strategy`` is ``custom``.
        :type custom_key: str, optional

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param id: The unique identifier for this component.
        :type id: str

        :param password_key: Name of the environment variable or secret that holds the password. Used when ``auth_strategy`` is ``basic``.
        :type password_key: str, optional

        :param tls: TLS configuration for the WebSocket source. Use ``enabled`` for standard ``wss://`` connections, or ``with_client_cert`` to present a client certificate for mutual TLS.
        :type tls: ObservabilityPipelineWebsocketSourceTls, optional

        :param token_key: Name of the environment variable or secret that holds the bearer token. Used when ``auth_strategy`` is ``bearer``.
        :type token_key: str, optional

        :param type: The source type. The value should always be ``websocket``.
        :type type: ObservabilityPipelineWebsocketSourceType

        :param uri_key: Name of the environment variable or secret that holds the WebSocket server URI ( ``ws://`` or ``wss://`` ).
        :type uri_key: str, optional

        :param username_key: Name of the environment variable or secret that holds the username. Used when ``auth_strategy`` is ``basic``.
        :type username_key: str, optional
        """
        if custom_key is not unset:
            kwargs["custom_key"] = custom_key
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if tls is not unset:
            kwargs["tls"] = tls
        if token_key is not unset:
            kwargs["token_key"] = token_key
        if uri_key is not unset:
            kwargs["uri_key"] = uri_key
        if username_key is not unset:
            kwargs["username_key"] = username_key
        super().__init__(kwargs)

        self_.auth_strategy = auth_strategy
        self_.decoding = decoding
        self_.id = id
        self_.type = type
