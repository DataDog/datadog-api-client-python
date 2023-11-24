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
    from datadog_api_client.v1.model.calendar_interval import CalendarInterval


class LogsQueryCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.calendar_interval import CalendarInterval

        return {
            "aggregation": (str,),
            "facet": (str,),
            "interval": (int,),
            "rollup": (CalendarInterval,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "facet": "facet",
        "interval": "interval",
        "rollup": "rollup",
    }

    def __init__(
        self_,
        aggregation: str,
        facet: Union[str, UnsetType] = unset,
        interval: Union[int, UnsetType] = unset,
        rollup: Union[CalendarInterval, UnsetType] = unset,
        **kwargs,
    ):
        """
        Define computation for a log query.

        :param aggregation: The aggregation method.
        :type aggregation: str

        :param facet: Facet name.
        :type facet: str, optional

        :param interval: Fixed numeric interval for compute (in milliseconds).
            Fields ``interval`` (numeric interval) and ``rollup`` (calendar interval) are mutually exclusive.
        :type interval: int, optional

        :param rollup: Calendar interval options for compute.
            Fields ``interval`` (numeric interval) and ``rollup`` (calendar interval) are mutually exclusive.

            For instance:

            * { type: 'day', alignment: '1pm', timezone: 'Europe/Paris' }
            * { type: 'week', alignment: 'tuesday', quantity: 2 }
            * { type: 'month', alignment: '15th' }
            * { type: 'year', alignment: 'april' }
        :type rollup: CalendarInterval, optional
        """
        if facet is not unset:
            kwargs["facet"] = facet
        if interval is not unset:
            kwargs["interval"] = interval
        if rollup is not unset:
            kwargs["rollup"] = rollup
        super().__init__(kwargs)

        self_.aggregation = aggregation
