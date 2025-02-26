# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityWafCustomRuleConditionOperator(ModelSimple):
    """
    Operator to use for the WAF Condition.

    :param value: Must be one of ["match_regex", "!match_regex", "phrase_match", "!phrase_match", "is_xss", "is_sqli", "exact_match", "!exact_match", "ip_match", "!ip_match", "capture_data"].
    :type value: str
    """

    allowed_values = {
        "match_regex",
        "!match_regex",
        "phrase_match",
        "!phrase_match",
        "is_xss",
        "is_sqli",
        "exact_match",
        "!exact_match",
        "ip_match",
        "!ip_match",
        "capture_data",
    }
    MATCH_REGEX: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    NOT_MATCH_REGEX: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    PHRASE_MATCH: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    NOT_PHRASE_MATCH: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    IS_XSS: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    IS_SQLI: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    EXACT_MATCH: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    NOT_EXACT_MATCH: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    IP_MATCH: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    NOT_IP_MATCH: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]
    CAPTURE_DATA: ClassVar["ApplicationSecurityWafCustomRuleConditionOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityWafCustomRuleConditionOperator.MATCH_REGEX = ApplicationSecurityWafCustomRuleConditionOperator(
    "match_regex"
)
ApplicationSecurityWafCustomRuleConditionOperator.NOT_MATCH_REGEX = ApplicationSecurityWafCustomRuleConditionOperator(
    "!match_regex"
)
ApplicationSecurityWafCustomRuleConditionOperator.PHRASE_MATCH = ApplicationSecurityWafCustomRuleConditionOperator(
    "phrase_match"
)
ApplicationSecurityWafCustomRuleConditionOperator.NOT_PHRASE_MATCH = ApplicationSecurityWafCustomRuleConditionOperator(
    "!phrase_match"
)
ApplicationSecurityWafCustomRuleConditionOperator.IS_XSS = ApplicationSecurityWafCustomRuleConditionOperator("is_xss")
ApplicationSecurityWafCustomRuleConditionOperator.IS_SQLI = ApplicationSecurityWafCustomRuleConditionOperator("is_sqli")
ApplicationSecurityWafCustomRuleConditionOperator.EXACT_MATCH = ApplicationSecurityWafCustomRuleConditionOperator(
    "exact_match"
)
ApplicationSecurityWafCustomRuleConditionOperator.NOT_EXACT_MATCH = ApplicationSecurityWafCustomRuleConditionOperator(
    "!exact_match"
)
ApplicationSecurityWafCustomRuleConditionOperator.IP_MATCH = ApplicationSecurityWafCustomRuleConditionOperator(
    "ip_match"
)
ApplicationSecurityWafCustomRuleConditionOperator.NOT_IP_MATCH = ApplicationSecurityWafCustomRuleConditionOperator(
    "!ip_match"
)
ApplicationSecurityWafCustomRuleConditionOperator.CAPTURE_DATA = ApplicationSecurityWafCustomRuleConditionOperator(
    "capture_data"
)
