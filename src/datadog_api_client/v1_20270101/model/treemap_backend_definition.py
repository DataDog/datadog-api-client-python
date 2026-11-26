# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.treemap_backend_definition_color_by import TreemapBackendDefinitionColorBy
    from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1_20270101.model.treemap_backend_definition_group_by import TreemapBackendDefinitionGroupBy
    from datadog_api_client.v1_20270101.model.treemap_backend_request import TreemapBackendRequest
    from datadog_api_client.v1_20270101.model.treemap_backend_definition_size_by import TreemapBackendDefinitionSizeBy
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.treemap_backend_definition_type import TreemapBackendDefinitionType
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.treemap_backend_request20270101_one_of import (
        TreemapBackendRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.treemap_backend_request20270101_one_of4463750144 import (
        TreemapBackendRequest20270101OneOf4463750144,
    )
    from datadog_api_client.v1_20270101.model.treemap_backend_request20270101_one_of4463751424 import (
        TreemapBackendRequest20270101OneOf4463751424,
    )
    from datadog_api_client.v1_20270101.model.treemap_backend_request20270101_one_of4463752384 import (
        TreemapBackendRequest20270101OneOf4463752384,
    )
    from datadog_api_client.v1_20270101.model.treemap_backend_request20270101_one_of4463753824 import (
        TreemapBackendRequest20270101OneOf4463753824,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of import WidgetTime20270101OneOf
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464103552 import (
        WidgetTime20270101OneOf4464103552,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464104512 import (
        WidgetTime20270101OneOf4464104512,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464105312 import (
        WidgetTime20270101OneOf4464105312,
    )
    from datadog_api_client.v1.model.widget_time20270101_one_of4464105952 import WidgetTime20270101OneOf4464105952


class TreemapBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.treemap_backend_definition_color_by import (
            TreemapBackendDefinitionColorBy,
        )
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.treemap_backend_definition_group_by import (
            TreemapBackendDefinitionGroupBy,
        )
        from datadog_api_client.v1_20270101.model.treemap_backend_request import TreemapBackendRequest
        from datadog_api_client.v1_20270101.model.treemap_backend_definition_size_by import (
            TreemapBackendDefinitionSizeBy,
        )
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.treemap_backend_definition_type import TreemapBackendDefinitionType

        return {
            "color_by": (TreemapBackendDefinitionColorBy,),
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "group_by": (TreemapBackendDefinitionGroupBy,),
            "notes": (str,),
            "requests": ([TreemapBackendRequest],),
            "size_by": (TreemapBackendDefinitionSizeBy,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (TreemapBackendDefinitionType,),
        }

    attribute_map = {
        "color_by": "color_by",
        "custom_links": "custom_links",
        "description": "description",
        "group_by": "group_by",
        "notes": "notes",
        "requests": "requests",
        "size_by": "size_by",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[
            Union[
                TreemapBackendRequest,
                TreemapBackendRequest20270101OneOf,
                TreemapBackendRequest20270101OneOf4463750144,
                TreemapBackendRequest20270101OneOf4463751424,
                TreemapBackendRequest20270101OneOf4463752384,
                TreemapBackendRequest20270101OneOf4463753824,
            ]
        ],
        type: TreemapBackendDefinitionType,
        color_by: Union[TreemapBackendDefinitionColorBy, UnsetType] = unset,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        group_by: Union[TreemapBackendDefinitionGroupBy, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        size_by: Union[TreemapBackendDefinitionSizeBy, UnsetType] = unset,
        time: Union[
            WidgetTime,
            WidgetTime20270101OneOf,
            WidgetTime20270101OneOf4464103552,
            WidgetTime20270101OneOf4464104512,
            WidgetTime20270101OneOf4464105312,
            WidgetTime20270101OneOf4464105952,
            EmptyObject,
            UnsetType,
        ] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_by: TreemapBackendDefinitionColorBy, optional

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: TreemapBackendDefinitionGroupBy, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [TreemapBackendRequest]

        :param size_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type size_by: TreemapBackendDefinitionSizeBy, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: TreemapBackendDefinitionType
        """
        if color_by is not unset:
            kwargs["color_by"] = color_by
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if notes is not unset:
            kwargs["notes"] = notes
        if size_by is not unset:
            kwargs["size_by"] = size_by
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
