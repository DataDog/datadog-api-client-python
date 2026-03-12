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
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_parquet_type import (
        ObservabilityPipelineAmazonS3GenericEncodingParquetType,
    )


class ObservabilityPipelineAmazonS3GenericEncodingParquet(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_parquet_type import (
            ObservabilityPipelineAmazonS3GenericEncodingParquetType,
        )

        return {
            "type": (ObservabilityPipelineAmazonS3GenericEncodingParquetType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ObservabilityPipelineAmazonS3GenericEncodingParquetType, **kwargs):
        """
        Parquet encoding.

        :param type: The encoding type. Always ``parquet``.
        :type type: ObservabilityPipelineAmazonS3GenericEncodingParquetType
        """
        super().__init__(kwargs)

        self_.type = type
