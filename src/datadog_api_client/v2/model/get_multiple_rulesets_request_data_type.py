# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GetMultipleRulesetsRequestDataType(ModelSimple):
    """
    Get multiple rulesets request resource type.

    :param value: If omitted defaults to "get_multiple_rulesets_request". Must be one of ["get_multiple_rulesets_request"].
    :type value: str
    """

    allowed_values = {
        "get_multiple_rulesets_request",
    }
    GET_MULTIPLE_RULESETS_REQUEST: ClassVar["GetMultipleRulesetsRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GetMultipleRulesetsRequestDataType.GET_MULTIPLE_RULESETS_REQUEST = GetMultipleRulesetsRequestDataType(
    "get_multiple_rulesets_request"
)
