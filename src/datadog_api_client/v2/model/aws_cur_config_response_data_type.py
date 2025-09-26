# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsCurConfigResponseDataType(ModelSimple):
    """
    AWS CUR config resource type.

    :param value: If omitted defaults to "aws_cur_config". Must be one of ["aws_cur_config"].
    :type value: str
    """

    allowed_values = {
        "aws_cur_config",
    }
    AWS_CUR_CONFIG: ClassVar["AwsCurConfigResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsCurConfigResponseDataType.AWS_CUR_CONFIG = AwsCurConfigResponseDataType("aws_cur_config")
