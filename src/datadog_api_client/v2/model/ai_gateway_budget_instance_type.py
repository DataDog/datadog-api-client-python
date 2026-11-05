# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetInstanceType(ModelSimple):
    """
    Budget instance counter resource type.

    :param value: If omitted defaults to "budget-instances". Must be one of ["budget-instances"].
    :type value: str
    """

    allowed_values = {
        "budget-instances",
    }
    BUDGET_INSTANCES: ClassVar["AiGatewayBudgetInstanceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetInstanceType.BUDGET_INSTANCES = AiGatewayBudgetInstanceType("budget-instances")
