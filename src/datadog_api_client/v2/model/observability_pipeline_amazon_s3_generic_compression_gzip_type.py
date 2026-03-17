# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3GenericCompressionGzipType(ModelSimple):
    """
    The compression type. Always `gzip`.

    :param value: If omitted defaults to "gzip". Must be one of ["gzip"].
    :type value: str
    """

    allowed_values = {
        "gzip",
    }
    GZIP: ClassVar["ObservabilityPipelineAmazonS3GenericCompressionGzipType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3GenericCompressionGzipType.GZIP = ObservabilityPipelineAmazonS3GenericCompressionGzipType(
    "gzip"
)
