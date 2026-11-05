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
    from datadog_api_client.v2.model.ai_gateway_budget_instances_summary_attributes import (
        AiGatewayBudgetInstancesSummaryAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_budget_instances_summary_type import AiGatewayBudgetInstancesSummaryType


class AiGatewayBudgetInstancesSummaryResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instances_summary_attributes import (
            AiGatewayBudgetInstancesSummaryAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_budget_instances_summary_type import (
            AiGatewayBudgetInstancesSummaryType,
        )

        return {
            "attributes": (AiGatewayBudgetInstancesSummaryAttributes,),
            "id": (UUID,),
            "type": (AiGatewayBudgetInstancesSummaryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayBudgetInstancesSummaryAttributes,
        id: UUID,
        type: AiGatewayBudgetInstancesSummaryType,
        **kwargs,
    ):
        """
        Aggregate state across budget instance counters.

        :param attributes: Aggregate state across budget instance counters.
        :type attributes: AiGatewayBudgetInstancesSummaryAttributes

        :param id: Resource identifier.
        :type id: UUID

        :param type: Budget instance summary resource type.
        :type type: AiGatewayBudgetInstancesSummaryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
