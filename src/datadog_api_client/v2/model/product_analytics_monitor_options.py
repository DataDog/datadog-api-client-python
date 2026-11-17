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
    from datadog_api_client.v2.model.product_analytics_monitor_thresholds import ProductAnalyticsMonitorThresholds
    from datadog_api_client.v2.model.product_analytics_monitor_variable import ProductAnalyticsMonitorVariable


class ProductAnalyticsMonitorOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_monitor_thresholds import ProductAnalyticsMonitorThresholds
        from datadog_api_client.v2.model.product_analytics_monitor_variable import ProductAnalyticsMonitorVariable

        return {
            "chart_uuid": (str,),
            "metric_selector": (str,),
            "query_index": (int,),
            "renotify_interval": (int,),
            "thresholds": (ProductAnalyticsMonitorThresholds,),
            "timeframe": (str,),
            "variables": ([ProductAnalyticsMonitorVariable],),
        }

    attribute_map = {
        "chart_uuid": "chart_uuid",
        "metric_selector": "metric_selector",
        "query_index": "query_index",
        "renotify_interval": "renotify_interval",
        "thresholds": "thresholds",
        "timeframe": "timeframe",
        "variables": "variables",
    }

    def __init__(
        self_,
        chart_uuid: Union[str, UnsetType] = unset,
        metric_selector: Union[str, UnsetType] = unset,
        query_index: Union[int, UnsetType] = unset,
        renotify_interval: Union[int, UnsetType] = unset,
        thresholds: Union[ProductAnalyticsMonitorThresholds, UnsetType] = unset,
        timeframe: Union[str, UnsetType] = unset,
        variables: Union[List[ProductAnalyticsMonitorVariable], UnsetType] = unset,
        **kwargs,
    ):
        """
        Options of a Product Analytics monitor.

        :param chart_uuid: UUID of the chart the monitor was created from.
        :type chart_uuid: str, optional

        :param metric_selector: Metric of the chart that the monitor evaluates.
        :type metric_selector: str, optional

        :param query_index: Index of the chart query that the monitor evaluates.
        :type query_index: int, optional

        :param renotify_interval: Number of minutes after the last notification before the monitor notifies again on the current status.
            ``0`` means it never notifies again.
        :type renotify_interval: int, optional

        :param thresholds: Alert thresholds of a Product Analytics monitor.
            Keep ``critical`` in sync with the comparison in the monitor query; the query is not derived from these values.
        :type thresholds: ProductAnalyticsMonitorThresholds, optional

        :param timeframe: Time frame of the chart that the monitor evaluates.
        :type timeframe: str, optional

        :param variables: Query variables referenced by the monitor query.
        :type variables: [ProductAnalyticsMonitorVariable], optional
        """
        if chart_uuid is not unset:
            kwargs["chart_uuid"] = chart_uuid
        if metric_selector is not unset:
            kwargs["metric_selector"] = metric_selector
        if query_index is not unset:
            kwargs["query_index"] = query_index
        if renotify_interval is not unset:
            kwargs["renotify_interval"] = renotify_interval
        if thresholds is not unset:
            kwargs["thresholds"] = thresholds
        if timeframe is not unset:
            kwargs["timeframe"] = timeframe
        if variables is not unset:
            kwargs["variables"] = variables
        super().__init__(kwargs)
