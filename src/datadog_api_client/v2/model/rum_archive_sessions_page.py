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


class RumArchiveSessionsPage(ModelNormal):
    validations = {
        "total_count": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "next_cursor": (str,),
            "total_count": (int,),
        }

    attribute_map = {
        "next_cursor": "next_cursor",
        "total_count": "total_count",
    }

    def __init__(self_, total_count: int, next_cursor: Union[str, UnsetType] = unset, **kwargs):
        """
        Search pagination.

        :param next_cursor: Opaque continuation cursor. Omitted when no further page is available.
        :type next_cursor: str, optional

        :param total_count: Search result count. Can be zero on continuation pages even when sessions are returned. Use ``next_cursor`` to determine whether more pages are available.
        :type total_count: int
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)

        self_.total_count = total_count
