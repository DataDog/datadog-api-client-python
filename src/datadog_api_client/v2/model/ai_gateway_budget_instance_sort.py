# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayBudgetInstanceSort(ModelSimple):
    """
    Sort order for budget instance counters.

    :param value: If omitted defaults to "spend_desc". Must be one of ["spend_desc", "spend_asc", "key_asc"].
    :type value: str
    """

    allowed_values = {
        "spend_desc",
        "spend_asc",
        "key_asc",
    }
    SPEND_DESC: ClassVar["AiGatewayBudgetInstanceSort"]
    SPEND_ASC: ClassVar["AiGatewayBudgetInstanceSort"]
    KEY_ASC: ClassVar["AiGatewayBudgetInstanceSort"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayBudgetInstanceSort.SPEND_DESC = AiGatewayBudgetInstanceSort("spend_desc")
AiGatewayBudgetInstanceSort.SPEND_ASC = AiGatewayBudgetInstanceSort("spend_asc")
AiGatewayBudgetInstanceSort.KEY_ASC = AiGatewayBudgetInstanceSort("key_asc")
