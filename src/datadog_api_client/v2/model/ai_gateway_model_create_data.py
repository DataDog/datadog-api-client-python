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
    from datadog_api_client.v2.model.ai_gateway_model_create_attributes import AiGatewayModelCreateAttributes
    from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_type import AiGatewayModelCatalogEntryType


class AiGatewayModelCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_create_attributes import AiGatewayModelCreateAttributes
        from datadog_api_client.v2.model.ai_gateway_model_catalog_entry_type import AiGatewayModelCatalogEntryType

        return {
            "attributes": (AiGatewayModelCreateAttributes,),
            "type": (AiGatewayModelCatalogEntryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AiGatewayModelCreateAttributes, type: AiGatewayModelCatalogEntryType, **kwargs):
        """
        Data used to create a model catalog entry.

        :param attributes: Attributes used to create a model catalog entry.
        :type attributes: AiGatewayModelCreateAttributes

        :param type: Model catalog entry resource type.
        :type type: AiGatewayModelCatalogEntryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
