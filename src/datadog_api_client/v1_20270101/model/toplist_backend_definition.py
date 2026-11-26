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
    from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1_20270101.model.toplist_backend_request import ToplistBackendRequest
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style import ToplistBackendDefinitionStyle
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_type import ToplistBackendDefinitionType
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of import (
        ToplistBackendRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463319360 import (
        ToplistBackendRequest20270101OneOf4463319360,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463320800 import (
        ToplistBackendRequest20270101OneOf4463320800,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463321920 import (
        ToplistBackendRequest20270101OneOf4463321920,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463323520 import (
        ToplistBackendRequest20270101OneOf4463323520,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463325120 import (
        ToplistBackendRequest20270101OneOf4463325120,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463325920 import (
        ToplistBackendRequest20270101OneOf4463325920,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463326720 import (
        ToplistBackendRequest20270101OneOf4463326720,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463327520 import (
        ToplistBackendRequest20270101OneOf4463327520,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463328320 import (
        ToplistBackendRequest20270101OneOf4463328320,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463329120 import (
        ToplistBackendRequest20270101OneOf4463329120,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463526592 import (
        ToplistBackendRequest20270101OneOf4463526592,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463527392 import (
        ToplistBackendRequest20270101OneOf4463527392,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463528192 import (
        ToplistBackendRequest20270101OneOf4463528192,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463528992 import (
        ToplistBackendRequest20270101OneOf4463528992,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463529792 import (
        ToplistBackendRequest20270101OneOf4463529792,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463530592 import (
        ToplistBackendRequest20270101OneOf4463530592,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463531392 import (
        ToplistBackendRequest20270101OneOf4463531392,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463532192 import (
        ToplistBackendRequest20270101OneOf4463532192,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463532992 import (
        ToplistBackendRequest20270101OneOf4463532992,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463533792 import (
        ToplistBackendRequest20270101OneOf4463533792,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_request20270101_one_of4463535232 import (
        ToplistBackendRequest20270101OneOf4463535232,
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


class ToplistBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.toplist_backend_request import ToplistBackendRequest
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_style import ToplistBackendDefinitionStyle
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_type import ToplistBackendDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "notes": (str,),
            "requests": ([ToplistBackendRequest],),
            "style": (ToplistBackendDefinitionStyle,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ToplistBackendDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "description": "description",
        "notes": "notes",
        "requests": "requests",
        "style": "style",
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
                ToplistBackendRequest,
                ToplistBackendRequest20270101OneOf,
                ToplistBackendRequest20270101OneOf4463319360,
                ToplistBackendRequest20270101OneOf4463320800,
                ToplistBackendRequest20270101OneOf4463321920,
                ToplistBackendRequest20270101OneOf4463323520,
                ToplistBackendRequest20270101OneOf4463325120,
                ToplistBackendRequest20270101OneOf4463325920,
                ToplistBackendRequest20270101OneOf4463326720,
                ToplistBackendRequest20270101OneOf4463327520,
                ToplistBackendRequest20270101OneOf4463328320,
                ToplistBackendRequest20270101OneOf4463329120,
                ToplistBackendRequest20270101OneOf4463526592,
                ToplistBackendRequest20270101OneOf4463527392,
                ToplistBackendRequest20270101OneOf4463528192,
                ToplistBackendRequest20270101OneOf4463528992,
                ToplistBackendRequest20270101OneOf4463529792,
                ToplistBackendRequest20270101OneOf4463530592,
                ToplistBackendRequest20270101OneOf4463531392,
                ToplistBackendRequest20270101OneOf4463532192,
                ToplistBackendRequest20270101OneOf4463532992,
                ToplistBackendRequest20270101OneOf4463533792,
                ToplistBackendRequest20270101OneOf4463535232,
            ]
        ],
        type: ToplistBackendDefinitionType,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        style: Union[ToplistBackendDefinitionStyle, UnsetType] = unset,
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

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [ToplistBackendRequest]

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: ToplistBackendDefinitionStyle, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ToplistBackendDefinitionType
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if notes is not unset:
            kwargs["notes"] = notes
        if style is not unset:
            kwargs["style"] = style
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
