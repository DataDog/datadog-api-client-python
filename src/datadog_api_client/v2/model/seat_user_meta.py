# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class SeatUserMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str, none_type),
            "limit": (int, none_type),
            "next_cursor": (str, none_type),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
        "next_cursor": "next_cursor",
    }

    def __init__(
        self_,
        cursor: Union[str, none_type, UnsetType] = unset,
        limit: Union[int, none_type, UnsetType] = unset,
        next_cursor: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param cursor: The cursor for the seat users.
        :type cursor: str, none_type, optional

        :param limit: The limit for the seat users.
        :type limit: int, none_type, optional

        :param next_cursor: The next cursor for the seat users.
        :type next_cursor: str, none_type, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if limit is not unset:
            kwargs["limit"] = limit
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)
