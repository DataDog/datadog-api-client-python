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
    from datadog_api_client.v2.model.ai_gateway_rate_limit_instance_attributes import (
        AiGatewayRateLimitInstanceAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_rate_limit_instance_type import AiGatewayRateLimitInstanceType


class AiGatewayRateLimitInstanceResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_instance_attributes import (
            AiGatewayRateLimitInstanceAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_rate_limit_instance_type import AiGatewayRateLimitInstanceType

        return {
            "attributes": (AiGatewayRateLimitInstanceAttributes,),
            "id": (str,),
            "type": (AiGatewayRateLimitInstanceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayRateLimitInstanceAttributes, id: str, type: AiGatewayRateLimitInstanceType, **kwargs
    ):
        """
        One counter of a template rate limit.

        :param attributes: One counter of a template rate limit and its live usage.
        :type attributes: AiGatewayRateLimitInstanceAttributes

        :param id: Counter ID, the rate limit UUID and instance key joined by ``|``.
        :type id: str

        :param type: AI Gateway rate limit counter resource type.
        :type type: AiGatewayRateLimitInstanceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
