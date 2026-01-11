# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_http_client_destination_compression_algorithm import (
        ObservabilityPipelineHttpClientDestinationCompressionAlgorithm,
    )


class ObservabilityPipelineHttpClientDestinationCompression(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_http_client_destination_compression_algorithm import (
            ObservabilityPipelineHttpClientDestinationCompressionAlgorithm,
        )

        return {
            "algorithm": (ObservabilityPipelineHttpClientDestinationCompressionAlgorithm,),
        }

    attribute_map = {
        "algorithm": "algorithm",
    }

    def __init__(self_, algorithm: ObservabilityPipelineHttpClientDestinationCompressionAlgorithm, **kwargs):
        """
        Compression configuration for HTTP requests.

        :param algorithm: Compression algorithm.
        :type algorithm: ObservabilityPipelineHttpClientDestinationCompressionAlgorithm
        """
        super().__init__(kwargs)

        self_.algorithm = algorithm
