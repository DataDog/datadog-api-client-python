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
    from datadog_api_client.v2.model.rum_metric_update_compute import RUMMetricUpdateCompute
    from datadog_api_client.v2.model.rum_metric_filter import RUMMetricFilter
    from datadog_api_client.v2.model.rum_metric_group_by import RUMMetricGroupBy


class RUMMetricUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_update_compute import RUMMetricUpdateCompute
        from datadog_api_client.v2.model.rum_metric_filter import RUMMetricFilter
        from datadog_api_client.v2.model.rum_metric_group_by import RUMMetricGroupBy

        return {
            "compute": (RUMMetricUpdateCompute,),
            "filter": (RUMMetricFilter,),
            "group_by": ([RUMMetricGroupBy],),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(
        self_,
        compute: Union[RUMMetricUpdateCompute, UnsetType] = unset,
        filter: Union[RUMMetricFilter, UnsetType] = unset,
        group_by: Union[List[RUMMetricGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM-based metric properties to update. Omitted properties keep their current value.

        :param compute: The compute rule properties that can be updated. Only valid for metrics whose ``aggregation_type`` is ``distribution``.
        :type compute: RUMMetricUpdateCompute, optional

        :param filter: The RUM-based metric filter. Events matching this filter are aggregated in this metric. The ``event_type`` filter is added automatically.
        :type filter: RUMMetricFilter, optional

        :param group_by: The rules to group the metric by. When provided, replaces all the existing group by rules.
        :type group_by: [RUMMetricGroupBy], optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)
