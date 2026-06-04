# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBasicAuthJWTAlgorithm(ModelSimple):
    """
    Algorithm to use for the JWT authentication.

    :param value: Must be one of ["HS256", "RS256", "ES256"].
    :type value: str
    """

    allowed_values = {
        "HS256",
        "RS256",
        "ES256",
    }
    HS256: ClassVar["SyntheticsBasicAuthJWTAlgorithm"]
    RS256: ClassVar["SyntheticsBasicAuthJWTAlgorithm"]
    ES256: ClassVar["SyntheticsBasicAuthJWTAlgorithm"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBasicAuthJWTAlgorithm.HS256 = SyntheticsBasicAuthJWTAlgorithm("HS256")
SyntheticsBasicAuthJWTAlgorithm.RS256 = SyntheticsBasicAuthJWTAlgorithm("RS256")
SyntheticsBasicAuthJWTAlgorithm.ES256 = SyntheticsBasicAuthJWTAlgorithm("ES256")
