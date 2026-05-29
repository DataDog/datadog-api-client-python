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
    from datadog_api_client.v1.model.host_map_widget_infrastructure_request_leaf import (
        HostMapWidgetInfrastructureRequestLeaf,
    )
    from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
    from datadog_api_client.v1.model.host_map_widget_scalar_request import HostMapWidgetScalarRequest
    from datadog_api_client.v1.model.host_map_widget_group_by import HostMapWidgetGroupBy
    from datadog_api_client.v1.model.host_map_widget_node_type import HostMapWidgetNodeType
    from datadog_api_client.v1.model.host_map_widget_infrastructure_request_request_type import (
        HostMapWidgetInfrastructureRequestRequestType,
    )
    from datadog_api_client.v1.model.host_map_widget_infrastructure_style import HostMapWidgetInfrastructureStyle


class HostMapWidgetInfrastructureRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_map_widget_infrastructure_request_leaf import (
            HostMapWidgetInfrastructureRequestLeaf,
        )
        from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
        from datadog_api_client.v1.model.host_map_widget_scalar_request import HostMapWidgetScalarRequest
        from datadog_api_client.v1.model.host_map_widget_group_by import HostMapWidgetGroupBy
        from datadog_api_client.v1.model.host_map_widget_node_type import HostMapWidgetNodeType
        from datadog_api_client.v1.model.host_map_widget_infrastructure_request_request_type import (
            HostMapWidgetInfrastructureRequestRequestType,
        )
        from datadog_api_client.v1.model.host_map_widget_infrastructure_style import HostMapWidgetInfrastructureStyle

        return {
            "child": (HostMapWidgetInfrastructureRequestLeaf,),
            "conditional_formats": ([WidgetConditionalFormat],),
            "enrichments": ([HostMapWidgetScalarRequest],),
            "filter": (str,),
            "group_by": ([HostMapWidgetGroupBy],),
            "no_group_hosts": (bool,),
            "no_metric_hosts": (bool,),
            "node_type": (HostMapWidgetNodeType,),
            "request_type": (HostMapWidgetInfrastructureRequestRequestType,),
            "style": (HostMapWidgetInfrastructureStyle,),
        }

    attribute_map = {
        "child": "child",
        "conditional_formats": "conditional_formats",
        "enrichments": "enrichments",
        "filter": "filter",
        "group_by": "group_by",
        "no_group_hosts": "no_group_hosts",
        "no_metric_hosts": "no_metric_hosts",
        "node_type": "node_type",
        "request_type": "request_type",
        "style": "style",
    }

    def __init__(
        self_,
        enrichments: List[HostMapWidgetScalarRequest],
        node_type: HostMapWidgetNodeType,
        request_type: HostMapWidgetInfrastructureRequestRequestType,
        child: Union[HostMapWidgetInfrastructureRequestLeaf, UnsetType] = unset,
        conditional_formats: Union[List[WidgetConditionalFormat], UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        group_by: Union[List[HostMapWidgetGroupBy], UnsetType] = unset,
        no_group_hosts: Union[bool, UnsetType] = unset,
        no_metric_hosts: Union[bool, UnsetType] = unset,
        style: Union[HostMapWidgetInfrastructureStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Infrastructure-backed request for the host map widget. Supports entity-based
        visualization with metric query enrichments, tag-based filtering, flexible grouping,
        and hierarchical views.

        :param child: Infrastructure-backed host map child request (leaf node, no further nesting supported).
        :type child: HostMapWidgetInfrastructureRequestLeaf, optional

        :param conditional_formats: List of conditional formatting rules applied to fill values.
        :type conditional_formats: [WidgetConditionalFormat], optional

        :param enrichments: Metric or event queries joined to the entity set. Each formula specifies a visual dimension.
        :type enrichments: [HostMapWidgetScalarRequest]

        :param filter: Filter string for the entity set in tag format (for example, ``env:prod`` ).
        :type filter: str, optional

        :param group_by: Defines how entities are grouped into tiles. The ordering of entries implies
            the grouping hierarchy.
        :type group_by: [HostMapWidgetGroupBy], optional

        :param no_group_hosts: Whether to hide entities that have no group assignment.
        :type no_group_hosts: bool, optional

        :param no_metric_hosts: Whether to hide entities that have no enrichment data.
        :type no_metric_hosts: bool, optional

        :param node_type: Which type of infrastructure entity to visualize in the host map.
        :type node_type: HostMapWidgetNodeType

        :param request_type: Identifies this as an infrastructure-backed host map request.
        :type request_type: HostMapWidgetInfrastructureRequestRequestType

        :param style: Style configuration for the infrastructure host map.
        :type style: HostMapWidgetInfrastructureStyle, optional
        """
        if child is not unset:
            kwargs["child"] = child
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if no_group_hosts is not unset:
            kwargs["no_group_hosts"] = no_group_hosts
        if no_metric_hosts is not unset:
            kwargs["no_metric_hosts"] = no_metric_hosts
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.enrichments = enrichments
        self_.node_type = node_type
        self_.request_type = request_type
