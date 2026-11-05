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
    from datadog_api_client.v2.model.ai_gateway_budget_instance_attributes import AiGatewayBudgetInstanceAttributes
    from datadog_api_client.v2.model.ai_gateway_budget_instance_type import AiGatewayBudgetInstanceType


class AiGatewayBudgetInstanceResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instance_attributes import AiGatewayBudgetInstanceAttributes
        from datadog_api_client.v2.model.ai_gateway_budget_instance_type import AiGatewayBudgetInstanceType

        return {
            "attributes": (AiGatewayBudgetInstanceAttributes,),
            "id": (str,),
            "type": (AiGatewayBudgetInstanceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayBudgetInstanceAttributes, id: str, type: AiGatewayBudgetInstanceType, **kwargs
    ):
        """
        One budget instance counter.

        :param attributes: One budget instance counter.
        :type attributes: AiGatewayBudgetInstanceAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: Budget instance counter resource type.
        :type type: AiGatewayBudgetInstanceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
