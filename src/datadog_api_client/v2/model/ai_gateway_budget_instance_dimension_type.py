# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetInstanceDimensionType(ModelSimple):
    """
    Budget split dimension values resource type.

    :param value: If omitted defaults to "budget-instance-dimensions". Must be one of ["budget-instance-dimensions"].
    :type value: str
    """

    allowed_values = {
        "budget-instance-dimensions",
    }
    BUDGET_INSTANCE_DIMENSIONS: ClassVar["AiGatewayBudgetInstanceDimensionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetInstanceDimensionType.BUDGET_INSTANCE_DIMENSIONS = AiGatewayBudgetInstanceDimensionType(
    "budget-instance-dimensions"
)
