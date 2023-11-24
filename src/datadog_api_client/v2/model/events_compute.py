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
    from datadog_api_client.v2.model.events_aggregation import EventsAggregation
    from datadog_api_client.v2.model.calendar_interval import CalendarInterval


class EventsCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.events_aggregation import EventsAggregation
        from datadog_api_client.v2.model.calendar_interval import CalendarInterval

        return {
            "aggregation": (EventsAggregation,),
            "interval": (int,),
            "metric": (str,),
            "rollup": (CalendarInterval,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "rollup": "rollup",
    }

    def __init__(
        self_,
        aggregation: EventsAggregation,
        interval: Union[int, UnsetType] = unset,
        metric: Union[str, UnsetType] = unset,
        rollup: Union[CalendarInterval, UnsetType] = unset,
        **kwargs,
    ):
        """
        The instructions for what to compute for this query.

        :param aggregation: The type of aggregation that can be performed on events-based queries.
        :type aggregation: EventsAggregation

        :param interval: Fixed numeric interval for compute (in milliseconds).
            Fields ``interval`` (numeric interval) and ``rollup`` (calendar interval) are mutually exclusive.
        :type interval: int, optional

        :param metric: The "measure" attribute on which to perform the computation.
        :type metric: str, optional

        :param rollup: Calendar interval options for compute.
            Fields ``interval`` (numeric interval) and ``rollup`` (calendar interval) are mutually exclusive.

            For instance:

            * { type: 'day', alignment: '1pm', timezone: 'Europe/Paris' }
            * { type: 'week', alignment: 'tuesday', quantity: 2 }
            * { type: 'month', alignment: '15th' }
            * { type: 'year', alignment: 'april' }
        :type rollup: CalendarInterval, optional
        """
        if interval is not unset:
            kwargs["interval"] = interval
        if metric is not unset:
            kwargs["metric"] = metric
        if rollup is not unset:
            kwargs["rollup"] = rollup
        super().__init__(kwargs)

        self_.aggregation = aggregation
