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
    from datadog_api_client.v2.model.observability_pipeline_http_client_source_auth_strategy import (
        ObservabilityPipelineHttpClientSourceAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_http_client_source_type import (
        ObservabilityPipelineHttpClientSourceType,
    )


class ObservabilityPipelineHttpClientSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_http_client_source_auth_strategy import (
            ObservabilityPipelineHttpClientSourceAuthStrategy,
        )
        from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
        from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
        from datadog_api_client.v2.model.observability_pipeline_http_client_source_type import (
            ObservabilityPipelineHttpClientSourceType,
        )

        return {
            "auth_strategy": (ObservabilityPipelineHttpClientSourceAuthStrategy,),
            "custom_key": (str,),
            "decoding": (ObservabilityPipelineDecoding,),
            "endpoint_url_key": (str,),
            "id": (str,),
            "password_key": (str,),
            "scrape_interval_secs": (int,),
            "scrape_timeout_secs": (int,),
            "tls": (ObservabilityPipelineTls,),
            "token_key": (str,),
            "type": (ObservabilityPipelineHttpClientSourceType,),
            "username_key": (str,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "custom_key": "custom_key",
        "decoding": "decoding",
        "endpoint_url_key": "endpoint_url_key",
        "id": "id",
        "password_key": "password_key",
        "scrape_interval_secs": "scrape_interval_secs",
        "scrape_timeout_secs": "scrape_timeout_secs",
        "tls": "tls",
        "token_key": "token_key",
        "type": "type",
        "username_key": "username_key",
    }

    def __init__(
        self_,
        decoding: ObservabilityPipelineDecoding,
        id: str,
        type: ObservabilityPipelineHttpClientSourceType,
        auth_strategy: Union[ObservabilityPipelineHttpClientSourceAuthStrategy, UnsetType] = unset,
        custom_key: Union[str, UnsetType] = unset,
        endpoint_url_key: Union[str, UnsetType] = unset,
        password_key: Union[str, UnsetType] = unset,
        scrape_interval_secs: Union[int, UnsetType] = unset,
        scrape_timeout_secs: Union[int, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        token_key: Union[str, UnsetType] = unset,
        username_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``http_client`` source scrapes logs from HTTP endpoints at regular intervals.

        **Supported pipeline types:** logs

        :param auth_strategy: Optional authentication strategy for HTTP requests.
        :type auth_strategy: ObservabilityPipelineHttpClientSourceAuthStrategy, optional

        :param custom_key: Name of the environment variable or secret that holds a custom header value (used with custom auth strategies).
        :type custom_key: str, optional

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param endpoint_url_key: Name of the environment variable or secret that holds the HTTP endpoint URL to scrape.
        :type endpoint_url_key: str, optional

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param password_key: Name of the environment variable or secret that holds the password (used when ``auth_strategy`` is ``basic`` ).
        :type password_key: str, optional

        :param scrape_interval_secs: The interval (in seconds) between HTTP scrape requests.
        :type scrape_interval_secs: int, optional

        :param scrape_timeout_secs: The timeout (in seconds) for each scrape request.
        :type scrape_timeout_secs: int, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param token_key: Name of the environment variable or secret that holds the bearer token (used when ``auth_strategy`` is ``bearer`` ).
        :type token_key: str, optional

        :param type: The source type. The value should always be ``http_client``.
        :type type: ObservabilityPipelineHttpClientSourceType

        :param username_key: Name of the environment variable or secret that holds the username (used when ``auth_strategy`` is ``basic`` ).
        :type username_key: str, optional
        """
        if auth_strategy is not unset:
            kwargs["auth_strategy"] = auth_strategy
        if custom_key is not unset:
            kwargs["custom_key"] = custom_key
        if endpoint_url_key is not unset:
            kwargs["endpoint_url_key"] = endpoint_url_key
        if password_key is not unset:
            kwargs["password_key"] = password_key
        if scrape_interval_secs is not unset:
            kwargs["scrape_interval_secs"] = scrape_interval_secs
        if scrape_timeout_secs is not unset:
            kwargs["scrape_timeout_secs"] = scrape_timeout_secs
        if tls is not unset:
            kwargs["tls"] = tls
        if token_key is not unset:
            kwargs["token_key"] = token_key
        if username_key is not unset:
            kwargs["username_key"] = username_key
        super().__init__(kwargs)

        self_.decoding = decoding
        self_.id = id
        self_.type = type
