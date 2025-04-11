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


class ScheduleUpdateRequestDataAttributesLayersItemsInterval(ModelNormal):
    validations = {
        "days": {
            "inclusive_maximum": 400,
        },
        "seconds": {
            "inclusive_maximum": 2592000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "days": (int,),
            "seconds": (int,),
        }

    attribute_map = {
        "days": "days",
        "seconds": "seconds",
    }

    def __init__(self_, days: Union[int, UnsetType] = unset, seconds: Union[int, UnsetType] = unset, **kwargs):
        """
        Specifies how the rotation repeats: number of days, plus optional seconds, up to the given maximums.

        :param days: How many days each rotation cycle should span.
        :type days: int, optional

        :param seconds: Additional seconds to add to the rotation cycle (for example, partial days).
        :type seconds: int, optional
        """
        if days is not unset:
            kwargs["days"] = days
        if seconds is not unset:
            kwargs["seconds"] = seconds
        super().__init__(kwargs)
