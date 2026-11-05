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
    from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_attributes import (
        AiGatewayModelCatalogEntryAttributes,
    )
    from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_type import AiGatewayModelCatalogEntryType


class AiGatewayModelCatalogEntryResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_attributes import (
            AiGatewayModelCatalogEntryAttributes,
        )
        from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_type import AiGatewayModelCatalogEntryType

        return {
            "attributes": (AiGatewayModelCatalogEntryAttributes,),
            "id": (str,),
            "type": (AiGatewayModelCatalogEntryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: AiGatewayModelCatalogEntryAttributes, id: str, type: AiGatewayModelCatalogEntryType, **kwargs
    ):
        """
        AI Gateway model catalog entry resource.

        :param attributes: Model catalog entry configuration and metadata.
        :type attributes: AiGatewayModelCatalogEntryAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: Model catalog entry resource type.
        :type type: AiGatewayModelCatalogEntryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
