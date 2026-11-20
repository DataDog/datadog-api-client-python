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
    from datadog_api_client.v1_20270101.model.has_search_bar import HasSearchBar
    from datadog_api_client.v1_20270101.model.query_table_backend_request import QueryTableBackendRequest
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.query_table_backend_definition_type import QueryTableBackendDefinitionType
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of import (
        QueryTableBackendRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4459913248 import (
        QueryTableBackendRequest20270101OneOf4459913248,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4459916288 import (
        QueryTableBackendRequest20270101OneOf4459916288,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4459919328 import (
        QueryTableBackendRequest20270101OneOf4459919328,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460101856 import (
        QueryTableBackendRequest20270101OneOf4460101856,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460104096 import (
        QueryTableBackendRequest20270101OneOf4460104096,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460106336 import (
        QueryTableBackendRequest20270101OneOf4460106336,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460108576 import (
        QueryTableBackendRequest20270101OneOf4460108576,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460110816 import (
        QueryTableBackendRequest20270101OneOf4460110816,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460113056 import (
        QueryTableBackendRequest20270101OneOf4460113056,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460115296 import (
        QueryTableBackendRequest20270101OneOf4460115296,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460117536 import (
        QueryTableBackendRequest20270101OneOf4460117536,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460300064 import (
        QueryTableBackendRequest20270101OneOf4460300064,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460302304 import (
        QueryTableBackendRequest20270101OneOf4460302304,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460304544 import (
        QueryTableBackendRequest20270101OneOf4460304544,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460306784 import (
        QueryTableBackendRequest20270101OneOf4460306784,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460309024 import (
        QueryTableBackendRequest20270101OneOf4460309024,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460311264 import (
        QueryTableBackendRequest20270101OneOf4460311264,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460313504 import (
        QueryTableBackendRequest20270101OneOf4460313504,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460513216 import (
        QueryTableBackendRequest20270101OneOf4460513216,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460516096 import (
        QueryTableBackendRequest20270101OneOf4460516096,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460519136 import (
        QueryTableBackendRequest20270101OneOf4460519136,
    )
    from datadog_api_client.v1_20270101.model.query_table_backend_request20270101_one_of4460522016 import (
        QueryTableBackendRequest20270101OneOf4460522016,
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


class QueryTableBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.has_search_bar import HasSearchBar
        from datadog_api_client.v1_20270101.model.query_table_backend_request import QueryTableBackendRequest
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.query_table_backend_definition_type import (
            QueryTableBackendDefinitionType,
        )

        return {
            "auto_horizontal_scrolling": (bool,),
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "has_search_bar": (HasSearchBar,),
            "notes": (str,),
            "num_sticky_columns": (float,),
            "requests": ([QueryTableBackendRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (QueryTableBackendDefinitionType,),
        }

    attribute_map = {
        "auto_horizontal_scrolling": "auto_horizontal_scrolling",
        "custom_links": "custom_links",
        "description": "description",
        "has_search_bar": "has_search_bar",
        "notes": "notes",
        "num_sticky_columns": "num_sticky_columns",
        "requests": "requests",
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
                QueryTableBackendRequest,
                QueryTableBackendRequest20270101OneOf,
                QueryTableBackendRequest20270101OneOf4459913248,
                QueryTableBackendRequest20270101OneOf4459916288,
                QueryTableBackendRequest20270101OneOf4459919328,
                QueryTableBackendRequest20270101OneOf4460101856,
                QueryTableBackendRequest20270101OneOf4460104096,
                QueryTableBackendRequest20270101OneOf4460106336,
                QueryTableBackendRequest20270101OneOf4460108576,
                QueryTableBackendRequest20270101OneOf4460110816,
                QueryTableBackendRequest20270101OneOf4460113056,
                QueryTableBackendRequest20270101OneOf4460115296,
                QueryTableBackendRequest20270101OneOf4460117536,
                QueryTableBackendRequest20270101OneOf4460300064,
                QueryTableBackendRequest20270101OneOf4460302304,
                QueryTableBackendRequest20270101OneOf4460304544,
                QueryTableBackendRequest20270101OneOf4460306784,
                QueryTableBackendRequest20270101OneOf4460309024,
                QueryTableBackendRequest20270101OneOf4460311264,
                QueryTableBackendRequest20270101OneOf4460313504,
                QueryTableBackendRequest20270101OneOf4460513216,
                QueryTableBackendRequest20270101OneOf4460516096,
                QueryTableBackendRequest20270101OneOf4460519136,
                QueryTableBackendRequest20270101OneOf4460522016,
            ]
        ],
        type: QueryTableBackendDefinitionType,
        auto_horizontal_scrolling: Union[bool, UnsetType] = unset,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        has_search_bar: Union[HasSearchBar, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        num_sticky_columns: Union[float, UnsetType] = unset,
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

        :param auto_horizontal_scrolling: Test-only generated schema for the dashboard versioning proof of concept.
        :type auto_horizontal_scrolling: bool, optional

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param has_search_bar: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_search_bar: HasSearchBar, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param num_sticky_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type num_sticky_columns: float, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [QueryTableBackendRequest]

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: QueryTableBackendDefinitionType
        """
        if auto_horizontal_scrolling is not unset:
            kwargs["auto_horizontal_scrolling"] = auto_horizontal_scrolling
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if has_search_bar is not unset:
            kwargs["has_search_bar"] = has_search_bar
        if notes is not unset:
            kwargs["notes"] = notes
        if num_sticky_columns is not unset:
            kwargs["num_sticky_columns"] = num_sticky_columns
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
