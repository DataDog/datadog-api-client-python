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


class TriggerRateLimit(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "interval": (str,),
        }

    attribute_map = {
        "count": "count",
        "interval": "interval",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, interval: Union[str, UnsetType] = unset, **kwargs):
        """
        Defines a rate limit for a trigger.

        :param count: The ``TriggerRateLimit`` ``count``.
        :type count: int, optional

        :param interval: The ``TriggerRateLimit`` ``interval``. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
        :type interval: str, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if interval is not unset:
            kwargs["interval"] = interval
        super().__init__(kwargs)
