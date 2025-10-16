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
    from datadog_api_client.v2.model.cloud_asset_type import CloudAssetType


class ScannedAssetMetadataAsset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_asset_type import CloudAssetType

        return {
            "name": (str,),
            "type": (CloudAssetType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: CloudAssetType, **kwargs):
        """
        The asset of a scanned asset metadata.

        :param name: The name of the asset.
        :type name: str

        :param type: The cloud asset type
        :type type: CloudAssetType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
