# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafCustomRuleConditionParametersType(ModelSimple):
    """
    The type of the value to compare against. Only used with the equals and !equals operator.

    :param value: Must be one of ["boolean", "signed", "unsigned", "float", "string"].
    :type value: str
    """

    allowed_values = {
        "boolean",
        "signed",
        "unsigned",
        "float",
        "string",
    }
    BOOLEAN: ClassVar["ApplicationSecurityWafCustomRuleConditionParametersType"]
    SIGNED: ClassVar["ApplicationSecurityWafCustomRuleConditionParametersType"]
    UNSIGNED: ClassVar["ApplicationSecurityWafCustomRuleConditionParametersType"]
    FLOAT: ClassVar["ApplicationSecurityWafCustomRuleConditionParametersType"]
    STRING: ClassVar["ApplicationSecurityWafCustomRuleConditionParametersType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafCustomRuleConditionParametersType.BOOLEAN = (
    ApplicationSecurityWafCustomRuleConditionParametersType("boolean")
)
ApplicationSecurityWafCustomRuleConditionParametersType.SIGNED = (
    ApplicationSecurityWafCustomRuleConditionParametersType("signed")
)
ApplicationSecurityWafCustomRuleConditionParametersType.UNSIGNED = (
    ApplicationSecurityWafCustomRuleConditionParametersType("unsigned")
)
ApplicationSecurityWafCustomRuleConditionParametersType.FLOAT = ApplicationSecurityWafCustomRuleConditionParametersType(
    "float"
)
ApplicationSecurityWafCustomRuleConditionParametersType.STRING = (
    ApplicationSecurityWafCustomRuleConditionParametersType("string")
)
