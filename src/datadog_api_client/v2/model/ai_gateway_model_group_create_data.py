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
    from datadog_api_client.v2.model.ai_gateway_model_group_create_attributes import AiGatewayModelGroupCreateAttributes
    from datadog_api_client.v2.model.ai_gateway_model_group_type import AiGatewayModelGroupType


class AiGatewayModelGroupCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_group_create_attributes import (
            AiGatewayModelGroupCreateAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_model_group_type import AiGatewayModelGroupType

        return {
            "attributes": (AiGatewayModelGroupCreateAttributes,),
            "type": (AiGatewayModelGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayModelGroupCreateAttributes, type: AiGatewayModelGroupType, **kwargs):
        """
        Data used to create an AI Gateway model group.

        :param attributes: Attributes used to create an AI Gateway model group.
        :type attributes: AiGatewayModelGroupCreateAttributes

        :param type: AI Gateway model group resource type.
        :type type: AiGatewayModelGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
