# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RUMQueryOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "time_offset": (int,),
            "timezone": (str,),
        }

    attribute_map = {
        "time_offset": "time_offset",
        "timezone": "timezone",
    }

    def __init__(self_, time_offset: Union[int, UnsetType] = unset, timezone: Union[str, UnsetType] = unset, **kwargs):
        """
        Global query options that are used during the query.
        Note: Only supply timezone or time offset, not both. Otherwise, the query fails.

        :param time_offset: The time offset (in seconds) to apply to the query.
        :type time_offset: int, optional

        :param timezone: The timezone can be specified both as an offset, for example: "UTC+03:00".
        :type timezone: str, optional
        """
        if time_offset is not unset:
            kwargs["time_offset"] = time_offset
        if timezone is not unset:
            kwargs["timezone"] = timezone
        super().__init__(kwargs)
