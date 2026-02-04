# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AWSCloudAuthPersonaMappingType(ModelSimple):
    """
    Type identifier for AWS cloud authentication persona mapping

    :param value: If omitted defaults to "aws_cloud_auth_config". Must be one of ["aws_cloud_auth_config"].
    :type value: str
    """

    allowed_values = {
        "aws_cloud_auth_config",
    }
    AWS_CLOUD_AUTH_CONFIG: ClassVar["AWSCloudAuthPersonaMappingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AWSCloudAuthPersonaMappingType.AWS_CLOUD_AUTH_CONFIG = AWSCloudAuthPersonaMappingType("aws_cloud_auth_config")
