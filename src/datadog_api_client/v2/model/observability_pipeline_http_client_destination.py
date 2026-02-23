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
    from datadog_api_client.v2.model.observability_pipeline_http_client_destination_auth_strategy import (
        ObservabilityPipelineHttpClientDestinationAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_client_destination_compression import (
        ObservabilityPipelineHttpClientDestinationCompression,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_client_destination_encoding import (
        ObservabilityPipelineHttpClientDestinationEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_http_client_destination_type import (
        ObservabilityPipelineHttpClientDestinationType,
    )


class ObservabilityPipelineHttpClientDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_http_client_destination_auth_strategy import (
            ObservabilityPipelineHttpClientDestinationAuthStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_http_client_destination_compression import (
            ObservabilityPipelineHttpClientDestinationCompression,
        )
        from datadog_api_client.v2.model.observability_pipeline_http_client_destination_encoding import (
            ObservabilityPipelineHttpClientDestinationEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_http_client_destination_type import (
            ObservabilityPipelineHttpClientDestinationType,
        )

        return {
            "auth_strategy": (ObservabilityPipelineHttpClientDestinationAuthStrategy,),
            "compression": (ObservabilityPipelineHttpClientDestinationCompression,),
            "custom_key": (str,),
            "encoding": (ObservabilityPipelineHttpClientDestinationEncoding,),
            "id": (str,),
            "inputs": ([str],),
            "password_key": (str,),
            "tls": (ObservabilityPipelineTls,),
            "token_key": (str,),
            "type": (ObservabilityPipelineHttpClientDestinationType,),
            "uri_key": (str,),
            "username_key": (str,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "compression": "compression",
        "custom_key": "custom_key",
        "encoding": "encoding",
        "id": "id",
        "inputs": "inputs",
        "password_key": "password_key",
        "tls": "tls",
        "token_key": "token_key",
        "type": "type",
        "uri_key": "uri_key",
        "username_key": "username_key",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineHttpClientDestinationEncoding,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineHttpClientDestinationType,
        auth_strategy: Union[ObservabilityPipelineHttpClientDestinationAuthStrategy, UnsetType] = unset,
        compression: Union[ObservabilityPipelineHttpClientDestinationCompression, UnsetType] = unset,
        custom_key: Union[str, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        token_key: Union[str, UnsetType] = unset,
        uri_key: Union[str, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``http_client`` destination sends data to an HTTP endpoint.

        **Supported pipeline types:** logs, metrics

        :param auth_strategy: HTTP authentication strategy.
        :type auth_strategy: ObservabilityPipelineHttpClientDestinationAuthStrategy, optional

        :param compression: Compression configuration for HTTP requests.
        :type compression: ObservabilityPipelineHttpClientDestinationCompression, optional

        :param custom_key: Name of the environment variable or secret that holds a custom header value (used with custom auth strategies).
        :type custom_key: str, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineHttpClientDestinationEncoding

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the input for this component.
        :type inputs: [str]

        :param password_key: Name of the environment variable or secret that holds the password (used when ``auth_strategy`` is ``basic`` ).
        :type password_key: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param token_key: Name of the environment variable or secret that holds the bearer token (used when ``auth_strategy`` is ``bearer`` ).
        :type token_key: str, optional

        :param type: The destination type. The value should always be ``http_client``.
        :type type: ObservabilityPipelineHttpClientDestinationType

        :param uri_key: Name of the environment variable or secret that holds the HTTP endpoint URI.
        :type uri_key: str, optional

        :param username_key: Name of the environment variable or secret that holds the username (used when ``auth_strategy`` is ``basic`` ).
        :type username_key: str, optional
        """
        if auth_strategy is not unset:
            kwargs["auth_strategy"] = auth_strategy
        if compression is not unset:
            kwargs["compression"] = compression
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

        self_.encoding = encoding
        self_.id = id
        self_.inputs = inputs
        self_.type = type
