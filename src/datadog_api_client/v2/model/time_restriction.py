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
    from datadog_api_client.v2.model.weekday import Weekday


class TimeRestriction(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.weekday import Weekday

        return {
            "end_day": (Weekday,),
            "end_time": (str,),
            "start_day": (Weekday,),
            "start_time": (str,),
        }

    attribute_map = {
        "end_day": "end_day",
        "end_time": "end_time",
        "start_day": "start_day",
        "start_time": "start_time",
    }

    def __init__(
        self_,
        end_day: Union[Weekday, UnsetType] = unset,
        end_time: Union[str, UnsetType] = unset,
        start_day: Union[Weekday, UnsetType] = unset,
        start_time: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a single time restriction rule with start and end times and the applicable weekdays.

        :param end_day: A day of the week.
        :type end_day: Weekday, optional

        :param end_time: Specifies the ending time for this restriction.
        :type end_time: str, optional

        :param start_day: A day of the week.
        :type start_day: Weekday, optional

        :param start_time: Specifies the starting time for this restriction.
        :type start_time: str, optional
        """
        if end_day is not unset:
            kwargs["end_day"] = end_day
        if end_time is not unset:
            kwargs["end_time"] = end_time
        if start_day is not unset:
            kwargs["start_day"] = start_day
        if start_time is not unset:
            kwargs["start_time"] = start_time
        super().__init__(kwargs)
