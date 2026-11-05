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
    from datadog_api_client.v2.model.ai_gateway_provider_create_attributes import AiGatewayProviderCreateAttributes
    from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType


class AiGatewayProviderCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_create_attributes import AiGatewayProviderCreateAttributes
        from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType

        return {
            "attributes": (AiGatewayProviderCreateAttributes,),
            "type": (AiGatewayProviderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayProviderCreateAttributes, type: AiGatewayProviderType, **kwargs):
        """
        Data used to create an AI Gateway provider.

        :param attributes: Attributes used to create an AI Gateway provider.
        :type attributes: AiGatewayProviderCreateAttributes

        :param type: AI Gateway provider resource type.
        :type type: AiGatewayProviderType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
