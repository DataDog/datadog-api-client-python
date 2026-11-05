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
    from datadog_api_client.v2.model.ai_gateway_budget_resource import AiGatewayBudgetResource


class AiGatewayBudgetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_resource import AiGatewayBudgetResource

        return {
            "data": (AiGatewayBudgetResource,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AiGatewayBudgetResource, **kwargs):
        """
        Response containing one AI Gateway budget.

        :param data: AI Gateway budget resource.
        :type data: AiGatewayBudgetResource
        """
        super().__init__(kwargs)

        self_.data = data
