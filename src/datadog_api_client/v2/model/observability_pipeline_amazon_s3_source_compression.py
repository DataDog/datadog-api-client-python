# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3SourceCompression(ModelSimple):
    """
    Compression format for objects retrieved from the S3 bucket. Use `auto` to detect compression from the object's Content-Encoding header or file extension.

    :param value: Must be one of ["auto", "none", "gzip", "zstd"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "none",
        "gzip",
        "zstd",
    }
    AUTO: ClassVar["ObservabilityPipelineAmazonS3SourceCompression"]
    NONE: ClassVar["ObservabilityPipelineAmazonS3SourceCompression"]
    GZIP: ClassVar["ObservabilityPipelineAmazonS3SourceCompression"]
    ZSTD: ClassVar["ObservabilityPipelineAmazonS3SourceCompression"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3SourceCompression.AUTO = ObservabilityPipelineAmazonS3SourceCompression("auto")
ObservabilityPipelineAmazonS3SourceCompression.NONE = ObservabilityPipelineAmazonS3SourceCompression("none")
ObservabilityPipelineAmazonS3SourceCompression.GZIP = ObservabilityPipelineAmazonS3SourceCompression("gzip")
ObservabilityPipelineAmazonS3SourceCompression.ZSTD = ObservabilityPipelineAmazonS3SourceCompression("zstd")
