# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetWindowPolicy(ModelSimple):
    """
    UTC accounting period for a budget.

    :param value: Must be one of ["DAILY", "WEEKLY", "MONTHLY"].
    :type value: str
    """

    allowed_values = {
        "DAILY",
        "WEEKLY",
        "MONTHLY",
    }
    DAILY: ClassVar["AiGatewayBudgetWindowPolicy"]
    WEEKLY: ClassVar["AiGatewayBudgetWindowPolicy"]
    MONTHLY: ClassVar["AiGatewayBudgetWindowPolicy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetWindowPolicy.DAILY = AiGatewayBudgetWindowPolicy("DAILY")
AiGatewayBudgetWindowPolicy.WEEKLY = AiGatewayBudgetWindowPolicy("WEEKLY")
AiGatewayBudgetWindowPolicy.MONTHLY = AiGatewayBudgetWindowPolicy("MONTHLY")
