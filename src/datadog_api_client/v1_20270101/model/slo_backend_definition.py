# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.slo_widget_time_window import SloWidgetTimeWindow
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.slo_backend_definition_type import SloBackendDefinitionType
    from datadog_api_client.v1_20270101.model.slo_widget_view_mode import SloWidgetViewMode
    from datadog_api_client.v1_20270101.model.slo_backend_definition_view_type import SloBackendDefinitionViewType
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


class SloBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.slo_widget_time_window import SloWidgetTimeWindow
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.slo_backend_definition_type import SloBackendDefinitionType
        from datadog_api_client.v1_20270101.model.slo_widget_view_mode import SloWidgetViewMode
        from datadog_api_client.v1_20270101.model.slo_backend_definition_view_type import SloBackendDefinitionViewType

        return {
            "additional_query_filters": (str,),
            "description": (str,),
            "global_time_target": (str,),
            "notes": (str,),
            "show_error_budget": (bool,),
            "slo_id": (str, none_type),
            "time": (WidgetTime,),
            "time_windows": ([SloWidgetTimeWindow],),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SloBackendDefinitionType,),
            "view_mode": (SloWidgetViewMode,),
            "view_type": (SloBackendDefinitionViewType,),
        }

    attribute_map = {
        "additional_query_filters": "additional_query_filters",
        "description": "description",
        "global_time_target": "global_time_target",
        "notes": "notes",
        "show_error_budget": "show_error_budget",
        "slo_id": "slo_id",
        "time": "time",
        "time_windows": "time_windows",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "view_mode": "view_mode",
        "view_type": "view_type",
    }

    def __init__(
        self_,
        show_error_budget: bool,
        slo_id: Union[str, none_type],
        time_windows: List[SloWidgetTimeWindow],
        type: SloBackendDefinitionType,
        view_mode: SloWidgetViewMode,
        view_type: SloBackendDefinitionViewType,
        additional_query_filters: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        global_time_target: Union[str, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
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

        :param additional_query_filters: Test-only generated schema for the dashboard versioning proof of concept.
        :type additional_query_filters: str, optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param global_time_target: Test-only generated schema for the dashboard versioning proof of concept.
        :type global_time_target: str, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param show_error_budget: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_error_budget: bool

        :param slo_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type slo_id: str, none_type

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param time_windows: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_windows: [SloWidgetTimeWindow]

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: SloBackendDefinitionType

        :param view_mode: Test-only generated schema for the dashboard versioning proof of concept.
        :type view_mode: SloWidgetViewMode

        :param view_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type view_type: SloBackendDefinitionViewType
        """
        if additional_query_filters is not unset:
            kwargs["additional_query_filters"] = additional_query_filters
        if description is not unset:
            kwargs["description"] = description
        if global_time_target is not unset:
            kwargs["global_time_target"] = global_time_target
        if notes is not unset:
            kwargs["notes"] = notes
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.show_error_budget = show_error_budget
        self_.slo_id = slo_id
        self_.time_windows = time_windows
        self_.type = type
        self_.view_mode = view_mode
        self_.view_type = view_type
