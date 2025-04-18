# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3SourceType(ModelSimple):
    """
    The source type. Always `aws_s3`.

    :param value: If omitted defaults to "aws_s3". Must be one of ["aws_s3"].
    :type value: str
    """

    allowed_values = {
        "aws_s3",
    }
    AWS_S3: ClassVar["ObservabilityPipelineAmazonS3SourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3SourceType.AWS_S3 = ObservabilityPipelineAmazonS3SourceType("aws_s3")
