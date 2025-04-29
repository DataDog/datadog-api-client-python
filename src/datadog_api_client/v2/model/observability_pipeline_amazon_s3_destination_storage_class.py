# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3DestinationStorageClass(ModelSimple):
    """
    S3 storage class.

    :param value: Must be one of ["STANDARD", "REDUCED_REDUNDANCY", "INTELLIGENT_TIERING", "STANDARD_IA", "EXPRESS_ONEZONE", "ONEZONE_IA", "GLACIER", "GLACIER_IR", "DEEP_ARCHIVE"].
    :type value: str
    """

    allowed_values = {
        "STANDARD",
        "REDUCED_REDUNDANCY",
        "INTELLIGENT_TIERING",
        "STANDARD_IA",
        "EXPRESS_ONEZONE",
        "ONEZONE_IA",
        "GLACIER",
        "GLACIER_IR",
        "DEEP_ARCHIVE",
    }
    STANDARD: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    REDUCED_REDUNDANCY: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    INTELLIGENT_TIERING: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    STANDARD_IA: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    EXPRESS_ONEZONE: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    ONEZONE_IA: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    GLACIER: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    GLACIER_IR: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]
    DEEP_ARCHIVE: ClassVar["ObservabilityPipelineAmazonS3DestinationStorageClass"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3DestinationStorageClass.STANDARD = ObservabilityPipelineAmazonS3DestinationStorageClass(
    "STANDARD"
)
ObservabilityPipelineAmazonS3DestinationStorageClass.REDUCED_REDUNDANCY = (
    ObservabilityPipelineAmazonS3DestinationStorageClass("REDUCED_REDUNDANCY")
)
ObservabilityPipelineAmazonS3DestinationStorageClass.INTELLIGENT_TIERING = (
    ObservabilityPipelineAmazonS3DestinationStorageClass("INTELLIGENT_TIERING")
)
ObservabilityPipelineAmazonS3DestinationStorageClass.STANDARD_IA = ObservabilityPipelineAmazonS3DestinationStorageClass(
    "STANDARD_IA"
)
ObservabilityPipelineAmazonS3DestinationStorageClass.EXPRESS_ONEZONE = (
    ObservabilityPipelineAmazonS3DestinationStorageClass("EXPRESS_ONEZONE")
)
ObservabilityPipelineAmazonS3DestinationStorageClass.ONEZONE_IA = ObservabilityPipelineAmazonS3DestinationStorageClass(
    "ONEZONE_IA"
)
ObservabilityPipelineAmazonS3DestinationStorageClass.GLACIER = ObservabilityPipelineAmazonS3DestinationStorageClass(
    "GLACIER"
)
ObservabilityPipelineAmazonS3DestinationStorageClass.GLACIER_IR = ObservabilityPipelineAmazonS3DestinationStorageClass(
    "GLACIER_IR"
)
ObservabilityPipelineAmazonS3DestinationStorageClass.DEEP_ARCHIVE = (
    ObservabilityPipelineAmazonS3DestinationStorageClass("DEEP_ARCHIVE")
)
