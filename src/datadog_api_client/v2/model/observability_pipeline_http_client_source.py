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
            "decoding": (ObservabilityPipelineDecoding,),
            "id": (str,),
            "scrape_interval_secs": (int,),
            "scrape_timeout_secs": (int,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineHttpClientSourceType,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "decoding": "decoding",
        "id": "id",
        "scrape_interval_secs": "scrape_interval_secs",
        "scrape_timeout_secs": "scrape_timeout_secs",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        decoding: ObservabilityPipelineDecoding,
        id: str,
        type: ObservabilityPipelineHttpClientSourceType,
        auth_strategy: Union[ObservabilityPipelineHttpClientSourceAuthStrategy, UnsetType] = unset,
        scrape_interval_secs: Union[int, UnsetType] = unset,
        scrape_timeout_secs: Union[int, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``http_client`` source scrapes logs from HTTP endpoints at regular intervals.

        :param auth_strategy: Optional authentication strategy for HTTP requests.
        :type auth_strategy: ObservabilityPipelineHttpClientSourceAuthStrategy, optional

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param scrape_interval_secs: The interval (in seconds) between HTTP scrape requests.
        :type scrape_interval_secs: int, optional

        :param scrape_timeout_secs: The timeout (in seconds) for each scrape request.
        :type scrape_timeout_secs: int, optional

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``http_client``.
        :type type: ObservabilityPipelineHttpClientSourceType
        """
        if auth_strategy is not unset:
            kwargs["auth_strategy"] = auth_strategy
        if scrape_interval_secs is not unset:
            kwargs["scrape_interval_secs"] = scrape_interval_secs
        if scrape_timeout_secs is not unset:
            kwargs["scrape_timeout_secs"] = scrape_timeout_secs
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.decoding = decoding
        self_.id = id
        self_.type = type
