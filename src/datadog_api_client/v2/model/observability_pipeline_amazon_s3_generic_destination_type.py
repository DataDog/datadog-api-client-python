# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3GenericDestinationType(ModelSimple):
    """
    The destination type. Always `amazon_s3_generic`.

    :param value: If omitted defaults to "amazon_s3_generic". Must be one of ["amazon_s3_generic"].
    :type value: str
    """

    allowed_values = {
        "amazon_s3_generic",
    }
    GENERIC_ARCHIVES_S3: ClassVar["ObservabilityPipelineAmazonS3GenericDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3GenericDestinationType.GENERIC_ARCHIVES_S3 = (
    ObservabilityPipelineAmazonS3GenericDestinationType("amazon_s3_generic")
)
