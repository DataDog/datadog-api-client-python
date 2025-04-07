# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafCustomRuleTagsCategory(ModelSimple):
    """
    The category of the WAF Rule, can be either `business_logic`, `attack_attempt` or `security_response`.

    :param value: Must be one of ["attack_attempt", "business_logic", "security_response"].
    :type value: str
    """

    allowed_values = {
        "attack_attempt",
        "business_logic",
        "security_response",
    }
    ATTACK_ATTEMPT: ClassVar["ApplicationSecurityWafCustomRuleTagsCategory"]
    BUSINESS_LOGIC: ClassVar["ApplicationSecurityWafCustomRuleTagsCategory"]
    SECURITY_RESPONSE: ClassVar["ApplicationSecurityWafCustomRuleTagsCategory"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafCustomRuleTagsCategory.ATTACK_ATTEMPT = ApplicationSecurityWafCustomRuleTagsCategory(
    "attack_attempt"
)
ApplicationSecurityWafCustomRuleTagsCategory.BUSINESS_LOGIC = ApplicationSecurityWafCustomRuleTagsCategory(
    "business_logic"
)
ApplicationSecurityWafCustomRuleTagsCategory.SECURITY_RESPONSE = ApplicationSecurityWafCustomRuleTagsCategory(
    "security_response"
)
