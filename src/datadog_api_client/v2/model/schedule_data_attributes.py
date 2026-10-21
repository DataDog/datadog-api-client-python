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


class ScheduleDataAttributes(ModelNormal):
    validations = {
        "max_responders": {
            "inclusive_maximum": 10,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "max_responders": (int,),
            "name": (str,),
            "tags": ([str],),
            "time_zone": (str,),
        }

    attribute_map = {
        "max_responders": "max_responders",
        "name": "name",
        "tags": "tags",
        "time_zone": "time_zone",
    }

    def __init__(
        self_,
        max_responders: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        time_zone: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provides core properties of a schedule object such as its name and time zone.

        :param max_responders: Maximum number of users who can be on call at the same time.
            The value is between 1 and the number of layers, and no greater than 10.
        :type max_responders: int, optional

        :param name: A short name for the schedule.
        :type name: str, optional

        :param tags: A list of tags associated with the schedule.
        :type tags: [str], optional

        :param time_zone: The time zone in which this schedule operates.
        :type time_zone: str, optional
        """
        if max_responders is not unset:
            kwargs["max_responders"] = max_responders
        if name is not unset:
            kwargs["name"] = name
        if tags is not unset:
            kwargs["tags"] = tags
        if time_zone is not unset:
            kwargs["time_zone"] = time_zone
        super().__init__(kwargs)
