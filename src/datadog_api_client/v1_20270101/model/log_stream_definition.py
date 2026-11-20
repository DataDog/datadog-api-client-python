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
    from datadog_api_client.v1_20270101.model.message_display import MessageDisplay
    from datadog_api_client.v1_20270101.model.sort_pair import SortPair
    from datadog_api_client.v1_20270101.model.storage_type import StorageType
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.log_stream_definition_type import LogStreamDefinitionType
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


class LogStreamDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.message_display import MessageDisplay
        from datadog_api_client.v1_20270101.model.sort_pair import SortPair
        from datadog_api_client.v1_20270101.model.storage_type import StorageType
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.log_stream_definition_type import LogStreamDefinitionType

        return {
            "columns": ([str],),
            "cross_org_uuids": ([str],),
            "description": (str,),
            "indexes": ([str],),
            "message_display": (MessageDisplay,),
            "notes": (str,),
            "query": (str,),
            "show_date_column": (bool,),
            "show_message_column": (bool,),
            "sort": (SortPair,),
            "storage": (StorageType,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (LogStreamDefinitionType,),
        }

    attribute_map = {
        "columns": "columns",
        "cross_org_uuids": "cross_org_uuids",
        "description": "description",
        "indexes": "indexes",
        "message_display": "message_display",
        "notes": "notes",
        "query": "query",
        "show_date_column": "show_date_column",
        "show_message_column": "show_message_column",
        "sort": "sort",
        "storage": "storage",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        type: LogStreamDefinitionType,
        columns: Union[List[str], UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        message_display: Union[MessageDisplay, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        show_date_column: Union[bool, UnsetType] = unset,
        show_message_column: Union[bool, UnsetType] = unset,
        sort: Union[SortPair, UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
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

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [str], optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param message_display: Test-only generated schema for the dashboard versioning proof of concept.
        :type message_display: MessageDisplay, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str, optional

        :param show_date_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_date_column: bool, optional

        :param show_message_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_message_column: bool, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: SortPair, optional

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: LogStreamDefinitionType
        """
        if columns is not unset:
            kwargs["columns"] = columns
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if description is not unset:
            kwargs["description"] = description
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if message_display is not unset:
            kwargs["message_display"] = message_display
        if notes is not unset:
            kwargs["notes"] = notes
        if query is not unset:
            kwargs["query"] = query
        if show_date_column is not unset:
            kwargs["show_date_column"] = show_date_column
        if show_message_column is not unset:
            kwargs["show_message_column"] = show_message_column
        if sort is not unset:
            kwargs["sort"] = sort
        if storage is not unset:
            kwargs["storage"] = storage
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.type = type
