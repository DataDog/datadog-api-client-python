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
    from datadog_api_client.v2.model.ai_gateway_rate_limit_instances_summary_resource import (
        AiGatewayRateLimitInstancesSummaryResource,
    )


class AiGatewayRateLimitInstancesSummaryListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_instances_summary_resource import (
            AiGatewayRateLimitInstancesSummaryResource,
        )

        return {
            "data": ([AiGatewayRateLimitInstancesSummaryResource],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[AiGatewayRateLimitInstancesSummaryResource], **kwargs):
        """
        Response containing the counter summary of every template rate limit in the organization.

        :param data:
        :type data: [AiGatewayRateLimitInstancesSummaryResource]
        """
        super().__init__(kwargs)

        self_.data = data
