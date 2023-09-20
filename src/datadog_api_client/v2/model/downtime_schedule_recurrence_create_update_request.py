# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class DowntimeScheduleRecurrenceCreateUpdateRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            UUID,
            none_type,
        )

    @cached_property
    def openapi_types(_):
        return {
            "duration": (str,),
            "rrule": (str,),
            "start": (str, none_type),
        }

    attribute_map = {
        "duration": "duration",
        "rrule": "rrule",
        "start": "start",
    }

    def __init__(self_, duration: str, rrule: str, start: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        An object defining the recurrence of the downtime.

        :param duration: The length of the downtime. Must begin with an integer and end with one of 'm', 'h', d', or 'w'.
        :type duration: str

        :param rrule: The ``RRULE`` standard for defining recurring events.
            For example, to have a recurring event on the first day of each month, set the type to ``rrule`` and set the ``FREQ`` to ``MONTHLY`` and ``BYMONTHDAY`` to ``1``.
            Most common ``rrule`` options from the `iCalendar Spec <https://tools.ietf.org/html/rfc5545>`_ are supported.

            **Note** : Attributes specifying the duration in ``RRULE`` are not supported (for example, ``DTSTART`` , ``DTEND`` , ``DURATION`` ).
            More examples available in this `downtime guide <https://docs.datadoghq.com/monitors/guide/suppress-alert-with-downtimes/?tab=api>`_.
        :type rrule: str

        :param start: ISO-8601 Datetime to start the downtime. Must not include a UTC offset. If not provided, the
            downtime starts the moment it is created.
        :type start: str, none_type, optional
        """
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)

        self_.duration = duration
        self_.rrule = rrule
