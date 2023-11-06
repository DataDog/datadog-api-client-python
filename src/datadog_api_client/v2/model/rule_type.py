# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class RuleType(StringEnum):
    """
    The JSON:API type for scorecard rules.

    :param value: If omitted defaults to "rule". Must be one of ["rule"].
    :type value: str
    """

    allowed_values = {
        "rule",
    }
    RULE: ClassVar["RuleType"]


RuleType.RULE = RuleType("rule")
