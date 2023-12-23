# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class SecurityMonitoringRuleHardcodedEvaluatorType(StringEnum):
    """
    Hardcoded evaluator type.

    :param value: If omitted defaults to "log4shell". Must be one of ["log4shell"].
    :type value: str
    """

    allowed_values = {
        "log4shell",
    }
    LOG4SHELL: ClassVar["SecurityMonitoringRuleHardcodedEvaluatorType"]


SecurityMonitoringRuleHardcodedEvaluatorType.LOG4SHELL = SecurityMonitoringRuleHardcodedEvaluatorType("log4shell")
