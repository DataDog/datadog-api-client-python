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
    from datadog_api_client.v2.model.rum_metric_compute import RumMetricCompute
    from datadog_api_client.v2.model.rum_metric_event_type import RumMetricEventType
    from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
    from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy
    from datadog_api_client.v2.model.rum_metric_uniqueness import RumMetricUniqueness


class RumMetricCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_compute import RumMetricCompute
        from datadog_api_client.v2.model.rum_metric_event_type import RumMetricEventType
        from datadog_api_client.v2.model.rum_metric_filter import RumMetricFilter
        from datadog_api_client.v2.model.rum_metric_group_by import RumMetricGroupBy
        from datadog_api_client.v2.model.rum_metric_uniqueness import RumMetricUniqueness

        return {
            "compute": (RumMetricCompute,),
            "event_type": (RumMetricEventType,),
            "filter": (RumMetricFilter,),
            "group_by": ([RumMetricGroupBy],),
            "uniqueness": (RumMetricUniqueness,),
        }

    attribute_map = {
        "compute": "compute",
        "event_type": "event_type",
        "filter": "filter",
        "group_by": "group_by",
        "uniqueness": "uniqueness",
    }

    def __init__(
        self_,
        compute: RumMetricCompute,
        event_type: RumMetricEventType,
        filter: Union[RumMetricFilter, UnsetType] = unset,
        group_by: Union[List[RumMetricGroupBy], UnsetType] = unset,
        uniqueness: Union[RumMetricUniqueness, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing the Datadog RUM-based metric to create.

        :param compute: The compute rule to compute the RUM-based metric. It is set at creation and only ``include_percentiles`` can be updated afterwards.
        :type compute: RumMetricCompute

        :param event_type: The type of RUM events the metric is generated from. It is set at creation and cannot be changed.
        :type event_type: RumMetricEventType

        :param filter: The RUM-based metric filter. Events matching this filter will be aggregated in this metric. The ``event_type`` filter is added automatically.
        :type filter: RumMetricFilter, optional

        :param group_by: The rules to group the metric by. Each rule creates a tag on the generated metric. If omitted, the metric is not grouped.
        :type group_by: [RumMetricGroupBy], optional

        :param uniqueness: The rule to count updatable events.
            Required when ``event_type`` is ``session`` or ``view`` , and must be omitted for other event types. It cannot be changed after creation.
        :type uniqueness: RumMetricUniqueness, optional
        """
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if uniqueness is not unset:
            kwargs["uniqueness"] = uniqueness
        super().__init__(kwargs)

        self_.compute = compute
        self_.event_type = event_type
