# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafCustomRuleType(ModelSimple):
    """
    The type of the resource. The value should always be `custom_rule`.

    :param value: If omitted defaults to "custom_rule". Must be one of ["custom_rule"].
    :type value: str
    """

    allowed_values = {
        "custom_rule",
    }
    CUSTOM_RULE: ClassVar["ApplicationSecurityWafCustomRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafCustomRuleType.CUSTOM_RULE = ApplicationSecurityWafCustomRuleType("custom_rule")
