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
    from datadog_api_client.v1.model.host_map_widget_infrastructure_request import HostMapWidgetInfrastructureRequest
    from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
    from datadog_api_client.v1.model.host_map_widget_scalar_request import HostMapWidgetScalarRequest
    from datadog_api_client.v1.model.host_map_request import HostMapRequest
    from datadog_api_client.v1.model.host_map_widget_group_by import HostMapWidgetGroupBy
    from datadog_api_client.v1.model.host_map_widget_node_type import HostMapWidgetNodeType
    from datadog_api_client.v1.model.host_map_widget_projection import HostMapWidgetProjection
    from datadog_api_client.v1.model.dataset_list_query import DatasetListQuery
    from datadog_api_client.v1.model.host_map_widget_definition_request_type import HostMapWidgetDefinitionRequestType
    from datadog_api_client.v1.model.host_map_widget_infrastructure_style import HostMapWidgetInfrastructureStyle


class HostMapWidgetDefinitionRequests(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host_map_widget_infrastructure_request import (
            HostMapWidgetInfrastructureRequest,
        )
        from datadog_api_client.v1.model.widget_conditional_format import WidgetConditionalFormat
        from datadog_api_client.v1.model.host_map_widget_scalar_request import HostMapWidgetScalarRequest
        from datadog_api_client.v1.model.host_map_request import HostMapRequest
        from datadog_api_client.v1.model.host_map_widget_group_by import HostMapWidgetGroupBy
        from datadog_api_client.v1.model.host_map_widget_node_type import HostMapWidgetNodeType
        from datadog_api_client.v1.model.host_map_widget_projection import HostMapWidgetProjection
        from datadog_api_client.v1.model.dataset_list_query import DatasetListQuery
        from datadog_api_client.v1.model.host_map_widget_definition_request_type import (
            HostMapWidgetDefinitionRequestType,
        )
        from datadog_api_client.v1.model.host_map_widget_infrastructure_style import HostMapWidgetInfrastructureStyle

        return {
            "child": (HostMapWidgetInfrastructureRequest,),
            "conditional_formats": ([WidgetConditionalFormat],),
            "enrichments": ([HostMapWidgetScalarRequest],),
            "fill": (HostMapRequest,),
            "filter": (str,),
            "group_by": ([HostMapWidgetGroupBy],),
            "limit": (int,),
            "no_group_hosts": (bool,),
            "no_metric_hosts": (bool,),
            "node_type": (HostMapWidgetNodeType,),
            "projection": (HostMapWidgetProjection,),
            "query": (DatasetListQuery,),
            "request_type": (HostMapWidgetDefinitionRequestType,),
            "size": (HostMapRequest,),
            "style": (HostMapWidgetInfrastructureStyle,),
        }

    attribute_map = {
        "child": "child",
        "conditional_formats": "conditional_formats",
        "enrichments": "enrichments",
        "fill": "fill",
        "filter": "filter",
        "group_by": "group_by",
        "limit": "limit",
        "no_group_hosts": "no_group_hosts",
        "no_metric_hosts": "no_metric_hosts",
        "node_type": "node_type",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "size": "size",
        "style": "style",
    }

    def __init__(
        self_,
        child: Union[HostMapWidgetInfrastructureRequest, UnsetType] = unset,
        conditional_formats: Union[List[WidgetConditionalFormat], UnsetType] = unset,
        enrichments: Union[List[HostMapWidgetScalarRequest], UnsetType] = unset,
        fill: Union[HostMapRequest, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        group_by: Union[List[HostMapWidgetGroupBy], UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        no_group_hosts: Union[bool, UnsetType] = unset,
        no_metric_hosts: Union[bool, UnsetType] = unset,
        node_type: Union[HostMapWidgetNodeType, UnsetType] = unset,
        projection: Union[HostMapWidgetProjection, UnsetType] = unset,
        query: Union[DatasetListQuery, UnsetType] = unset,
        request_type: Union[HostMapWidgetDefinitionRequestType, UnsetType] = unset,
        size: Union[HostMapRequest, UnsetType] = unset,
        style: Union[HostMapWidgetInfrastructureStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Query definition for the host map widget. Supports three mutually exclusive formats distinguished by `request_type`: the deprecated legacy metric-based format (`fill`/`size`, no `request_type`), the infrastructure-backed format (`request_type: infrastructure_hostmap ``), and the DDSQL published-dataset format (`` request_type: data_projection`).

        :param child: Infrastructure-backed request for the host map widget. Supports entity-based
            visualization with metric query enrichments, tag-based filtering, flexible grouping,
            and hierarchical views.
        :type child: HostMapWidgetInfrastructureRequest, optional

        :param conditional_formats: List of conditional formatting rules applied to fill values.
        :type conditional_formats: [WidgetConditionalFormat], optional

        :param enrichments: Metric or event queries joined to the entity set. Each formula specifies a visual dimension. Only used by the infrastructure-backed format.
        :type enrichments: [HostMapWidgetScalarRequest], optional

        :param fill: Deprecated - Legacy metric-based host map request. Use the infrastructure-backed ( ``request_type: infrastructure_hostmap`` ) or DDSQL ( ``request_type: data_projection`` ) format instead. **Deprecated**.
        :type fill: HostMapRequest, optional

        :param filter: Filter string for the entity set in tag format (for example, ``env:prod`` ). Only used by the infrastructure-backed format.
        :type filter: str, optional

        :param group_by: Defines how entities are grouped into tiles. The ordering of entries implies
            the grouping hierarchy. Only used by the infrastructure-backed format.
        :type group_by: [HostMapWidgetGroupBy], optional

        :param limit: Maximum number of rows to return from the dataset query. Only used by the DDSQL format.
        :type limit: int, optional

        :param no_group_hosts: Whether to hide entities that have no group assignment.
        :type no_group_hosts: bool, optional

        :param no_metric_hosts: Whether to hide entities that have no enrichment data.
        :type no_metric_hosts: bool, optional

        :param node_type: Which type of infrastructure entity to visualize in the host map.
        :type node_type: HostMapWidgetNodeType, optional

        :param projection: Projection for the DDSQL host map request. Maps dataset columns to map dimensions: ``node`` identifies the entity, repeated ``group`` entries define the grouping hierarchy (outermost first), and ``fill`` / ``size`` drive the tile color and size.
        :type projection: HostMapWidgetProjection, optional

        :param query: Query that lists the rows of a published dataset (a DDSQL query) without aggregation.
        :type query: DatasetListQuery, optional

        :param request_type: Identifies which host map request format the sibling fields on ``HostMapWidgetDefinitionRequests`` describe: an infrastructure-backed request or a DDSQL published-dataset request.
        :type request_type: HostMapWidgetDefinitionRequestType, optional

        :param size: Deprecated - Legacy metric-based host map request. Use the infrastructure-backed ( ``request_type: infrastructure_hostmap`` ) or DDSQL ( ``request_type: data_projection`` ) format instead. **Deprecated**.
        :type size: HostMapRequest, optional

        :param style: Style configuration for the infrastructure host map.
        :type style: HostMapWidgetInfrastructureStyle, optional
        """
        if child is not unset:
            kwargs["child"] = child
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if enrichments is not unset:
            kwargs["enrichments"] = enrichments
        if fill is not unset:
            kwargs["fill"] = fill
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if limit is not unset:
            kwargs["limit"] = limit
        if no_group_hosts is not unset:
            kwargs["no_group_hosts"] = no_group_hosts
        if no_metric_hosts is not unset:
            kwargs["no_metric_hosts"] = no_metric_hosts
        if node_type is not unset:
            kwargs["node_type"] = node_type
        if projection is not unset:
            kwargs["projection"] = projection
        if query is not unset:
            kwargs["query"] = query
        if request_type is not unset:
            kwargs["request_type"] = request_type
        if size is not unset:
            kwargs["size"] = size
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)
