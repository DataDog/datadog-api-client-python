# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SensitiveDataScannerMachineLearningRuleType(ModelSimple):
    """
    Type of a rule based on a standard machine learning rule.

    :param value: If omitted defaults to "machine_learning_standard_rule". Must be one of ["machine_learning_standard_rule"].
    :type value: str
    """

    allowed_values = {
        "machine_learning_standard_rule",
    }
    MACHINE_LEARNING_STANDARD_RULE: ClassVar["SensitiveDataScannerMachineLearningRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SensitiveDataScannerMachineLearningRuleType.MACHINE_LEARNING_STANDARD_RULE = (
    SensitiveDataScannerMachineLearningRuleType("machine_learning_standard_rule")
)
