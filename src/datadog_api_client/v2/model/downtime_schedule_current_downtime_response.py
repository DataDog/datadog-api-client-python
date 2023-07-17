# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class DowntimeScheduleCurrentDowntimeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime, none_type),
            "start": (datetime,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(
        self_, end: Union[datetime, none_type, UnsetType] = unset, start: Union[datetime, UnsetType] = unset, **kwargs
    ):
        """
        The most recent actual start and end dates for a recurring downtime. For a canceled downtime,
        this is the previously occurring downtime. For active downtimes, this is the ongoing downtime, and for scheduled
        downtimes it is the upcoming downtime.

        :param end: The end of the current downtime.
        :type end: datetime, none_type, optional

        :param start: The start of the current downtime.
        :type start: datetime, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)
