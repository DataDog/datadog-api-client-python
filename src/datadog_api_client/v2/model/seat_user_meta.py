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


class SeatUserMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str,),
            "limit": (int,),
            "next_cursor": (str,),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
        "next_cursor": "next_cursor",
    }

    def __init__(
        self_,
        cursor: Union[str, UnsetType] = unset,
        limit: Union[int, UnsetType] = unset,
        next_cursor: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param cursor:
        :type cursor: str, optional

        :param limit:
        :type limit: int, optional

        :param next_cursor:
        :type next_cursor: str, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if limit is not unset:
            kwargs["limit"] = limit
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)
