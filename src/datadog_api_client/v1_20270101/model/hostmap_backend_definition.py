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
    from datadog_api_client.v1_20270101.model.hostmap_backend_definition_node_type import (
        HostmapBackendDefinitionNodeType,
    )
    from datadog_api_client.v1_20270101.model.hostmap_backend_definition20270101_requests import (
        HostmapBackendDefinition20270101Requests,
    )
    from datadog_api_client.v1_20270101.model.hostmap_backend_definition_style import HostmapBackendDefinitionStyle
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.hostmap_backend_definition_type import HostmapBackendDefinitionType
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.metric_hostmap_requests import MetricHostmapRequests
    from datadog_api_client.v1_20270101.model.hostmap_infrastructure_request import HostmapInfrastructureRequest
    from datadog_api_client.v1_20270101.model.hostmap_data_projection_request import HostmapDataProjectionRequest
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


class HostmapBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.hostmap_backend_definition_node_type import (
            HostmapBackendDefinitionNodeType,
        )
        from datadog_api_client.v1_20270101.model.hostmap_backend_definition20270101_requests import (
            HostmapBackendDefinition20270101Requests,
        )
        from datadog_api_client.v1_20270101.model.hostmap_backend_definition_style import HostmapBackendDefinitionStyle
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.hostmap_backend_definition_type import HostmapBackendDefinitionType

        return {
            "custom_links": ([WidgetCustomLink],),
            "description": (str,),
            "group": ([str],),
            "no_group_hosts": (bool,),
            "no_metric_hosts": (bool,),
            "node_type": (HostmapBackendDefinitionNodeType,),
            "notes": (str,),
            "requests": (HostmapBackendDefinition20270101Requests,),
            "scope": ([str],),
            "style": (HostmapBackendDefinitionStyle,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (HostmapBackendDefinitionType,),
        }

    attribute_map = {
        "custom_links": "custom_links",
        "description": "description",
        "group": "group",
        "no_group_hosts": "no_group_hosts",
        "no_metric_hosts": "no_metric_hosts",
        "node_type": "node_type",
        "notes": "notes",
        "requests": "requests",
        "scope": "scope",
        "style": "style",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: Union[
            HostmapBackendDefinition20270101Requests,
            MetricHostmapRequests,
            HostmapInfrastructureRequest,
            HostmapDataProjectionRequest,
        ],
        type: HostmapBackendDefinitionType,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        group: Union[List[str], UnsetType] = unset,
        no_group_hosts: Union[bool, UnsetType] = unset,
        no_metric_hosts: Union[bool, UnsetType] = unset,
        node_type: Union[HostmapBackendDefinitionNodeType, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        scope: Union[List[str], UnsetType] = unset,
        style: Union[HostmapBackendDefinitionStyle, UnsetType] = unset,
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

        :param group: Test-only generated schema for the dashboard versioning proof of concept.
        :type group: [str], optional

        :param no_group_hosts: Test-only generated schema for the dashboard versioning proof of concept.
        :type no_group_hosts: bool, optional

        :param no_metric_hosts: Test-only generated schema for the dashboard versioning proof of concept.
        :type no_metric_hosts: bool, optional

        :param node_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type node_type: HostmapBackendDefinitionNodeType, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: HostmapBackendDefinition20270101Requests

        :param scope: Test-only generated schema for the dashboard versioning proof of concept.
        :type scope: [str], optional

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: HostmapBackendDefinitionStyle, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: HostmapBackendDefinitionType
        """
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if description is not unset:
            kwargs["description"] = description
        if group is not unset:
            kwargs["group"] = group
        if no_group_hosts is not unset:
            kwargs["no_group_hosts"] = no_group_hosts
        if no_metric_hosts is not unset:
            kwargs["no_metric_hosts"] = no_metric_hosts
        if node_type is not unset:
            kwargs["node_type"] = node_type
        if notes is not unset:
            kwargs["notes"] = notes
        if scope is not unset:
            kwargs["scope"] = scope
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
