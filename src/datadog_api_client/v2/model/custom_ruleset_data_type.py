# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomRulesetDataType(ModelSimple):
    """
    Resource type

    :param value: If omitted defaults to "custom_ruleset". Must be one of ["custom_ruleset"].
    :type value: str
    """

    allowed_values = {
        "custom_ruleset",
    }
    CUSTOM_RULESET: ClassVar["CustomRulesetDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomRulesetDataType.CUSTOM_RULESET = CustomRulesetDataType("custom_ruleset")
