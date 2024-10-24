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
    from datadog_api_client.v2.model.rum_metric_update_compute import RumMetricUpdateCompute
    from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
    from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy


class RumMetricUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_update_compute import RumMetricUpdateCompute
        from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
        from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy

        return {
            "compute": (RumMetricUpdateCompute,),
            "filter": (RumMetricFilter,),
            "group_by": ([RumMetricGroupBy],),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(
        self_,
        compute: Union[RumMetricUpdateCompute, UnsetType] = unset,
        filter: Union[RumMetricFilter, UnsetType] = unset,
        group_by: Union[List[RumMetricGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        The rum-based metric properties that will be updated.

        :param compute: The compute rule to compute the rum-based metric.
        :type compute: RumMetricUpdateCompute, optional

        :param filter: The rum-based metric filter. Events matching this filter will be aggregated in this metric.
        :type filter: RumMetricFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [RumMetricGroupBy], optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)
