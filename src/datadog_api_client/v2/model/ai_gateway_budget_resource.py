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
    from datadog_api_client.v2.model.ai_gateway_budget_attributes import AiGatewayBudgetAttributes
    from datadog_api_client.v2.model.ai_gateway_budget_type import AiGatewayBudgetType


class AiGatewayBudgetResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_attributes import AiGatewayBudgetAttributes
        from datadog_api_client.v2.model.ai_gateway_budget_type import AiGatewayBudgetType

        return {
            "attributes": (AiGatewayBudgetAttributes,),
            "id": (UUID,),
            "type": (AiGatewayBudgetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayBudgetAttributes, id: UUID, type: AiGatewayBudgetType, **kwargs):
        """
        AI Gateway budget resource.

        :param attributes: AI Gateway budget configuration and metadata.
        :type attributes: AiGatewayBudgetAttributes

        :param id: Resource identifier.
        :type id: UUID

        :param type: AI Gateway budget resource type.
        :type type: AiGatewayBudgetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
