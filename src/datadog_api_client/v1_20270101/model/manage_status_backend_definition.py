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
    from datadog_api_client.v1_20270101.model.manage_status_backend_definition_color_preference import (
        ManageStatusBackendDefinitionColorPreference,
    )
    from datadog_api_client.v1_20270101.model.manage_status_backend_definition_display_format import (
        ManageStatusBackendDefinitionDisplayFormat,
    )
    from datadog_api_client.v1_20270101.model.manage_status_backend_definition_last_triggered_format import (
        ManageStatusBackendDefinitionLastTriggeredFormat,
    )
    from datadog_api_client.v1_20270101.model.manage_status_backend_definition_summary_type import (
        ManageStatusBackendDefinitionSummaryType,
    )
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.manage_status_backend_definition_type import (
        ManageStatusBackendDefinitionType,
    )


class ManageStatusBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.manage_status_backend_definition_color_preference import (
            ManageStatusBackendDefinitionColorPreference,
        )
        from datadog_api_client.v1_20270101.model.manage_status_backend_definition_display_format import (
            ManageStatusBackendDefinitionDisplayFormat,
        )
        from datadog_api_client.v1_20270101.model.manage_status_backend_definition_last_triggered_format import (
            ManageStatusBackendDefinitionLastTriggeredFormat,
        )
        from datadog_api_client.v1_20270101.model.manage_status_backend_definition_summary_type import (
            ManageStatusBackendDefinitionSummaryType,
        )
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.manage_status_backend_definition_type import (
            ManageStatusBackendDefinitionType,
        )

        return {
            "color_preference": (ManageStatusBackendDefinitionColorPreference,),
            "count": (float,),
            "description": (str,),
            "display_format": (ManageStatusBackendDefinitionDisplayFormat,),
            "hide_zero_counts": (bool,),
            "last_triggered_format": (ManageStatusBackendDefinitionLastTriggeredFormat,),
            "notes": (str,),
            "query": (str,),
            "show_investigation": (bool,),
            "show_last_triggered": (bool,),
            "show_priority": (bool,),
            "show_status": (bool,),
            "sort": (str,),
            "start": (float,),
            "summary_type": (ManageStatusBackendDefinitionSummaryType,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ManageStatusBackendDefinitionType,),
        }

    attribute_map = {
        "color_preference": "color_preference",
        "count": "count",
        "description": "description",
        "display_format": "display_format",
        "hide_zero_counts": "hide_zero_counts",
        "last_triggered_format": "last_triggered_format",
        "notes": "notes",
        "query": "query",
        "show_investigation": "show_investigation",
        "show_last_triggered": "show_last_triggered",
        "show_priority": "show_priority",
        "show_status": "show_status",
        "sort": "sort",
        "start": "start",
        "summary_type": "summary_type",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        query: str,
        type: ManageStatusBackendDefinitionType,
        color_preference: Union[ManageStatusBackendDefinitionColorPreference, UnsetType] = unset,
        count: Union[float, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        display_format: Union[ManageStatusBackendDefinitionDisplayFormat, UnsetType] = unset,
        hide_zero_counts: Union[bool, UnsetType] = unset,
        last_triggered_format: Union[ManageStatusBackendDefinitionLastTriggeredFormat, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        show_investigation: Union[bool, UnsetType] = unset,
        show_last_triggered: Union[bool, UnsetType] = unset,
        show_priority: Union[bool, UnsetType] = unset,
        show_status: Union[bool, UnsetType] = unset,
        sort: Union[str, UnsetType] = unset,
        start: Union[float, UnsetType] = unset,
        summary_type: Union[ManageStatusBackendDefinitionSummaryType, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color_preference: Test-only generated schema for the dashboard versioning proof of concept.
        :type color_preference: ManageStatusBackendDefinitionColorPreference, optional

        :param count: Test-only generated schema for the dashboard versioning proof of concept.
        :type count: float, optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param display_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_format: ManageStatusBackendDefinitionDisplayFormat, optional

        :param hide_zero_counts: Test-only generated schema for the dashboard versioning proof of concept.
        :type hide_zero_counts: bool, optional

        :param last_triggered_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type last_triggered_format: ManageStatusBackendDefinitionLastTriggeredFormat, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str

        :param show_investigation: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_investigation: bool, optional

        :param show_last_triggered: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_last_triggered: bool, optional

        :param show_priority: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_priority: bool, optional

        :param show_status: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_status: bool, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: str, optional

        :param start: Test-only generated schema for the dashboard versioning proof of concept.
        :type start: float, optional

        :param summary_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type summary_type: ManageStatusBackendDefinitionSummaryType, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ManageStatusBackendDefinitionType
        """
        if color_preference is not unset:
            kwargs["color_preference"] = color_preference
        if count is not unset:
            kwargs["count"] = count
        if description is not unset:
            kwargs["description"] = description
        if display_format is not unset:
            kwargs["display_format"] = display_format
        if hide_zero_counts is not unset:
            kwargs["hide_zero_counts"] = hide_zero_counts
        if last_triggered_format is not unset:
            kwargs["last_triggered_format"] = last_triggered_format
        if notes is not unset:
            kwargs["notes"] = notes
        if show_investigation is not unset:
            kwargs["show_investigation"] = show_investigation
        if show_last_triggered is not unset:
            kwargs["show_last_triggered"] = show_last_triggered
        if show_priority is not unset:
            kwargs["show_priority"] = show_priority
        if show_status is not unset:
            kwargs["show_status"] = show_status
        if sort is not unset:
            kwargs["sort"] = sort
        if start is not unset:
            kwargs["start"] = start
        if summary_type is not unset:
            kwargs["summary_type"] = summary_type
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.query = query
        self_.type = type
