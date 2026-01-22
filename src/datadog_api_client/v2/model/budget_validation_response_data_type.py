# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class BudgetValidationResponseDataType(ModelSimple):
    """
    Budget validation resource type.

    :param value: If omitted defaults to "budget_validation". Must be one of ["budget_validation"].
    :type value: str
    """

    allowed_values = {
        "budget_validation",
    }
    BUDGET_VALIDATION: ClassVar["BudgetValidationResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


BudgetValidationResponseDataType.BUDGET_VALIDATION = BudgetValidationResponseDataType("budget_validation")
