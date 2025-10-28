# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetMultipleRulesetsResponseDataType(ModelSimple):
    """
    Get multiple rulesets response resource type.

    :param value: If omitted defaults to "get_multiple_rulesets_response". Must be one of ["get_multiple_rulesets_response"].
    :type value: str
    """

    allowed_values = {
        "get_multiple_rulesets_response",
    }
    GET_MULTIPLE_RULESETS_RESPONSE: ClassVar["GetMultipleRulesetsResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetMultipleRulesetsResponseDataType.GET_MULTIPLE_RULESETS_RESPONSE = GetMultipleRulesetsResponseDataType(
    "get_multiple_rulesets_response"
)
