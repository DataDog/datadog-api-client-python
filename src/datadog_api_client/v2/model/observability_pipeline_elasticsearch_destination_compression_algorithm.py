# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm(ModelSimple):
    """
    The compression algorithm applied when sending data to Elasticsearch.

    :param value: Must be one of ["none", "gzip", "zlib", "zstd", "snappy"].
    :type value: str
    """

    allowed_values = {
        "none",
        "gzip",
        "zlib",
        "zstd",
        "snappy",
    }
    NONE: ClassVar["ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm"]
    GZIP: ClassVar["ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm"]
    ZLIB: ClassVar["ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm"]
    ZSTD: ClassVar["ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm"]
    SNAPPY: ClassVar["ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm.NONE = (
    ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm("none")
)
ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm.GZIP = (
    ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm("gzip")
)
ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm.ZLIB = (
    ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm("zlib")
)
ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm.ZSTD = (
    ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm("zstd")
)
ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm.SNAPPY = (
    ObservabilityPipelineElasticsearchDestinationCompressionAlgorithm("snappy")
)
