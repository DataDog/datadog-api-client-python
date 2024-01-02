# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsCURConfigType(ModelSimple):
    """
    Type of AWS CUR config.

    :param value: If omitted defaults to "aws_cur_config". Must be one of ["aws_cur_config"].
    :type value: str
    """

    allowed_values = {
        "aws_cur_config",
    }
    AWS_CUR_CONFIG: ClassVar["AwsCURConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsCURConfigType.AWS_CUR_CONFIG = AwsCURConfigType("aws_cur_config")
