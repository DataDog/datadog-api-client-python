# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3DestinationType(ModelSimple):
    """
    The destination type. Always `amazon_s3`.

    :param value: If omitted defaults to "amazon_s3". Must be one of ["amazon_s3"].
    :type value: str
    """

    allowed_values = {
        "amazon_s3",
    }
    AMAZON_S3: ClassVar["ObservabilityPipelineAmazonS3DestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3DestinationType.AMAZON_S3 = ObservabilityPipelineAmazonS3DestinationType("amazon_s3")
