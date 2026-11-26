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
    from datadog_api_client.v1_20270101.model.service_summary_layout import ServiceSummaryLayout
    from datadog_api_client.v1_20270101.model.service_summary_size import ServiceSummarySize
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.service_summary_backend_definition_type import (
        ServiceSummaryBackendDefinitionType,
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


class ServiceSummaryBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.service_summary_layout import ServiceSummaryLayout
        from datadog_api_client.v1_20270101.model.service_summary_size import ServiceSummarySize
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.service_summary_backend_definition_type import (
            ServiceSummaryBackendDefinitionType,
        )

        return {
            "description": (str,),
            "display_format": (ServiceSummaryLayout,),
            "env": (str,),
            "notes": (str,),
            "service": (str,),
            "show_breakdown": (bool,),
            "show_distribution": (bool,),
            "show_errors": (bool,),
            "show_hits": (bool,),
            "show_latency": (bool,),
            "show_resource_list": (bool,),
            "size_format": (ServiceSummarySize,),
            "span_name": (str,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (ServiceSummaryBackendDefinitionType,),
        }

    attribute_map = {
        "description": "description",
        "display_format": "display_format",
        "env": "env",
        "notes": "notes",
        "service": "service",
        "show_breakdown": "show_breakdown",
        "show_distribution": "show_distribution",
        "show_errors": "show_errors",
        "show_hits": "show_hits",
        "show_latency": "show_latency",
        "show_resource_list": "show_resource_list",
        "size_format": "size_format",
        "span_name": "span_name",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        env: str,
        service: str,
        span_name: str,
        type: ServiceSummaryBackendDefinitionType,
        description: Union[str, UnsetType] = unset,
        display_format: Union[ServiceSummaryLayout, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        show_breakdown: Union[bool, UnsetType] = unset,
        show_distribution: Union[bool, UnsetType] = unset,
        show_errors: Union[bool, UnsetType] = unset,
        show_hits: Union[bool, UnsetType] = unset,
        show_latency: Union[bool, UnsetType] = unset,
        show_resource_list: Union[bool, UnsetType] = unset,
        size_format: Union[ServiceSummarySize, UnsetType] = unset,
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

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param display_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type display_format: ServiceSummaryLayout, optional

        :param env: Test-only generated schema for the dashboard versioning proof of concept.
        :type env: str

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param service: Test-only generated schema for the dashboard versioning proof of concept.
        :type service: str

        :param show_breakdown: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_breakdown: bool, optional

        :param show_distribution: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_distribution: bool, optional

        :param show_errors: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_errors: bool, optional

        :param show_hits: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_hits: bool, optional

        :param show_latency: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_latency: bool, optional

        :param show_resource_list: Test-only generated schema for the dashboard versioning proof of concept.
        :type show_resource_list: bool, optional

        :param size_format: Test-only generated schema for the dashboard versioning proof of concept.
        :type size_format: ServiceSummarySize, optional

        :param span_name: Test-only generated schema for the dashboard versioning proof of concept.
        :type span_name: str

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ServiceSummaryBackendDefinitionType
        """
        if description is not unset:
            kwargs["description"] = description
        if display_format is not unset:
            kwargs["display_format"] = display_format
        if notes is not unset:
            kwargs["notes"] = notes
        if show_breakdown is not unset:
            kwargs["show_breakdown"] = show_breakdown
        if show_distribution is not unset:
            kwargs["show_distribution"] = show_distribution
        if show_errors is not unset:
            kwargs["show_errors"] = show_errors
        if show_hits is not unset:
            kwargs["show_hits"] = show_hits
        if show_latency is not unset:
            kwargs["show_latency"] = show_latency
        if show_resource_list is not unset:
            kwargs["show_resource_list"] = show_resource_list
        if size_format is not unset:
            kwargs["size_format"] = size_format
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.env = env
        self_.service = service
        self_.span_name = span_name
        self_.type = type
