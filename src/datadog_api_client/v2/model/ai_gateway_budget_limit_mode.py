# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetLimitMode(ModelSimple):
    """
    How the budget limit applies. `shared` is one limit for all matching traffic. `per_instance` is one
        limit for each counter of a template budget that splits by value.

    :param value: Must be one of ["shared", "per_instance"].
    :type value: str
    """

    allowed_values = {
        "shared",
        "per_instance",
    }
    SHARED: ClassVar["AiGatewayBudgetLimitMode"]
    PER_INSTANCE: ClassVar["AiGatewayBudgetLimitMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetLimitMode.SHARED = AiGatewayBudgetLimitMode("shared")
AiGatewayBudgetLimitMode.PER_INSTANCE = AiGatewayBudgetLimitMode("per_instance")
