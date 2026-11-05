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
    from datadog_api_client.v2.model.ai_gateway_rate_limit_usage_attributes import AiGatewayRateLimitUsageAttributes
    from datadog_api_client.v2.model.ai_gateway_rate_limit_usage_type import AiGatewayRateLimitUsageType


class AiGatewayRateLimitUsageResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_usage_attributes import AiGatewayRateLimitUsageAttributes
        from datadog_api_client.v2.model.ai_gateway_rate_limit_usage_type import AiGatewayRateLimitUsageType

        return {
            "attributes": (AiGatewayRateLimitUsageAttributes,),
            "id": (str,),
            "type": (AiGatewayRateLimitUsageType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayRateLimitUsageAttributes, id: str, type: AiGatewayRateLimitUsageType, **kwargs
    ):
        """
        Live usage for one AI Gateway rate limit, or for the untracked or total traffic.

        :param attributes: Live consumption of one AI Gateway rate limit.
        :type attributes: AiGatewayRateLimitUsageAttributes

        :param id: Rate limit UUID, ``untracked`` for traffic no enforced rate limit covers, or ``total`` for all gateway traffic.
        :type id: str

        :param type: AI Gateway rate limit usage resource type.
        :type type: AiGatewayRateLimitUsageType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
