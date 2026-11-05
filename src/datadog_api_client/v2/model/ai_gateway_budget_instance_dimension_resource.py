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
    from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_attributes import (
        AiGatewayBudgetInstanceDimensionAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_type import (
        AiGatewayBudgetInstanceDimensionType,
    )


class AiGatewayBudgetInstanceDimensionResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_attributes import (
            AiGatewayBudgetInstanceDimensionAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_budget_instance_dimension_type import (
            AiGatewayBudgetInstanceDimensionType,
        )

        return {
            "attributes": (AiGatewayBudgetInstanceDimensionAttributes,),
            "id": (str,),
            "type": (AiGatewayBudgetInstanceDimensionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayBudgetInstanceDimensionAttributes,
        id: str,
        type: AiGatewayBudgetInstanceDimensionType,
        **kwargs,
    ):
        """
        Values of one budget split dimension.

        :param attributes: Values of one budget split dimension.
        :type attributes: AiGatewayBudgetInstanceDimensionAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: Budget split dimension values resource type.
        :type type: AiGatewayBudgetInstanceDimensionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
