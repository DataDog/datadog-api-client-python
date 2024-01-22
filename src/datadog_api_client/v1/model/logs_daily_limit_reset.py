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


class LogsDailyLimitReset(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "reset_time": (str,),
            "reset_utc_offset": (str,),
        }

    attribute_map = {
        "reset_time": "reset_time",
        "reset_utc_offset": "reset_utc_offset",
    }

    def __init__(
        self_, reset_time: Union[str, UnsetType] = unset, reset_utc_offset: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Object containing options to override the default daily limit reset time.

        :param reset_time: String in ``HH:00`` format representing the time of day the daily limit should be reset. The hours must be between 00 and 23 (inclusive).
        :type reset_time: str, optional

        :param reset_utc_offset: String in ``(-|+)HH:00`` format representing the UTC offset to apply to the given reset time. The hours must be between -12 and +14 (inclusive).
        :type reset_utc_offset: str, optional
        """
        if reset_time is not unset:
            kwargs["reset_time"] = reset_time
        if reset_utc_offset is not unset:
            kwargs["reset_utc_offset"] = reset_utc_offset
        super().__init__(kwargs)
