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
    from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_json_type import (
        ObservabilityPipelineAmazonS3GenericEncodingJsonType,
    )


class ObservabilityPipelineAmazonS3GenericEncodingJson(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_amazon_s3_generic_encoding_json_type import (
            ObservabilityPipelineAmazonS3GenericEncodingJsonType,
        )

        return {
            "type": (ObservabilityPipelineAmazonS3GenericEncodingJsonType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ObservabilityPipelineAmazonS3GenericEncodingJsonType, **kwargs):
        """
        JSON encoding.

        :param type: The encoding type. Always ``json``.
        :type type: ObservabilityPipelineAmazonS3GenericEncodingJsonType
        """
        super().__init__(kwargs)

        self_.type = type
