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
    from datadog_api_client.v2.model.ai_gateway_model_group_attributes import AiGatewayModelGroupAttributes
    from datadog_api_client.v2.model.ai_gateway_model_group_type import AiGatewayModelGroupType


class AiGatewayModelGroupResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_group_attributes import AiGatewayModelGroupAttributes
        from datadog_api_client.v2.model.ai_gateway_model_group_type import AiGatewayModelGroupType

        return {
            "attributes": (AiGatewayModelGroupAttributes,),
            "id": (str,),
            "type": (AiGatewayModelGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayModelGroupAttributes, id: str, type: AiGatewayModelGroupType, **kwargs):
        """
        AI Gateway model group resource.

        :param attributes: Complete AI Gateway model group configuration.
        :type attributes: AiGatewayModelGroupAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: AI Gateway model group resource type.
        :type type: AiGatewayModelGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
