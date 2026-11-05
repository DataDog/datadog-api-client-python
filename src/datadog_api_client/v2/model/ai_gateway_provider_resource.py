# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_provider_attributes import AiGatewayProviderAttributes
    from datadog_api_client.v2.model.ai_gateway_provider_relationships import AiGatewayProviderRelationships
    from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType


class AiGatewayProviderResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_provider_attributes import AiGatewayProviderAttributes
        from datadog_api_client.v2.model.ai_gateway_provider_relationships import AiGatewayProviderRelationships
        from datadog_api_client.v2.model.ai_gateway_provider_type import AiGatewayProviderType

        return {
            "attributes": (AiGatewayProviderAttributes,),
            "id": (str,),
            "relationships": (AiGatewayProviderRelationships,),
            "type": (AiGatewayProviderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AiGatewayProviderAttributes,
        id: str,
        type: AiGatewayProviderType,
        relationships: Union[AiGatewayProviderRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        AI Gateway provider resource.

        :param attributes: AI Gateway provider configuration and metadata.
        :type attributes: AiGatewayProviderAttributes

        :param id: Resource identifier.
        :type id: str

        :param relationships: Provider relationships.
        :type relationships: AiGatewayProviderRelationships, optional

        :param type: AI Gateway provider resource type.
        :type type: AiGatewayProviderType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
