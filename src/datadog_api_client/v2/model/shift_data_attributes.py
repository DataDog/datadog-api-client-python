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


class ShiftDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (datetime,),
            "start": (datetime,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(self_, end: Union[datetime, UnsetType] = unset, start: Union[datetime, UnsetType] = unset, **kwargs):
        """
        The definition of ``ShiftDataAttributes`` object.

        :param end: The end time of the shift.
        :type end: datetime, optional

        :param start: The start time of the shift.
        :type start: datetime, optional
        """
        if end is not unset:
            kwargs["end"] = end
        if start is not unset:
            kwargs["start"] = start
        super().__init__(kwargs)
