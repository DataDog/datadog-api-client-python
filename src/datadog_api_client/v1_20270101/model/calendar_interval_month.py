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
    from datadog_api_client.v1_20270101.model.day_of_the_month import DayOfTheMonth
    from datadog_api_client.v1_20270101.model.calendar_interval_month_type import CalendarIntervalMonthType


class CalendarIntervalMonth(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.day_of_the_month import DayOfTheMonth
        from datadog_api_client.v1_20270101.model.calendar_interval_month_type import CalendarIntervalMonthType

        return {
            "alignment": (DayOfTheMonth,),
            "quantity": (float,),
            "timezone": (str,),
            "type": (CalendarIntervalMonthType,),
        }

    attribute_map = {
        "alignment": "alignment",
        "quantity": "quantity",
        "timezone": "timezone",
        "type": "type",
    }

    def __init__(
        self_,
        type: CalendarIntervalMonthType,
        alignment: Union[DayOfTheMonth, UnsetType] = unset,
        quantity: Union[float, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alignment: Test-only generated schema for the dashboard versioning proof of concept.
        :type alignment: DayOfTheMonth, optional

        :param quantity: Test-only generated schema for the dashboard versioning proof of concept.
        :type quantity: float, optional

        :param timezone: IANA time zone identifier, for example America/New_York.
        :type timezone: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CalendarIntervalMonthType
        """
        if alignment is not unset:
            kwargs["alignment"] = alignment
        if quantity is not unset:
            kwargs["quantity"] = quantity
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)

        self_.type = type
