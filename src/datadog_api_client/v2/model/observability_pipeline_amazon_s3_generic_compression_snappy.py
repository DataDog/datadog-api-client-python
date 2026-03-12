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
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_snappy_type import (
        ObservabilityPipelineAmazonS3GenericCompressionSnappyType,
    )


class ObservabilityPipelineAmazonS3GenericCompressionSnappy(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_compression_snappy_type import (
            ObservabilityPipelineAmazonS3GenericCompressionSnappyType,
        )

        return {
            "type": (ObservabilityPipelineAmazonS3GenericCompressionSnappyType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ObservabilityPipelineAmazonS3GenericCompressionSnappyType, **kwargs):
        """
        Snappy compression.

        :param type: The compression type. Always ``snappy``.
        :type type: ObservabilityPipelineAmazonS3GenericCompressionSnappyType
        """
        super().__init__(kwargs)

        self_.type = type
