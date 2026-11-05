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
    from datadog_api_client.v2.model.ai_gateway_rate_limit_attributes import AiGatewayRateLimitAttributes
    from datadog_api_client.v2.model.ai_gateway_rate_limit_type import AiGatewayRateLimitType


class AiGatewayRateLimitResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_attributes import AiGatewayRateLimitAttributes
        from datadog_api_client.v2.model.ai_gateway_rate_limit_type import AiGatewayRateLimitType

        return {
            "attributes": (AiGatewayRateLimitAttributes,),
            "id": (UUID,),
            "type": (AiGatewayRateLimitType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayRateLimitAttributes, id: UUID, type: AiGatewayRateLimitType, **kwargs):
        """
        AI Gateway rate limit resource.

        :param attributes: Attributes of an AI Gateway rate limit.
        :type attributes: AiGatewayRateLimitAttributes

        :param id: Rate limit UUID.
        :type id: UUID

        :param type: AI Gateway rate limit resource type.
        :type type: AiGatewayRateLimitType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
