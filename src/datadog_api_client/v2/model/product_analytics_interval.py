# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProductAnalyticsInterval(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "milliseconds": (int,),
            "start_time": (int,),
            "times": ([int],),
            "type": (str,),
        }

    attribute_map = {
        "milliseconds": "milliseconds",
        "start_time": "start_time",
        "times": "times",
        "type": "type",
    }

    def __init__(
        self_,
        milliseconds: Union[int, UnsetType] = unset,
        start_time: Union[int, UnsetType] = unset,
        times: Union[List[int], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An interval definition in a timeseries response.

        :param milliseconds:
        :type milliseconds: int, optional

        :param start_time:
        :type start_time: int, optional

        :param times:
        :type times: [int], optional

        :param type:
        :type type: str, optional
        """
        if milliseconds is not unset:
            kwargs["milliseconds"] = milliseconds
        if start_time is not unset:
            kwargs["start_time"] = start_time
        if times is not unset:
            kwargs["times"] = times
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
