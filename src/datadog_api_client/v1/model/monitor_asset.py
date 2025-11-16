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
            "options": (dict,),
            "resource_key": (str,),
            "resource_type": (MonitorAssetResourceType,),
            "template_variables": (dict,),
            "url": (str,),
        }

    attribute_map = {
        "category": "category",
        "name": "name",
        "options": "options",
        "resource_key": "resource_key",
        "resource_type": "resource_type",
        "template_variables": "template_variables",
        "url": "url",
    }

    def __init__(
        self_,
        category: MonitorAssetCategory,
        name: str,
        url: str,
        options: Union[dict, UnsetType] = unset,
        resource_key: Union[str, UnsetType] = unset,
        resource_type: Union[MonitorAssetResourceType, UnsetType] = unset,
        template_variables: Union[dict, UnsetType] = unset,
        **kwargs,
    ):
        """
        Represents key links tied to a monitor to help users take action on alerts (runbooks, dashboards, Workflows).
        This feature is in Preview and only available to users with the feature enabled.

        :param category: Indicates the type of asset this entity represents on a monitor.
        :type category: MonitorAssetCategory

        :param name: Name for the monitor asset
        :type name: str

        :param options: Additional options that you can set on a monitor asset.
        :type options: dict, optional

        :param resource_key: Represents the identifier of the internal datadog resource that this asset represents. IDs in this field should be passed in as strings.
        :type resource_key: str, optional

        :param resource_type: Type of internal datadog resource associated with a monitor asset.
        :type resource_type: MonitorAssetResourceType, optional

        :param template_variables: Allows you to parameterize the URL for the monitor asset.
        :type template_variables: dict, optional

        :param url: Url link for the asset
        :type url: str
        """
        if options is not unset:
            kwargs["options"] = options
        if resource_key is not unset:
            kwargs["resource_key"] = resource_key
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        super().__init__(kwargs)

        self_.category = category
        self_.name = name
        self_.url = url
