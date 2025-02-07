# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.completion_condition_operator import CompletionConditionOperator


class CompletionCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.completion_condition_operator import CompletionConditionOperator

        return {
            "operand1": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "operand2": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "operator": (CompletionConditionOperator,),
        }

    attribute_map = {
        "operand1": "operand1",
        "operand2": "operand2",
        "operator": "operator",
    }

    def __init__(
        self_, operand1: Any, operator: CompletionConditionOperator, operand2: Union[Any, UnsetType] = unset, **kwargs
    ):
        """
        The definition of ``CompletionCondition`` object.

        :param operand1: The ``CompletionCondition`` ``operand1``.
        :type operand1: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param operand2: The ``CompletionCondition`` ``operand2``.
        :type operand2: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param operator: The definition of ``CompletionConditionOperator`` object.
        :type operator: CompletionConditionOperator
        """
        if operand2 is not unset:
            kwargs["operand2"] = operand2
        super().__init__(kwargs)

        self_.operand1 = operand1
        self_.operator = operator
