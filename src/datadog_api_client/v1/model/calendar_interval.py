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
    from datadog_api_client.v1.model.calendar_interval_type import CalendarIntervalType


class CalendarInterval(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.calendar_interval_type import CalendarIntervalType

        return {
            "alignment": (str,),
            "quantity": (int,),
            "timezone": (str,),
            "type": (CalendarIntervalType,),
        }

    attribute_map = {
        "alignment": "alignment",
        "quantity": "quantity",
        "timezone": "timezone",
        "type": "type",
    }

    def __init__(
        self_,
        type: CalendarIntervalType,
        alignment: Union[str, UnsetType] = unset,
        quantity: Union[int, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Calendar interval options for compute.
        Fields ``interval`` (numeric interval) and ``rollup`` (calendar interval) are mutually exclusive.

        For instance:

        * { type: 'day', alignment: '1pm', timezone: 'Europe/Paris' }
        * { type: 'week', alignment: 'tuesday', quantity: 2 }
        * { type: 'month', alignment: '15th' }
        * { type: 'year', alignment: 'april' }

        :param alignment: Optional alignment to define period start.
            Its possible values depend on the type field:

            * day: start hour of day as 12 or 24-hr format (for instance: 11pm, 3am, 15)
            * week: first day of the week (for instance: tuesday, note the lowercase)
            * month: first day of month (for instance: 1th, 2nd, 23th)
            * year: first month of the year (for instance: april, note the lowercase)
        :type alignment: str, optional

        :param quantity: Optional integer to specify how many units to group together.
        :type quantity: int, optional

        :param timezone: Optional timezone to define the calendar interval.
        :type timezone: str, optional

        :param type: Type of calendar interval (day, week, etc.).
        :type type: CalendarIntervalType
        """
        if alignment is not unset:
            kwargs["alignment"] = alignment
        if quantity is not unset:
            kwargs["quantity"] = quantity
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.type = type
