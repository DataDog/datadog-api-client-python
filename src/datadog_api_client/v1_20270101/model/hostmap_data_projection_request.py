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
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.hostmap_projection import HostmapProjection
    from datadog_api_client.v1_20270101.model.dataset_list_query import DatasetListQuery
    from datadog_api_client.v1_20270101.model.hostmap_data_projection_request_request_type import (
        HostmapDataProjectionRequestRequestType,
    )
    from datadog_api_client.v1_20270101.model.hostmap_style import HostmapStyle


class HostmapDataProjectionRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.hostmap_projection import HostmapProjection
        from datadog_api_client.v1_20270101.model.dataset_list_query import DatasetListQuery
        from datadog_api_client.v1_20270101.model.hostmap_data_projection_request_request_type import (
            HostmapDataProjectionRequestRequestType,
        )
        from datadog_api_client.v1_20270101.model.hostmap_style import HostmapStyle

        return {
            "conditional_formats": ([ThresholdFormattingRule],),
            "limit": (float,),
            "no_group_hosts": (bool,),
            "no_metric_hosts": (bool,),
            "projection": (HostmapProjection,),
            "query": (DatasetListQuery,),
            "request_type": (HostmapDataProjectionRequestRequestType,),
            "style": (HostmapStyle,),
        }

    attribute_map = {
        "conditional_formats": "conditional_formats",
        "limit": "limit",
        "no_group_hosts": "no_group_hosts",
        "no_metric_hosts": "no_metric_hosts",
        "projection": "projection",
        "query": "query",
        "request_type": "request_type",
        "style": "style",
    }

    def __init__(
        self_,
        projection: HostmapProjection,
        query: DatasetListQuery,
        request_type: HostmapDataProjectionRequestRequestType,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        limit: Union[float, UnsetType] = unset,
        no_group_hosts: Union[bool, UnsetType] = unset,
        no_metric_hosts: Union[bool, UnsetType] = unset,
        style: Union[HostmapStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param no_group_hosts: Test-only generated schema for the dashboard versioning proof of concept.
        :type no_group_hosts: bool, optional

        :param no_metric_hosts: Test-only generated schema for the dashboard versioning proof of concept.
        :type no_metric_hosts: bool, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: HostmapProjection

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: DatasetListQuery

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: HostmapDataProjectionRequestRequestType

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: HostmapStyle, optional
        """
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if limit is not unset:
            kwargs["limit"] = limit
        if no_group_hosts is not unset:
            kwargs["no_group_hosts"] = no_group_hosts
        if no_metric_hosts is not unset:
            kwargs["no_metric_hosts"] = no_metric_hosts
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.projection = projection
        self_.query = query
        self_.request_type = request_type
