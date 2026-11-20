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
    from datadog_api_client.v1_20270101.model.geomap_backend_request import GeomapBackendRequest
    from datadog_api_client.v1_20270101.model.geomap_style import GeomapStyle
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.geomap_backend_definition_type import GeomapBackendDefinitionType
    from datadog_api_client.v1_20270101.model.geomap_view import GeomapView
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.geomap_backend_regions_request import GeomapBackendRegionsRequest
    from datadog_api_client.v1_20270101.model.geomap_backend_points_request import GeomapBackendPointsRequest
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
    from datadog_api_client.v1.model.geomap_view20270101_one_of import GeomapView20270101OneOf
    from datadog_api_client.v1.model.geomap_view20270101_one_of4457650336 import GeomapView20270101OneOf4457650336


class GeomapBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.geomap_backend_request import GeomapBackendRequest
        from datadog_api_client.v1_20270101.model.geomap_style import GeomapStyle
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.geomap_backend_definition_type import GeomapBackendDefinitionType
        from datadog_api_client.v1_20270101.model.geomap_view import GeomapView

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "notes": (str,),
            "requests": ([GeomapBackendRequest],),
            "style": (GeomapStyle,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (GeomapBackendDefinitionType,),
            "view": (GeomapView,),
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
        "view": "view",
    }

    def __init__(
        self_,
        requests: List[Union[GeomapBackendRequest, GeomapBackendRegionsRequest, GeomapBackendPointsRequest]],
        style: GeomapStyle,
        type: GeomapBackendDefinitionType,
        view: Union[GeomapView, GeomapView20270101OneOf, GeomapView20270101OneOf4457650336],
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
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

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [GeomapBackendRequest]

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: GeomapStyle

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: GeomapBackendDefinitionType

        :param view: Test-only generated schema for the dashboard versioning proof of concept.
        :type view: GeomapView
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
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

        self_.requests = requests
        self_.style = style
        self_.type = type
        self_.view = view
