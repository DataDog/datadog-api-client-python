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
    from datadog_api_client.v2.model.scanned_asset_metadata_asset import ScannedAssetMetadataAsset
    from datadog_api_client.v2.model.scanned_asset_metadata_last_success import ScannedAssetMetadataLastSuccess


class ScannedAssetMetadataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scanned_asset_metadata_asset import ScannedAssetMetadataAsset
        from datadog_api_client.v2.model.scanned_asset_metadata_last_success import ScannedAssetMetadataLastSuccess

        return {
            "asset": (ScannedAssetMetadataAsset,),
            "first_success_timestamp": (str,),
            "last_success": (ScannedAssetMetadataLastSuccess,),
        }

    attribute_map = {
        "asset": "asset",
        "first_success_timestamp": "first_success_timestamp",
        "last_success": "last_success",
    }

    def __init__(
        self_,
        asset: ScannedAssetMetadataAsset,
        first_success_timestamp: str,
        last_success: ScannedAssetMetadataLastSuccess,
        **kwargs,
    ):
        """
        The attributes of a scanned asset metadata.

        :param asset: The asset of a scanned asset metadata.
        :type asset: ScannedAssetMetadataAsset

        :param first_success_timestamp: The timestamp when the scan of the asset was performed for the first time.
        :type first_success_timestamp: str

        :param last_success: Metadata for the last successful scan of an asset.
        :type last_success: ScannedAssetMetadataLastSuccess
        """
        super().__init__(kwargs)

        self_.asset = asset
        self_.first_success_timestamp = first_success_timestamp
        self_.last_success = last_success
