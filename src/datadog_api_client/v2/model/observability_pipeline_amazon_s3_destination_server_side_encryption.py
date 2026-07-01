# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonS3DestinationServerSideEncryption(ModelSimple):
    """
    Server-side encryption type for Amazon S3.

    :param value: Must be one of ["aws:kms", "AES256"].
    :type value: str
    """

    allowed_values = {
        "aws:kms",
        "AES256",
    }
    AWS_KMS: ClassVar["ObservabilityPipelineAmazonS3DestinationServerSideEncryption"]
    AES256: ClassVar["ObservabilityPipelineAmazonS3DestinationServerSideEncryption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonS3DestinationServerSideEncryption.AWS_KMS = (
    ObservabilityPipelineAmazonS3DestinationServerSideEncryption("aws:kms")
)
ObservabilityPipelineAmazonS3DestinationServerSideEncryption.AES256 = (
    ObservabilityPipelineAmazonS3DestinationServerSideEncryption("AES256")
)
