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
    from datadog_api_client.v2.model.ai_gateway_discovered_model_attributes import AiGatewayDiscoveredModelAttributes
    from datadog_api_client.v2.model.ai_gateway_discovered_model_type import AiGatewayDiscoveredModelType


class AiGatewayDiscoveredModelResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_discovered_model_attributes import (
            AiGatewayDiscoveredModelAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_discovered_model_type import AiGatewayDiscoveredModelType

        return {
            "attributes": (AiGatewayDiscoveredModelAttributes,),
            "id": (str,),
            "type": (AiGatewayDiscoveredModelType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayDiscoveredModelAttributes, id: str, type: AiGatewayDiscoveredModelType, **kwargs
    ):
        """
        Discovered provider model resource.

        :param attributes: Model discovered from a provider integration account.
        :type attributes: AiGatewayDiscoveredModelAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: Discovered provider model resource type.
        :type type: AiGatewayDiscoveredModelType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
