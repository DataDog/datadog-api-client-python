# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SensitiveDataScannerStandardRegexRuleType(ModelSimple):
    """
    Type of a rule based on a standard regex rule.

    :param value: If omitted defaults to "regex_standard_rule". Must be one of ["regex_standard_rule"].
    :type value: str
    """

    allowed_values = {
        "regex_standard_rule",
    }
    REGEX_STANDARD_RULE: ClassVar["SensitiveDataScannerStandardRegexRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SensitiveDataScannerStandardRegexRuleType.REGEX_STANDARD_RULE = SensitiveDataScannerStandardRegexRuleType(
    "regex_standard_rule"
)
