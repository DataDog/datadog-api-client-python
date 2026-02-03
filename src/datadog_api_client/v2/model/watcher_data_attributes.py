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


class WatcherDataAttributes(ModelNormal):
    validations = {
        "watch_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "icon": (str,),
            "last_watched_at": (datetime,),
            "name": (str,),
            "watch_count": (int,),
        }

    attribute_map = {
        "handle": "handle",
        "icon": "icon",
        "last_watched_at": "last_watched_at",
        "name": "name",
        "watch_count": "watch_count",
    }

    def __init__(
        self_,
        handle: str,
        last_watched_at: datetime,
        watch_count: int,
        icon: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param handle:
        :type handle: str

        :param icon:
        :type icon: str, optional

        :param last_watched_at:
        :type last_watched_at: datetime

        :param name:
        :type name: str, optional

        :param watch_count:
        :type watch_count: int
        """
        if icon is not unset:
            kwargs["icon"] = icon
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.handle = handle
        self_.last_watched_at = last_watched_at
        self_.watch_count = watch_count
