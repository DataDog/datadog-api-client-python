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
    from datadog_api_client.v2.model.dashboard_search_aggregation_bucket_multi_key import (
        DashboardSearchAggregationBucketMultiKey,
    )
    from datadog_api_client.v2.model.dashboard_search_aggregation_bucket_key import DashboardSearchAggregationBucketKey


class DashboardSearchAggregations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_search_aggregation_bucket_multi_key import (
            DashboardSearchAggregationBucketMultiKey,
        )
        from datadog_api_client.v2.model.dashboard_search_aggregation_bucket_key import (
            DashboardSearchAggregationBucketKey,
        )

        return {
            "author": ([DashboardSearchAggregationBucketMultiKey],),
            "is_shared": ([DashboardSearchAggregationBucketKey],),
            "share_type": ([DashboardSearchAggregationBucketKey],),
            "shared_by_handle": ([DashboardSearchAggregationBucketKey],),
            "status": ([DashboardSearchAggregationBucketKey],),
            "tags": ([DashboardSearchAggregationBucketKey],),
            "template_variables_name": ([DashboardSearchAggregationBucketKey],),
            "type": ([DashboardSearchAggregationBucketKey],),
            "widgets_metrics": ([DashboardSearchAggregationBucketKey],),
            "widgets_type": ([DashboardSearchAggregationBucketKey],),
        }

    attribute_map = {
        "author": "author",
        "is_shared": "is_shared",
        "share_type": "share_type",
        "shared_by_handle": "shared_by.handle",
        "status": "status",
        "tags": "tags",
        "template_variables_name": "template_variables.name",
        "type": "type",
        "widgets_metrics": "widgets.metrics",
        "widgets_type": "widgets.type",
    }

    def __init__(
        self_,
        author: Union[List[DashboardSearchAggregationBucketMultiKey], UnsetType] = unset,
        is_shared: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        share_type: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        shared_by_handle: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        status: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        tags: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        template_variables_name: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        type: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        widgets_metrics: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        widgets_type: Union[List[DashboardSearchAggregationBucketKey], UnsetType] = unset,
        **kwargs,
    ):
        """
        Aggregations of dashboard search results.

        :param author: Aggregation by author.
        :type author: [DashboardSearchAggregationBucketMultiKey], optional

        :param is_shared: Aggregation by share status.
        :type is_shared: [DashboardSearchAggregationBucketKey], optional

        :param share_type: Aggregation by share type.
        :type share_type: [DashboardSearchAggregationBucketKey], optional

        :param shared_by_handle: Aggregation by who shared the dashboard.
        :type shared_by_handle: [DashboardSearchAggregationBucketKey], optional

        :param status: Aggregation by status.
        :type status: [DashboardSearchAggregationBucketKey], optional

        :param tags: Aggregation by tags.
        :type tags: [DashboardSearchAggregationBucketKey], optional

        :param template_variables_name: Aggregation by template variable names.
        :type template_variables_name: [DashboardSearchAggregationBucketKey], optional

        :param type: Aggregation by dashboard type.
        :type type: [DashboardSearchAggregationBucketKey], optional

        :param widgets_metrics: Aggregation by widget metrics.
        :type widgets_metrics: [DashboardSearchAggregationBucketKey], optional

        :param widgets_type: Aggregation by widget type.
        :type widgets_type: [DashboardSearchAggregationBucketKey], optional
        """
        if author is not unset:
            kwargs["author"] = author
        if is_shared is not unset:
            kwargs["is_shared"] = is_shared
        if share_type is not unset:
            kwargs["share_type"] = share_type
        if shared_by_handle is not unset:
            kwargs["shared_by_handle"] = shared_by_handle
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        if template_variables_name is not unset:
            kwargs["template_variables_name"] = template_variables_name
        if type is not unset:
            kwargs["type"] = type
        if widgets_metrics is not unset:
            kwargs["widgets_metrics"] = widgets_metrics
        if widgets_type is not unset:
            kwargs["widgets_type"] = widgets_type
        super().__init__(kwargs)
