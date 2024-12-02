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
    AWS partition your AWS account is scoped to. Defaults to `aws`.
        See [Partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html) in the AWS documentation for more information.

    :param value: Must be one of ["aws", "aws-cn", "aws-us-gov"].
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
