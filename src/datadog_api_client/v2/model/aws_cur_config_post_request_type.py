# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsCURConfigPostRequestType(ModelSimple):
    """
    Type of AWS CUR config Post Request.

    :param value: If omitted defaults to "aws_cur_config_post_request". Must be one of ["aws_cur_config_post_request"].
    :type value: str
    """

    allowed_values = {
        "aws_cur_config_post_request",
    }
    AWS_CUR_CONFIG_POST_REQUEST: ClassVar["AwsCURConfigPostRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsCURConfigPostRequestType.AWS_CUR_CONFIG_POST_REQUEST = AwsCURConfigPostRequestType("aws_cur_config_post_request")
