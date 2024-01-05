# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSRelatedAccountType(ModelSimple):
    """
    Type of AWS related account.

    :param value: If omitted defaults to "aws_account". Must be one of ["aws_account"].
    :type value: str
    """

    allowed_values = {
        "aws_account",
    }
    AWS_ACCOUNT: ClassVar["AWSRelatedAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSRelatedAccountType.AWS_ACCOUNT = AWSRelatedAccountType("aws_account")
