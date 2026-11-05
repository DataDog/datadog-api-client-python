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
    from datadog_api_client.v2.model.ai_gateway_rate_limit_update_attributes import AiGatewayRateLimitUpdateAttributes
    from datadog_api_client.v2.model.ai_gateway_rate_limit_type import AiGatewayRateLimitType


class AiGatewayRateLimitUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_update_attributes import (
            AiGatewayRateLimitUpdateAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_rate_limit_type import AiGatewayRateLimitType

        return {
            "attributes": (AiGatewayRateLimitUpdateAttributes,),
            "id": (UUID,),
            "type": (AiGatewayRateLimitType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayRateLimitUpdateAttributes, id: UUID, type: AiGatewayRateLimitType, **kwargs
    ):
        """
        Data used to update an AI Gateway rate limit.

        :param attributes: Attributes used to update an AI Gateway rate limit. Only sent fields are changed.
        :type attributes: AiGatewayRateLimitUpdateAttributes

        :param id: Rate limit UUID. Must match the path parameter.
        :type id: UUID

        :param type: AI Gateway rate limit resource type.
        :type type: AiGatewayRateLimitType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
