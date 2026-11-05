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
    from datadog_api_client.v2.model.ai_gateway_provider_update_attributes import AiGatewayProviderUpdateAttributes
    from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType


class AiGatewayProviderUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_update_attributes import AiGatewayProviderUpdateAttributes
        from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType

        return {
            "attributes": (AiGatewayProviderUpdateAttributes,),
            "id": (str,),
            "type": (AiGatewayProviderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayProviderUpdateAttributes, id: str, type: AiGatewayProviderType, **kwargs):
        """
        Data used to update an AI Gateway provider.

        :param attributes: Attributes used to update an AI Gateway provider.
        :type attributes: AiGatewayProviderUpdateAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: AI Gateway provider resource type.
        :type type: AiGatewayProviderType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
