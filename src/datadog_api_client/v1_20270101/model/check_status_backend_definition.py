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
    from datadog_api_client.v1_20270101.model.check_status_backend_definition_grouping import (
        CheckStatusBackendDefinitionGrouping,
    )
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.check_status_backend_definition_type import (
        CheckStatusBackendDefinitionType,
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


class CheckStatusBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.check_status_backend_definition_grouping import (
            CheckStatusBackendDefinitionGrouping,
        )
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.check_status_backend_definition_type import (
            CheckStatusBackendDefinitionType,
        )

        return {
            "check": (str,),
            "description": (str,),
            "group": (str,),
            "group_by": ([str],),
            "grouping": (CheckStatusBackendDefinitionGrouping,),
            "notes": (str,),
            "tags": ([str],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (CheckStatusBackendDefinitionType,),
        }

    attribute_map = {
        "check": "check",
        "description": "description",
        "group": "group",
        "group_by": "group_by",
        "grouping": "grouping",
        "notes": "notes",
        "tags": "tags",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        check: str,
        grouping: CheckStatusBackendDefinitionGrouping,
        type: CheckStatusBackendDefinitionType,
        description: Union[str, UnsetType] = unset,
        group: Union[str, UnsetType] = unset,
        group_by: Union[List[str], UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
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

        :param check: Test-only generated schema for the dashboard versioning proof of concept.
        :type check: str

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param group: Test-only generated schema for the dashboard versioning proof of concept.
        :type group: str, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [str], optional

        :param grouping: Test-only generated schema for the dashboard versioning proof of concept.
        :type grouping: CheckStatusBackendDefinitionGrouping

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param tags: Test-only generated schema for the dashboard versioning proof of concept.
        :type tags: [str], optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CheckStatusBackendDefinitionType
        """
        if description is not unset:
            kwargs["description"] = description
        if group is not unset:
            kwargs["group"] = group
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if notes is not unset:
            kwargs["notes"] = notes
        if tags is not unset:
            kwargs["tags"] = tags
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.check = check
        self_.grouping = grouping
        self_.type = type
