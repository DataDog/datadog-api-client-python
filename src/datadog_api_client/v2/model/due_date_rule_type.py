# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DueDateRuleType(ModelSimple):
    """
    The JSON:API type for due date rules.

    :param value: If omitted defaults to "due_date_rules". Must be one of ["due_date_rules"].
    :type value: str
    """

    allowed_values = {
        "due_date_rules",
    }
    DUE_DATE_RULES: ClassVar["DueDateRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DueDateRuleType.DUE_DATE_RULES = DueDateRuleType("due_date_rules")
