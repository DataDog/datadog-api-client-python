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
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_gzip_type import (
        ObservabilityPipelineAmazonS3GenericCompressionGzipType,
    )


class ObservabilityPipelineAmazonS3GenericCompressionGzip(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_gzip_type import (
            ObservabilityPipelineAmazonS3GenericCompressionGzipType,
        )

        return {
            "algorithm": (ObservabilityPipelineAmazonS3GenericCompressionGzipType,),
            "level": (int,),
        }

    attribute_map = {
        "algorithm": "algorithm",
        "level": "level",
    }

    def __init__(self_, algorithm: ObservabilityPipelineAmazonS3GenericCompressionGzipType, level: int, **kwargs):
        """
        Gzip compression.

        :param algorithm: The compression type. Always ``gzip``.
        :type algorithm: ObservabilityPipelineAmazonS3GenericCompressionGzipType

        :param level: Gzip compression level.
        :type level: int
        """
        super().__init__(kwargs)

        self_.algorithm = algorithm
        self_.level = level
