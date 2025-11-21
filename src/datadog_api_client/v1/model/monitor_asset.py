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
    from datadog_api_client.v1.model.monitor_asset_category import MonitorAssetCategory
    from datadog_api_client.v1.model.monitor_asset_resource_type import MonitorAssetResourceType


class MonitorAsset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_asset_category import MonitorAssetCategory
        from datadog_api_client.v1.model.monitor_asset_resource_type import MonitorAssetResourceType

        return {
            "category": (MonitorAssetCategory,),
            "name": (str,),
            "resource_key": (str,),
            "resource_type": (MonitorAssetResourceType,),
            "url": (str,),
        }

    attribute_map = {
        "category": "category",
        "name": "name",
        "resource_key": "resource_key",
        "resource_type": "resource_type",
        "url": "url",
    }

    def __init__(
        self_,
        category: MonitorAssetCategory,
        name: str,
        url: str,
        resource_key: Union[str, UnsetType] = unset,
        resource_type: Union[MonitorAssetResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents key links tied to a monitor to help users take action on alerts.
        This feature is in Preview and only available to users with the feature enabled.

        :param category: Indicates the type of asset this entity represents on a monitor.
        :type category: MonitorAssetCategory

        :param name: Name for the monitor asset
        :type name: str

        :param resource_key: Represents the identifier of the internal Datadog resource that this asset represents. IDs in this field should be passed in as strings.
        :type resource_key: str, optional

        :param resource_type: Type of internal Datadog resource associated with a monitor asset.
        :type resource_type: MonitorAssetResourceType, optional

        :param url: URL link for the asset. For links with an internal resource type set, this should be the relative path to where the Datadog domain is appended internally. For external links, this should be the full URL path.
        :type url: str
        """
        if resource_key is not unset:
            kwargs["resource_key"] = resource_key
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        super().__init__(kwargs)

        self_.category = category
        self_.name = name
        self_.url = url
