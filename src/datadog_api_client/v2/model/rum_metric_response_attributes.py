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
    from datadog_api_client.v2.model.rum_metric_response_compute import RumMetricResponseCompute
    from datadog_api_client.v2.model.rum_metric_event_type import RumMetricEventType
    from datadog_api_client.v2.model.rum_metric_response_filter import RumMetricResponseFilter
    from datadog_api_client.v2.model.rum_metric_response_group_by import RumMetricResponseGroupBy
    from datadog_api_client.v2.model.rum_metric_response_uniqueness import RumMetricResponseUniqueness


class RumMetricResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_response_compute import RumMetricResponseCompute
        from datadog_api_client.v2.model.rum_metric_event_type import RumMetricEventType
        from datadog_api_client.v2.model.rum_metric_response_filter import RumMetricResponseFilter
        from datadog_api_client.v2.model.rum_metric_response_group_by import RumMetricResponseGroupBy
        from datadog_api_client.v2.model.rum_metric_response_uniqueness import RumMetricResponseUniqueness

        return {
            "compute": (RumMetricResponseCompute,),
            "event_type": (RumMetricEventType,),
            "filter": (RumMetricResponseFilter,),
            "group_by": ([RumMetricResponseGroupBy],),
            "uniqueness": (RumMetricResponseUniqueness,),
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
        compute: Union[RumMetricResponseCompute, UnsetType] = unset,
        event_type: Union[RumMetricEventType, UnsetType] = unset,
        filter: Union[RumMetricResponseFilter, UnsetType] = unset,
        group_by: Union[List[RumMetricResponseGroupBy], UnsetType] = unset,
        uniqueness: Union[RumMetricResponseUniqueness, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing a Datadog rum-based metric.

        :param compute: The compute rule to compute the rum-based metric.
        :type compute: RumMetricResponseCompute, optional

        :param event_type: The type of RUM events to filter on.
        :type event_type: RumMetricEventType, optional

        :param filter: The rum-based metric filter. RUM events matching this filter will be aggregated in this metric.
        :type filter: RumMetricResponseFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [RumMetricResponseGroupBy], optional

        :param uniqueness: The rule to count updatable events. Is only set if ``event_type`` is ``session`` or ``view``.
        :type uniqueness: RumMetricResponseUniqueness, optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if event_type is not unset:
            kwargs["event_type"] = event_type
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if uniqueness is not unset:
            kwargs["uniqueness"] = uniqueness
        super().__init__(kwargs)
