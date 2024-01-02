# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AwsCURConfigPatchRequestType(ModelSimple):
    """
    Type of AWS CUR config Patch Request.

    :param value: If omitted defaults to "aws_cur_config_patch_request". Must be one of ["aws_cur_config_patch_request"].
    :type value: str
    """

    allowed_values = {
        "aws_cur_config_patch_request",
    }
    AWS_CUR_CONFIG_PATCH_REQUEST: ClassVar["AwsCURConfigPatchRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AwsCURConfigPatchRequestType.AWS_CUR_CONFIG_PATCH_REQUEST = AwsCURConfigPatchRequestType("aws_cur_config_patch_request")
