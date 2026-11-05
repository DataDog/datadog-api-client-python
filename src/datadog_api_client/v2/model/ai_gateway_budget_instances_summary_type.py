# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetInstancesSummaryType(ModelSimple):
    """
    Budget instance summary resource type.

    :param value: If omitted defaults to "budget-instances-summary". Must be one of ["budget-instances-summary"].
    :type value: str
    """

    allowed_values = {
        "budget-instances-summary",
    }
    BUDGET_INSTANCES_SUMMARY: ClassVar["AiGatewayBudgetInstancesSummaryType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetInstancesSummaryType.BUDGET_INSTANCES_SUMMARY = AiGatewayBudgetInstancesSummaryType(
    "budget-instances-summary"
)
