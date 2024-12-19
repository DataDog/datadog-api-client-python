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
    from datadog_api_client.v2.model.asset_attributes import AssetAttributes
    from datadog_api_client.v2.model.asset_entity_type import AssetEntityType


class Asset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asset_attributes import AssetAttributes
        from datadog_api_client.v2.model.asset_entity_type import AssetEntityType

        return {
            "attributes": (AssetAttributes,),
            "id": (str,),
            "type": (AssetEntityType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AssetAttributes, id: str, type: AssetEntityType, **kwargs):
        """
        A single vulnerable asset

        :param attributes: The JSON:API attributes of the asset.
        :type attributes: AssetAttributes

        :param id: The unique ID for this asset.
        :type id: str

        :param type: The JSON:API type.
        :type type: AssetEntityType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
