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
    from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_compression_algorithm import (
        ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm,
    )


class ObservabilityPipelineElasticsearchDestinationCompression(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_elasticsearch_destination_compression_algorithm import (
            ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm,
        )

        return {
            "algorithm": (ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm,),
            "level": (int,),
        }

    attribute_map = {
        "algorithm": "algorithm",
        "level": "level",
    }

    def __init__(
        self_,
        algorithm: ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm,
        level: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Compression configuration for the Elasticsearch destination.

        :param algorithm: The compression algorithm applied when sending data to Elasticsearch.
        :type algorithm: ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm

        :param level: The compression level. Only applicable for ``gzip`` , ``zlib`` , and ``zstd`` algorithms.
        :type level: int, optional
        """
        if level is not unset:
            kwargs["level"] = level
        super().__init__(kwargs)

        self_.algorithm = algorithm
