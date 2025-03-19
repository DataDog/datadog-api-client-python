# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsOnDemandType(ModelSimple):
    """
    The type of the on demand task. The value should always be `aws_resource`.

    :param value: If omitted defaults to "aws_resource". Must be one of ["aws_resource"].
    :type value: str
    """

    allowed_values = {
        "aws_resource",
    }
    AWS_RESOURCE: ClassVar["AwsOnDemandType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsOnDemandType.AWS_RESOURCE = AwsOnDemandType("aws_resource")
