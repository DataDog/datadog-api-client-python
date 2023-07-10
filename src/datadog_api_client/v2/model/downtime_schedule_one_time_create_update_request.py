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


class DowntimeScheduleOneTimeCreateUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime, none_type),
            "start": (datetime, none_type),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(
        self_,
        end: Union[datetime, none_type, UnsetType] = unset,
        start: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A one-time downtime definition.

        :param end: ISO-8601 Datetime to end the downtime. Must include a UTC offset of zero. If not provided, the
            downtime continues forever.
        :type end: datetime, none_type, optional

        :param start: ISO-8601 Datetime to start the downtime. Must include a UTC offset of zero. If not provided, the
            downtime starts the moment it is created.
        :type start: datetime, none_type, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)
