# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSAccountPartition(ModelSimple):
    """
    AWS Account partition

    :param value: If omitted defaults to "aws". Must be one of ["aws", "aws-cn", "aws-us-gov"].
    :type value: str
    """

    allowed_values = {
        "aws",
        "aws-cn",
        "aws-us-gov",
    }
    AWS: ClassVar["AWSAccountPartition"]
    AWS_CN: ClassVar["AWSAccountPartition"]
    AWS_US_GOV: ClassVar["AWSAccountPartition"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSAccountPartition.AWS = AWSAccountPartition("aws")
AWSAccountPartition.AWS_CN = AWSAccountPartition("aws-cn")
AWSAccountPartition.AWS_US_GOV = AWSAccountPartition("aws-us-gov")
