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
    from datadog_api_client.v2.model.scanned_asset_metadata_attributes import ScannedAssetMetadataAttributes


class ScannedAssetMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scanned_asset_metadata_attributes import ScannedAssetMetadataAttributes

        return {
            "attributes": (ScannedAssetMetadataAttributes,),
            "id": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
    }

    def __init__(self_, attributes: ScannedAssetMetadataAttributes, id: str, **kwargs):
        """
        The metadata of a scanned asset.

        :param attributes: The attributes of a scanned asset metadata.
        :type attributes: ScannedAssetMetadataAttributes

        :param id: The ID of the scanned asset metadata.
        :type id: str
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
