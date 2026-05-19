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
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_auth_strategy import (
        ObservabilityPipelineHttpServerSourceAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_type import (
        ObservabilityPipelineHttpServerSourceType,
    )
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token import (
        ObservabilityPipelineHttpServerSourceValidToken,
    )


class ObservabilityPipelineHttpServerSource(ModelNormal):
    validations = {
        "valid_tokens": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_http_server_source_auth_strategy import (
            ObservabilityPipelineHttpServerSourceAuthStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_http_server_source_type import (
            ObservabilityPipelineHttpServerSourceType,
        )
        from datadog_api_client.v2.model.observability_pipeline_http_server_source_valid_token import (
            ObservabilityPipelineHttpServerSourceValidToken,
        )

        return {
            "address_key": (str,),
            "auth_strategy": (ObservabilityPipelineHttpServerSourceAuthStrategy,),
            "custom_key": (str,),
            "decoding": (ObservabilityPipelineDecoding,),
            "id": (str,),
            "password_key": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineHttpServerSourceType,),
            "username_key": (str,),
            "valid_tokens": ([ObservabilityPipelineHttpServerSourceValidToken],),
        }

    attribute_map = {
        "address_key": "address_key",
        "auth_strategy": "auth_strategy",
        "custom_key": "custom_key",
        "decoding": "decoding",
        "id": "id",
        "password_key": "password_key",
        "tls": "tls",
        "type": "type",
        "username_key": "username_key",
        "valid_tokens": "valid_tokens",
    }

    def __init__(
        self_,
        auth_strategy: ObservabilityPipelineHttpServerSourceAuthStrategy,
        decoding: ObservabilityPipelineDecoding,
        id: str,
        type: ObservabilityPipelineHttpServerSourceType,
        address_key: Union[str, UnsetType] = unset,
        custom_key: Union[str, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        valid_tokens: Union[List[ObservabilityPipelineHttpServerSourceValidToken], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``http_server`` source collects logs over HTTP POST from external services.

        **Supported pipeline types:** logs

        :param address_key: Name of the environment variable or secret that holds the listen address for the HTTP server.
        :type address_key: str, optional

        :param auth_strategy: HTTP authentication method.
        :type auth_strategy: ObservabilityPipelineHttpServerSourceAuthStrategy

        :param custom_key: Name of the environment variable or secret that holds a custom header value (used with custom auth strategies).
        :type custom_key: str, optional

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param id: Unique ID for the HTTP server source.
        :type id: str

        :param password_key: Name of the environment variable or secret that holds the password (used when ``auth_strategy`` is ``plain`` ).
        :type password_key: str, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``http_server``.
        :type type: ObservabilityPipelineHttpServerSourceType

        :param username_key: Name of the environment variable or secret that holds the username (used when ``auth_strategy`` is ``plain`` ).
        :type username_key: str, optional

        :param valid_tokens: A list of tokens that are accepted for authenticating incoming HTTP requests. When set,
            the source rejects any request whose token does not match an enabled entry in this list.
            Cannot be combined with the ``plain`` auth strategy.
        :type valid_tokens: [ObservabilityPipelineHttpServerSourceValidToken], optional
        """
        if address_key is not unset:
            kwargs["address_key"] = address_key
        if custom_key is not unset:
            kwargs["custom_key"] = custom_key
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if tls is not unset:
            kwargs["tls"] = tls
        if username_key is not unset:
            kwargs["username_key"] = username_key
        if valid_tokens is not unset:
            kwargs["valid_tokens"] = valid_tokens
        super().__init__(kwargs)

        self_.auth_strategy = auth_strategy
        self_.decoding = decoding
        self_.id = id
        self_.type = type
