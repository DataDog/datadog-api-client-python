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
    from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_attributes import (
        AiGatewayBudgetInstanceResetAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_budget_instance_type import AiGatewayBudgetInstanceType


class AiGatewayBudgetInstanceResetData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instance_reset_attributes import (
            AiGatewayBudgetInstanceResetAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_budget_instance_type import AiGatewayBudgetInstanceType

        return {
            "attributes": (AiGatewayBudgetInstanceResetAttributes,),
            "type": (AiGatewayBudgetInstanceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayBudgetInstanceResetAttributes, type: AiGatewayBudgetInstanceType, **kwargs
    ):
        """
        Data used to reset one budget instance's active-period spend.

        :param attributes: Attributes used to reset one budget instance's active-period spend.
        :type attributes: AiGatewayBudgetInstanceResetAttributes

        :param type: Budget instance counter resource type.
        :type type: AiGatewayBudgetInstanceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
