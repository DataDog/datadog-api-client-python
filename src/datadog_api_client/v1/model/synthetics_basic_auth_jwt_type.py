# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBasicAuthJWTType(ModelSimple):
    """
    The type of authentication to use when performing the test.

    :param value: If omitted defaults to "jwt". Must be one of ["jwt"].
    :type value: str
    """

    allowed_values = {
        "jwt",
    }
    JWT: ClassVar["SyntheticsBasicAuthJWTType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBasicAuthJWTType.JWT = SyntheticsBasicAuthJWTType("jwt")
