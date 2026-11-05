# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_data import AiGatewayBudgetInstanceResetData


class AiGatewayBudgetInstanceResetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_data import AiGatewayBudgetInstanceResetData

        return {
            "data": (AiGatewayBudgetInstanceResetData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayBudgetInstanceResetData, **kwargs):
        """
        Request to reset one budget instance's active-period spend.

        :param data: Data used to reset one budget instance's active-period spend.
        :type data: AiGatewayBudgetInstanceResetData
        """
        super().__init__(kwargs)

        self_.data = data
