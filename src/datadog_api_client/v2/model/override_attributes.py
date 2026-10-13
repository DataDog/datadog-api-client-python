# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class OverrideAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime,),
            "inactive": (bool,),
            "start": (datetime,),
        }

    attribute_map = {
        "end": "end",
        "inactive": "inactive",
        "start": "start",
    }

    def __init__(
        self_,
        end: Union[datetime, UnsetType] = unset,
        inactive: Union[bool, UnsetType] = unset,
        start: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an on-call schedule override.

        :param end: The end time of the override.
        :type end: datetime, optional

        :param inactive: Whether the override is inactive (for example, because its time range has ended).
        :type inactive: bool, optional

        :param start: The start time of the override.
        :type start: datetime, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if inactive is not unset:
            kwargs["inactive"] = inactive
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)
