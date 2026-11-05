# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_budget_instance_resource import AiGatewayBudgetInstanceResource
    from datadog_api_client.v2.model.ai_gateway_restricted_details_meta import AiGatewayRestrictedDetailsMeta


class AiGatewayBudgetInstanceListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_budget_instance_resource import AiGatewayBudgetInstanceResource
        from datadog_api_client.v2.model.ai_gateway_restricted_details_meta import AiGatewayRestrictedDetailsMeta

        return {
            "data": ([AiGatewayBudgetInstanceResource],),
            "meta": (AiGatewayRestrictedDetailsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[AiGatewayBudgetInstanceResource], meta: AiGatewayRestrictedDetailsMeta, **kwargs):
        """
        Response containing budget instance counters.

        :param data:
        :type data: [AiGatewayBudgetInstanceResource]

        :param meta: Visibility information for identifying instance details.
        :type meta: AiGatewayRestrictedDetailsMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
