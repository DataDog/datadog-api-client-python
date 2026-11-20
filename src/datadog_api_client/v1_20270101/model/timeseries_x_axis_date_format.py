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
    from datadog_api_client.v1_20270101.model.timeseries_x_axis_day_date_format import TimeseriesXAxisDayDateFormat
    from datadog_api_client.v1_20270101.model.timeseries_x_axis_month_date_format import TimeseriesXAxisMonthDateFormat


class TimeseriesXAxisDateFormat(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.timeseries_x_axis_day_date_format import TimeseriesXAxisDayDateFormat
        from datadog_api_client.v1_20270101.model.timeseries_x_axis_month_date_format import (
            TimeseriesXAxisMonthDateFormat,
        )

        return {
            "day": (TimeseriesXAxisDayDateFormat,),
            "month": (TimeseriesXAxisMonthDateFormat,),
        }

    attribute_map = {
        "day": "day",
        "month": "month",
    }

    def __init__(
        self_,
        day: Union[TimeseriesXAxisDayDateFormat, UnsetType] = unset,
        month: Union[TimeseriesXAxisMonthDateFormat, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param day: Test-only generated schema for the dashboard versioning proof of concept.
        :type day: TimeseriesXAxisDayDateFormat, optional

        :param month: Test-only generated schema for the dashboard versioning proof of concept.
        :type month: TimeseriesXAxisMonthDateFormat, optional
        """
        if day is not unset:
            kwargs["day"] = day
        if month is not unset:
            kwargs["month"] = month
        super().__init__(kwargs)
