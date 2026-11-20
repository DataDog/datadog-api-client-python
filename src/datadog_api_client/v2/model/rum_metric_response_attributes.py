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
    from datadog_api_client.v2.model.rum_metric_response_compute import RUMMetricResponseCompute
    from datadog_api_client.v2.model.rum_metric_event_type import RUMMetricEventType
    from datadog_api_client.v2.model.rum_metric_response_filter import RUMMetricResponseFilter
    from datadog_api_client.v2.model.rum_metric_response_group_by import RUMMetricResponseGroupBy
    from datadog_api_client.v2.model.rum_metric_response_uniqueness import RUMMetricResponseUniqueness


class RUMMetricResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_metric_response_compute import RUMMetricResponseCompute
        from datadog_api_client.v2.model.rum_metric_event_type import RUMMetricEventType
        from datadog_api_client.v2.model.rum_metric_response_filter import RUMMetricResponseFilter
        from datadog_api_client.v2.model.rum_metric_response_group_by import RUMMetricResponseGroupBy
        from datadog_api_client.v2.model.rum_metric_response_uniqueness import RUMMetricResponseUniqueness

        return {
            "compute": (RUMMetricResponseCompute,),
            "event_type": (RUMMetricEventType,),
            "filter": (RUMMetricResponseFilter,),
            "group_by": ([RUMMetricResponseGroupBy],),
            "uniqueness": (RUMMetricResponseUniqueness,),
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
        compute: Union[RUMMetricResponseCompute, UnsetType] = unset,
        event_type: Union[RUMMetricEventType, UnsetType] = unset,
        filter: Union[RUMMetricResponseFilter, UnsetType] = unset,
        group_by: Union[List[RUMMetricResponseGroupBy], UnsetType] = unset,
        uniqueness: Union[RUMMetricResponseUniqueness, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing a Datadog RUM-based metric.

        :param compute: The compute rule of the RUM-based metric.
        :type compute: RUMMetricResponseCompute, optional

        :param event_type: The type of RUM events the metric is generated from. It is set at creation and cannot be changed.
        :type event_type: RUMMetricEventType, optional

        :param filter: The RUM-based metric filter. RUM events matching this filter are aggregated in this metric. Omitted if the metric only filters on the event type.
        :type filter: RUMMetricResponseFilter, optional

        :param group_by: The rules the metric is grouped by. An empty array is returned if the metric is not grouped.
        :type group_by: [RUMMetricResponseGroupBy], optional

        :param uniqueness: The rule to count updatable events. Only present if ``event_type`` is ``session`` or ``view`` , and absent on older metrics created before this setting existed.
        :type uniqueness: RUMMetricResponseUniqueness, optional
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
