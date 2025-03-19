# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CompletionConditionOperator(ModelSimple):
    """
    The definition of `CompletionConditionOperator` object.

    :param value: Must be one of ["OPERATOR_EQUAL", "OPERATOR_NOT_EQUAL", "OPERATOR_GREATER_THAN", "OPERATOR_LESS_THAN", "OPERATOR_GREATER_THAN_OR_EQUAL_TO", "OPERATOR_LESS_THAN_OR_EQUAL_TO", "OPERATOR_CONTAINS", "OPERATOR_DOES_NOT_CONTAIN", "OPERATOR_IS_NULL", "OPERATOR_IS_NOT_NULL", "OPERATOR_IS_EMPTY", "OPERATOR_IS_NOT_EMPTY"].
    :type value: str
    """

    allowed_values = {
        "OPERATOR_EQUAL",
        "OPERATOR_NOT_EQUAL",
        "OPERATOR_GREATER_THAN",
        "OPERATOR_LESS_THAN",
        "OPERATOR_GREATER_THAN_OR_EQUAL_TO",
        "OPERATOR_LESS_THAN_OR_EQUAL_TO",
        "OPERATOR_CONTAINS",
        "OPERATOR_DOES_NOT_CONTAIN",
        "OPERATOR_IS_NULL",
        "OPERATOR_IS_NOT_NULL",
        "OPERATOR_IS_EMPTY",
        "OPERATOR_IS_NOT_EMPTY",
    }
    OPERATOR_EQUAL: ClassVar["CompletionConditionOperator"]
    OPERATOR_NOT_EQUAL: ClassVar["CompletionConditionOperator"]
    OPERATOR_GREATER_THAN: ClassVar["CompletionConditionOperator"]
    OPERATOR_LESS_THAN: ClassVar["CompletionConditionOperator"]
    OPERATOR_GREATER_THAN_OR_EQUAL_TO: ClassVar["CompletionConditionOperator"]
    OPERATOR_LESS_THAN_OR_EQUAL_TO: ClassVar["CompletionConditionOperator"]
    OPERATOR_CONTAINS: ClassVar["CompletionConditionOperator"]
    OPERATOR_DOES_NOT_CONTAIN: ClassVar["CompletionConditionOperator"]
    OPERATOR_IS_NULL: ClassVar["CompletionConditionOperator"]
    OPERATOR_IS_NOT_NULL: ClassVar["CompletionConditionOperator"]
    OPERATOR_IS_EMPTY: ClassVar["CompletionConditionOperator"]
    OPERATOR_IS_NOT_EMPTY: ClassVar["CompletionConditionOperator"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CompletionConditionOperator.OPERATOR_EQUAL = CompletionConditionOperator("OPERATOR_EQUAL")
CompletionConditionOperator.OPERATOR_NOT_EQUAL = CompletionConditionOperator("OPERATOR_NOT_EQUAL")
CompletionConditionOperator.OPERATOR_GREATER_THAN = CompletionConditionOperator("OPERATOR_GREATER_THAN")
CompletionConditionOperator.OPERATOR_LESS_THAN = CompletionConditionOperator("OPERATOR_LESS_THAN")
CompletionConditionOperator.OPERATOR_GREATER_THAN_OR_EQUAL_TO = CompletionConditionOperator(
    "OPERATOR_GREATER_THAN_OR_EQUAL_TO"
)
CompletionConditionOperator.OPERATOR_LESS_THAN_OR_EQUAL_TO = CompletionConditionOperator(
    "OPERATOR_LESS_THAN_OR_EQUAL_TO"
)
CompletionConditionOperator.OPERATOR_CONTAINS = CompletionConditionOperator("OPERATOR_CONTAINS")
CompletionConditionOperator.OPERATOR_DOES_NOT_CONTAIN = CompletionConditionOperator("OPERATOR_DOES_NOT_CONTAIN")
CompletionConditionOperator.OPERATOR_IS_NULL = CompletionConditionOperator("OPERATOR_IS_NULL")
CompletionConditionOperator.OPERATOR_IS_NOT_NULL = CompletionConditionOperator("OPERATOR_IS_NOT_NULL")
CompletionConditionOperator.OPERATOR_IS_EMPTY = CompletionConditionOperator("OPERATOR_IS_EMPTY")
CompletionConditionOperator.OPERATOR_IS_NOT_EMPTY = CompletionConditionOperator("OPERATOR_IS_NOT_EMPTY")
