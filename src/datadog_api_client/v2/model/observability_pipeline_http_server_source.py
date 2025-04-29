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
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_auth_strategy import (
        ObservabilityPipelineHttpServerSourceAuthStrategy,
    )
    from datadog_api_client.v2.model.observability_pipeline_decoding import ObservabilityPipelineDecoding
    from datadog_api_client.v2.model.observability_pipeline_tls import ObservabilityPipelineTls
    from datadog_api_client.v2.model.observability_pipeline_http_server_source_type import (
        ObservabilityPipelineHttpServerSourceType,
    )


class ObservabilityPipelineHttpServerSource(ModelNormal):
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

        return {
            "auth_strategy": (ObservabilityPipelineHttpServerSourceAuthStrategy,),
            "decoding": (ObservabilityPipelineDecoding,),
            "id": (str,),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineHttpServerSourceType,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "decoding": "decoding",
        "id": "id",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        auth_strategy: ObservabilityPipelineHttpServerSourceAuthStrategy,
        decoding: ObservabilityPipelineDecoding,
        id: str,
        type: ObservabilityPipelineHttpServerSourceType,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``http_server`` source collects logs over HTTP POST from external services.

        :param auth_strategy: HTTP authentication method.
        :type auth_strategy: ObservabilityPipelineHttpServerSourceAuthStrategy

        :param decoding: The decoding format used to interpret incoming logs.
        :type decoding: ObservabilityPipelineDecoding

        :param id: Unique ID for the HTTP server source.
        :type id: str

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The source type. The value should always be ``http_server``.
        :type type: ObservabilityPipelineHttpServerSourceType
        """
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.auth_strategy = auth_strategy
        self_.decoding = decoding
        self_.id = id
        self_.type = type
