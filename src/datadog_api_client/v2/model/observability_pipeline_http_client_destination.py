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
            "encoding": (ObservabilityPipelineHttpClientDestinationEncoding,),
            "id": (str,),
            "inputs": ([str],),
            "tls": (ObservabilityPipelineTls,),
            "type": (ObservabilityPipelineHttpClientDestinationType,),
        }

    attribute_map = {
        "auth_strategy": "auth_strategy",
        "compression": "compression",
        "encoding": "encoding",
        "id": "id",
        "inputs": "inputs",
        "tls": "tls",
        "type": "type",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineHttpClientDestinationEncoding,
        id: str,
        inputs: List[str],
        type: ObservabilityPipelineHttpClientDestinationType,
        auth_strategy: Union[ObservabilityPipelineHttpClientDestinationAuthStrategy, UnsetType] = unset,
        compression: Union[ObservabilityPipelineHttpClientDestinationCompression, UnsetType] = unset,
        tls: Union[ObservabilityPipelineTls, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``http_client`` destination sends data to an HTTP endpoint.

        **Supported pipeline types:** logs, metrics

        :param auth_strategy: HTTP authentication strategy.
        :type auth_strategy: ObservabilityPipelineHttpClientDestinationAuthStrategy, optional

        :param compression: Compression configuration for HTTP requests.
        :type compression: ObservabilityPipelineHttpClientDestinationCompression, optional

        :param encoding: Encoding format for log events.
        :type encoding: ObservabilityPipelineHttpClientDestinationEncoding

        :param id: The unique identifier for this component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the input for this component.
        :type inputs: [str]

        :param tls: Configuration for enabling TLS encryption between the pipeline component and external services.
        :type tls: ObservabilityPipelineTls, optional

        :param type: The destination type. The value should always be ``http_client``.
        :type type: ObservabilityPipelineHttpClientDestinationType
        """
        if auth_strategy is not unset:
            kwargs["auth_strategy"] = auth_strategy
        if compression is not unset:
            kwargs["compression"] = compression
        if tls is not unset:
            kwargs["tls"] = tls
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.id = id
        self_.inputs = inputs
        self_.type = type
