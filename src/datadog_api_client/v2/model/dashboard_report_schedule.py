# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report_schedule_frequency import DashboardReportScheduleFrequency
    from datadog_api_client.v2.model.dashboard_report_schedule_repeat_at import DashboardReportScheduleRepeatAt
    from datadog_api_client.v2.model.dashboard_report_schedule_repeat_on_day_of_month import (
        DashboardReportScheduleRepeatOnDayOfMonth,
    )
    from datadog_api_client.v2.model.dashboard_report_schedule_repeat_on_day_of_week import (
        DashboardReportScheduleRepeatOnDayOfWeek,
    )


class DashboardReportSchedule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_schedule_frequency import DashboardReportScheduleFrequency
        from datadog_api_client.v2.model.dashboard_report_schedule_repeat_at import DashboardReportScheduleRepeatAt
        from datadog_api_client.v2.model.dashboard_report_schedule_repeat_on_day_of_month import (
            DashboardReportScheduleRepeatOnDayOfMonth,
        )
        from datadog_api_client.v2.model.dashboard_report_schedule_repeat_on_day_of_week import (
            DashboardReportScheduleRepeatOnDayOfWeek,
        )

        return {
            "active": (bool,),
            "frequency": (DashboardReportScheduleFrequency,),
            "repeat_at": (DashboardReportScheduleRepeatAt,),
            "repeat_on_day_of_month": (DashboardReportScheduleRepeatOnDayOfMonth,),
            "repeat_on_day_of_week": (DashboardReportScheduleRepeatOnDayOfWeek,),
            "timezone": (str,),
        }

    attribute_map = {
        "active": "active",
        "frequency": "frequency",
        "repeat_at": "repeat_at",
        "repeat_on_day_of_month": "repeat_on_day_of_month",
        "repeat_on_day_of_week": "repeat_on_day_of_week",
        "timezone": "timezone",
    }

    def __init__(
        self_,
        active: Union[bool, UnsetType] = unset,
        frequency: Union[DashboardReportScheduleFrequency, UnsetType] = unset,
        repeat_at: Union[DashboardReportScheduleRepeatAt, UnsetType] = unset,
        repeat_on_day_of_month: Union[DashboardReportScheduleRepeatOnDayOfMonth, none_type, UnsetType] = unset,
        repeat_on_day_of_week: Union[DashboardReportScheduleRepeatOnDayOfWeek, none_type, UnsetType] = unset,
        timezone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Report schedule-specific configuration that defines when and how often a report is sent.

        :param active: Enables or disables automatic report sending as configured in the report's schedule. If set to ``false`` , schedule is paused and reports are not sent.
        :type active: bool, optional

        :param frequency: Frequency with which to send the report.
        :type frequency: DashboardReportScheduleFrequency, optional

        :param repeat_at: ISO8601 formatted time (HH:MM) to send the report, using the time zone specified in the ``timezone`` field.
        :type repeat_at: DashboardReportScheduleRepeatAt, optional

        :param repeat_on_day_of_month: Defines which day of the month to send the monthly report. If the frequency field uses months (for example, ``1mo`` ), this field is required. If the frequency field does not use months (for example ``1d`` , ``1w`` ), then this field must be ``null`` (if provided). If this field is not provided in an update request, and the update request changes the frequency to use days or weeks (for example, ``1d`` , ``1w`` ), then this field is automatically set to ``null``. This field is mutually exclusive with ``repeat_on_day_of_week`` , and cannot be defined in the same request that includes a non-null value for ``repeat_on_day_of_week``.
        :type repeat_on_day_of_month: DashboardReportScheduleRepeatOnDayOfMonth, none_type, optional

        :param repeat_on_day_of_week: Defines which day of the week to send the weekly report. If the frequency field uses weeks (such as ``1w`` ), this field is required and defines which day of the week to send the report. If the frequency field does not use weeks (for example, ``1d`` , ``1mo`` ), then this field must be ``null`` (if provided). If this field is not provided in an update request, and the update request changes the frequency to use days or months (for example, ``1d`` , ``1mo`` ), then this field is automatically set to ``null``.  This field is mutually exclusive with ``repeat_on_day_of_month`` and cannot be defined in the same request that includes a non-null value for ``repeat_on_day_of_month``.
        :type repeat_on_day_of_week: DashboardReportScheduleRepeatOnDayOfWeek, none_type, optional

        :param timezone: Time zone to use for repeat_at. Must be a valid Time Zone Database (https://www.iana.org/time-zones) name
        :type timezone: str, optional
        """
        if active is not unset:
            kwargs["active"] = active
        if frequency is not unset:
            kwargs["frequency"] = frequency
        if repeat_at is not unset:
            kwargs["repeat_at"] = repeat_at
        if repeat_on_day_of_month is not unset:
            kwargs["repeat_on_day_of_month"] = repeat_on_day_of_month
        if repeat_on_day_of_week is not unset:
            kwargs["repeat_on_day_of_week"] = repeat_on_day_of_week
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)
