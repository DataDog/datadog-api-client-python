# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetType(ModelSimple):
    """
    AI Gateway budget resource type.

    :param value: If omitted defaults to "budgets". Must be one of ["budgets"].
    :type value: str
    """

    allowed_values = {
        "budgets",
    }
    BUDGETS: ClassVar["AiGatewayBudgetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetType.BUDGETS = AiGatewayBudgetType("budgets")
