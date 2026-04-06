# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ConditionOperator(ModelSimple):
    """
    The operator used in a targeting condition.

    :param value: Must be one of ["LT", "LTE", "GT", "GTE", "MATCHES", "NOT_MATCHES", "ONE_OF", "NOT_ONE_OF", "IS_NULL", "EQUALS"].
    :type value: str
    """

    allowed_values = {
        "LT",
        "LTE",
        "GT",
        "GTE",
        "MATCHES",
        "NOT_MATCHES",
        "ONE_OF",
        "NOT_ONE_OF",
        "IS_NULL",
        "EQUALS",
    }
    LT: ClassVar["ConditionOperator"]
    LTE: ClassVar["ConditionOperator"]
    GT: ClassVar["ConditionOperator"]
    GTE: ClassVar["ConditionOperator"]
    MATCHES: ClassVar["ConditionOperator"]
    NOT_MATCHES: ClassVar["ConditionOperator"]
    ONE_OF: ClassVar["ConditionOperator"]
    NOT_ONE_OF: ClassVar["ConditionOperator"]
    IS_NULL: ClassVar["ConditionOperator"]
    EQUALS: ClassVar["ConditionOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ConditionOperator.LT = ConditionOperator("LT")
ConditionOperator.LTE = ConditionOperator("LTE")
ConditionOperator.GT = ConditionOperator("GT")
ConditionOperator.GTE = ConditionOperator("GTE")
ConditionOperator.MATCHES = ConditionOperator("MATCHES")
ConditionOperator.NOT_MATCHES = ConditionOperator("NOT_MATCHES")
ConditionOperator.ONE_OF = ConditionOperator("ONE_OF")
ConditionOperator.NOT_ONE_OF = ConditionOperator("NOT_ONE_OF")
ConditionOperator.IS_NULL = ConditionOperator("IS_NULL")
ConditionOperator.EQUALS = ConditionOperator("EQUALS")
