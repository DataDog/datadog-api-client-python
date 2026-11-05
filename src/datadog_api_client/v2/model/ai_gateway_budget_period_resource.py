# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_budget_period_attributes import AiGatewayBudgetPeriodAttributes
    from datadog_api_client.v2.model.ai_gateway_budget_period_type import AiGatewayBudgetPeriodType


class AiGatewayBudgetPeriodResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_period_attributes import AiGatewayBudgetPeriodAttributes
        from datadog_api_client.v2.model.ai_gateway_budget_period_type import AiGatewayBudgetPeriodType

        return {
            "attributes": (AiGatewayBudgetPeriodAttributes,),
            "id": (UUID,),
            "type": (AiGatewayBudgetPeriodType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayBudgetPeriodAttributes, id: UUID, type: AiGatewayBudgetPeriodType, **kwargs
    ):
        """
        Active accounting period for an AI Gateway budget.

        :param attributes: Accounting state enforced for an AI Gateway budget's active period.
        :type attributes: AiGatewayBudgetPeriodAttributes

        :param id: Budget identifier associated with this active period.
        :type id: UUID

        :param type: AI Gateway budget period resource type.
        :type type: AiGatewayBudgetPeriodType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
