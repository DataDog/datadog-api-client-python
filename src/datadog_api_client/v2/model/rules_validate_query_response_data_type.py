# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RulesValidateQueryResponseDataType(ModelSimple):
    """
    Validate response resource type.

    :param value: If omitted defaults to "validate_response". Must be one of ["validate_response"].
    :type value: str
    """

    allowed_values = {
        "validate_response",
    }
    VALIDATE_RESPONSE: ClassVar["RulesValidateQueryResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RulesValidateQueryResponseDataType.VALIDATE_RESPONSE = RulesValidateQueryResponseDataType("validate_response")
