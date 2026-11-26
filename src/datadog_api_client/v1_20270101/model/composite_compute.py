# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator
    from datadog_api_client.v1_20270101.model.calendar_interval import CalendarInterval
    from datadog_api_client.v1_20270101.model.calendar_interval_day import CalendarIntervalDay
    from datadog_api_client.v1_20270101.model.calendar_interval_week import CalendarIntervalWeek
    from datadog_api_client.v1_20270101.model.calendar_interval_month import CalendarIntervalMonth
    from datadog_api_client.v1_20270101.model.calendar_interval_year import CalendarIntervalYear


class CompositeCompute(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.events_aggregator import EventsAggregator
        from datadog_api_client.v1_20270101.model.calendar_interval import CalendarInterval

        return {
            "aggregation": (EventsAggregator,),
            "interval": (float,),
            "metric": (str,),
            "name": (str,),
            "rollup": (CalendarInterval,),
            "source": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "name": "name",
        "rollup": "rollup",
        "source": "source",
    }

    def __init__(
        self_,
        aggregation: Union[EventsAggregator, str],
        name: str,
        interval: Union[float, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        rollup: Union[
            CalendarInterval,
            CalendarIntervalDay,
            CalendarIntervalWeek,
            CalendarIntervalMonth,
            CalendarIntervalYear,
            UnsetType,
        ] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: EventsAggregator

        :param interval: Test-only generated schema for the dashboard versioning proof of concept.
        :type interval: float, optional

        :param metric: Test-only generated schema for the dashboard versioning proof of concept.
        :type metric: str, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param rollup: Test-only generated schema for the dashboard versioning proof of concept.
        :type rollup: CalendarInterval, optional

        :param source: Test-only generated schema for the dashboard versioning proof of concept.
        :type source: str, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        if rollup is not unset:
            kwargs["rollup"] = rollup
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.name = name
