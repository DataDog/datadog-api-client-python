# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SensitiveDataScannerStandardRuleType(ModelSimple):
    """
    Type of standard rule, based on how it detects sensitive data.

    :param value: Must be one of ["regex_standard_rule", "machine_learning_standard_rule"].
    :type value: str
    """

    allowed_values = {
        "regex_standard_rule",
        "machine_learning_standard_rule",
    }
    REGEX_STANDARD_RULE: ClassVar["SensitiveDataScannerStandardRuleType"]
    MACHINE_LEARNING_STANDARD_RULE: ClassVar["SensitiveDataScannerStandardRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SensitiveDataScannerStandardRuleType.REGEX_STANDARD_RULE = SensitiveDataScannerStandardRuleType("regex_standard_rule")
SensitiveDataScannerStandardRuleType.MACHINE_LEARNING_STANDARD_RULE = SensitiveDataScannerStandardRuleType(
    "machine_learning_standard_rule"
)
